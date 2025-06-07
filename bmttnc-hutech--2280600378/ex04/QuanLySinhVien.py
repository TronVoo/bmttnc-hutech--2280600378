from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxID = 1
        if self.soluongSinhVien() > 0:
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxID < sv._id:
                    maxID = sv._id
            maxID += 1
        return maxID
    
    def soluongSinhVien(self):
        return len(self.listSinhVien)  # Corrected len() usage
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None
    
    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.upper() in sv._name.upper():
                listSV.append(sv)
        return listSV
    
    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False
    
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"
    
    def showSinhVien(self, listSV):
        print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format("id", "name", "sex", "major", "diemTB", "HocLuc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sach Sinh Vien trong!")
    
    def getListSinhVien(self):
        return self.listSinhVien
