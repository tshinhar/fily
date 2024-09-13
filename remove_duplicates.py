import os
import hashlib
import argparse

def calculate_file_hash(file_path):
    """Calculates the hash value of a file's content."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_files(root_folder):
    """Traverses through the root folder and identifies duplicate files."""
    print(f"looking for duplicate files under {root_folder}...")
    duplicates = {}
    for folder_path, _, file_names in os.walk(root_folder):
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            file_hash = calculate_file_hash(file_path)
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]
    return duplicates

def remove_duplicate_files(duplicates, confirmed=False):
    """Removes duplicate files from the file system."""
    for file_paths in duplicates.values():
        if len(file_paths) > 1:
            print(f"Duplicate files found:\n{file_paths}\n")
            for file_path in file_paths[1:]:
                delete_flag = confirmed
                if not confirmed:
                    confirmation = input("delete?")
                    if confirmation.lower() in ["yes", "y", "ok"]:
                        delete_flag = True
                if delete_flag:
                    os.remove(file_path)
                    print(f"{file_path} has been deleted.\n")
                else:
                    print("duplicate file was not deleted")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Remove duplicate files")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument(
        "-y", "--yes", action="store_true", help="pre-confirm files removal"
    )
    parser.add_argument("root_path", nargs="+", help="Path to the root directory")
    # Parse the command-line arguments
    args = parser.parse_args()

    for path in args.root_path:
        duplicates = find_duplicate_files(path)
        remove_duplicate_files(duplicates, args.yes)
