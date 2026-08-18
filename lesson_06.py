from pathlib import Path
ml_project_dir = Path("ml_project")
data_dir = ml_project_dir / "data"
raw_dir = data_dir / "raw"
processed_dir = data_dir  / "processed"
models_dir = ml_project_dir  / "models"
logs_dir = ml_project_dir  / "logs"
configs_dir = ml_project_dir  / "configs"
src_dir = ml_project_dir  / "src"

data_dir.mkdir(parents=True, exist_ok=True)
raw_dir.mkdir(parents=True, exist_ok=True)
processed_dir.mkdir(parents=True, exist_ok=True)
models_dir.mkdir(parents=True, exist_ok=True)
logs_dir.mkdir(parents=True, exist_ok=True)
configs_dir.mkdir(parents=True, exist_ok=True)
src_dir.mkdir(parents=True, exist_ok=True)
print(Path.cwd())

file_path = configs_dir / "app.txt"

file_path.write_text("environment=development\n"
                      "model_version=1\n")

content = file_path.read_text()

print("File content:")
print(content)



print(file_path.exists())
print(file_path.is_file())
