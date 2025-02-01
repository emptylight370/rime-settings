def sort_rime_dict_yaml(input_path, output_path):
    """
    对Rime输入法的YAML格式词库文件按拼音进行排序。
    
    :param input_path: 原始词库文件路径
    :param output_path: 排序后的输出文件路径
    """
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 分离元数据和词条部分
    metadata = []
    entries = []
    in_entries = False

    for line in lines:
        if line.strip() == '...':
            in_entries = True
            metadata.append(line)
            continue
        if not in_entries:
            metadata.append(line)
        else:
            entries.append(line.strip())

    # 解析词条部分并排序
    def parse_entry(entry):
        parts = entry.split('\t')
        word = parts[0]
        pinyin = parts[1].split(',')[0]  # 如果有多个拼音，只取第一个作为排序依据
        return {'word': word, 'pinyin': pinyin}

    parsed_entries = [parse_entry(e) for e in entries if '\t' in e]  # 确保是有效的词条行
    sorted_entries = sorted(parsed_entries, key=lambda x: x['pinyin'])

    # 准备新的词条内容
    sorted_entries_content = [f"{entry['word']}\t{entry['pinyin']}" for entry in sorted_entries]

    # 写入新的文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(metadata)  # 写入元数据
        output_file.write('\n')  # 添加一个空行分隔元数据和词条
        for entry in sorted_entries_content:
            output_file.write(entry + '\n')

if __name__ == '__main__':
    # 使用示例
    input_file = input("将文件拖入到此处:")  # 替换为你的输入文件路径
    strs = input_file.split(".dict")
    output_file = strs[0] + ".sorted.dict" + strs[1]  # 替换为你想要保存的输出文件路径

    sort_rime_dict_yaml(input_file, output_file)
