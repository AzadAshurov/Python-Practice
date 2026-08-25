from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir / "example.txt"

file_path.write_text("Hello Python")

print(file_path.exists())
print(file_path.is_file())
print(file_path.read_text())