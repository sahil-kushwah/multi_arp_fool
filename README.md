# multi_arp_fool
Arp spoofer


Usage: 

arp_spoofer.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET_IP, --target-ip=TARGET_IP
                        Enter Target Ip (eg: -t 192.168.1.12
  -g GATEWAY_IP, --gateway-ip=GATEWAY_IP
                        Enter gateway Ip which you want to spoof (eg: -g
                        192.168.1.1)
                        
![Screenshot 2022-12-29 132608](https://user-images.githubusercontent.com/109381227/209921075-622f644d-20d0-46df-a661-ee0928ef123a.jpg)

Example:

python3 arp_spoofer.py -t 192.168.1.6 -g 192.168.1.1

![Screenshot 2022-12-29 133036](https://user-images.githubusercontent.com/109381227/209921461-571eba31-6e15-401b-8ef6-9d9039cf7f73.jpg)
