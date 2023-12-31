import re
def lexical_analysis(input_str):
    # 定义正则表达式模式
    const_pattern = re.compile(r'\bconst\b')
    identifier_pattern = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
    char_pattern = re.compile(r'\'[^\'？]\'')
    string_pattern = re.compile(r'\"[^\"]*\"')
    integer_pattern = re.compile(r'[+-]?\d+')
    float_pattern = re.compile(r'[+-]?\d+\.\d+?')
    scientific_notation_pattern = re.compile(r'[+-]?\d+(\.\d*)?[eE][+-]?\d+')
    # 初始化统计变量
    char_count = 0
    string_count = 0
    integer_count = 0
    float_count = 0
    scientific_notation_count = 0
    # 存储已解析的常量名称及其计数
    parsed_names = {}
    # 判断是否以 "const" 开头
    if const_pattern.match(input_str):
        # 去除空格
        input_str = input_str.replace(" ", "")
        # 分割输入字符串
        declarations = input_str[5:].split(',')
        for declaration in declarations:
            try:
                # 判断常量名
                match_identifier = identifier_pattern.match(declaration)
                if not match_identifier:
                    print("Error: 无效符号")
                    return
                original_name = match_identifier.group()
                # 处理重复的常量名
                if original_name in parsed_names:
                    parsed_names[original_name] += 1
                    new_name = f"{original_name}_{parsed_names[original_name]}"
                    print(f"Warning: 常量名'{original_name}'重复，为其生成新的名称'{new_name}'")
                    constant_name = new_name
                else:
                    parsed_names[original_name] = 1
                    constant_name = original_name
                declaration = declaration[len(original_name):]
                # 判断等号
                if not declaration.startswith('='):
                    print("Error: 没‘=’")
                    return
                declaration = declaration[1:]
                # 识别常量类型和值
                if char_pattern.match(declaration):
                    char_count += 1
                    constant_type = "char"
                    constant_value = declaration[1:-1]
                elif string_pattern.match(declaration):
                    string_count += 1
                    constant_type = "string"
                    constant_value = declaration[1:-1]
                elif scientific_notation_pattern.match(declaration):
                    scientific_notation_count += 1
                    constant_type = "scientific_notation"
                elif '.' in declaration and float_pattern.match(declaration):
                    # 如果字符串中存在小数点，且匹配浮点数模式
                    float_count += 1
                    constant_type = "float"
                    constant_value = float(declaration)
                elif integer_pattern.match(declaration):
                    # 否则，匹配整数模式
                    integer_count += 1
                    constant_type = "integer"
                    constant_value = int(declaration)
                else:
                    constant_value = "Error: 无效值"
                # 输出二元组
                print(f"{constant_name}({constant_type}, {constant_value})")
            except Exception as e:
                continue
        # 输出统计信息
        print(f"Integer Count: {integer_count}")
        print(f"Float Count: {float_count}")
        print(f"Char Count: {char_count}")
        print(f"String Count: {string_count}")
        print(f"scientific_notation Count: {scientific_notation_count}")
    else:
        print("Error: 必须以const开头.")
# 从键盘输入或从文件读入字符串
if __name__ == "__main__":
    while True:
        input_str = input("请输入字符串: ")
        if input_str.lower() == "exit":
            break
        lexical_analysis(input_str)
