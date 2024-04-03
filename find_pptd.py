import os

def find_pptd_files(root_dir):
    pptd_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith((".pptd","cfg")):
                pptd_files.append(os.path.join(dirpath, filename))
    return pptd_files

# 请指定你想要搜索 .pptd 文件的根目录
root_directory = r"E:\\hentai"

# 调用函数查找 .pptd 文件
pptd_files_list = find_pptd_files(root_directory)

# 打印 .pptd 文件列表
for pptd_file in pptd_files_list:
    print(pptd_file)
