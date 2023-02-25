# EinsteiniumPY
Python Library for Pulling/Processing basic Scientific Info

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY)
[![GitHub contributors](https://img.shields.io/github/contributors/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/commits/master)

## Donations below

[![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://mempool.space/address/bc1qk6l6s65q90s6gsfwp35h4gymxhxkt5x0fcq3p8)[![Tether USD](https://img.shields.io/badge/USDT-Tether%20USD-29B6AF?style=for-the-badge&logo=tether)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Nano](https://img.shields.io/badge/NANO-Nano-4A90E2?style=for-the-badge&logo=nano)](https://www.nanolooker.com/account/nano_1sc1dd1p6gi95i1sueposfbub1p9pxuuoqi8ttyjrfernuchrueqsxpfn48r)[![XRP](https://img.shields.io/badge/XRP-XRP-ED287B?style=for-the-badge&logo=xrp)](https://xrpscan.com/account/rHRLASZHdw3NWHsz1Vbk3Uz5ujXDEBTaQE)[![Stellar](https://img.shields.io/badge/XLM-Stellar-08B6FF?style=for-the-badge&logo=stellar)](https://stellar.expert/explorer/public/account/GDLSW7LQCBSZCEOHV4SDQDYEZ7PUV4SEDQ3DNQDMWCBCAP3M7L24MNJI)[![Chainlink](https://img.shields.io/badge/LINK-Chainlink-2C3E50?style=for-the-badge&logo=chainlink)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Dogecoin](https://img.shields.io/badge/DOGE-Dogecoin-C2A633?style=for-the-badge&logo=dogecoin)](https://blockchair.com/dogecoin/address/DTz1Uns3958e6N3ZJUMbbZxmL5GFPZwFwj)[![Dash](https://img.shields.io/badge/DASH-Dash-008DE4?style=for-the-badge&logo=dash)](https://blockchair.com/dash/address/XuoFyPKKge6heyQDmbmHBx23FvDZJYGk4M)

# Installation
Put the ```Einsteinium.py``` file into your scripts folder and Import the File as a library with
```import Einsteinium as einsteinium```

If You need help importing files as libraries use [how-to-import-a-library-in-python](https://codeberryschool.com/blog/en/how-to-import-a-library-in-python/) by [codeberryschool.com](codeberryschool.com)

# Functionality
-.periodic_table_get fetch about a certain periodic table element

-.particle_info_get Which gets info like charge,mass,symbol about a type of particle

## .particle_info_get
The .particle_info_get Is limited but can get the Symbol,Charge and mass of over 10 types of particles. This is very Limited right now and we are working on it.
## Example
```
import Einsteinium as einsteinium

proton_info = einsteinium.particle_info_get('proton')

# Print the information
print(f"Symbol: {proton_info['symbol']}")
print(f"Charge: {proton_info['charge']}")
print(f"Mass: {proton_info['mass']}")
```

**Exsample Output**
```
Symbol: p+
Charge: 1
Mass: 1.007276466879
```

## .periodic_table_get

The .periodic_table_get function can fetch the data about a element such as the, symbol(Eg."H"), atomic number(Eg. 1),atomic mass(Eg. 1.008),group(Eg. 1),period(1),category(Eg. nonmetal). 

We have a Index of all 118 elements in the periodic table
## Example
```
import Einsteinium as einsteinium
element_name = "hydrogen"
element_info = einsteinium.periodic_table_get(element_name)
if element_info:
    print(f"Symbol: {element_info['symbol']}")
    print(f"Atomic number: {element_info['atomic number']}")
    print(f"Atomic mass: {element_info['atomic mass']}")
    print(f"Group: {element_info['group']}")
    print(f"Period: {element_info['period']}")
    print(f"Category: {element_info['category']}")
else:
    print("Element not found.")
```
**Example Output**
```
Symbol: H
Atomic number: 1
Atomic mass: 1.008
Group: 1
Period: 1
Category: nonmetal
```

## .Kelvin2Celsius
the Kelvin2Celsius Converts Kelvin to Celsius, quite straightforward.
## Example
```
import Einsteinium as einsteinium
kelvin_temp = 300.0  # Temperature in Kelvin
celsius_temp = einsteinium.Kelvin2Celsius(kelvin_temp)  # Convert to Celsius
print(celsius_temp)
```
**Example Output**

```26.850000000000023```

## .Celsius2Kelvin
the Celsius2Kelvin Converts Kelvin to Celcuis, quite straightforward.
## Example
```
import Einsteinium as einsteinium
celsius_temp = 100.0  # Temperature in Celsius
kelvin_temp = einsteinium.Celsius2Kelvin(celsius_temp)  # Convert to Kelvin
print(kelvin_temp) 
```
**Example Output**

```373.15```

## .Fahrenheit2Celsius
the Fahrenheit2Celsius Converts Fahrenheit to Celcuis, quite straightforward.
## Example
```
import Einsteinium as einsteinium
fahrenheit_temp = 77.0  # Temperature in Fahrenheit
celsius_temp = einsteinium.Fahrenheit2Celsius(fahrenheit_temp)  # Convert to Celsius
print(celsius_temp)
```
**Example Output**

```25.0```

## .Celsius2Fahrenheit
the Celsius2Fahrenheit Converts Celcuis to Fahrenheit, quite straightforward.
## Example
```
import Einsteinium as einsteinium
celsius_temp = 25.0  # Temperature in Celsius
fahrenheit_temp = einsteinium.Celsius2Fahrenheit(celsius_temp)  # Convert to Fahrenheit
print(fahrenheit_temp)  
```
**Example Output**

```77.0```

## .Meter2Feet
the Meter2Feet Converts Meters to Feet, quite straightforward.
## Example
```
import Einsteinium as einsteinium
meters = 10.0  # Length in meters
feet = einsteinium.Meter2Feet(meters)  # Convert to feet
print(feet)
```
**Example Output**

```32.8084```

## .Meter2Feet
the Meter2Feet Converts Meters to Feet, quite straightforward.
## Example
```
import Einsteinium as einsteinium
meters = 10.0  # Length in meters
feet = einsteinium.Meter2Feet(meters)  # Convert to feet
print(feet)
```
**Example Output**

```32.8084```
## .Feet2Meter
the Feet2Meter Converts Feet to Meter.
## Example
```
import Einsteinium as einsteinium
feet = 32.8084  # Length in feet
meters = einsteinium.Feet2Meter(feet)  # Convert to meters
print(meters)     
```
**Example Output**

```10.0```

## .Kg2Pound
the Kg2Pound Converts Kg to Pound.
## Example
```
kg = 75.0  # Weight in kilograms
pounds = Kg2Pound(kg)  # Convert to pounds
print(pounds)
```

**Example Output**
```165.3465```

## .Pound2Kg

```Pound2kg converts Pound to Kg
## Example
pounds = 165.3465  # Weight in pounds
kg = pound2kg(pounds)  # Convert to kilograms
print(kg)
```

**Example Output**

```75.0```
