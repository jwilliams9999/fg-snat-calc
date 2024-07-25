#!/usr/bin/python3

import ipaddress


def snat_ip(srcip, natip1, nattotal):
	srcip_as_dec = int.from_bytes(srcip.packed, 'big')
	mod = srcip_as_dec % nattotal
	snat_ip = natip1 + mod
	print(f'snat ip is : {snat_ip}')


while True:
    try:
        srcip = ipaddress.ip_address(input('Enter your source IP address: '))
        natip1 = ipaddress.ip_address(input('Enter the first IP address in the NAT Pool: '))
        nattotal = int(input('Enter total number of IP addresses in the NAT Pool: '))
        snat_ip(srcip, natip1, nattotal)
        break


    except ValueError:
    	print('Please enter a valid input.')
    	continue



while True:
	try:
		srcip = ipaddress.ip_address(input('Enter your source IP address: '))
		snat_ip(srcip, natip1, nattotal)

	except ValueError:
		print('Please enter a valid IP address.')
		continue




