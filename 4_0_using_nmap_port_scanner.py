import nmap


def scanner(hostname):
    nm = nmap.PortScanner()
    # nm.scan(hostname, '21,22,25,80,110,9090')
    nm.scan(hostname, '21-443')
    for host_names in nm.all_hosts():
        # address = nm[host_names].get('addresses')
        ports = nm[host_names].get('tcp')
        return ports


def get_host_names():
    f = open('host_names', 'r')
    hosts = f.read()
    hosts = hosts.rsplit('\n')
    return hosts


hosts = get_host_names()
for host_name in hosts:
    ports = scanner(host_name)
    for port in ports:
        print("{0} : {1} {2}".format(host_name, port, ports.get(port)))
    print("\n****************\n")
