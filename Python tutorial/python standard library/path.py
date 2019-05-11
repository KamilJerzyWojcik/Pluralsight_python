from pathlib import Path

path = Path("ecommerce/__init__.py")

print("exist:", path.exists())
print("is file:", path.is_file())
print("is dir:", path.is_dir())
print("name: ", path.name)
print("name2:", path.stem)
print("suffix: ", path.suffix)
print("parent:", path.parent)

# path = path.with_name("file.txt")
# print("absolute: ", path.absolute())

path = path.with_suffix(".txt")
print(path)