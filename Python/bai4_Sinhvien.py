#Python 3.6.x
class Khoa:
    def __init__(self, maKhoa, tenKhoa):
        self.maKhoa = maKhoa
        self.tenKhoa = tenKhoa
    def getMaKhoa(self):
        return self.maKhoa
    def setMaKhoa(self, maKhoa):
        self.maKhoa = maKhoa
    def getTenKhoa(self):
        return self.tenKhoa
    def setTenKhoa(self, tenKhoa):
        self.tenKhoa = tenKhoa
    def xuat(self):
        print(self.maKhoa + "\t\t" + self.tenKhoa)

class SinhVien(Khoa): 
    def __init__(self, mssv, hoTen, maKhoa):
        self.mssv = mssv
        self.hoTen = hoTen
        self.maKhoa = maKhoa
    def getMSSV(self):
        return self.mssv
    def setMSSV(self, mssv):
        self.mssv = mssv
    def getHoTen(self):
        return self.hoTen
    def setHoTen(self, hoTen):
        self.hoTen = hoTen
    def xuat(self):
        print(self.mssv + "\t\t" + self.hoTen + "\t\t" + self.maKhoa)

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
