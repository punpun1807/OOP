class phong_ban:
    def __init__(self , ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong ,luong_toi_da):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_Ten = ho_Ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.luong_toi_da = luong_toi_da
        self.he_so_luong = he_so_luong
    def tinh_luong(self):
        return self.he_so_luong * 2000000
    
    
class cong_tac_vien(phong_ban):
    def __init__(self , ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong , luong_toi_da  , thoi_gian_hop_dong , phu_cap ):
        super().__init__(ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong , luong_toi_da)
        self.thoi_gian_hop_dong = thoi_gian_hop_dong
        self.phu_cap = phu_cap
    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap

class nhan_vien_chinh_thuc(phong_ban):
    def __init__(self , ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong , luong_toi_da , vi_tri_cong_viec ):
        super().__init__(ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong , luong_toi_da)
        self.vi_tri_cong_viec = vi_tri_cong_viec
    def tinh_luong(self):
        return super().tinh_luong()
class truong_phong(phong_ban):
    def __init__(self , ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong , luong_toi_da , ngay_bat_dau_quan_ly , phu_cap):
        super().__init__(ma_nhan_vien , ho_Ten , nam_sinh , gioi_tinh , dia_chi , he_so_luong ,luong_toi_da)
        self.ngay_bat_dau_quan_ly = ngay_bat_dau_quan_ly
        self.phu_cap = phu_cap
    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap
    
truong_phong = truong_phong("001" , "Nguyen Van A" , 1980 , "Nam" , "123 ABC Street" , 4.0 , 10000000 , "2020-01-01" , 5000000)
cong_tac_vien = cong_tac_vien("002" , "Le Thi B" , 1990 , "Nu" , "456 DEF Street" , 2.0 , 8000000 , "2021-06-01" , 2000000)
nhan_vien_chinh_thuc = nhan_vien_chinh_thuc("003" , "Tran Van C" , 1985 , "Nam" , "789 GHI Street" , 2.5 , 9000000 , "Nhan vien chinh thuc")
print(f" luong cua cong_tac_vien: {cong_tac_vien.tinh_luong()}") 
print(f" luong cua truong_phong: {truong_phong.tinh_luong()}")
print(f" luong cua nhan_vien_chinh_thuc: {nhan_vien_chinh_thuc.tinh_luong()}")        