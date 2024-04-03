import os

def get_folder_size(folder_path):
    """
    计算文件夹中所有文件的总大小。
    Args:
        folder_path (str): 文件夹路径。
    Returns:
        int: 总大小（以字节为单位）。
    """
    total_size = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            folder_size = get_folder_size(file_path)
            total_size += folder_size
        else:
            total_size += os.path.getsize(file_path)
    return total_size

def sort_folders_by_size(root_path):
    """
    按大小（从大到小）对指定根路径下的文件夹进行排序。
    Args:
        root_path (str): 根文件夹路径。
    Returns:
        list: 包含元组（文件夹路径，文件夹大小）的列表。
    """
    folder_sizes = []
    for filename in os.listdir(root_path):
        folder_path = os.path.join(root_path, filename)
        if os.path.isdir(folder_path):
            folder_size = get_folder_size(folder_path)
            folder_sizes.append((folder_path, folder_size))
    
    # 按大小（从大到小）对文件夹排序
    sorted_folders = sorted(folder_sizes, key=lambda x: x[1], reverse=True)
    return sorted_folders

if __name__ == "__main__":
    specified_path = "/mnt/e/manga"
    sorted_folders = sort_folders_by_size(specified_path)
    
    print("\n按大小排序的文件夹（从大到小）：")
    for folder_path, folder_size in sorted_folders:
        print(f"{folder_path} - {folder_size} 字节")
