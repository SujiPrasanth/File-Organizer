import os
from pathlib import Path

subcategory = {
    'DOCUMENTS': ['.pdf', '.txt', '.doc', '.rtf', '.pptx', '.docx', '.odt'],
    'AUDIO': ['.mp3', '.m4b', '.m4a', '.webvtt', '.cea-608/708', '.dfxp',
              '.sami', '.scc', '.srt', '.ttml', '.3gpp'],
    'VIDEOS': ['.mov', '.avi', '.mp4', '.3gp', '.ogg', '.oga', '.ogv',
               '.ogx', '.wmv', '.webm', '.flv', '.QuickTime', '.hdv',
               '.mxf', '.mpeg-2', '.ts', '.wav', '.lfx', '.gfx', '.vob'],
    'IMAGES': ['.jpg', '.jpeg', '.raw', '.png', '.tiff', '.gif'],
    'PROGRAMMING FILES': ['.htm', '.html', '.cpp', '.c', '.py', '.css', '.java']
}

def find_category(extension):
    for category, extensions in subcategory.items():
        if extension in extensions:
            return category
    return 'MISC'

def organize_dir(target_folder='.'):
    target_path = Path(target_folder)

    if not target_path.exists():
        print(f" Folder does not exist: {target_folder}")
        return

    print(f"\n Organizing files in: {target_path.resolve()}\n")

    for item in target_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            category = find_category(ext)
            category_path = target_path / category

            if not category_path.exists():
                category_path.mkdir()

            destination = category_path / item.name

            try:
                item.rename(destination)
                print(f" Moved: {item.name} → {category}/")
            except Exception as e:
                print(f"❌ Could not move {item.name}: {e}")

    print("\n File organization complete.")


folder = input("Enter the folder path to organize: ").strip()
organize_dir(folder)
