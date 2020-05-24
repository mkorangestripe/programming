#!/usr/bin/env python3
# Gavin Purcell

# To do:
# classes to share variables
# unit test

"""
Scan a network by pinging a CIDR range in parallel.
CIDR notation examples:
192.168.0.0/28
10.0.0.0/28
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
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-i', '--infile',
                        help="Input file. Expects subnets in CIDR notation.")
    parser.add_argument('-c', '--cidr',
                        help="Scan a CIDR range i.e. 10.0.0.0/24 which would scan address range 10.0.0.0 - 10.0.0.255")
    parser.add_argument('-w', '--deadline', default=5, help='Specify a timeout, in seconds, before ping exits.')
    parser.add_argument('-u', '--up', action='store_true', help='Only output hosts that are up.')
    parser.add_argument('-d', '--down', action='store_true', help='Only output hosts that are down.')
    args = parser.parse_args()
    if args.up is True and args.down is True:
        print("Arguments 'up' and 'down' should not be used together.")
        sys.exit(1)
    if args.infile is not None and args.cidr is not None:
        print("Arguments 'infile' and 'cidr' should not be used together.")
        sys.exit(1)
    if args.infile is None and args.cidr is None:
        print("Either 'infile' or 'cidr' is required.")
        sys.exit(1)
    return args


def run_ping_cmd(ip, ping_deadline):
    """Run the ping command."""
    ping_cmd = 'ping -w %s %s' % (ping_deadline, ip)
    return subprocess.Popen(ping_cmd,
                            shell=True,
                            stdout=subprocess.PIPE)


def print_ip_group(ips, requested_return_code, response_by_ip):
    """Print group of IPs, either up or down."""
    for ip in ips:
        ip = str(ip)
        ret_code = response_by_ip[ip][0]
        if ret_code == requested_return_code:
            print(ip)
    print()


def print_ips_state(ips, response_by_ip):
    """Print all IPs in CIDR range with up/down state."""
    for ip in ips:
        ip = str(ip)
        ret_code = response_by_ip[ip][0]
        if ret_code == 0:
            print('%s is %sup%s' % (ip, Color.green, Color.end))
        else:
            print('%s is %sdown%s' % (ip, Color.red, Color.end))
    print()


def print_stdout(ips, response_by_ip):
    """Print stdout if verbose argument is given."""
    for ip in ips:
        ip = str(ip)
        print(ip)
        stdout = response_by_ip[ip][1]
        for line in stdout:
            print(line.strip().decode('utf-8'))
        print()


def generate_ip_addrs(net_address):
    """Generate the list of IP addresses to ping."""
    try:
        ip_net = ipaddress.ip_network(net_address)
    except ValueError as e:
        print(e)
        sys.exit(1)
    return list(ip_net.hosts())


def create_ping_processes(net_address, ip_list):
    """Create a ping subprocesses per IP address."""
    jobs = []
    response_by_ip = {}
    print('Starting ping of', net_address)
    for ip in ip_list:
        ip = str(ip)
        response_by_ip[ip] = []
        ping_process = run_ping_cmd(ip, args.deadline)
        jobs.append((ping_process, ip))
    return jobs, response_by_ip


def get_return_code_response(jobs, response_by_ip):
    """Wait for the ping subprocesses to finish and get the return code and response."""
    for job in jobs:
        process, ip = job[0], job[1]
        process.wait()
        return_code = process.returncode
        response = process.stdout.readlines()
        response_by_ip[ip] = (return_code, response)
    return response_by_ip


if __name__ == '__main__':

    args = _get_argparser()

    if args.infile is not None:
        with open(args.infile) as infile:
            cidr_list = infile.read().split()
    elif args.cidr is not None:
        cidr_list = [args.cidr]

    for net_addr in cidr_list:
        ip_addr_list = generate_ip_addrs(net_addr)
        ping_jobs, response_by_ip_empty = create_ping_processes(net_addr, ip_addr_list)
        ping_response_by_ip = get_return_code_response(ping_jobs, response_by_ip_empty)

        if args.up is True:
            print('The following hosts are up.\n')
            print_ip_group(ip_addr_list, 0, ping_response_by_ip)
        elif args.down is True:
            print('The following hosts are down.\n')
            print_ip_group(ip_addr_list, 1, ping_response_by_ip)
        else:
            print()
            print_ips_state(ip_addr_list, ping_response_by_ip)

        if args.verbose is True:
            print()
            print_stdout(ip_addr_list, ping_response_by_ip)
