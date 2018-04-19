#Python 3.6.x
try:
    n = int(input("Nhap n: "))
    if n <= 0:
        exit()
except:
    print("n phai la so nguyen va n > 0!")
    exit()
arr = []
for i in range(n):
    arr.append(i + 1)

print("Day so:", arr)
def tongChan(arr, n):
    tong = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            tong += arr[i]
    return tong

print("Trong cac so chan trong day so =", tongChan(arr, n))