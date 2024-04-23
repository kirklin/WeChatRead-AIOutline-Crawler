import json

# 假设您的JSON数据存储在 'result.json' 文件中
json_file_path = 'result.json'

# 读取JSON文件
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 准备Markdown文件
markdown_lines = []

# 遍历每个章节
for chapter in data["itemsArray"]:
    if "items" in chapter:
        # 初始化最大层级
        max_level = 0
        for item in chapter["items"]:
            # 更新最大层级
            max_level = max(max_level, item.get("level"))

        for item in chapter["items"]:
            level = item.get("level")
            title = item.get("text")
            # 计算井号数量，最大层级的标题使用最大数量的井号
            hash_count = '#' * level if level != max_level else ''
            # 添加标题或文本
            markdown_lines.append(f"{hash_count} {title}\n")

# 将Markdown文本合并为一个字符串
markdown_text = '\n'.join(markdown_lines)

# 写入Markdown文件
with open('output.md', 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_text)

print("Markdown file has been created.")
