import os
import shutil
import zipfile


def copy_folder(src, dst):
    if not os.path.exists(src):
        print(f"源文件夹 {src} 不存在。")
        return

    new_dst = os.path.join(dst, os.path.basename(src))
    if not os.path.exists(new_dst):
        os.makedirs(new_dst)

    try:
        shutil.copytree(src, new_dst, dirs_exist_ok=True)
    except Exception as e:
        print(f"复制文件夹时出错: {e}")


def copy_file(src_file, dst_folder):
    if not os.path.isfile(src_file):
        print(f"源文件 {src_file} 不存在。")
        return

    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    file_name = os.path.basename(src_file)
    dst_file = os.path.join(dst_folder, file_name)

    try:
        shutil.copy(src_file, dst_file)
    except Exception as e:
        print(f"复制文件时出错: {e}")


def extract_zip(zip_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)