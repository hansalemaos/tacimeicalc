# Generates phone-related data including IMSI, IMEI, ICCID, MAC address, and phone number

## pip install tacimeicalc

### Tested against Windows / Python 3.11 / Anaconda


```python

Generates phone-related data including IMSI, IMEI, ICCID, MAC address, and phone number.

    Args:
        tac (str): Type Allocation Code.
        mcc_number (int): Mobile Country Code number.
        mnc_number (int): Mobile Network Code number.
        mac_prefix (str): MAC address prefix.
        line_country (int): Line country code.
        phonenumber (str): Phone number.

    Returns:
        dict: A dictionary containing phone-related data.
from tacimeicalc import calculate_phone_data
phonedata=calculate_phone_data(tac='35440811', mcc_number=724, mnc_number=11, mac_prefix='00:0A:00', line_country=55, phonenumber='82984743677')
print(phonedata)
# {'imsi': '724118298474367', 'imei': '354408113368770', 'iccid': '89550000118298474360', 'macaddress': '00:0A:00:89:83:3A', 'phone_number': '5582984743677'}
```