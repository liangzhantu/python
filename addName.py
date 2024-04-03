import os

# 获取当前目录
folder_path = "D:\BaiduNetdiskDownload\漫画\[桂正和]Is"

# 遍历目录中的所有文件
for file_name in os.listdir(folder_path):
    # 判断文件类型是否为 pdf
    if file_name.endswith('.pdf'):
        # 添加指定字符到文件名前面
        new_file_name = "I''s_" + file_name
        # 重命名文件
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
        print(f"Renamed: {file_name} to {new_file_name}")

print("All files renamed successfully!")
