class GitAI:
    def __init__(self):
        self.name = "Git"  # AI 名称
        self.icon = "🚀"  # 代表高效版本控制的图标

    def generate_commit_message(self, change_description):
        """根据代码变更描述生成提交信息"""
        return f"{self.icon} {self.name} 生成：{change_description[:30]}...（优化提交语义）"

    def suggest_code_review(self, code_snippet):
        """对代码片段提出改进建议"""
        return f"{self.icon} {self.name} 建议：检查循环效率，可尝试列表推导式或生成器优化"


# 测试 AI 功能
if __name__ == "__main__":
    git_ai = GitAI()
    print(f"AI 名称：{git_ai.name}，图标：{git_ai.icon}")
    print("提交信息生成示例：", git_ai.generate_commit_message("修复用户登录模块的输入校验逻辑"))
    print("代码审查建议示例：", git_ai.suggest_code_review("for num in range(100):\n    if num % 2 == 0:\n        print(num)"))
