class HangHoa:
    def __init__(self , ma_hang , ten_hang , nha_san_xuat , gia_ban):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_san_xuat = nha_san_xuat    
        self.gia_ban = gia_ban
        
    
 
class hangdienmay(HangHoa):
    def __init__(self , ma_hang , ten_hang , nha_san_xuat , gia_ban , cong_suat , tg_bao_hanh , dien_ap):
        super().__init__(ma_hang , ten_hang , nha_san_xuat , gia_ban)
        self.cong_suat = cong_suat
        self.tg_bao_hanh = tg_bao_hanh
        self.dien_ap = dien_ap


class HangSanhSu(HangHoa):
    def __init__(self , ma_hang , ten_hang , nha_san_xuat , gia_ban , loai_nguyen_lieu ):
        super().__init__(ma_hang , ten_hang , nha_san_xuat , gia_ban)
        self.loai_nguyen_lieu = loai_nguyen_lieu

class HangThucPham(HangHoa):
    def __init__(self , ma_hang , ten_hang , nha_san_xuat , gia_ban , ngay_san_xuat , ngay_het_han):
        super().__init__(ma_hang , ten_hang , nha_san_xuat , gia_ban)
        self.ngay_san_xuat = ngay_san_xuat
        self.ngay_het_han = ngay_het_han
        
hangdienmay = hangdienmay("lol" , "tivi" , "samsung" , 10000000 , "200W" , "24 thang" , "220V")
hangsanhsu = HangSanhSu("lmao" , "bát" , "nha_san_xuat" , 10000 , "gỗ")
hangthucpham = HangThucPham("skibidi" , "sữa" , "nha_san_xuat" , 20000 , "2023-01-01" , "2023-12-31")

print(hangdienmay.ten_hang)
print(hangsanhsu.nha_san_xuat)
print(hangthucpham.gia_ban)