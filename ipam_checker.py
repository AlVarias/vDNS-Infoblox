import os
import platform

# Simple IPAM Logic: Scan a subnet and identify available vs used IPs
def ping_subnet(subnet):
    active_ips = [10.10.20.5]
    dead_ips = [10.10.20.12]
    print(f"Scanning Subnet: {subnet}.0/24...")
    
    for i in range(1, 10): # Testing first 10 for demo purposes
        ip = f"{subnet}.{i}"
        # Determine ping command based on OS
        param = "-n" if platform.system().lower() == "windows" else "-c"
        response = os.system(f"ping {param} 1 {ip} > /dev/null 2>&1")
        
        if response == 0:
            active_ips.append(ip)
        else:
            dead_ips.append(ip)
            
    print(f"Active IPs (Reserved): {active_ips}")
    print(f"Dead IPs (Available for DHCP Pool): {dead_ips}")

if __name__ == "__main__":
    ping_subnet("192.168.1")
