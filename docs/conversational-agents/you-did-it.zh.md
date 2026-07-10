---
source_hash: f5dace92b48b8305fc193ea1106a663e
---

# 大功告成！

!!! tip "恭喜你！"

    你构建了一个以真实文档为知识基础的对话式智能体，把它连接到了实时的自动化工具，并通过四类真实对话完成了验证。

---

## 你构建了什么

你在 **Agent Builder** 中创建了一个对话式智能体，它能实时回答关于发票和 ServiceNow 工单的问题。你用一个 **Context Grounding** 索引让它以 UiPath Security 文档为依据，然后把它连接到了发布在 **Orchestrator** 中的 RPA 和 API 工具。最后，你通过一次数据查询、一次事件查找、一次写入操作和一个知识问答对它做了测试——全程实时观看每一次工具调用。

| 组件 | 角色 |
|-----------|------|
| **对话式智能体** | 实时回答问题，范围限定在有据可查的知识和已连接的工具内 |
| **Context Grounding** | 让回答锚定在 UiPath Security 文档上，且来源可引用 |
| **Orchestrator Tools** | 让智能体按需获取发票数据和 ServiceNow 事件详情 |
| **提示词** | 引导用户提出智能体擅长回答的问题 |

---

## 接下来做什么？

什么时候用哪种智能体类型？

| | 自主式 | 对话式 |
|-|------------|----------------|
| **交互模式** | 单轮，根据初始提示词执行任务 | 多轮，来回对话 |
| **主要用例** | 根据明确、结构化的提示词执行复杂任务 | 实时用户支持与协助、交互式信息收集 |
| **用户输入** | 单条结构化的提示词或命令 | 持续的聊天消息，常带有模糊性 |
| **核心优势** | 执行预定义流程和自动化工作流 | 保持对话、理解上下文、处理细微差别 |

### 1. 部署并分享你的智能体

从 **Agent Builder** 发布你的智能体，把端点分享给同事。试着问它一些超出知识范围的问题——观察它如何处理不该回答的话题。

### 2. 查看可观测性数据

打开 Agent Builder 中的可观测性仪表盘。查看对话日志、工具调用频率和用户反馈，决定下一步改进什么。

---

## 持续迭代

**拓宽知识库**

- 向上下文关联来源添加更多文档索引，观察智能体的覆盖范围如何变化。

**添加更多 Orchestrator 工具**

- 连接更多工具和连接（例如 MCP 服务器）。

**打磨系统提示词**

- 根据数据和反馈定期回顾系统提示词。收紧领域约束、调整工具使用规则，看看智能体的行为如何变化。

---

## 了解更多

| 资源 | 说明 |
|----------|-------------|
| [对话式智能体](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents) | UiPath Agent Builder 中对话式智能体的概览 |
| [快速入门](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-getting-started) | 手把手教你创建第一个对话式智能体 |
| [智能体设计](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-design) | 提示词配置、工具与知识关联选项 |
| [部署](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-deployment) | 如何发布和分享对话式智能体 |
| [可观测性](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-observability) | 监控对话和工具使用情况 |
| [索引管理](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes) | 为上下文关联配置文档索引 |
