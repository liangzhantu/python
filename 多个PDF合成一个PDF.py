import os
from PyPDF2 import PdfMerger

# 指定目标文件夹路径
target_path = ''

# 获取目标文件夹中的所有 PDF 文件
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

# 创建 PdfMerger 对象
pdf_merger = PdfMerger()

# 将所有文件添加到合并对象中
for pdf in pdf_lst:
    pdf_merger.append(pdf)

# 合并 PDF 文件
output_filename = os.path.basename(target_path) + '.pdf'  # 使用目录的基本名称作为输出文件名
output_path = os.path.join(target_path, output_filename)
with open(output_path, 'wb') as output_file:
    pdf_merger.write(output_file)

print(f"合并后的文件已保存在：{output_path}")
