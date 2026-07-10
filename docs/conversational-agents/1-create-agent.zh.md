---
source_hash: 6f9859a85684dafb0674c1aff4cbac32
---

# 使用 Autopilot 创建对话式智能体

!!! tip "这节课的计划如下："

    1. 在 **Studio Web** 中创建一个新的对话式智能体
    2. 让 **Autopilot** 根据你对智能体用途的描述生成系统提示词
    3. 检查 Autopilot 发现的工具和上下文
    4. 连接一个 **Context Grounding 索引**，让智能体的回答有据可依

## 目标

你将创建一个可用的对话式智能体，它能回答关于此前练习中的发票和 ServiceNow 工单的问题。**Autopilot** 会分析你的描述，自动接入可用的工具，并生成一份指导智能体行为的系统提示词。完成后，你的聊天机器人智能体将以真实数据和文档为依据，避免凭空编造答案。

## 为什么 Autopilot 很重要

从零开始配置一个智能体可能让人不知所措。你需要选对工具、写清指令，还要确保一切协同运转。**Autopilot** 替你完成这些重活：它读取你的自然语言描述，扫描 **Orchestrator** 中可用的工具和上下文来源，然后生成一份把这一切整合起来的系统提示词。检查生成结果并做出调整——手动改，或者通过 Autopilot 聊天来改。

## 操作步骤

### 1. 打开 Studio Web 并创建新智能体


[[[
在 **Studio Web** 中，点击右上角蓝色的 **Create New**（新建）按钮。在下拉菜单中选择 **Agent**，创建一个新的解决方案。
|30|
![Studio Web 的 Create New 菜单，高亮显示 Agent 选项](1-create-agent.images/1-create-new-menu.png){ .screenshot }
]]]

### 2. 选择 Conversational 智能体类型

向导会出现，询问你想构建哪种智能体。

[[[
![智能体类型选择界面，显示 Conversational 选项和描述输入框](1-create-agent.images/2-select-conversational-type.png){ .screenshot }
|70|

选择 **Conversational**（对话式）——这种类型专为交互式对话设计，智能体通过持续对话回答用户的问题。

在描述框中，告诉 **Autopilot** 你的智能体应该做什么：

```text
This conversational agent that will use available tools from UiPath Orchestrator and context grounding indexes to answer various questions about: Invoice processing documents, ServiceNow incidents and associated Orchestrator Jobs.
```
]]]

这段描述会指导 **Autopilot** 生成你的系统提示词。要写得具体：点明领域（发票、作业），并提示你期望用到的工具或上下文。另外，明确智能体不应涉及的范围、写出其他约束条件，也很实用。

点击 **Generate Agent**（生成智能体），让 **Autopilot** 分析你的设置。

!!! tip "最佳实践"
    把任务交给最擅长的对象。写提示词这件事，最擅长的对象就是……那个整天读提示词的家伙。

### 3. 观看 Autopilot 发现工具和上下文

**Autopilot** 运行时会：

- 扫描你的 **Orchestrator**，寻找可用工具
- 识别上下文来源（比如 **Context Grounding 索引**）
- 分析你的描述，判断哪些内容相关

![Autopilot 分析进行中，显示已成功发现工具和上下文](1-create-agent.images/3-autopilot-analyzing.png){ .screenshot width="800" }

**Autopilot** 会列出它在你的 **Orchestrator** 中找到的工具。仔细检查这个列表。每个工具都代表一个智能体可以调用的 RPA 流程、API 或其他自动化。

![Autopilot 发现的可用工具列表，高亮显示 Accept 按钮](1-create-agent.images/4-available-tools.png){ .screenshot width="800" }

点击 **Accept**（接受），确认这些工具将对你的智能体可用。注意，你只能看到自己有权限使用的工具，这由 Orchestrator 的基于角色的访问控制（RBAC）决定。当你发布并运行这个自动化时，机器人用户也需要同样的权限——否则工具调用会失败。

### 4. 检查生成的系统提示词

**Autopilot** 现在已经创建了一份完整的系统提示词。这份提示词定义了：

- **角色** —— 智能体是什么（例如“You are an invoice and job query specialist”）
- **工具规则** —— 何时以及如何使用每个可用工具
- **领域约束** —— 智能体应该做什么、不应该做什么

!!! tip
    系统提示词是智能体的操作指南兼岗位说明书。一份写得好的提示词，决定了智能体是帮上忙还是瞎编。


![左侧为系统提示词编辑器，右侧为显示生成提示词的 Autopilot Preview](1-create-agent.images/5-review-system-prompt-W.png){ .screenshot width="900" }

[[[
如果提示词看起来没问题，点击 **Accept** 确认。

之后你随时可以再编辑它。
|50|
![带有智能体行为准则的最终确认对话框](1-create-agent.images/6-confirm-behavior.png){ .screenshot }
]]]

### 5. 添加 Context Grounding 索引

为了让配置更完整，我们来接入一些现有索引中的数据。有了上下文，对话式智能体就能引用来源，这对需要阅读冗长复杂文档的聊天机器人自动化非常有用。

在**智能体画布**上，点击 Agent 节点下 **Context** 处的 **+** 图标，添加一个知识源。

![智能体画布，高亮显示 Context 连接点的添加按钮](1-create-agent.images/7-add-context.png){ .screenshot width="800" }

右侧面板会打开，显示可用的上下文来源。搜索“security”，找到 **UiPath Security data** 索引，其中包含关于 UiPath 平台的非常全面的文档。你可以询问的主题包括：**数据加密、基于角色的访问控制、智能体安全、数据驻留**。

- 如果想保留源文件，可以下载：[UiPath Security Whitepaper.pdf](../assets/UiPath Security Whitepaper.pdf)
- 想探索更多有意思的白皮书、了解 UiPath 平台安全，请访问 [UiPath Trust Portal](https://trust.uipath.com/) 和 [UiPath Security 页面](https://www.uipath.com/legal/trust-and-security/security)

### 6. 配置智能体如何从索引中检索

[[[
选择索引后，会出现一个配置表单。

这些设置控制智能体如何搜索和检索信息。

使用简单的语义搜索即可。你可以把相关度阈值提高到 0.3–0.5 来收窄结果——对这种大文档很有用。

你的智能体现在已经配置完毕。
|50|
![索引配置表单，显示所有检索设置](1-create-agent.images/8-configure-context-W.png){ .screenshot width="900" }
]]]

### 7. 检查完整的智能体配置

你的智能体现在已经接好了工具和上下文，可以回答问题了。你可以在画布上看到全貌。

![完整的智能体配置，显示上下文和工具连接到中央的 Agent 节点](1-create-agent.images/9-complete-agent-W.png){ .screenshot width="900" }


[[[
别忘了照例给它起一个有意义的名字：
|50|
![解决方案 Explorer 中展开的 Conversational Agent 组件](1-create-agent.images/10-agent-in-explorer.png){ .screenshot }
]]]


!!! tip "每日一贴"
    很重要的一点是把所有工具像触手一样排布，如图所示。这样智能体就能高效地多线作业——而且就像真正的章鱼一样，当某次工具调用失败时，它可以重新长出那条触手。更妙的是，这只**智能体章鱼**还能随着时间长出新触手，不断扩大自己的能力范围。当然，这只是一个注意力测试，也就是说你完全可以换任何一种动物，让智能体模仿它的天然优势！

你的智能体现在可以测试了。但先别急——在下一课中，你将探索它可以使用的工具，并理解它们的工作原理。
