# EinsteiniumPY
Python Library for pulling basic Scientific Info

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY)
[![GitHub contributors](https://img.shields.io/github/contributors/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/commits/master)

## Donations below

[![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://mempool.space/address/bc1qk6l6s65q90s6gsfwp35h4gymxhxkt5x0fcq3p8)[![Tether USD](https://img.shields.io/badge/USDT-Tether%20USD-29B6AF?style=for-the-badge&logo=tether)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Nano](https://img.shields.io/badge/NANO-Nano-4A90E2?style=for-the-badge&logo=nano)](https://www.nanolooker.com/account/nano_1sc1dd1p6gi95i1sueposfbub1p9pxuuoqi8ttyjrfernuchrueqsxpfn48r)[![XRP](https://img.shields.io/badge/XRP-XRP-ED287B?style=for-the-badge&logo=xrp)](https://xrpscan.com/account/rHRLASZHdw3NWHsz1Vbk3Uz5ujXDEBTaQE)[![Stellar](https://img.shields.io/badge/XLM-Stellar-08B6FF?style=for-the-badge&logo=stellar)](https://stellar.expert/explorer/public/account/GDLSW7LQCBSZCEOHV4SDQDYEZ7PUV4SEDQ3DNQDMWCBCAP3M7L24MNJI)[![Chainlink](https://img.shields.io/badge/LINK-Chainlink-2C3E50?style=for-the-badge&logo=chainlink)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Dogecoin](https://img.shields.io/badge/DOGE-Dogecoin-C2A633?style=for-the-badge&logo=dogecoin)](https://blockchair.com/dogecoin/address/DTz1Uns3958e6N3ZJUMbbZxmL5GFPZwFwj)[![Dash](https://img.shields.io/badge/DASH-Dash-008DE4?style=for-the-badge&logo=dash)](https://blockchair.com/dash/address/XuoFyPKKge6heyQDmbmHBx23FvDZJYGk4M)


## Example 
```import Einsteinium as einsteinium
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
    print("Element not found.")```

**Example's Output**

```Symbol: H
Atomic number: 1
Atomic mass: 1.008
Group: 1
Period: 1
Category: nonmetal```

# Installation
Put the ```Einsteinium.py``` file into your scripts folder and Import the File as a library with
```import Einsteinium as einsteinium```

If You need help importing files as libraries use [how-to-import-a-library-in-python](https://codeberryschool.com/blog/en/how-to-import-a-library-in-python/) by [codeberryschool.com](codeberryschool.com)

# Functionality
We have the .periodic_table_get function that can fetch about a certain element and the .particle_info_get Which gets info about a certain particle and its charge,mass,symbol

## .particle_info_get
The .particle_info_get Is limited but can get the Symbol,Charge and mass of over 10 types of particles. This is very Limited right now and we are working on it.
## Example
```import Einsteinium as einsteinium
# Get information about a proton
proton_info = einsteinium.particle_info_get('proton')

# Print the information
print(f"Symbol: {proton_info['symbol']}")
print(f"Charge: {proton_info['charge']}")
print(f"Mass: {proton_info['mass']}")```

**Example's Output*

```Symbol: p+
Charge: 1
Mass: 1.007276466879 kg```

## .periodic_table_get

The .periodic_table_get function can fetch the data about a element such as the, symbol(Eg."H"), atomic number(Eg. 1),atomic mass(Eg. 1.008),group(Eg. 1),period(1),category(Eg. nonmetal). 

We have a Index of all 118 elements in the periodic table
## Example 1
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
**Example's Output**
```
Symbol: H
Atomic number: 1
Atomic mass: 1.008
Group: 1
Period: 1
Category: nonmetal
```
