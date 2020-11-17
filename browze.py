#!/usr/bin/env python3
# Written by GroTEK
# Icon by: Freepik http://www.freepik.com"

import webbrowser, sys, os, math

from colorama import Fore, Back, Style

banner = Fore.CYAN + '''
 /$$                                                            
| $$                                                            
| $$$$$$$   /$$$$$$   /$$$$$$  /$$  /$$  /$$ /$$$$$$$$  /$$$$$$ 
| $$__  $$ /$$__  $$ /$$__  $$| $$ | $$ | $$|____ /$$/ /$$__  $$
| $$  \ $$| $$  \__/| $$  \ $$| $$ | $$ | $$   /$$$$/ | $$$$$$$$
| $$  | $$| $$      | $$  | $$| $$ | $$ | $$  /$$__/  | $$_____/
| $$$$$$$/| $$      |  $$$$$$/|  $$$$$/$$$$/ /$$$$$$$$|  $$$$$$$
|_______/ |__/       \______/  \_____/\___/ |________/ \_______/
''' + Style.RESET_ALL

def Browser():
    counter = 0
    cur_iteration = 0
    totallines = sum(1 for line in open(iplist))
    int(totallines)
    iterations = math.ceil(totallines / tabs)
    print("There will be " + str(iterations) + " batches to go through." )
    if protocol in ("HTTP","http"):
        with open(iplist, 'r') as f:
            for line in f.readlines():
                webbrowser.open_new_tab(protocol + "://" + line.strip() + ":" + port)
                counter += 1
                if counter < tabs:
                    pass
                else:
                    cur_iteration += 1
                    maxTabsMessage = input(Fore.YELLOW +"[+]"+" Open next group? Batch ("+str(cur_iteration)+" of "+str(iterations)+ "). " + Style.RESET_ALL)
                    if maxTabsMessage in ("yes", "y"):
                        counter = 0
                        webbrowser.open_new_tab(protocol + "://" + line.strip() + ":" + port)
                        continue
                    else:
                        print("Godspeed, Friendo.")
                        sys.exit()
                continue
            f.close()
        print("End of list. Godspeed, Friendo.")

    if protocol in ("HTTPS","https"):
        with open(iplist, 'r') as f:
            for line in f.readlines():
                webbrowser.open_new_tab(protocol + "://" + line.strip() + ":" + port)
                counter += 1
                if counter < tabs:
                    pass
                else:
                    cur_iteration += 1
                    maxTabsMessage = input(Fore.YELLOW +"[+]"+" Open next group? Batch ("+str(cur_iteration)+" of "+str(iterations)+ "). " + Style.RESET_ALL)
                    if maxTabsMessage in ("yes", "y"):
                        counter = 0
                        webbrowser.open_new_tab(protocol + "://" + line.strip() + ":" + port)
                        continue
                    else:
                        print("Godspeed, Friendo.")
                        sys.exit()
                continue
            f.close()
        print("End of list. Godspeed, Friendo.")

    if protocol in ("FTP","ftp"):
        with open(iplist, 'r') as f:
            for line in f.readlines():
                webbrowser.open(str(protocol + "://" + line.strip() + ":" + port), new=2)
                counter += 1
                if counter < tabs:
                    pass
                else:
                    cur_iteration += 1
                    maxTabsMessage = input(Fore.YELLOW +"[+]"+" Open next group? Batch ("+str(cur_iteration)+" of "+str(iterations)+ "). " + Style.RESET_ALL)
                    if maxTabsMessage in ("yes", "y"):
                        counter = 0
                        webbrowser.open_new_tab(protocol + "://" + line.strip() + ":" + port)
                        continue
                    else:
                        print("Godspeed, Friendo.")
                        sys.exit()
                continue
            f.close()
        print("End of list. Godspeed, Friendo.")

def Selector():
    global iplist, protocol, port, tabs
    iplist = input(Fore.GREEN +"[+]"+ " List location: " + Style.RESET_ALL)
    protocol = input(Fore.GREEN +"[+]"+ " Protocol type: (HTTP/S, FTP, SSH): " + Style.RESET_ALL)
    if protocol in ("HTTP", "http", "HTTPS", "https","FTP", "ftp", "SSH", "ssh"):
        if protocol in ("HTTP", "http", "HTTPS", "https"):
            port = input(Fore.GREEN +"[+]"+" Specific port: " + Style.RESET_ALL)
        elif protocol in ("FTP", "ftp"):
            ftpoption = input(Fore.GREEN +"[+]"+" Do you want to open this in a browser or terminal? " + Style.RESET_ALL)
            if ftpoption in ("Browser", "browser"):
                port = ""
                pass
            else:
                print("put terminal method here.")
                port = ""
        elif protocol in ("SSH", "ssh"):
            print("put terminal method here.")
            port =""
        else:
            print(Fore.RED +"[+]"+" No known protocol selected. Exiting." + Style.RESET_ALL)
            sys.exit()
    else:
        print(Fore.RED + "[+]" + " No known protocol selected. Exiting." + Style.RESET_ALL)
        sys.exit()
    tabs = int(input(Fore.GREEN +"[+]"+" How many tabs do you want open at a time? "+Style.RESET_ALL))
    if tabs > 100:
        conf = str(input(Fore.YELLOW +"[!]"+ " You sure about that, cowboy? These tabs are hungrier than some hippos. " + Style.RESET_ALL))
        if conf in ("yes", "y", "yep", "yepperino"):
            tabs = int(input("How many tabs do you want, then? "))
    print("\nFormat will be " + Fore.GREEN + protocol + Style.RESET_ALL + "://IPAddress:" + Fore.YELLOW + str(
        port) + Style.RESET_ALL + " with " + Fore.CYAN + str(tabs) + Style.RESET_ALL + " tabs. \n")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print("Welcome to browze, by GroTEK.\n\n This is a simple script to open a list containing IP Addresses and quickly\n open then in a terminal/browser.\n")
    Selector()
    Browser()
    # Viewer()
    sys.exit()
