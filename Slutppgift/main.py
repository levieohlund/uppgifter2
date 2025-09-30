import psutil
import time
import os

def display_usage(usage):
    print(f"CPU Usage: {usage[0]}%")
    print(f"Memory Usage: {usage[1]}%")
    print(f"Disk Usage: {usage[2]}%")
    break
time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    
while True:
    display_usage((psutil.cpu_percent(), psutil.virtual_memory().percent, 30))

    def main_menu ():
        while True:
            print("\nMain menu")
            print("1. View system information")
            print("2. list of surrveliance")
            print("3. Quit Menu")
            choice = input("\n Choose an option")