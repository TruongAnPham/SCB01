class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def show(self):
    print(f"This is {self.name} & he is {self.age} years old")

xitrum = Dog("Xi trum", 3)
print(xitrum.show())

class Student:
    def __init__(self, name, age, gpa):
     self.name = name
     self.age = age
     self.gpa = gpa
    
    def show(self):
        print(f"Đây là {self.name} và cậu ấy {self.age}, gpa của cậu ấy là {self.gpa}")

truongan = Student("Trường An", 17, 3.98)
print(truongan.show())

class Shape:
    def __init__(self, chieu_dai, chieu_rong):
        self.dai = chieu_dai
        self.rong = chieu_rong

    def dien_tich(self):
        print("dien tich")


class HinhChuNhat(Shape):
    def dien_tich(self):
        return self.dai * self.rong


class HinhVuong(Shape):
    def __init__(self, canh):
        self.dai = canh
        self.rong = canh

    def dien_tich(self):
        return self.dai * self.dai


hcn = HinhChuNhat(5, 10)
print(f"Dien tich hinh chu nhat: {hcn.dien_tich()}") 

hv = HinhVuong(4)
print(f"Dien tich hinh vuong: {hv.dien_tich()}")


