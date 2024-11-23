
danh_sach_benh_nhan = []


def them_benh_nhan():

    ma_bn = input("Nhập mã bệnh nhân: ")
    ho_ten = input("Nhập họ tên: ")
    ngay_sinh = input("Nhập ngày sinh: ")
    chuan_doan = input("Nhập chuẩn đoán: ")

    benh_nhan_moi = {
        'ma_bn': ma_bn,
        'ho_ten': ho_ten,
        'ngay_sinh': ngay_sinh,
        'chuan_doan': chuan_doan
    }
    danh_sach_benh_nhan.append(benh_nhan_moi)
    print("Đã thêm bệnh nhân thành công!")


def xoa_benh_nhan():

    ma_bn = input("Nhập mã bệnh nhân cần xóa: ")
    for i, bn in enumerate(danh_sach_benh_nhan):
        if bn['ma_bn'] == ma_bn:
            danh_sach_benh_nhan.pop(i)
            print("Đã xóa bệnh nhân thành công!")
            return
    print("Không tìm thấy bệnh nhân có mã này!")


def sua_thong_tin_benh_nhan():

    ma_bn = input("Nhập mã bệnh nhân cần sửa: ")
    for bn in danh_sach_benh_nhan:
        if bn['ma_bn'] == ma_bn:
            bn['ho_ten'] = input("Nhập họ tên mới: ")
            bn['ngay_sinh'] = input("Nhập ngày sinh mới: ")
            bn['chuan_doan'] = input("Nhập chuẩn đoán mới: ")
            print("Đã cập nhật thông tin thành công!")
            return
    print("Không tìm thấy bệnh nhân có mã này!")


def tim_kiem_benh_nhan():

    keyword = input("Nhập từ khóa tìm kiếm: ")
    ket_qua = [bn for bn in danh_sach_benh_nhan if keyword.lower()
               in bn['ho_ten'].lower()]
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for bn in ket_qua:
            print(f"Mã BN: {bn['ma_bn']}, Họ tên: {bn['ho_ten']}, Ngày sinh: {
                  bn['ngay_sinh']}, Chuẩn đoán: {bn['chuan_doan']}")
    else:
        print("Không tìm thấy kết quả!")


def hien_thi_danh_sach_benh_nhan():

    if not danh_sach_benh_nhan:
        print("Danh sách bệnh nhân rỗng.")
    else:
        print("Danh sách bệnh nhân:")
        for bn in danh_sach_benh_nhan:
            print(f"Mã BN: {bn['ma_bn']}, Họ tên: {bn['ho_ten']}, Ngày sinh: {
                  bn['ngay_sinh']}, Chuẩn đoán: {bn['chuan_doan']}")


# Menu chính
while True:
    print("\n--- Quản lý bệnh nhân ---")
    print("1. Thêm bệnh nhân")
    print("2. Xóa bệnh nhân")
    print("3. Sửa thông tin bệnh nhân")
    print("4. Tìm kiếm bệnh nhân")
    print("5. Hiển thị danh sách bệnh nhân")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn: ")

    if lua_chon == "1":
        them_benh_nhan()
    elif lua_chon == "2":
        xoa_benh_nhan()
    elif lua_chon == "3":
        sua_thong_tin_benh_nhan()
    elif lua_chon == "4":
        tim_kiem_benh_nhan()
    elif lua_chon == "5":
        hien_thi_danh_sach_benh_nhan()
    elif lua_chon == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")
