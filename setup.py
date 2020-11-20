import os
import time
import sys
import pyAesCrypt
import pybase64

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

print(bcolors.CGREY + """
=====================================
             BE GEN SETUP
=====================================
""" + bcolors.CGREY)

print(bcolors.CGREY + f"[Message]: Create folder .tmp" + bcolors.CGREY)
time.sleep(1.00)

os.mkdir(".tmp")

print(bcolors.CGREY + f"[Message]: Create folder: data" + bcolors.CGREY)
time.sleep(1.00)

os.mkdir("data")

print(bcolors.CGREY + f"[Message]: Create folder sub: data/users_data" + bcolors.CGREY)
time.sleep(1.00)

os.chdir("data")
os.mkdir("data/users_data")

print(bcolors.CGREY + f"[Message]: Create folder sub: data/users_data/table_users_data" + bcolors.CGREY)
time.sleep(1.00)

os.chdir("data/users_data")
os.mkdir("users_data/table_users_data")

print(bcolors.CGREY + f"[Message]: Create folder  Documentation(docs)" + bcolors.CGREY)
time.sleep(1.00)

os.mkdir("docs")

print(bcolors.CGREY + f"[Message]: Make Documentation" + bcolors.CGREY)
time.sleep(.9)

os.chdir("docs")

print(bcolors.CGREY + f"[Message]: Everything was done successfully!, We wish you successful work with the program!\n" + bcolors.CGREY)
time.sleep(1.00)

os.system("pause")

os.system("color 7")
os.system("cls")