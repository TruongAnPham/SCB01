# App Management OrderItem
from data_io import write_file, read_file

class Item:
  def __init__(self, name, price, quantity):
    self.name = name 
    self.price = price 
    self.quantity = quantity

class Customer:
  def __init__(self, customer_id, customer_name):
    self.customer_id = customer_id
    self.customer_name = customer_name

class Order:
  def __init__(self, item_list, customer_id):
    self.item_list = item_list
    self.customer_id = customer_id
    self.total = 0

class Promotion:
  def __init__(self, price):
    self.price = price
  
  def discount(self):
    return 1
  
class Management:
  def __init__(self):
    items = read_file("item")
    self.item_list = [item for item in items if item]
    orders = read_file("order")
    self.order_list = [item for item in orders if item]

  def show_menu(self):
    menu = "\n1. Xem danh sach san pham hien co\n2. Xem danh sach don hang\n3. Them moi san pham\n4. Them moi don hang\n5. Luu san pham vao file\n6. Luu don hang vao file\n7. Thoat chuong trinh"
    print(menu)
    chosen = int(input("\nMoi ban lua chon chuc nang: "))
    match chosen:
      case 1:
        self.show_items()
      case 2:
        self.show_orders()
      case 3:
        self.add_item()
      case 4:
        self.add_order()
      case 5:
        self.save_item_to_file
      case 6:
        self.save_order_to_file()
      case 7: 
        return
    

  def show_orders(self):
    if len(self.order_list) == 0:
      print("Hien chua co san pham nao")
    else:
      print("Danh sach cac san pham hien co trong he thong\n")
      for item in self.order_list:
        print(item)
    self.show_menu()

  def add_item(self):
    print("\n\nThem san pham moi\n\n")
    name = input("Nhap ten san pham: ")
    price = float(input("Nhap gia san pham: "))
    quantity = int(input("So luong san pham: "))

    new_item = Item(name, price, quantity)
    self.item_list.append(name)

    write_file(self.item_list, "item")
    print("Them san pham moi thanh cong!\n\n")
    self.show_menu()

  def add_order (self):
    print("\n\nThem don hang moi\n\n")
    item_list = input("nhap ten don hang: ")
    price = float(input("Nhap gia don hang: "))
    quantity = int(input("So luong san pham: "))
    
    new_order = Order(name, price, quantity)
    self.order_list.append(name)





  def show_items(self):
    if len(self.item_list) == 0:
      print("Hien chua co san pham nao")
    else:
      print("Danh sach cac san pham hien co trong he thong\n")
      for item in self.item_list:
        print(item)
    self.show_menu()

  def save_order_to_file(self, order):
        with open('orders.txt', 'a') as file:  # 'a' là chế độ thêm (append)
            file.write(order + '\n')

app = Management()
app.show_menu()