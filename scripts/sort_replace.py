import shutil
import sys
import unicodedata


def normalize_pinyin(pinyin):
    """
    将拼音字符串标准化，去除音调符号等修饰字符

    :param pinyin: 需要去除拼音的原始字符串
    :return str: 处理之后的干净字符串
    """
    return ''.join(c for c in unicodedata.normalize('NFD', pinyin) if unicodedata.category(c) != 'Mn')

def sort_rime_dict_yaml(file_path):
    """
    对Rime输入法的YAML格式词库文件按拼音进行排序，并保留词频和注释行。

    :param file_path: 词库文件路径
    :param backup_path: 备份词库文件路径
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 分离元数据、词条部分和注释
    metadata = []
    entries = []
    comments = []
    in_entries = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '...':
            in_entries = True
            continue  # 跳过 ... 标记，不加入 metadata 列表
        if not in_entries:
            metadata.append(line)
        else:
            if not stripped_line or stripped_line.startswith('#'):
                # 保留注释行
                comments.append(line)
            else:
                entries.append(line.strip())

    # 解析词条部分并排序
    def parse_entry(entry):
        parts = entry.split('\t')
        word = parts[0]
        pinyin = parts[1]  # 只有一个拼音
        freq = parts[2] if len(parts) > 2 else None  # 如果有词频则保留
        return {'word': word, 'pinyin': pinyin, 'freq': freq, 'original': entry}

    parsed_entries = [parse_entry(e) for e in entries if '\t' in e]
    sorted_entries = sorted(parsed_entries, key=lambda x: normalize_pinyin(x['pinyin']))
    sorted_entries_content = [entry['original'] for entry in sorted_entries]

    # 写入新的文件
    with open(file_path, 'w', encoding='utf-8') as output_file:
        # 写入元数据
        output_file.writelines(metadata)
        output_file.write('...\n')  # 添加结束符
        # 原本有空行就不要再加了
        # output_file.write('\n')  # 添加一个空行分隔元数据和词条

        # 写入注释行
        for comment in comments:
            output_file.write(comment)

        # 写入排序后的词条
        for entry in sorted_entries_content:
            output_file.write(entry + '\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print("将文件拖入到此处:" + input_file)
        backup_file = input_file + ".bak"
    else:
        # 使用示例
        input_file = input("将文件拖入到此处:")  # 替换为你的输入文件路径
        backup_file = input_file + ".bak"

    shutil.copy(input_file, backup_file)
    sort_rime_dict_yaml(input_file)
