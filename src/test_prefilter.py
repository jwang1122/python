from physics import Q

def test_format():
    a = Q('1.45 m')
    s = "{}".format(a)
    print(s)
    assert s == '1.45 m'
    s = "{:.4E}".format(a)
    print(s)
    assert s == '1.4500E+00 m'
    s = "{.value}".format(a)
    print(s)
    assert s == '1.45'
    s = "%s" % a
    print(s)
    assert s == '1.45 m'

if __name__ == '__main__':
    test_format()
