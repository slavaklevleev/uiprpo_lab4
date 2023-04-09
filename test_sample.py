from prog import *

def test_check_age():
    assert check_age(130) == "-"
    assert check_age(0) == '0'
    assert check_age(-1) == '-'
    assert check_age(55) == '55'

def test_check_phone():
    assert check_phone('+3552611586340') == '+355 (261) 158-63-40'
    assert check_phone('+79103424180') == '+7 (910) 342-41-80'
    assert check_phone('+0') == '-'

def test_check_email():
    assert check_email('slava.klevleev@gmail.com') == 'slava.klevleev@gmail.com'
    assert check_email('slava.klevleev@@gmail..com') == 'slava.klevleev@gmail.com'
    assert check_email('slava.klevleev@@gmail') == '-'