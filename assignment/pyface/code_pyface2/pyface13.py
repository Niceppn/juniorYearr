import os

c_path = os.getcwd()

print(c_path) # path ที่อยู่ของโค้ดที่เรากำลังรัน

folder = 'image99'

print(folder)

new_path = os.path.join(c_path,folder)

print(new_path)

file_list = []

for (root, dirs, file) in os.walk(new_path):
    for f in file:
        if '.jpg' in f:
            jpg_file = os.path.abspath(os.path.join(root, f))
            file_list.append(jpg_file)
            print(jpg_file)
