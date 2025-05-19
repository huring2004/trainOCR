import cv2
import pytesseract
import numpy as np
import os
import gc
# Đặt đường dẫn đến tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Đọc x ảnh đầu tiên
for i in range(1,101):
    image_path = f"../data2/image{i}.tif"
    # image_path = f"./img.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print("Không thể đọc ảnh. Kiểm tra đường dẫn!")
        exit()
    # Chuyển sang RGB (Pytesseract yêu cầu RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Trích xuất dữ liệu văn bản với ngôn ngữ
    text_data = pytesseract.image_to_data(img_rgb, lang="vie", output_type=pytesseract.Output.DICT)
    res =""
    print(i)

    # Vẽ hộp giới hạn và in văn bản
    for i in range(len(text_data["text"])):
    # Chỉ xử lý các vùng có độ tin cậy (conf) > 0 và có văn bản
        if float(text_data["conf"][i]) > 0 and text_data["text"][i].strip():
            x = text_data["left"][i]
            y = text_data["top"][i]
            w = text_data["width"][i]
            h = text_data["height"][i]
            text = text_data["text"][i]

            # Vẽ hộp giới hạn
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            res+= text +" "

    res = res.strip()
    # Tạo tên file .gt.txt
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    gt_txt_filename = f"{base_name}.gt.txt"

    # Ghi ra file
    output_path = os.path.join(os.path.dirname(image_path), gt_txt_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(res)

    del img
    del img_rgb
    del text_data
    gc.collect()
print("Xong")