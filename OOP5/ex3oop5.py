class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh  # "nam", "nữ", "khác"
        self.dia_chi = dia_chi

    def hien_thi(self):
        print(f"  Họ tên   : {self.ho_ten}")
        print(f"  Tuổi     : {self.tuoi}")
        print(f"  Giới tính: {self.gioi_tinh}")
        print(f"  Địa chỉ  : {self.dia_chi}")


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc công nhân phải từ 1 đến 10!")
        self.bac = bac

    def hien_thi(self):
        print("[Công Nhân]")
        super().hien_thi()
        print(f"  Bậc      : {self.bac}")


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi(self):
        print("[Kỹ Sư]")
        super().hien_thi()
        print(f"  Ngành ĐT : {self.nganh_dao_tao}")


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi(self):
        print("[Nhân Viên]")
        super().hien_thi()
        print(f"  Công việc: {self.cong_viec}")


class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_moi(self, can_bo):
        """Thêm một cán bộ vào danh sách."""
        self.danh_sach.append(can_bo)
        print(f">> Đã thêm: {can_bo.ho_ten}")

    def tim_kiem(self, ho_ten):
        """Tìm kiếm cán bộ theo họ tên (không phân biệt hoa thường)."""
        ket_qua = [cb for cb in self.danh_sach
                   if ho_ten.lower() in cb.ho_ten.lower()]
        if ket_qua:
            print(f"\n=== Kết quả tìm kiếm '{ho_ten}' ===")
            for cb in ket_qua:
                cb.hien_thi()
                print()
        else:
            print(f"Không tìm thấy cán bộ nào với tên '{ho_ten}'.")

    def hien_thi_tat_ca(self):
        """Hiển thị toàn bộ danh sách cán bộ."""
        if not self.danh_sach:
            print("Danh sách cán bộ trống.")
            return
        print("\n========== DANH SÁCH CÁN BỘ ==========")
        for i, cb in enumerate(self.danh_sach, 1):
            print(f"--- #{i} ---")
            cb.hien_thi()
            print()

    def menu(self):
        """Vòng lặp menu chính."""
        while True:
            print("\n====== QUẢN LÝ CÁN BỘ ======")
            print("1. Thêm mới cán bộ")
            print("2. Tìm kiếm theo họ tên")
            print("3. Hiển thị danh sách cán bộ")
            print("4. Thoát")
            lua_chon = input("Chọn chức năng (1-4): ").strip()

            if lua_chon == "1":
                self._them_can_bo()
            elif lua_chon == "2":
                ten = input("Nhập họ tên cần tìm: ").strip()
                self.tim_kiem(ten)
            elif lua_chon == "3":
                self.hien_thi_tat_ca()
            elif lua_chon == "4":
                print("Thoát chương trình. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")

    def _them_can_bo(self):
        print("\n-- Loại cán bộ --")
        print("1. Công nhân")
        print("2. Kỹ sư")
        print("3. Nhân viên")
        loai = input("Chọn loại (1-3): ").strip()

        ho_ten   = input("Họ tên   : ").strip()
        tuoi     = int(input("Tuổi     : "))
        gioi_tinh = input("Giới tính (nam/nữ/khác): ").strip()
        dia_chi  = input("Địa chỉ  : ").strip()

        if loai == "1":
            bac = int(input("Bậc (1-10): "))
            cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
        elif loai == "2":
            nganh = input("Ngành đào tạo: ").strip()
            cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif loai == "3":
            cv = input("Công việc: ").strip()
            cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cv)
        else:
            print("Loại không hợp lệ!")
            return

        self.them_moi(cb)


# ── Chạy thử với dữ liệu mẫu ──────────────────────────────────────────────
if __name__ == "__main__":
    ql = QLCB()

    # Thêm dữ liệu mẫu
    ql.them_moi(CongNhan("Nguyễn Văn An", 30, "nam", "Hà Nội", 5))
    ql.them_moi(KySu("Trần Thị Bình", 28, "nữ", "TP.HCM", "Công nghệ thông tin"))
    ql.them_moi(NhanVien("Lê Văn Cường", 35, "nam", "Đà Nẵng", "Kế toán"))

    # Khởi động menu
    ql.menu()