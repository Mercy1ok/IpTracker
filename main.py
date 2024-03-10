import os
import pyfiglet

try:
    import requests
except:
    os.system("pip install requests")
try:
    import colorama
except:
    os.system("pip install colorama")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
from colorama import *

auth = '1840e53e-0a8b-4d4d-b4e6-4d34d1033d91';
import time as t

t.sleep(2)
os.system("clear")



def loop():
    head = pyfiglet.figlet_format("__")
    os.system("clear")
    print(Fore.BLACK + head)
    print(Fore.RED + """    
██╗     ██╗██╗   ██╗███████╗
██║     ██║██║   ██║██╔════╝
██║     ██║██║   ██║█████╗  
██║     ██║╚██╗ ██╔╝██╔══╝  
███████╗██║ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═══╝  ╚══════╝ V1.0                                                                                                                                              
   ┌┬┐┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
    │ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
    ┴ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─ """)

    print(Fore.WHITE + """                                                                                                                       
 ============================================== """)
    print(Fore.RED + """
[+]Author  : Hamooda[+]
[+]GitHub  : https://github.com/Mercy1ok[+]""")

    print(Fore.WHITE + """ ==============================================""")
    # print("Usage:Iptracker [Ip address]\n\nExample:Iptracker our prsnal ip")
    print(Fore.WHITE + """
    Type \"show\" to show all command """)

    def track():
        tip = input(Fore.RED + "Iptracker > " + Style.RESET_ALL)
        if tip == "help":
            print(Fore.BLACK + """
            show :  Its Display all commands
            iptracker :  This is used for tracking an Ip address
            help :  Its display how to use this tool
            exit : For quitting ip tracker

            update:  Its update Ip-Tracker automatically 
            """)
            track()
        elif tip == "show":
            print(Fore.BLACK + """


            These are all the available commands
            help
            show
            exit
            iptracker
            update
            """)
            track()
        elif tip == "exit":
            print(
                Fore.BLACK + "Till next time")
            exit()
        elif tip == "iptracker":
            print(Fore.RED + """________________________________Track Ip____________________________""")
            print("""
            """)

            ip = (input(Fore.WHITE + Back.BLACK + "Enter IP Address : " + Style.RESET_ALL + ""))
            print(Fore.BLACK + " Fetching data from " + ip)

            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                    "Ip Address": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name"),
                    "Ip Address Type": response.get("version"),
                    "Region Code": response.get("region_code"),
                    "Postal Code": response.get("postal"),
                    "Latitude": response.get(str("latitude")),
                    "Longitude": response.get(str("longitude")),
                    "TimeZone": response.get("timezone"),
                    "Country code": response.get("country_calling_code"),
                    "Currency": response.get("currency"),
                    "Currency Name": response.get("currency_name"),
                    "Languages": response.get("languages"),
                    "Country Area": response.get("country_area"),
                    "Population": response.get("country_population"),
                    "ASN": response.get("asn"),
                    "Organization": response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat + "," + long + "/@" + lat + "," + long + ",16z"

                return location_data

            print(Fore.BLACK, get_location())
            print(Fore.BLACK + "\nGoogle Maps: " + Fore.RED + url)
            opn = "xdg-open " + url
            map = input(Fore.BLACK + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
            if map == "yes" or map == "Yes":
                os.system(opn)

        elif tip == "update":
            print(Fore.BLACK + "Updating Ip Tracker")
            os.system("""
            cd
            rm -f -r Ip-Tracker
            https://github.com/Mercy1ok

            """)

            print(Fore.BLACK + """Now type the following command
            cd $HOME
            cd Ip-Tracker
            python3 tracker.py
            """)
            exit()
        else:
            print(Fore.BLACK + "Invalid Command!")
            t.sleep(3)
            track()

    track()

    cont = input(
        "\n\n" + Fore.BLACK + Back.BLACK + "Would you like to track another IP address? [y/n] " + Style.RESET_ALL + " ")
    if cont == "y" or cont == "Y":
        loop()
    else:
        exit()

loop()