import datetime
import re
import random
from typing import Dict, List, Optional, Tuple, Any


class GitAI:
    def __init__(self, user_name: str = "开发者"):
        # 基础属性
        self.name = "Git"
        self.icon = "📦"
        self.user_name = user_name
        self.super_brain_connected = True  # 模拟超级大脑已连接

        # 1. 新增：Git基础知识库（核心概念+入门知识）
        self.basic_knowledge: Dict[str, Any] = {
            "核心概念": {
                "仓库（Repository）": {
                    "定义": "存储项目代码和版本历史的数据库，分为本地仓库（本地文件夹）和远程仓库（如GitHub）",
                    "作用": "追踪所有文件的修改记录，支持回滚到任意历史版本",
                    "示例": "通过git init初始化本地仓库，git clone <远程地址>复制远程仓库到本地"
                },
                "工作区（Working Directory）": {
                    "定义": "本地电脑中能看到的项目文件夹，存放当前正在编辑的文件",
                    "作用": "开发者实际修改文件的区域，修改后需通过git add提交到暂存区",
                    "关联": "工作区 → 暂存区（git add） → 本地仓库（git commit）"
                },
                "分支（Branch）": {
                    "定义": "独立的代码开发线路，默认主分支为main（或master）",
                    "作用": "隔离不同功能/修复的开发，避免相互干扰，完成后合并到主分支",
                    "实操": "git branch <分支名> 创建分支，git checkout <分支名> 切换分支"
                },
                "提交（Commit）": {
                    "定义": "将暂存区的修改保存到本地仓库的操作，每个提交有唯一ID（哈希值）",
                    "作用": "记录一次完整的修改，包含修改内容、作者、时间，是版本回溯的基础",
                    "规范": "提交信息需清晰描述修改（如'fix: 修复登录按钮无响应问题'）"
                }
                # 可扩展更多基础概念...
            },
            "入门流程": [
                "1. 安装Git并配置用户信息（git config --global user.name '姓名'；git config --global user.email '邮箱'）",
                "2. 初始化仓库（git init）或克隆远程仓库（git clone <URL>）",
                "3. 编辑文件后，通过git add <文件名> 将修改加入暂存区",
                "4. 通过git commit -m '提交信息' 将暂存区修改提交到本地仓库",
                "5. 通过git push 推送到远程仓库，或git pull 获取远程最新代码"
            ],
            "常见术语": {
                "HEAD": "指向当前分支的最新提交（可理解为'当前位置'）",
                "暂存区（Index）": "介于工作区和仓库之间的临时存储区，用于确认要提交的修改",
                "合并（Merge）": "将一个分支的修改合并到另一个分支的操作"
            }
        }

        # 2. 原有知识库升级（整合基础概念查询）
        self.knowledge_base: Dict[str, Any] = {
            "commands": {  # 命令手册（同上一版本，略）
                "git commit": {"desc": "提交暂存区变更...", "usage": "git commit -m '信息'", ...},
                "git branch": {"desc": "管理分支...", "usage": "git branch <名称>", ...},
                ...
            },
            "best_practices": {...},  # 最佳实践（同上）
            "errors": {...},  # 错误解决方案（同上）
            "user_added": {}  # 用户补充知识（同上）
        }

        # 3. 超级大脑接口（模拟）
        self.super_brain = {
            "get_advanced_knowledge": self._super_brain_query  # 模拟调用外部知识源
        }

        # 4. 用户学习系统（记录学习进度）
        self.user_learning: Dict[str, Any] = {
            "已掌握概念": [],  # 如["仓库", "提交"]
            "学习难点": [],  # 如["rebase与merge的区别"]
            "学习阶段": "入门"  # 入门/进阶/精通
        }

        # 其他状态（仓库状态、用户画像等，同上一版本）
        self.repo_state = {...}
        self.user_profile = {...}

    def _super_brain_query(self, query: str) -> str:
        """
        模拟调用超级大脑获取深度知识（如前沿技巧、复杂场景方案）
        实际场景可对接GitHub API、Stack Overflow、技术文档库等
        """
        # 模拟返回结果（根据查询内容生成专业信息）
        if "最新工作流" in query:
            return (f"🔍 超级大脑提供2025年主流Git工作流：\n"
                    "1. Trunk-Based Development（主干开发）：适合敏捷团队，短周期合并到主干，依赖自动化测试\n"
                    "2. GitLab Flow：在GitHub Flow基础上增加环境分支（如test/prod），通过CI/CD自动部署\n"
                    "3. 企业级混合流：结合GitFlow的分支隔离和Trunk的快速迭代，适合大型团队多版本并行开发")
        
        elif "rebase与merge区别" in query:
            return (f"🔍 超级大脑深度解析：\n"
                    "• 原理：rebase是'重新基于'目标分支应用提交（线性历史），merge是创建新的合并提交（保留分支历史）\n"
                    "• 场景：个人开发分支用rebase保持历史整洁；公共分支（如main）用merge保留协作痕迹\n"
                    "• 风险：rebase会改写历史，已推送到远程的分支慎用（需强制推送，可能影响协作）")
        
        elif "企业级安全配置" in query:
            return (f"🔍 超级大脑企业方案：\n"
                    "1. 启用Git签名（git config --global commit.gpgsign true）确保提交真实性\n"
                    "2. 通过GitLab/GitHub的分支保护规则，禁止直接推送到main分支，必须通过PR/MR审核\n"
                    "3. 使用secret scanning工具检测提交中的密钥/密码泄露")
        
        else:
            return f"🔍 超级大脑暂未收录该内容，已记录查询：{query}（将定期更新）"

    def _query_basic_knowledge(self, query: str) -> Optional[str]:
        """查询基础知识库（核心概念、入门流程、术语）"""
        query = query.lower()
        
        # 1. 查询核心概念
        for concept, info in self.basic_knowledge["核心概念"].items():
            if concept.lower() in query or any(kw in query for kw in concept.split("（")):
                # 标记为已掌握（学习进度更新）
                if concept not in self.user_learning["已掌握概念"]:
                    self.user_learning["已掌握概念"].append(concept)
                return (f"📖 基础概念：{concept}\n"
                        f"定义：{info['定义']}\n"
                        f"作用：{info['作用']}\n"
                        f"实操：{info.get('示例') or info.get('实操') or '无'}")
        
        # 2. 查询入门流程
        if re.search(r"流程|步骤|怎么开始|入门", query):
            return "📝 Git入门流程：\n" + "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.basic_knowledge["入门流程"])])
        
        # 3. 查询常见术语
        for term, desc in self.basic_knowledge["常见术语"].items():
            if term.lower() in query:
                return f"📚 术语解释：{term} → {desc}"
        
        return None

    def _query_knowledge(self, query: str) -> str:
        """
        升级知识查询逻辑：
        1. 先查基础知识（适合新手）
        2. 再查本地专业知识（命令/错误/实践）
        3. 最后调用超级大脑（深度/前沿知识）
        """
        # 1. 优先查询基础知识
        basic_info = self._query_basic_knowledge(query)
        if basic_info:
            return basic_info
        
        # 2. 查询本地专业知识库
        professional_info = super()._query_knowledge(query)  # 复用之前的知识库查询逻辑
        if professional_info:
            return professional_info
        
        # 3. 调用超级大脑（若已连接）
        if self.super_brain_connected:
            return self.super_brain["get_advanced_knowledge"](query)
        else:
            return f"{self.icon} 未找到相关知识，且超级大脑未连接（请检查网络）"

    def _parse_natural_language(self, user_input: str) -> Tuple[str, Dict]:
        """增强解析：识别基础知识查询（如“什么是仓库”“Git入门步骤”）"""
        user_input = user_input.lower().strip()
        
        # 基础知识查询（优先处理）
        if re.search(r"什么是|是什么|定义|概念|术语|入门|流程|步骤", user_input):
            return "query_knowledge", {"query": user_input}
        
        # 其他意图解析（复用之前的逻辑：提交/分支/冲突等）
        return super()._parse_natural_language(user_input)

    def get_learning_progress(self) -> str:
        """生成用户学习进度报告（结合基础知识掌握情况）"""
        mastered = len(self.user_learning["已掌握概念"])
        total_concepts = len(self.basic_knowledge["核心概念"])
        progress = round(mastered / total_concepts * 100, 1) if total_concepts > 0 else 0
        
        return (f"{self.icon} 您的Git学习进度：\n"
                f"- 已掌握核心概念：{', '.join(self.user_learning['已掌握概念']) or '暂无'}\n"
                f"- 进度：{progress}%（共{total_concepts}个核心概念）\n"
                f"- 建议学习：{'、'.join(self.basic_knowledge['核心概念'].keys() - set(self.user_learning['已掌握概念']))[:50]}...")

    def run(self):
        """升级交互入口：支持基础知识学习和超级大脑调用"""
        print(f"👋 你好，{self.user_name}！我是{self.name} AI {self.icon}，已加载Git基础知识库并连接超级大脑")
        print("💡 可查询基础概念（如'什么是分支'）、实操命令，或获取前沿技巧（输入'帮助'查看功能）\n")
        
        while True:
            user_input = input(f"{self.user_name} > ")
            if user_input.lower() in ["退出", "exit"]:
                # 输出学习总结
                print(f"\n{self.icon} 学习总结：\n" + self.get_learning_progress())
                print("再见！持续学习，Git技能会越来越强~")
                break
            
            # 解析输入并执行
            cmd_type, params = self._parse_natural_language(user_input)
            result = ""
            
            if cmd_type == "query_knowledge":
                result = self._query_knowledge(params["query"])
                # 记录学习难点（若查询多次未掌握的概念）
                if "未找到" not in result and any(concept in params["query"] for concept in self.basic_knowledge["核心概念"]):
                    if params["query"] not in self.user_learning["学习难点"]:
                        self.user_learning["学习难点"].append(params["query"])
            
            # 其他功能（提交/分支/冲突检测等，复用之前的逻辑）
            elif cmd_type == "generate_commit":
                result = self.generate_commit_message(params["type"], params["desc"])
            elif cmd_type == "create_branch":
                ...  # 分支创建逻辑
            elif cmd_type == "detect_conflict":
                ...  # 冲突检测逻辑
            else:
                result = f"{self.icon} 请尝试查询概念（如'什么是提交'）或操作（如'创建分支'）"
            
            print(f"{self.name} AI > {result}\n")


# 启动交互（直接运行体验）
if __name__ == "__main__":
    git_ai = GitAI(user_name="编程新手")
    git_ai.run()
