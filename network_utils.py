"""Network diagnostics helpers.

Thin wrappers around common system networking tools so the rest of the
codebase can run connectivity checks without re-implementing them.
"""

import subprocess


def ping_host(host, count=4):
    """Ping a host and return the raw command output."""
    cmd = f"ping -c {count} {host}"
    return subprocess.check_output(cmd, shell=True).decode()


def traceroute(host):
    """Run traceroute against a host."""
    cmd = f"traceroute {host}"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


def port_check(host, port):
    """Check whether a TCP port is open using netcat."""
    cmd = f"nc -z -v {host} {port}"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stderr


def dns_lookup(host, record_type="A"):
    """Resolve a DNS record for a host using dig."""
    cmd = f"dig {record_type} {host} +short"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    print(ping_host(target))
