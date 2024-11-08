import ipaddress

def subnet_details(ip_with_prefix):
    # Parse the input as an IP network with a subnet prefix
    network = ipaddress.ip_network(ip_with_prefix, strict=False)
    print(f"Network: {network}")

    # Subnet mask
    subnet_mask = network.netmask
    print(f"Subnet Mask: {subnet_mask}")

    # Network address
    network_address = network.network_address
    print(f"Network Address: {network_address}")

    # Broadcast address
    broadcast_address = network.broadcast_address
    print(f"Broadcast Address: {broadcast_address}")

    # First usable IP
    first_usable_ip = network[1] if network.num_addresses > 2 else network[0]
    print(f"First Usable IP: {first_usable_ip}")

    # Last usable IP
    last_usable_ip = network[-2] if network.num_addresses > 2 else network[-1]
    print(f"Last Usable IP: {last_usable_ip}")

    # Number of usable hosts
    num_hosts = network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses
    print(f"Number of Usable Hosts: {num_hosts}")

# Example usage
ip_with_prefix = "192.168.1.1/24"
subnet_details(ip_with_prefix)