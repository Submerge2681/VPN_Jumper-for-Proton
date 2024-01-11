#!/usr/bin/env python3
from time import sleep
import random
import subprocess

MIN_RANGE_IN_MIN = 20
MAX_RANGE_IN_MIN = 30
FAIL_CONDITION = 3
T1_COUNTRIES = ["CH", "IS", "SE", "RO", "DE", "ES", "AT", "GR"]
T2_COUNTRIES = ["PT", "IT", "IE", "NL", "BE", "LU", "DK", "NO", "FI", "CZ", "HU", "HR", "MT", "RS"]
T3_COUNTRIES = ["FR", "BR", "CL", "CO", "EE", "LV", "LT", "PL", "HK", "IN", "MD", "MA", "MK", "SG", "SK", "SL", "ZA", "VN"]
COUNTRY_LIST = T1_COUNTRIES #+ T2_COUNTRIES + T3_COUNTRIES

previousCountry = ""
failCount = 0

# Random country
def randomCountry():
  global previousCountry
  newCountry = random.choice (COUNTRY_LIST)
  if newCountry == previousCountry:
    while newCountry == previousCountry:
      newCountry = random.choice (COUNTRY_LIST)
  previousCountry = newCountry
  print ("\n# Changing the IP Address...")
  return newCountry

# Connect
def connect(min, max):
  global failCount
  if failCount <= FAIL_CONDITION:
    country = randomCountry()
    subprocess.run(["protonvpn-cli", "connect", "--cc", country], timeout=60, check=True)
    status = subprocess.run(["protonvpn-cli", "status"], check=True)
    if status.returncode > 0:
      failCount += 1
      print (f"\n# Connection failed {failCount} times. Retrying...")
    else:
      failCount = 0
      sleep (random.randrange (min*60,max*60))
      connect(min, max)

# Main
try:
  connect(MIN_RANGE_IN_MIN, MAX_RANGE_IN_MIN)
except Exception as e:
      print (f"\nError occurred: {str (e)}\n Exiting...")
finally:
  subprocess.run(["protonvpn-cli", "disconnect"])
