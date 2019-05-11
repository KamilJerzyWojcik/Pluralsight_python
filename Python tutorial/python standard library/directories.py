from pathlib import Path

path = Path("ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

paths = [p for p in path.iterdir() if p.is_dir()]
python_files = [p for p in path.glob("*.py")]
python_files_rglob = [p for p in path.rglob("*.py")]

print(paths)
print(python_files)
print(python_files_rglob)