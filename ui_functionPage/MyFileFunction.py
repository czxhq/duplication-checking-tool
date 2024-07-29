import json
import os
import shutil
import zipfile
from datetime import datetime


def copy_folder(src_folder, dst_folder, file_type):
    if not os.path.exists(src_folder):
        print(f"源文件夹 {src_folder} 不存在。")
        return

    new_dst = os.path.join(dst_folder, os.path.basename(src_folder))
    print(new_dst)
    if not os.path.exists(new_dst):
        os.makedirs(new_dst)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 只复制 .py 文件
            if file.endswith(file_type):
                src_file_path = os.path.join(root, file)
                # 构建目标文件路径
                relative_path = os.path.relpath(root, src_folder)
                dst_file_path = os.path.join(new_dst, relative_path, file)

                # 创建目标文件夹（如果不存在）
                dst_file_dir = os.path.dirname(dst_file_path)
                if not os.path.exists(dst_file_dir):
                    os.makedirs(dst_file_dir)

                # 复制文件
                shutil.copy(src_file_path, dst_file_path)
                print(f"文件 {src_file_path} 已复制到 {dst_file_path}")


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

def addPACKAGE(path, username, file_type):
    time = datetime.now()
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
    file_type_index = {
        '.c': 'c',
        '.py': 'python',
        '.cpp': 'cc',
        '.java': 'java',
        '.v': 'verilog',
        '.asm': 'mips',
        '.js': 'javascript'
    }
    data = {
        'username': username,
        'date' : formatted_time,
        'foldername' : 'codes',
        'Mode': file_type_index.get(file_type)
    }
    file_path = os.path.join(path, "PACKAGE.json")
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"PACKAGE.json 文件成功创建")

def getHighRedundancyFiles(json_file, code_file, work_dir):
    with open(json_file, 'r') as f:
        data = json.load(f)

    high_redundancy_files = set()

    for item in data:
        file1 = item[0]
        file2 = item[1]
        redundancy_file1 = item[2]
        redundancy_file2 = item[3]

        if redundancy_file1 >= 30:
            high_redundancy_files.add(file1)
        if redundancy_file2 >= 30:
            high_redundancy_files.add(file2)
    plagiarize_code_path = os.path.join(work_dir, "plagiarize_code")
    extract_zip(code_file, plagiarize_code_path)

    plagiarize_codes_path = os.path.join(plagiarize_code_path, "codes")

    new_high_redundancy_files = set()

    for file_path in high_redundancy_files:
        new_file_path = os.path.join(plagiarize_codes_path, file_path[2:])
        new_high_redundancy_files.add(new_file_path)

    delete_unlisted_files(plagiarize_codes_path, new_high_redundancy_files)

def delete_unlisted_files(folder_path, keep_files):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path not in keep_files:
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
