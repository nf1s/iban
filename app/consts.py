import string
from csv import DictReader


def parse_iban_csv():
    iban_mappin = {}
    with open("data/ibans.csv") as f:
        for line in DictReader(f):
            iban_mappin[line["country_code"]] = line
    return iban_mappin


IBAN_FORMATS_PER_COUNTRY = parse_iban_csv()

IBAN_CHAR_TO_NUM = {
    val: str(key) for key, val in enumerate(string.digits + string.ascii_uppercase)
}
