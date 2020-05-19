#!/usr/bin/env python3
"""
Scan a network by pinging a CIDR range in parallel.'
"""

# To do:
# default mode: up/down
# verbose: output specific failure message per host
# use argparse args
# add -c count to args

import subprocess
import ipaddress
from argparse import ArgumentParser

class color:
    green = '\033[92m'
    end = '\033[0m'

# For testing...
# IPs = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.14', '192.168.0.15', '192.168.0.16']
# net_addr = '192.168.0.0/28'
net_addr = '192.168.0.0/27'
# ip_net = ipaddress.ip_network(net_addr, strict=False)
ip_net = ipaddress.ip_network(net_addr)
all_hosts = list(ip_net.hosts())
IPs = all_hosts
deadline = 5  # specified by ping -w


def _get_argparser():
    parser = ArgumentParser(description=__doc__)
    # parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--infile",
                        help="input file. This expects subnets in CIDR notation.")
    parser.add_argument("--outfile",
                        help="output file. This will out put the result of a scan. default: outfile.txt", default="outfile.txt")
    parser.add_argument("--cidr",
                        help="Scan a CIDR range i.e. 10.0.0.0/24 which would scan address range 10.0.0.0 - 10.0.0.255")
    parser.add_argument('-w', '--deadline', help='Specify a timeout, in seconds, before ping exits')
    args = parser.parse_args()


def run_ping_cmd(ipaddr, ping_deadline):
    """Run the ping command."""
    ping_cmd = 'ping -w %s %s' % (ping_deadline, ipaddr)
    return subprocess.Popen(ping_cmd,
                            shell=True,
                            stdout=subprocess.PIPE)


jobs = []
ping_response_by_IP = {}
for IP in IPs:
    IP = str(IP)
    ping_response_by_IP[IP] = []
    process = run_ping_cmd(IP, deadline)
    jobs.append((process, IP))

print('Starting ping of', net_addr)
for job in jobs:
    process, IP = job[0], job[1]
    # print("Waiting for " + IP)
    process.wait()
    return_code = process.returncode
    ping_response = process.stdout.readlines()
    ping_response_by_IP[IP] = (return_code, ping_response)
print('')

for IP in IPs:
    IP = str(IP)
    return_code = ping_response_by_IP[IP][0]
    if return_code == 0:
        # print(IP + ' is up')
        print('%s is %sup%s' % (IP, color.green, color.end))
    else:
        print(IP + ' is down')

# for IP in IPs:
#     stdout = ping_response_by_IP[IP][1]
#     for line in stdout:
#         print(line.strip())
#     print('\n')
