import os
import re

def batch_rename(work_dir, patterns):
    """
    This will batch rename a group of files in a given directory,
    based on the specified patterns.
    :param work_dir: The directory where the files are located.
    :param patterns: A list of tuples (old_pattern, new_pattern).
    """
    for filename in os.listdir(work_dir):
        for old_pattern, new_pattern in patterns:
            # Check if the old pattern exists in the filename
            if re.search(old_pattern, filename):
                # Replace the old pattern with the new pattern
                newfile = re.sub(old_pattern, new_pattern, filename)
                os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
                print(f"Renamed {filename} to {newfile}")
                break  # Break out of the loop after the first match

# Example usage
folder_path = "D:\manga\高木同學\擅長捉弄人的高木同學"  # 设置你的文件夹路径
patterns_to_remove = [
    ("\[\]", ""),  # 去除 "迷之彼女X_"
    # ("话", ""),  # 去除 "第"
    # 添加其他需要去除的部分
]

batch_rename(folder_path, patterns_to_remove)
