import socket

def ip_to_url(ip_address):
    try:
        url = socket.gethostbyaddr(ip_address)
        return url[0]
    except socket.herror:
        return "Could not resolve the IP address to a URL."

def url_to_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return "Could not resolve the URL to an IP address."

while True:
    print("DNS Lookup Menu:")
    print("1. IP to URL")
    print("2. URL to IP")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        ip_address = input("Enter the IP address: ")
        url = ip_to_url(ip_address)
        print(f"The URL for {ip_address} is: {url}")
    elif choice == '2':
        url = input("Enter the URL: ")
        ip_address = url_to_ip(url)
        print(f"The IP address for {url} is: {ip_address}")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
