import sys

def sort_rime_dict_yaml(input_path, output_path):
    """
    对Rime输入法的YAML格式词库文件按拼音进行排序，并保留词频和注释行。

    :param input_path: 原始词库文件路径
    :param output_path: 排序后的输出文件路径
    """
    with open(input_path, 'r', encoding='utf-8') as file:
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
    sorted_entries = sorted(parsed_entries, key=lambda x: x['pinyin'])
    sorted_entries_content = [entry['original'] for entry in sorted_entries]

    # 写入新的文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
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
        strs = input_file.split(".dict")
        output_file = strs[0] + ".sorted.dict" + strs[1]
    else:
        # 使用示例
        input_file = input("将文件拖入到此处:")  # 替换为你的输入文件路径
        strs = input_file.split(".dict")
        output_file = strs[0] + ".sorted.dict" + strs[1]  # 替换为你想要保存的输出文件路径

    sort_rime_dict_yaml(input_file, output_file)
