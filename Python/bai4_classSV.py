#Python 3.6.x
from bai4_classKhoa import Khoa

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