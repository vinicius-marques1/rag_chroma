import magic

# print(magic.from_file("/mnt/c/Projetos/Apostila.pdf"))

# # recommend using at least the first 2048 bytes, as less can produce incorrect identification
# print(magic.from_buffer(open("/mnt/c/Projetos/Apostila.pdf", "rb").read(2048)))

# pdf type
print(magic.from_file("Test_type/test.pdf"))

# python type
print(magic.from_file("./Test_type/test.py"))

# text type
print(magic.from_file("./Test_type/test.txt"))

# json type
print(magic.from_file("./Test_type/test.json"))

# js type
print(magic.from_file("./Test_type/test.js"))

# sql type
print(magic.from_file("./Test_type/test.sql"))

# typescript type
print(magic.from_file("./Test_type/test.ts"))
print(magic.from_file("./Test_type/test.tsx"))
print(magic.from_file("./Test_type/test.jsx"))

# html type
print(magic.from_file("./Test_type/test.html"))

# css type
print(magic.from_file("./Test_type/test.css"))

# scss type
print(magic.from_file("./Test_type/test.scss"))

# sass type
print(magic.from_file("./Test_type/test.sass"))

# xml type
print(magic.from_file("./Test_type/test.xml"))

# yaml type
print(magic.from_file("./Test_type/test.yaml"))
print(magic.from_file("./Test_type/test.yml"))

# markdown type
print(magic.from_file("./Test_type/test.md"))

# rst type
print(magic.from_file("./Test_type/test.rst"))


