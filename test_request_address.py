from request_address import request_address


def test_request_address():
    zipcode = '7830060'

    address = request_address(zipcode)

    assert address.address1 == '高知県'
    assert address.address2 == '南国市'
    assert address.address3 == '蛍が丘'
    assert address.kana1 == 'ｺｳﾁｹﾝ'
    assert address.kana2 == 'ﾅﾝｺｸｼ'
    assert address.kana3 == 'ﾎﾀﾙｶﾞｵｶ'
    assert address.prefcode == '39'
    assert address.zipcode == '7830060'
