def subnet(ip, subnet_mask, networks):
    def calculate_magic_number(subnet_bits):
        return 2 ** (8 - subnet_bits)

    def find_ip(bit, ip_list):
        magic_number = calculate_magic_number(bit)
        subnetted_ips = []

        for _ in range(networks):
            subnetted_ips.append(ip_list.copy())
            ip_list[-1] += magic_number

        return subnetted_ips

    def display_result(ip_address, subnet_mask):
        print("============== Result ================")
        print(f"IP Address: {'.'.join(map(str, ip_address))}")
        print(f"Subnet Mask: {subnet_mask}")
        print("======================================")

    ip_list = list(map(int, ip.split(".")))

    # Detect IP class
    ip_class = "C"
    if 1 <= ip_list[0] <= 126:
        ip_class = "A"
    elif 128 <= ip_list[0] <= 191:
        ip_class = "B"

    print(f"Your IP Address {ip_list} is Class {ip_class}")

    for subnet_bits in range(1, 25):
        total_networks = 2**subnet_bits

        if (
            networks <= total_networks - 2
        ):  # Subtract 2 for network and broadcast addresses
            subnetted_ips = find_ip(subnet_bits, ip_list)
            display_result(subnetted_ips[0], subnet_mask)
            for subnet_ip in subnetted_ips[1:]:
                print(".".join(map(str, subnet_ip)))
            break  # Exit the loop once a valid subnetting is found


# Example usage
# subnet("192.168.10.192", "255.255.255.0", 1000)
subnet("10.0.0.1", "255.0.0.0", 1000)
# subnet("172.16.0.1", "255.255.0.0", 16)
