import os

c_path = os.getcwd()

print(c_path) # path ที่อยู่ของโค้ดที่เรากำลังรัน

folder = 'image99'

print(folder)

new_path = os.path.join(c_path,folder)

print(new_path)
