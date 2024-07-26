import os
import json
import multiprocessing
import mosspy
import zipfile
import shutil

def __Upload(Folder, Mode, userid = 795462167):
    os.chdir(Folder)
    # Moss脚本
    moss = mosspy.Moss(userid, Mode)
    moss_folder = './moss_result/'
    moss_result = './moss_result.zip'
    # 删除临时文件夹
    try:
        shutil.rmtree(moss_folder)
    except:
        print('not ok')
        pass
    Files = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            f = os.path.join(root, file)
            moss.addFile(f)
            Files.append(f.replace('./', ''))
    print(Files)
    # 下载结果
    url = moss.send(lambda file_path, display_name: print('*', end='', flush=True))
    print ("\nReport Url: " + url)
    mosspy.download_report(url, moss_folder, connections = min((len(Files)**2)*3, 1000), log_level=3, on_read=lambda url: print('*', end='', flush=True)) 
    # 正则提取信息
    result = []
    from bs4 import BeautifulSoup
    with open(os.path.join(moss_folder, 'index.html'), 'r', encoding='utf-8') as file:
        html_doc = file.read()
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_doc, 'html.parser')
        # 查找所有的表格行<tr>元素
        rows = soup.find_all('tr')
        # 跳过第一行，因为第一行是表头
        for row in rows[1:]:
            # 找到当前行的所有单元格<td>元素
            columns = row.find_all('td')
            # 提取文件位置信息，通常在<a>标签内
            file1 = columns[0].find('a').get_text() if columns[0].find('a') else ''
            file2 = columns[1].find('a').get_text() if columns[1].find('a') else ''
            # 提取百分比信息，它位于文件位置信息的括号内
            percent1 = int(file1.split('(')[-1].split('%')[0])
            percent2 = int(file2.split('(')[-1].split('%')[0])
            file1 = file1.replace(f" ({percent1}%)", '')
            file2 = file2.replace(f" ({percent2}%)", '')
            # 提取匹配的行数
            lines_matched = columns[2].text.strip() if len(columns) > 2 else ''
            # 打印结果
            result.append([str(file1), str(file2), int(percent1), int(percent2), int(lines_matched)])
    # 导出结果为JSON
    with open(os.path.join(moss_folder, 'result.json'), 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)
    # 替换颜色
    for root, dirs, files in os.walk(moss_folder):
        for file in files:
            f = os.path.join(root, file)
            with open(f, 'r', encoding='utf-8') as html:
                content = html.read()
                content.replace('<font color="#00FF00">', '<font color="#00CC00">')
                content.replace('<font color="#00FFFF">', '<font color="#00CCCC">')
            with open(f, 'w', encoding='utf-8') as html:
                html.write(content)
    # 打包结果为Zip
    with zipfile.ZipFile(moss_result, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(moss_folder):
            for filename in filenames:
                zipf.write(os.path.join(foldername, filename), os.path.relpath(os.path.join(foldername, filename), moss_folder))
    # 删除临时文件夹
    try:
        shutil.rmtree(moss_folder)
    except:
        pass
def run(Folder, Mode):
    p = multiprocessing.Process(target=__Upload, args=(Folder,Mode,))
    p.start()
    p.join()
    
if __name__ == '__main__':
    #
    # 只能用run起一个线程运行Upload函数，不可直接运行Upload
    #
    # 针对 {Mode} 类型的语言进行查重，可选 Mode 如下：
    #     {"c","cc","java","ml","pascal","ada","lisp","scheme",
    #     "haskell","fortran","ascii","vhdl","verilog","perl",
    #     "matlab","python","mips","prolog","spice","vb",
    #     "csharp","modula2","a8086","javascript","plsql"}
    run(Folder='./moss_test/', Mode='python')
    print(os.getcwd())