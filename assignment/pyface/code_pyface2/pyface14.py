import os

jpg_file = 'D:\pyface1\code_pyface1\image99\mountains.jpg'

dirname = os.path.dirname(jpg_file)
print(dirname)

last_foldername = os.path.basename(dirname)
print(last_foldername)

