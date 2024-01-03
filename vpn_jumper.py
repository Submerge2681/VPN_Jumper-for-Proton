#!/usr/bin/env python3
import os
from time import sleep
import random
import subprocess

MIN_RANGE_IN_MIN = 15
MAX_RANGE_IN_MIN = 20

t1Countries = ["CH", "IS", "SE", "RO", "DE", "ES", "AT", "GR"]
t2Countries = ["PT", "IT", "IE", "NL", "BE", "LU", "DK", "NO", "FI", "CZ", "HU", "HR", "MT", "RS"]
t3Countries = ["FR", "BR", "CL", "CO", "EE", "LV", "LT", "PL", "HK", "IN", "MD", "MA", "MK", "SG", "SK", "SL", "ZA", "VN"]
countryList = t1Countries #+ t2Countries + t3Countries

previousCountry = ''

# Random country
def randomCountry ():
  global previousCountry
  newCountry = random.choice (countryList)
  if newCountry == previousCountry:
    while newCountry == previousCountry:
      newCountry = random.choice (countryList)
  previousCountry = newCountry
  print ("\n# Changing the IP Address...")
  return newCountry

# Main
try:
  os.system ("protonvpn-cli killswitch --permanent")
  while True:
    country = randomCountry()
    subprocess.run(["protonvpn-cli", "connect", "--cc", country], timeout=60, check=True)
    status = os.system ("protonvpn-cli status")
    if status == 0:
      sleep (random.randrange (MIN_RANGE_IN_MIN*60,MAX_RANGE_IN_MIN*60))
except Exception as e:
      print (f"Error occurred: {str (e)}\n Exiting...")
finally:
  os.system ("protonvpn-cli disconnect")
  os.system ("protonvpn-cli killswitch --off")
