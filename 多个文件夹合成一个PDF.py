import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_jpgs_to_single_pdf(input_dir):
    # 创建一个 PDF 文件
    pdf_path = os.path.join(input_dir, "combined_images.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # 遍历输入目录中的所有 JPG 图像文件
    for root, dirs, files in os.walk(input_dir):
        for image_file in files:
            if image_file.lower().endswith((".jpg",".png",".webp",".jpeg")):
                jpg_path = os.path.join(root, image_file)
                image = Image.open(jpg_path)

                # 获取图像的原始大小
                image_width, image_height = image.size

                # 设置 PDF 页面大小为图像的大小
                c.setPageSize((image_width, image_height))

                # 在 PDF 中绘制图像，不进行缩放
                c.drawImage(jpg_path, 0, 0, width=image_width, height=image_height)
                c.showPage()

    c.save()
    print(f"Converted JPG files to {pdf_path}")

if __name__ == "__main__":
    input_directory = r"E:\\download_temp\\hentai\\[Arai Kei] Gunjo Gunzo [Chinese] [心血來潮的村民渣重嵌] [Digital]"
    convert_jpgs_to_single_pdf(input_directory)
