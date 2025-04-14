"""
    cody by: SALMAN MALLAH, BS CYBER SEC.
    The code allows you to input an IP address,
    a subnet mask, and the number of desired networks, generating the respective subnets
"""


def Subnetting(ip="192.168.10.0", subnet_mask="255.255.255.0", networks=2):
    total_network = {}
    for i in range(1, 25):
        total_network[i] = 2**i

    octate = {
        1: {1: 128, 2: 64, 3: 32, 4: 16, 5: 8, 6: 4, 7: 2, 8: 1},  # _(._.)_._
        2: {1: 128, 2: 64, 3: 32, 4: 16, 5: 8, 6: 4, 7: 2, 8: 1},  # _._(._.)_
        3: {1: 128, 2: 64, 3: 32, 4: 16, 5: 8, 6: 4, 7: 2, 8: 1},  # _._._(._)
    }

    ip_list = [int(i) for i in ip.split(".")]  # magic numbers will be added at index 3
    print(f"Your IP Address {ip_list}")

    final_result = {}

    def Find_ip(bit):
        final_result
        magic_number = octate[1][bit]
        print("magic: number", magic_number)
        temp = []
        for j in range(networks):
            if j == 0:
                temp.insert(j, ip_list.copy())
            else:
                ip_list[3] += magic_number
                temp.insert(j, ip_list.copy())

            final_result[j] = temp[j]
        print("Final result\n", *temp, sep="\n")

    if networks == 1:
        print("============== Result ================")
        print(f"IP: {ip}\nSubnetMask: {subnet_mask}")
    else:
        for bit, net in total_network.items():
            if networks == net:
                Find_ip(bit)
            #       7   <=   8     &     7       > 4
            elif (networks <= net) and (networks > total_network[bit - 1]):
                print("============== Result ================")
                print(f"we us ")

                Find_ip(bit)


# ip = input('Please Enter your IP address: ')
# subnet_mask = input('Please Enter your Subnet Mask: ')
# network = int(input('How much networks you want: '))

Subnetting("192.168.10.192", "255.255.255.0", 5)
