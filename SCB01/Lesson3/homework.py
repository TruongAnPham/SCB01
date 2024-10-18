# Lớp mô tả tài khoản ngân hàng chung
class TaiKhoan:
    def __init__(self, so_tai_khoan, chu_tai_khoan, so_du):
        self.so_tai_khoan = so_tai_khoan
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du

    def hien_thi_thong_tin(self):
        print(f"Số tài khoản: {self.so_tai_khoan}")
        print(f"Chủ tài khoản: {self.chu_tai_khoan}")
        print(f"Số dư: {self.so_du}")

    def nap_tien(self, so_tien):
        self.so_du += so_tien

    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
        else:
            print("Số dư không đủ")
            
# Lớp mô tả tài khoản chính
class TaiKhoanChinh(TaiKhoan):
    def __init__(self, so_tai_khoan, chu_tai_khoan, so_du):
        super().__init__(so_tai_khoan, chu_tai_khoan, so_du)

# Lớp mô tả tài khoản tiết kiệm
class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, so_tai_khoan, chu_tai_khoan, so_du, lai_suat):
        super().__init__(so_tai_khoan, chu_tai_khoan, so_du)
        self.lai_suat = lai_suat

    def tinh_lai(self):
        return self.so_du * self.lai_suat / 100