#!/usr/bin/env python3

import os
from time import sleep
import random

codeList = ["CH", "IS", "SE", "RO", "DE", "ES", "AT", "GR"] #Switzerland(CH), Iceland(IS), Sweden(SE), Romania(RO), Germany(DE), Spain(ES), Austria(AT), Greece(GR)
#Germany, Sweden and spain are part of the 14 eyes.
try:
  os.system("protonvpn-cli killswitch --on")
  os.system("protonvpn-cli connect -f") ###Connects to the fastest server!
  os.system("protonvpn-cli status")
  while True:
    codeChoice = random.choice(codeList)
    sleep(random.randrange(600,900))
    print("#Changing the IP Address...")
    os.system("protonvpn-cli connect " + "--cc " + codeChoice)  #Concatinate Proton commands with country code(--cc) from the codelist!
    os.system("protonvpn-cli status")
except:
  os.system("protonvpn-cli killswitch --off")
  os.system("protonvpn-cli disconnect")
  print("Error occured")
