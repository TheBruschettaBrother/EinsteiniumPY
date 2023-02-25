# EinsteiniumPY
Python Library for pulling basic Scientific Info

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY)
[![GitHub contributors](https://img.shields.io/github/contributors/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheBruschettaBrother/EinsteiniumPY)](https://github.com/TheBruschettaBrother/EinsteiniumPY/commits/master)

Donations below
[![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)](https://mempool.space/address/bc1qk6l6s65q90s6gsfwp35h4gymxhxkt5x0fcq3p8)[![Tether USD](https://img.shields.io/badge/USDT-Tether%20USD-29B6AF?style=for-the-badge&logo=tether)](https://etherscan.io/address/0x872C3ea985120bE349182Ce8087442D5D51115a0)[![Nano](https://img.shields.io/badge/NANO-Nano-4A90E2?style=for-the-badge&logo=nano)](https://nano.org/)[![XRP](https://img.shields.io/badge/XRP-XRP-ED287B?style=for-the-badge&logo=xrp)](https://ripple.com/xrp/)[![Stellar](https://img.shields.io/badge/XLM-Stellar-08B6FF?style=for-the-badge&logo=stellar)](https://www.stellar.org/)[![Polkadot](https://img.shields.io/badge/DOT-Polkadot-E6007A?style=for-the-badge&logo=polkadot)](https://polkadot.network/)[![Chainlink](https://img.shields.io/badge/LINK-Chainlink-2C3E50?style=for-the-badge&logo=chainlink)](https://chain.link/)[![Dogecoin](https://img.shields.io/badge/DOGE-Dogecoin-C2A633?style=for-the-badge&logo=dogecoin)](https://dogecoin.com/)[![Dash](https://img.shields.io/badge/DASH-Dash-008DE4?style=for-the-badge&logo=dash)](https://dash.org/)[![Binance Token](https://img.shields.io/badge/BNB-Binance%20Token-F3BA2F?style=for-the-badge&logo=binance)](https://www.binance.com/en/trade/BNB_USDT)



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
**Exsample 1's Output**
```
Symbol: H
Atomic number: 1
Atomic mass: 1.008
Group: 1
Period: 1
Category: nonmetal
```

# Installation
Put the ```Einsteinium.py``` file into your scripts folder and Import the File as a library with
```import Einsteinium as einsteinium```

If You need help importing files as libraries use [how-to-import-a-library-in-python](https://codeberryschool.com/blog/en/how-to-import-a-library-in-python/) by [codeberryschool.com](codeberryschool.com)

# Functionality
as of now we have the .periodic_table_get function that can fetch about a certain element

## .periodic_table_get

The .periodic_table_get function can fetch the data about a element such as the, symbol(Eg."H"), atomic number(Eg. 1),atomic mass(Eg. 1.008),group(Eg. 1),period(1),category(Eg. nonmetal). 


We are working on adding all the elements of the elements to our index but for now we only have
- hydrogen
- lithium
- helium
