#Python 3.6.x

from bai4_classKhoa import Khoa
from bai4_classSV import SinhVien

DSSV = []
DSSV.append(SinhVien("001", "Mai A", "01"))
DSSV.append(SinhVien("002", "Tran B", "01"))
DSSV.append(SinhVien("003", "Tran C", "02"))
DSSV.append(SinhVien("004", "Thi K", "001"))
print("MSSV \t\t Ho ten \t Ma khoa")
for i in DSSV:
    i.xuat()

DSKhoa = []
DSKhoa.append(Khoa("01", "CNTT"))
DSKhoa.append(Khoa("02", "Ke Toan"))
DSKhoa.append(Khoa("03", "Co Khi"))
DSKhoa.append(Khoa("04", "Nuoi"))
print("\n")
print("Ma khoa \t Ten Khoa")
for i in DSKhoa:
    i.xuat()

print("\n")
print("DSSV Khoa CNTT:")
print("MSSV \t\t Ho ten \t Ma khoa")
for i in DSSV:
    if(i.getMaKhoa() == "01"):
        i.xuat()
