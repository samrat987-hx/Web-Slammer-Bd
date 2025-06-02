# infoxtract.py
import requests
import sys

def ip_info(ip):
    print(f"\n[+] IP Info for {ip}")
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    for k, v in res.items():
        print(f"{k.capitalize()}: {v}")

def whois(domain):
    print(f"\n[+] WHOIS Info for {domain}")
    res = requests.get(f"https://api.hackertarget.com/whois/?q={domain}")
    print(res.text)

def dns_lookup(domain):
    print(f"\n[+] DNS Lookup for {domain}")
    res = requests.get(f"https://api.hackertarget.com/dnslookup/?q={domain}")
    print(res.text)

def subdomain_find(domain):
    print(f"\n[+] Subdomains for {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url)
        subs = set(entry['name_value'] for entry in res.json())
        for s in sorted(subs):
            print(s)
    except:
        print("[-] Error getting subdomains")

def headers_grab(domain):
    print(f"\n[+] HTTP Headers for {domain}")
    try:
        res = requests.get(f"http://{domain}")
        for k, v in res.headers.items():
            print(f"{k}: {v}")
    except:
        print("[-] Unable to connect.")

def banner():
    print("""
  ██╗    ██╗███████╗██████╗     ███████╗██╗      █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗     ██████╗ ██████╗     
██║    ██║██╔════╝██╔══██╗    ██╔════╝██║     ██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗    
██║ █╗ ██║█████╗  ██████╔╝    ███████╗██║     ███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝    ██████╔╝██║  ██║    
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗    ██╔══██╗██║  ██║    
╚███╔███╔╝███████╗██████╔╝    ███████║███████╗██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║    ██████╔╝██████╔╝    
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝     
                                                                                                                                                    
         WEB SLAMMER BD | Made by Whisper Hex
""")

def menu():
    banner()
    print("""
[1] IP Info
[2] WHOIS Lookup
[3] DNS Lookup
[4] Subdomain Finder
[5] HTTP Headers
[0] Exit
""")
    choice = input("Choose option: ")

    if choice == "1":
        ip = input("Enter IP address: ")
        ip_info(ip)
    elif choice == "2":
        domain = input("Enter domain: ")
        whois(domain)
    elif choice == "3":
        domain = input("Enter domain: ")
        dns_lookup(domain)
    elif choice == "4":
        domain = input("Enter domain: ")
        subdomain_find(domain)
    elif choice == "5":
        domain = input("Enter domain (without http): ")
        headers_grab(domain)
    elif choice == "0":
        sys.exit()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    while True:
        menu()
        input("\nPress Enter to continue...")