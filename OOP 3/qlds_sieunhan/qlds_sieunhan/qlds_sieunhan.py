class sieu_nhan:
    class SieuNhan:
    
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    
    def hien_thi(self):
        print(f"Ten: {self.ten} - Vu khi: {self.vu_khi} - Mau sac: {self.mau_sac}")
ds_sieu_nhan = []

while True:
    
    ten = input("Nhap ten sieu nhan: ")
    vu_khi = input("Nhap vu khi: ")
    mau = input("Nhap mau sac: ")
    
    sn = SieuNhan(ten, vu_khi, mau)
    
    ds_sieu_nhan.append(sn)
    
    tiep = input("Nhap tiep? (y/n): ")
    
    if tiep == "n":
        break


print("\nDanh sach sieu nhan:")

for sn in ds_sieu_nhan:
    sn.hien_thi()