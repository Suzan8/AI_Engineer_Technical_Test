from pathlib import Path

def get_file_extension(file_path: Path):
    return file_path.suffix.lower()