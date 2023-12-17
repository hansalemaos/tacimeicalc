import random


def checksum(number, alphabet="0123456789"):
    r"""Calculate the Luhn checksum of a number.

    Args:
        number (int or str): The number for which to calculate the checksum.
        alphabet (str, optional): The alphabet used for the checksum calculation.
            Defaults to "0123456789".

    Returns:
        int: The Luhn checksum of the number.
    """
    n = len(alphabet)
    number = tuple(alphabet.index(i) for i in reversed(str(number)))
    return (sum(number[::2]) + sum(sum(divmod(i * 2, n)) for i in number[1::2])) % n


def calc_check_digit(number, alphabet="0123456789"):
    r"""Calculate the Luhn check digit for a given number.

    Args:
        number (int or str): The number for which to calculate the check digit.
        alphabet (str, optional): The alphabet used for the checksum calculation.
            Defaults to "0123456789".

    Returns:
        str: The Luhn check digit as a string.
    """
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]


def calculate_phone_data(tac, mcc_number, mnc_number, mac_prefix, line_country, phonenumber):
    """Generate phone-related data including IMSI, IMEI, ICCID, MAC address, and phone number.

    Args:
        tac (str): Type Allocation Code.
        mcc_number (int): Mobile Country Code number.
        mnc_number (int): Mobile Network Code number.
        mac_prefix (str): MAC address prefix.
        line_country (int): Line country code.
        phonenumber (str): Phone number.

    Returns:
        dict: A dictionary containing phone-related data.
    """
    imsi = str(str(mcc_number) + str(mnc_number) + phonenumber)[:15]

    imei = (tac + str(random.randint(0, 999999)).zfill(6))[:14]

    checknumberimei = calc_check_digit(imei, alphabet="0123456789")
    imei = imei + checknumberimei

    iccid = str(
        "89"
        + (str(line_country) + "0" * 6)[:6]
        + str(mnc_number)
        + (str(phonenumber) + 12 * "0")[:10]
    )[:19]
    iccid += calc_check_digit(iccid)

    macaddressprefix = mac_prefix
    totallen = 17
    macaddressprefixlen = totallen - len(macaddressprefix)
    macaddress = (
        str(macaddressprefix)
        + (":%02x:%02x:%02x" % tuple(random.randint(0, 255) for v in range(3)))[
            -macaddressprefixlen:
        ]
    ).upper()
    return dict(
        imsi=imsi,
        imei=imei,
        iccid=iccid,
        macaddress=macaddress,
        phone_number=(str(line_country)) + phonenumber,
    )
