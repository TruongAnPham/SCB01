def read_file(type_data):
    if type_data == 'item':
        file = 'item.txt'
    else:
        file = 'order.txt'
    with open(file, "r") as file:
        item = file.read()
    return item.split("\n")

def write_file(data,type_data):
    if type_data == 'item':
        file = "item.txt"
    else:
        file = 'order.txt'
    with open(file, "w") as file:
      for item in data:
          file.write(item + "\n")