import os
import shutil

# Folder to organize
folder = input("Enter folder path: ").strip()

if not os.path.exists(folder):
    print("❌ Folder does not exist!")
    exit()

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".sql"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

moved = 0

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Ignore folders
    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()

    category = "Others"

    for name, extensions in categories.items():
        if extension in extensions:
            category = name
            break

    category_folder = os.path.join(folder, category)

    # Create category folder if needed
    os.makedirs(category_folder, exist_ok=True)

    destination = os.path.join(category_folder, file)

    # Avoid overwriting existing files
    if os.path.exists(destination):
        base, ext = os.path.splitext(file)
        counter = 1

        while os.path.exists(destination):
            new_name = f"{base}_{counter}{ext}"
            destination = os.path.join(category_folder, new_name)
            counter += 1

    shutil.move(file_path, destination)

    print(f"Moved: {file} → {category}/")
    moved += 1

print("\n✅ Organization completed!")
print(f"📦 Files organized: {moved}")
