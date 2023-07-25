#################################
# Date          : 26.07.2023    #
# Programmer    : cpu-astatine  #
# Project       : H A S H I N G #
################################# 

import os
import hashlib
import time

os.system("clear")
while True:
    try:
        print("###############################################")
        print("# H A S H I N G                               #")
        print("# Coded by cpu-astatine                       #")
        print("# Note : This program can only be encoding    #")
        print("# Note - 2 : Exist CTRL + C                   #")
        print("# Enjoy!                                      #")
        print("###############################################")
        input()
        print("\n")

        text = input("Please write something > ")
        message = text.encode()
        sha256 = hashlib.sha256(message).hexdigest()
        md5 = hashlib.md5(message).hexdigest()
        print("\n")

        print(f"Normal Text      : {text}")
        print(f"SHA256           : {sha256}")
        print(f"MD5              : {md5}")
        input()
        os.system("clear")
            
    except KeyboardInterrupt:
        print("Exiting...")
        time.sleep(2)
        os.system("clear")
        break
