from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:  # Infinite loop for menu
    print("\n CHƯƠNG TRÌNH QUẢN LÍ SINH VIÊN")
    print("********************MENU***********************")
    print("** 1. Them Sinh Vien.                        **")
    print("** 2. Cap nhat thong tin sinh vien boi id.   **")
    print("** 3. Xoa Sinh Vien boi id.                  **")
    print("** 4. Tim kiem Sinh Vien theo ten.           **")
    print("** 5. Sap xep Sinh Vien theo diem trung binh.**")
    print("** 6. Sap xep Sinh Vien theo ten chuyen nganh**")
    print("** 7. Hien Thi danh sach Sinh Vien.          **")
    print("** 0. Thoat.                                 **")
    print("***********************************************")

    key = int(input("Nhap tuy chon: "))
    
    if key == 1:
        print("\n1. Them Sinh Vien.")
        qlsv.nhapSinhVien()
        print("\nThem Sinh Vien Thanh Cong!")
    elif key == 2:
        if qlsv.soluongSinhVien() > 0:
            print("\n2. Cap nhat thong tin Sinh Vien.")
            print("\nNhap ID sinh vien can cap nhat: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh Sach Sinh Vien trong!")
    elif key == 3:
        if qlsv.soluongSinhVien() > 0:
            print("\n3. Xoa Sinh Vien.")
            print("\nNhap ID sinh vien can xoa: ")
            ID = int(input())
            if qlsv.deleteById(ID):
                print(f"\nSinh Vien co id = {ID} da bi xoa.")
            else:
                print(f"\nSinh Vien co id = {ID} khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 4:
        if qlsv.soluongSinhVien() > 0:
            print("\n4. Tim kiem Sinh Vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            if searchResult:
                qlsv.showSinhVien(searchResult)
            else:
                print("Khong tim thay sinh vien nao.")
        else:
            print("\nDanh sach Sinh Vien trong!")
    elif key == 5:
        if qlsv.soluongSinhVien() > 0:
            print("\n5. Sap Xep Sinh Vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach Sinh Vien trong!")
    elif key == 6:
        if qlsv.soluongSinhVien() > 0:
            print("\n6. Sap xep Sinh Vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach Sinh Vien trong!")
    elif key == 7:
        if qlsv.soluongSinhVien() > 0:
            print("\n7. Hien Thi Danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sach Sinh Vien trong!")
    elif key == 0:
        print("\nBan da chon thoat chuong trinh.")
        break
    else:
        print("\nKhong co chuc nang nay.")
        print("\nHay chon chuc nang trong hop menu.")
