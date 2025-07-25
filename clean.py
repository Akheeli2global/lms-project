import os
import shutil

def clean_pycache(directory):
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            # Remove __pycache__ directories
            for dir_name in dirs:
                if dir_name == "__pycache__":
                    pycache_path = os.path.join(root, dir_name)
                    shutil.rmtree(pycache_path)
                    print(f"Removed: {pycache_path}")
            
            # Remove .pyc files
            for file_name in files:
                if file_name.endswith('.pyc'):
                    pyc_file_path = os.path.join(root, file_name)
                    os.remove(pyc_file_path)
                    print(f"Removed: {pyc_file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = "C:\\Users\\akhee\\Documents\\GitHub\\lms-project"
    if not os.path.isdir(directory_path):
        print("Invalid directory path!")
    else:
        clean_pycache(directory_path)
        print("Cache cleaning completed.")