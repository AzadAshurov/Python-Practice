from pathlib import Path
from typing import Any
ml_project_dir = Path("ml_project")
data_dir = ml_project_dir / "data"
raw_dir = data_dir / "raw"


data_dir.mkdir(parents=True, exist_ok=True)
raw_dir.mkdir(parents=True, exist_ok=True)

print(Path.cwd())


users_csv_path = raw_dir / "users.csv"
sales_csv_path = raw_dir / "sales.csv"
products_csv_path = raw_dir / "products.csv"
users_csv_path.touch()
sales_csv_path.touch()
products_csv_path.touch()
csv_file_amount: int = 0
for file in raw_dir.glob("*.csv"):
    print(file.name, file.stat().st_size)
    csv_file_amount += 1

csv_files = list(raw_dir.glob("*.csv"))
print(csv_files)
print(f"Total CSV files: {csv_file_amount}")
