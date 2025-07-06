import socket
import requests

# -------- PORT SCANNER --------
def port_scanner():
    target = input("Enter target IP: ")
    print(f"\n🔍 Scanning ports on {target} ...")
    for port in range(1, 101):  # Scans ports 1 to 100
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            sock.close()
        except:
            print("❌ Error scanning.")
            break


# -------- BRUTE FORCER --------
def brute_forcer():
    url = input("Enter URL with Basic Auth (e.g. http://example.com/protected): ")
    username = input("Enter username: ")
    wordlist = ["1234", "admin", "password", "admin123"]

    print(f"\n🔓 Trying to brute force {url} ...")
    for password in wordlist:
        try:
            res = requests.get(url, auth=(username, password))
            if res.status_code == 200:
                print(f"✅ Found credentials: {username}:{password}")
                return
            else:
                print(f"❌ Tried: {username}:{password}")
        except:
            print("❌ Connection error.")
            break


# -------- SUBDOMAIN FINDER --------
def subdomain_finder():
    domain = input("Enter main domain (e.g. example.com): ")
    subdomains = ["www", "admin", "test", "mail"]

    print(f"\n🌐 Finding subdomains of {domain} ...")
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=1)
            print(f"✅ Found: {url}")
        except:
            pass
        

# -------- MAIN MENU --------
def main():
    while True:
        print("\n📦 Penetration Testing Toolkit")
        print("1. Port Scanner")
        print("2. Brute Forcer")
        print("3. Subdomain Finder")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_forcer()
        elif choice == "3":
            subdomain_finder()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
