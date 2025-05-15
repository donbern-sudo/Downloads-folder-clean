### Scrpit to clean and organize downloads folder on computer
# Set Dowloads folder path 
# Define File types for organizing




import os
import shutil
from pathlib import Path

#Set Downloads foler path 
downloads_path = Path("/mnt/c/Users/donov_55g91hw/Downloads")


#Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Presentations": [".pptx", ".ppt"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".go", ".sh"],
    "Executables": [".exe", ".msi", ".dmg", ".apk"]
}

# Organizing function
def organize_downloads(folder):
    for item in folder.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in file_types.items():
                if item.suffix.lower() in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(item), str(target_dir / item.name))
                    moved = True
                    break
            if not moved:
                other_dir = folder / "Other"
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(other_dir / item.name))

if __name__ == "__main__":
    print(f"Organizing files in: {downloads_path}")
    organize_downloads(downloads_path)
    print("Download folder organized successfully.")
