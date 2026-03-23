class sieu_nhan:
    def __init__(self , ten , vu_khi ,mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def hien_thi(self) :
        print( f"ten: {self.ten} , vu_khi: {self.vu_khi} , mau_sac: {self.mau_sac}")
sieu_nhan_A = sieu_nhan("A" , "kiem" , "xanh")
sieu_nhan_B = sieu_nhan("B " , "sung" , "do")   
sieu_nhan_A.hien_thi()
sieu_nhan_B.hien_thi()