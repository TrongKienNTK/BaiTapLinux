#Python 3.6.x
import math

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
phepToan = input("Nhap phep toan (+, -, *, /, %, **): ")

def _Cong(a, b):
    return a + b
def _Tru(a, b):
    return a - b
def _Nhan(a, b):
    return a * b
def _Chia(a, b):
    return a / b
def _ChiaDu(a, b):
    return a % b
def _LuyThua(a, b):
    return math.pow(a, b)

if phepToan == "+":
    print("a + b = ", _Cong(a, b))
else:
    if phepToan == "-":
        print("a - b = ", _Tru(a, b))
    else:
        if phepToan == "*":
            print("a * b = ", _Nhan(a, b))
        else:
            if phepToan == "/":
                print("a / b = ", _Chia(a, b))
            else:
                if phepToan == "%":
                    print("a % b = ", _ChiaDu(a, b))
                else:
                    if phepToan == "**":
                        print("a ** b = ", _LuyThua(a, b))
                    else:
                        print("Phep toan khong hop le!")


