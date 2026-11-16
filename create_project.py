from pathlib import Path

#Current working directory
root = Path(".")

#Folders to create 

folders ={
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
}

# Files to create 
files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]

# Create folders


for folder in folders:
    folder_path = root/folder   # (root/folder).mkdir(parents=True, exist_ok= True)
    folder_path.mkdir(parents = True, exist_ok=True)
    print(f"Created folder: {folder_path}")

#File Creation 
for file in files:
    (root/file).touch(exist_ok=True)

print("Project structure created successfully")