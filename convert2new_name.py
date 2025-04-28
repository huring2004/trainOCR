import os

folder_path = "./photo"
file_list = os.listdir(folder_path)

image_files = [f for f in file_list if f.lower().endswith(('.png'))]

for idx, filename in enumerate(sorted(image_files), start=2001):
    old_path = os.path.join(folder_path, filename)

    # Giữ nguyên đuôi file gốc
    ext = os.path.splitext(filename)[1]

    # Tên mới
    new_filename = f"image{idx}{ext}"  # VD: sample_001.png
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)
    print(f"Đổi {filename} → {new_filename}")
