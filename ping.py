import subprocess
import time

def ping_host(host):

    try:
        subprocess.check_output(['ping', '-c', '1', host])
        return True
    except subprocess.CalledProcessError:
        return False

def automatic_pinger(host, interval):

    while True:
        if ping_host(host):
            print(f"Host {host} is reachable.")
        else:
            print(f"Host {host} is unreachable.")
        time.sleep(interval)

if __name__ == "__main__":
    host = input("Enter the host to ping: ")
    interval = int(input("Enter the interval between pings (in seconds): "))
    print(f"Pinging {host} every {interval} seconds...")
    automatic_pinger(host, interval)
