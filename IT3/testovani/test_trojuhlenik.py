from trojuhelnik import *

def test_trojuhelniku():
    assert lze_sestrojit(5, 6, 20) == False
    assert lze_sestrojit(3, 4, 5) == True
    assert lze_sestrojit(7, 12, 13) == True
    assert lze_sestrojit(10, 10, 10) == True

    