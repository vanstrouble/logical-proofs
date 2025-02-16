import os
import shutil


platforms = {
    "hackerrank": "#!/bin/python3",
    "codewars": "katas",
    "leetcode": "class Solution:",
    "codechef": "#include <iostream>",
}
platforms_inverted = {v: k for k, v in platforms.items()}

current_dir_files = "katas/"
platforms_dir = os.getcwd()


def organize_files(filename, platform):
    platform_dir = os.path.join(platforms_dir, platform)
    file_path = os.path.join(current_dir_files, filename)
    dest_path = os.path.join(platform_dir, filename)
    print(dest_path)
    print(platform_dir, file_path)
    if not os.path.exists(platform_dir):
        print("Platform does not exist. Creating directory...")
        os.makedirs(platform_dir)
    if os.path.exists(dest_path):
        print(f"File {filename} alredy exists")
        return
    try:
        shutil.move(file_path, platform_dir)
        # print("File moved")
    except Exception as e:
        print(f"Error moving file: {e}")


def main():
    for filename in os.listdir(current_dir_files):
        file_path = os.path.join(current_dir_files, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()
                platform = platforms_inverted.get(first_line, "codewars")
                organize_files(filename, platform)


if __name__ == "__main__":
    main()
