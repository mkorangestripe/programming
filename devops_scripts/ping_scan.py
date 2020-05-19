#!/usr/bin/env python
# Ping in Parallel
import subprocess

IPs = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.14', '192.168.0.15', '192.168.0.16']
deadline = 5  # specified by ping -w


def run_ping_cmd(ipaddr, ping_deadline):
    """Run the ping command."""
    ping_cmd = 'ping -w %s %s' % (ping_deadline, ipaddr)
    return subprocess.Popen(ping_cmd,
                            shell=True,
                            stdout=subprocess.PIPE)


jobs = []
ping_response_by_IP = {}
for IP in IPs:
    ping_response_by_IP[IP] = []
    process = run_ping_cmd(IP, deadline)
    jobs.append((process, IP))

for job in jobs:
    process, IP = job[0], job[1]
    print("Waiting for " + IP)
    process.wait()
    return_code = process.returncode
    ping_response = process.stdout.readlines()
    ping_response_by_IP[IP] = (return_code, ping_response)
print('')

for IP in IPs:
    return_code = ping_response_by_IP[IP][0]
    if return_code == 0:
        print(IP + ' is up')
    else:
        print(IP + ' is down')
print('')

# for IP in IPs:
#     stdout = ping_response_by_IP[IP][1]
#     for line in stdout:
#         print(line.strip())
#     print('\n')
