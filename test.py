#     1: {1: 128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1}, # _(._.)_._
#     2: {1: 128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1}, # _._(._.)_
#     3: {1: 128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1}  # _._._(._)
# }

# magic_number = octate[1][9]
# print(magic_number)



def subnets(ip, mask):

    net, host = NetHostSplit(ip, mask)

    if len(net) == 32:
        host = 0

    if not int(host):
        
        # if host is '0' then subnet should be equal to IP (e.g 192.168.1.0)
        subnet = ip
         # convert to decimal value. This is required to compute next IP block
        net_dec = int(net, 2)
    else:
            # if host is non zero then convert network to decimal and add 1, then re-convert to binary
        net_dec = int(net, 2)
        net_dec = net_dec + 1
        binary_ip_tmp = bin(net_dec)[2:].rjust(len(net), '0')
        binary_ip_tmp = binary_ip_tmp.ljust(32, '0')
        #print(binary_ip)
        # convert binary to standard IP format (e.g '11001000000000000000000000000000' to 192.168.1.0)
        subnet = ConverToIP(binary_ip_tmp)
            
    net_dec = net_dec + 1
        
    binary_ip = bin(net_dec)[2:].rjust(len(net), '0')
    binary_ip = binary_ip.ljust(32, '0')
        
    next_block = ConverToIP(binary_ip)
    return subnet, next_block

def ConverToIP(binary_ip):
    oct1 = int(binary_ip[0:8], 2)
    oct2 = int(binary_ip[8:16], 2)
    oct3 = int(binary_ip[16:24], 2)
    oct4 = int(binary_ip[24:32], 2)

    ip = '{}.{}.{}.{}'.format(oct1,oct2,oct3,oct4)

    return ip

def NetHostSplit(ip, mask):
      
    binary_ip = ''
    ip_list = ip.split('.')

    for octet in ip_list:
            octet_bin = bin(int(octet))[2:]
            octet_bin = octet_bin.zfill(8)
            binary_ip = binary_ip + octet_bin
                
    net_bits = binary_ip[:int(mask)]
    host_bits = binary_ip[int(mask):]
        
    return net_bits, host_bits

def subnets(ip, mask):

    net, host = NetHostSplit(ip, mask)

    if len(net) == 32:
        host = 0

    if not int(host):
        
        # if host is '0' then subnet should be equal to IP (e.g 192.168.1.0)
        subnet = ip
         # convert to decimal value. This is required to compute next IP block
        net_dec = int(net, 2)
    else:
            # if host is non zero then convert network to decimal and add 1, then re-convert to binary
        net_dec = int(net, 2)
        net_dec = net_dec + 1
        binary_ip_tmp = bin(net_dec)[2:].rjust(len(net), '0')
        binary_ip_tmp = binary_ip_tmp.ljust(32, '0')
        #print(binary_ip)
        # convert binary to standard IP format (e.g '11001000000000000000000000000000' to 192.168.1.0)
        subnet = ConverToIP(binary_ip_tmp)
            
    net_dec = net_dec + 1
        
    binary_ip = bin(net_dec)[2:].rjust(len(net), '0')
    binary_ip = binary_ip.ljust(32, '0')
        
    next_block = ConverToIP(binary_ip)
    return subnet, next_block


def main_allocations():


    # starting ip for subnet allocation 
    start_ip = '192.168.10.0'
    mask_list = [24]

    result_list = []    
    
    next_block = start_ip

    for mask in mask_list:
        subnet, next_block = subnets(next_block, mask)
        result_list.append('{}/{}'.format(subnet, mask))

    print(result_list)

main_allocations()


  
def main_allocations():

    # starting_ip is the block for subnet allocation. Replace the IP as per your requirement
    start_ip = '192.168.11.0' 
    # this is the list of subnet mask required
    mask_list = [23,24,25,26,27,27]

    result_list = []    

    next_block = start_ip

    for mask in mask_list:
        subnet, next_block = subnets(next_block, mask)
        result_list.append('{}/{}'.format(subnet, mask))

    print(result_list)

main_allocations()