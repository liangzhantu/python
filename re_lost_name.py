import os

def change_file_extension(directory, old_extension, new_extension):
    """
    修改指定目录下文件的文件后缀。

    Args:
        directory (str): 包含文件的目录路径。
        old_extension (str): 要替换的旧文件后缀。
        new_extension (str): 用于替换旧后缀的新文件后缀。

    Returns:
        None
    """
    for filename in os.listdir(directory):
        if filename.endswith(old_extension):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, filename.replace(old_extension, new_extension))
            os.rename(old_path, new_path)
            print(f"已将 {old_path} 重命名为 {new_path}")

# 示例用法：将指定目录中的所有 .txt 文件改为 .csv
directory_path = "E:\music\Bob Dylan temp\\blood on the tracks"
old_extension = ".flac"
new_extension = ""
change_file_extension(directory_path, old_extension, new_extension)
