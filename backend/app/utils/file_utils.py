import os
import shutil

def cleanup_temp_files(folder: str = "media/uploads", extensions: list = [".mp4", ".srt"]):
    """
    Removes temporary files with specific extensions from a folder.
    """
    for file in os.listdir(folder):
        if any(file.endswith(ext) for ext in extensions):
            os.remove(os.path.join(folder, file))

def move_file(src: str, dest_folder: str) -> str:
    """
    Moves a file to the destination folder and returns new path.
    """
    os.makedirs(dest_folder, exist_ok=True)
    filename = os.path.basename(src)
    dest_path = os.path.join(dest_folder, filename)
    shutil.move(src, dest_path)
    return dest_path
