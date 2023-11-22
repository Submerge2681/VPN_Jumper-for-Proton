#!/usr/bin/env python3
import os
from time import sleep
import random

codeList = ["CH", "IS", "SE", "RO", "DE", "ES", "AT", "GR"] #Switzerland(CH), Iceland(IS), Sweden(SE), Romania(RO), Germany(DE), Spain(ES), Austria(AT), Greece(GR)
#Germany, Sweden and spain are part of the 14 eyes.

previous = ''

def lottery():
  global previous
  codeChoice = random.choice(codeList)
  if codeChoice == previous:
    while codeChoice == previous:
      codeChoice = random.choice(codeList)
  previous = codeChoice
  print("\n#Changing the IP Address...")
  return codeChoice

try:
  while True:
    os.system("protonvpn-cli connect  --cc " + lottery())  #Concatinate Proton commands with country code(--cc) from the codelist
    os.system("protonvpn-cli status")
    sleep(random.randrange(600,900))
except Exception as e:
  print("Error occured")
  print(f"{str(e)}")
finally:
  os.system("protonvpn-cli disconnect")
