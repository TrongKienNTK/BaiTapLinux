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
