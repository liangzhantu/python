import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_jpgs_to_single_pdf(input_dir):
    # 遍历输入目录中的所有子目录
    for root, dirs, files in os.walk(input_dir):
        pdf_path = os.path.join(input_dir, f"{os.path.basename(root)}.pdf")
        images = [filename for filename in files if filename.lower().endswith((".jpg",".png",".jpeg","webp"))]
        if images:
            convert_images_to_single_pdf(images, root, pdf_path)

def convert_images_to_single_pdf(image_files, output_dir, pdf_path):
    # 创建一个 PDF 文件
    c = canvas.Canvas(pdf_path, pagesize=letter)

    for image_file in image_files:
        jpg_path = os.path.join(output_dir, image_file)
        image = Image.open(jpg_path)

        # 获取图像的原始大小
        image_width, image_height = image.size

        # 设置 PDF 页面大小为图像的大小
        c.setPageSize((image_width, image_height))

        # 在 PDF 中绘制图像，不进行缩放
        c.drawImage(jpg_path, 0, 0, width=image_width, height=image_height)
        c.showPage()

    c.save()
    print(f"Converted {len(image_files)} JPG files to {pdf_path}")

if __name__ == "__main__":
    input_directory = r"E:\download_temp"
    convert_jpgs_to_single_pdf(input_directory)
