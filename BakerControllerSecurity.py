import os
import time
import sys
import pyAesCrypt
import pybase64
import sql
import sqlite3
import ctypes
import time 

os.system("cls")
print("Loading...")
time.sleep(5)
os.system("cls")

class bcolors:
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

rundirectory = os.path.dirname(os.path.abspath(__file__))
zonetime = time.time()
cryptotextrundirectory = pybase64.b64encode(b'rundirectory')

print("""
                    _ ____        _                ____            _             _ _             ____                       _ _         _                   
  _____ _____ _____| | __ )  __ _| | _____ _ __   / ___|___  _ __ | |_ _ __ ___ | | | ___ _ __  / ___|  ___  ___ _   _ _ __(_) |_ _   _| |_____ _____ _____ 
 |_____|_____|_____| |  _ \ / _` | |/ / _ \ '__| | |   / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__| \___ \ / _ \/ __| | | | '__| | __| | | | |_____|_____|_____|
 |_____|_____|_____| | |_) | (_| |   <  __/ |    | |__| (_) | | | | |_| | | (_) | | |  __/ |     ___) |  __/ (__| |_| | |  | | |_| |_| | |_____|_____|_____|
                   | |____/ \__,_|_|\_\___|_|     \____\___/|_| |_|\__|_|  \___/|_|_|\___|_|    |____/ \___|\___|\__,_|_|  |_|\__|\__, | |                  
                   |_|                                                                                                            |___/|_|

                   |*******************************************************************************************************************|
                   |                                                                                                                   |
                   |  Verison: 0.1              Gmail: ilyah@gmail.com                                                                 |
                   |  Author: IlyaHasandx       GitHubLink: https://github.com/IlyaHasan/Baker-Controller-Security                                  |
                   |                                                                                                                   |
                   |*******************************************************************************************************************|                                               
""")

time.sleep(3.0)

os.system("cls")

print(bcolors.CGREEN2 + "[OK]: Connection internet!" + bcolors.CGREEN2)
time.sleep(1.00)
print(bcolors.CGREEN2 + "[OK]: Connection MySQL DataBase for program!\n" + bcolors.CGREEN2)
print(bcolors.CGREY + """
=====================================
             CREATE FILES
=====================================
""" + bcolors.CGREY)
print(bcolors.CGREY + f"[Message]: Run Program of directory: {rundirectory}" + bcolors.CGREY)
time.sleep(1.00)

print(bcolors.CGREY + f"[Message]: Create folder .tmp" + bcolors.CGREY)
time.sleep(1.00)

os.mkdir(".tmp")
os.chdir(".tmp")

print(bcolors.CGREY + f"[Message]: Create file: runhash.tmp" + bcolors.CGREY)
time.sleep(1.00)

f=open(f"{zonetime}{cryptotextrundirectory}.tmp", 'a')
f.write(f"""
{rundirectory}
""")
f.close()

print(bcolors.CGREY + f"[Message]: Create folder: data" + bcolors.CGREY)
time.sleep(1.00)

os.mkdir("../data")

print(bcolors.CGREY + f"[Message]: Create folder sub: data/users_data" + bcolors.CGREY)
time.sleep(1.00)

os.chdir("../data")
os.mkdir("../data/users_data")

print(bcolors.CGREY + f"[Message]: Create folder sub: data/users_data/table_users_data" + bcolors.CGREY)
time.sleep(1.00)

os.chdir("../data/users_data")
os.mkdir("../users_data/table_users_data")

print(bcolors.CGREY + f"[Message]: Create folder  Documentation(docs)" + bcolors.CGREY)
time.sleep(1.00)

os.chdir("../../")
os.mkdir("docs")

print(bcolors.CGREY + f"[Message]: Make Documentation" + bcolors.CGREY)
time.sleep(.9)

os.chdir("docs")

print(bcolors.CGREY + f"[Message]: Everything was done successfully!, We wish you successful work with the program!\n" + bcolors.CGREY)
time.sleep(1.00)

os.system("pause")

os.system("color 7")
os.system("cls")


print("""
[1] - Login
[2] - Registration
""")

user = input(":> ")
