class LL1Parser:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table

    def parse(self, input_string):
        stack = ["$", "S"]  # 初始化栈
        input_tokens = list(input_string) + ["$"]  # 在输入的末尾添加$
        current_input = input_tokens.pop(0)

        while stack:
            top_of_stack = stack[-1]

            if top_of_stack in self.parsing_table and current_input in self.parsing_table[top_of_stack]:
                # 用相应的产生规则替换栈顶的非终结符
                production = self.parsing_table[top_of_stack][current_input]
                stack.pop()
                stack.extend(reversed(production))
            elif top_of_stack == current_input:
                # 匹配终结符
                stack.pop()
                current_input = input_tokens.pop(0)
            else:
                print("错误：无效的输入字符串")
                return

        print("输入字符串是有效的！")

# 示例用法
parsing_table = {
    # 在这里构建你的LL(1)分析表
}
ll1_parser = LL1Parser(parsing_table)
input_string = input("输入要分析的字符串：")
ll1_parser.parse(input_string)
