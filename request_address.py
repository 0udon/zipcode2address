import requests
import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ZipCodeParam:
    zipcode: str


@dataclass_json
@dataclass
class Address:
    address1: str
    address2: str
    address3: str
    kana1: str
    kana2: str
    kana3: str
    prefcode: str
    zipcode: str


def request_address(zipcode: str):
    url = 'https://zipcloud.ibsnet.co.jp/api/search'
    params = ZipCodeParam(zipcode=zipcode)

    res = requests.get(url, params=params.to_dict())
    data = json.loads(res.text)

    results = data['results']

    addresses = [Address(**result) for result in results]
    address = addresses[0]

    return address


if __name__ == '__main__':
    zipcode = '7830060'
    address = request_address(zipcode)
    print(address)
