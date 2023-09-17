
#!/usr/bin/python

import os
import urllib.request
import json
from urllib import *
from platform import system
import sys
from datetime import datetime
import time


def t7ngprint(s):

    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)


def ipinfo():
       ip=input(" ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴠɪᴄᴛɪᴍ ɪᴘ : \033[1;32m ")
       url = ("http://ip-api.com/json/")
       response = urllib.request.urlopen(url + ip)
       data = response.read()
       values = json.loads(data)
       os.system("clear")

       print ("\033[1;32m\007\n")
       t7ngprint("\033[1;36m =====================================")
       t7ngprint("\033[1;91m|    ɪᴘ ɪɴғᴏs ᴛᴏᴏʟ ʙʏ 🦊 • ᴛ7ɴɢ       |")
       t7ngprint("\033[1;36m =====================================")
       
       t7ngprint("\033[1;36m" + "\n ɪᴘ ᴀᴅʀᴇss ʏᴏᴜ ᴇɴᴛᴇʀᴇᴅ : \033[1;32m " + values['query'])

       t7ngprint("\033[1;91m" + " ʀᴇɢɪᴏɴ      : \033[1;32m " + values['regionName'])
       t7ngprint("\033[1;91m" + " ᴄᴏᴜɴᴛʀʏ     : \033[1;32m " + values['country'])
       t7ngprint("\033[1;91m" + " ᴅᴀᴛᴇ & ᴛɪᴍᴇ : \033[1;32m " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       t7ngprint("\033[1;91m" + " ᴄɪᴛʏ        : \033[1;32m " + values['city'])
       t7ngprint("\033[1;91m" + " ɪsᴘ         : \033[1;32m " + values['isp'])
       t7ngprint("\033[1;91m" + " ʟᴀᴛɪᴛᴜᴅᴇ , ʟᴏɴɢɪᴛᴜᴅᴇ     : \033[1;32m " + str(values['lat']) + "," + str(values['lon']))
       t7ngprint("\033[1;91m" + " ᴢɪᴘᴄᴏᴅᴇ     : \033[1;32m " + values['zip'])
       t7ngprint("\033[1;91m" + " ᴛɪᴍᴇ ᴢᴏɴᴇ    : \033[1;32m " + values['timezone'])
       t7ngprint("\033[1;91m" + " ᴀs          : \033[1;32m " + values['as'] + "\n")
       print (" ")
       t7ngprint("\033[1;36m =====================================")
       t7ngprint("\033[1;91m|       ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ       |")
       t7ngprint("\033[1;36m =====================================")
       
       print (" ")
      
       vpp = input("\033[1;91m \033[1;91m")
       if vpp == " ":
                os.system("clear")
                return main()

       else:
            os.system("clear")
            return main()


def about():
       os.system("clear")
       print ("\033[1;32m\007\n")
       t7ngprint ("\033[1;91m -----------------------------------------------")
       t7ngprint ("\033[1;33m" + "         [+] ᴄʀᴇᴀᴛᴏʀ       =>\033[1;36m" + " 🦊 • T7ng")
       t7ngprint ("\033[1;33m" + "         [+] ɴᴀᴍᴇ ᴛᴏᴏʟ     =>\033[1;36m" + " ɪᴘ ɪɴғᴏs ᴛᴏᴏʟ")
       t7ngprint ("\033[1;33m" + "         [+] ᴠᴇʀsɪᴏɴ       =>\033[1;36m" + " 1.0")
       t7ngprint ("\033[1;33m" + "         [+] ᴜᴘᴅᴀᴛᴇ ᴅᴀᴛᴇ   =>\033[1;36m" + " 17/09/2023")
       t7ngprint ("\033[1;91m -----------------------------------------------")
       t7ngprint ("\033[1;95m" + "          [+] https://t.me/T7ngLua [+]          ")
       t7ngprint ("\033[1;91m -----------------------------------------------")
       magas = input("\033[1;32m [+] ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ [+]")
       if magas == " ":
           os.system("clear")
           return main()

       else:
           os.system("clear")
           return main()


def ext():
      t7ngprint("ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍʏ ᴛᴏᴏʟ")
      t7ngprint("ɪɴsᴛᴀɢʀᴀᴍ : s6x2ɴ")
      t7ngprint("ʏᴏᴜᴛᴜʙᴇ : ᴍ3ʀᴏO")
      time.sleep(1)
      exit()


def main():
      os.system("clear")
      

      t7ngprint("\033[1;91m-----------------------------------------------")
      t7ngprint("\033[1;91m          ɪᴘ ɪɴғᴏs ᴛᴏᴏʟ ʙʏ 🦊 • ᴛ7ɴɢ       ")
      t7ngprint("-----------------------------------------------")
      t7ngprint("")
      
      
      t7ngprint ("\033[1;34m [ 1 ]\033[1;20m ʟᴏᴄᴀʟɪᴛᴇ ᴀɴ ɪᴘ")
      t7ngprint ("\033[1;34m [ 2 ]\033[1;20m ɪɴғᴏs ᴄʀᴇᴀᴛᴏʀ")
      t7ngprint ("\033[1;34m [ 3 ]\033[1;20m ᴇxɪᴛ ᴛᴏᴏʟ")
      print("     ")
      option = input("\033[1;50m [😏] Choose an option : \033[1;32m")
      if option == "1":
          os.system("clear")
          ipinfo()
          exit()

      elif option == "3":
          os.system("clear")
          ext()
          exit()

      elif option == "2":
          os.system("clear")
          about()
          exit()

      else:
          os.system("clear")
          t7ngprint ("\033[1;91m ⚠️ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴄᴏʀʀᴇᴄᴛ ɴᴜᴍʙᴇʀ ⚠️")
          time.sleep(2)
          os.system("clear")
          return main()

main()
