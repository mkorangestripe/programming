#!/usr/bin/env python3

# CIDR examples for testing script:
# 192.168.0.0/28
# 192.168.0.0/27

# To do:
# infile and outfile

"""
Scan a network by pinging a CIDR range in parallel.
"""

import sys
import subprocess
import ipaddress
from argparse import ArgumentParser


class Color:
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'


def _get_argparser():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--infile",
                        help="Input file. This expects subnets in CIDR notation.")
    parser.add_argument("--outfile",
                        help="Output file. This will output the result of a scan. default: outfile.txt", default="outfile.txt")
    parser.add_argument('-c', '--cidr', required=True,
                        help="Scan a CIDR range i.e. 10.0.0.0/24 which would scan address range 10.0.0.0 - 10.0.0.255")
    parser.add_argument('-w', '--deadline', default=5, help='Specify a timeout, in seconds, before ping exits.')
    parser.add_argument('-u', '--up', action='store_true', help='Only output hosts that are up.')
    parser.add_argument('-d', '--down', action='store_true', help='Only output hosts that are down.')
    args = parser.parse_args()
    if args.up is True and args.down is True:
        print("Arguments 'up' and 'down' should not be used together.")
        sys.exit(1)
    return args


def run_ping_cmd(ipaddr, ping_deadline):
    """Run the ping command."""
    ping_cmd = 'ping -w %s %s' % (ping_deadline, ipaddr)
    return subprocess.Popen(ping_cmd,
                            shell=True,
                            stdout=subprocess.PIPE)


def print_ip_group(ips, requested_return_code):
    """Print group of IPs, either up or down."""
    for ip in ips:
        ip = str(ip)
        ret_code = ping_response_by_IP[ip][0]
        if ret_code == requested_return_code:
            print(ip)


def print_ips_state(ips):
    """Print all IPs in CIDR range with up/down state."""
    for ip in ips:
        ip = str(ip)
        ret_code = ping_response_by_IP[ip][0]
        if ret_code == 0:
            print('%s is %sup%s' % (ip, Color.green, Color.end))
        else:
            print('%s is %sdown%s' % (ip, Color.red, Color.end))


def print_stdout(ips):
    """Print stdout if verbose argument is given."""
    for ip in ips:
        ip = str(ip)
        print(ip)
        stdout = ping_response_by_IP[ip][1]
        for line in stdout:
            print(line.strip().decode('utf-8'))
        print()


if __name__ == '__main__':

    args = _get_argparser()

    # Generate the list of IP addresses to ping.
    net_addr = args.cidr
    try:
        ip_net = ipaddress.ip_network(net_addr)
    except ValueError as e:
        print(e)
        sys.exit(1)
    IPs = list(ip_net.hosts())

    # Create a ping subprocesses per IP address.
    jobs = []
    ping_response_by_IP = {}
    print('Starting ping of', net_addr)
    for IP in IPs:
        IP = str(IP)
        ping_response_by_IP[IP] = []
        process = run_ping_cmd(IP, args.deadline)
        jobs.append((process, IP))

    # Wait for the ping subprocesses to finish and get the return code and response.
    for job in jobs:
        process, IP = job[0], job[1]
        process.wait()
        return_code = process.returncode
        ping_response = process.stdout.readlines()
        ping_response_by_IP[IP] = (return_code, ping_response)

    # Call functions to print IP addresses with/without state.
    if args.up is True:
        print('The following hosts are up\n')
        print_ip_group(IPs, 0)
    elif args.down is True:
        print('The following hosts are down\n')
        print_ip_group(IPs, 1)
    else:
        print()
        print_ips_state(IPs)

    if args.verbose is True:
        print()
        print_stdout(IPs)
