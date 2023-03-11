version='2.3.0'
import os
import sys
import time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
full=red+"\n\n\n\t\tYOUR DEVICE SYSTEM HAS ERROR!\n\n"
off=red+"\n\n\n\t\tYOU ARE BANNED FOR 4 HOURS PLEASE MEET THIS CREATOR OWNER\n\n"
delete=red+'\n\n\n\t\tYOUR DDOS-ATTACK SYSTEM IS UNISTALLING IN 5 SECOND\n\n'
line=yellow+"==============================================================="+end

logo=red+str("""\n\n\n    8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b\n\n""")+end
def header():
    print(logo+cyan+'\n\n\tDEVOLOPED BY : GHOST X0N4Y3M\n\n'+green+'\t\tVERSION : '+ str(version)+'\n\n'+end+line)

os.system('clear')
header()


print(cyan+'\n\t\t[•] CHECKING FOR UPDATES\n\t\t')
time.sleep(99.7)
r = requests.get("https://pastebin.com/raw/bTVAMH7X").text

if r=="on":
	os.system('cd $PREFIX/share/DDos-Attack && python2 ddos-attack.py')

