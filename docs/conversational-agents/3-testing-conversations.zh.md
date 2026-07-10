---
source_hash: 07185e64a6f32e9d734977e8fe6a6628
---

# 一试身手

!!! tip "这节课的计划如下："

    1. 以调试模式运行智能体，从多个不同角度测试它
    2. 评估每个回答——智能体用对工具了吗？引用来源了吗？写入操作真的生效了吗？
    3. 了解评估选项，并将你的智能体正式发布上线

## 目标

学完这节课，你将带着智能体完成四类对话：一次数据查询、一次事件查找、一次发表备注的写入操作，以及一个基于上下文来源的知识问答。你会使用调试界面实时观察每一次工具调用，并亲自判断这些回答是否准确、可信。

## 通过对话来测试

自动化测试能发现回归问题。手动对话测试发现的是另一类问题：智能体是否真的*言之有理*，是否给了你想要的东西。如果哪里不对——回去检查提示词。

运行对话测试时，重点看四件事：

- **工具使用** —— 智能体调用了正确的工具吗？传入的参数合理吗？
- **回答质量** —— 答案准确、格式清晰、详略得当吗？
- **写入操作** —— 当智能体修改数据时，修改真的生效了吗？
- **知识关联（Grounding）** —— 当答案来自你的文档时，有没有正确引用来源？

围绕这四个类别精心挑选几段对话，就能对智能体的质量有一个可靠的判断。

## 操作步骤

### 1. 开始聊天会话

点击 **Debug**（调试），打开调试配置对话框。检查 **Context** 和 **Processes** 下列出的资源——这些就是智能体在会话期间可以访问的内容。

![调试配置，显示已选择的上下文来源和流程工具](3-testing-conversations.images/1-debug-configuration-W.png){ .screenshot width="900" }

确认所有你想测试的工具和上下文来源都已勾选，然后点击 **Save & Debug**。

### 2. 查看聊天界面

聊天加载完成后，你的起始提示词气泡已经就位。

[[[
点击某个气泡，或输入你自己的消息。智能体收到的始终是完整的实际提示词——而不只是简短的显示文本。
|30|
![智能体聊天首页，显示起始提示词气泡和消息输入框](3-testing-conversations.images/2-agent-chat-landing.png){ .screenshot }
]]]

### 3. 测试数据查询：发票支出

点击 **How much did we spend last month?**（上个月我们花了多少钱？）。实际发送给智能体的提示词是：

```text
Calculate total sum of all invoices during last 30 days.
```

观察执行轨迹。智能体以 `in_DaysAgo: 30` 调用 **Get Approved Invoices**，并从 Data Fabric 收到完整的发票列表：

![Get Approved Invoices 工具执行，显示输入参数和 JSON 输出](3-testing-conversations.images/3-invoice-tool-execution-W.png){ .screenshot width="900" }

智能体随后处理数据，返回一份清晰的汇总：

[[[
对照你所了解的系统中的发票数量，检查这些数字和币种分布是否合理。
|30|
![发票汇总结果，显示各币种总额和发票数量](3-testing-conversations.images/4-invoice-summary-result.png){ .screenshot }
]]]

### 4. 测试事件查找并写入备注

点击 **How many things break recently?**（最近坏了多少东西？）。实际提示词是：

```text
In the last 7 days, what were top 5 support incidents, who was the assignee?
```

智能体以 `in_TicketAgeDays: 7` 调用 **Get ServiceNow Incidents**，得到一份近期工单列表，随后分析并给出前五名：

![ServiceNow 事件结果，显示前 5 个工单的编号、日期和类别](3-testing-conversations.images/5-incidents-query-result-W.png){ .screenshot width="900" }

注意，当初始结果中没有返回处理人信息时，智能体会如实指出，而不是编造数据。这是一个好迹象。

接下来是更有难度的一个。输入：

```text
Add an internal note to first ticket, say "This is critical to address it with highest priority! Fix it asap!". Validate that the note is added because it's important!
```

智能体调用 **Post ServiceNow Incident Note**，然后立即运行 **Get ServiceNow Incident Notes** 来验证这次修改：

![Post ServiceNow 备注的执行和验证，显示两次工具调用均成功完成](3-testing-conversations.images/6-post-note-validation-W.png){ .screenshot width="900" }

智能体没有一写了之、假设操作成功——它做了验证。这正是你应该关注的正确行为。

[[[
想彻底放心的话，可以请培训师直接在 **ServiceNow** 中查找该事件，检查活动时间线。智能体在真实系统中做出了一次真实的修改——备注一字不差地出现在那里。
|30|
![ServiceNow 活动时间线，高亮显示来自 UiPath Labs 的新增内部备注](3-testing-conversations.images/7-servicenow-activity-timeline.png){ .screenshot }
]]]


### 5. 测试上下文关联

最后，点击 **Is UiPath platform Secure?**（UiPath 平台安全吗？）。实际提示词专门询问的是 AI 安全特性。

智能体搜索 **UiPath Security data** 上下文来源，返回一个结构化的回答。点击引用标记（`1`）核实来源：

![安全问题的回答，弹出的引用信息显示文档名称和页码](3-testing-conversations.images/8-security-context-citation-W.png){ .screenshot width="900" }

引用会链接回知识库中正确的页面。每次点击引用，你都会被带到源文档/文件。没有引用的回答——或者引用指向了错误文档——都是上下文来源需要重新检查的信号。

### 6. 评估你的智能体

在把智能体送入生产环境之前，你可以用两种方式测试它：

**Debug Chat**（调试聊天）

- 在 **Studio Web** 中进行交互式测试，附带实时执行日志。
- 用点赞/点踩反馈把结果加入评估集，并查看引用以追溯来源。
- 非常适合开发期间的快速迭代——即时测试改动，边发现边收集边缘情况。

**Evaluation Sets**（评估集）

- 单轮评估测试工具选择、语气，以及对单条提示词的回应。
- 多轮评估携带完整对话历史进行测试，模拟真实的用户旅程。
- 两种类型都支持基于执行轨迹和基于期望回答的评估器。还可以在同类模型之间做基准对比。
- 用 **Autopilot** 通过自然语言描述自动生成评估集。

### 7. 正式上线

和其他 UiPath 解决方案一样，你的智能体需要发布并部署到一个文件夹中。

为了避免产生太多副本，大家可以共用这个已发布到 Conversational Agent 文件夹的智能体：[直达链接](https://cloud.uipath.com/tpenlabs/AgenticPractice/autopilotforeveryone_/conversational-agents/?agentId=418563&mode=embedded)。它会出现在 Deployed Agents（已部署智能体）列表中，你可以在这里监控统计和使用数据。用户发送的反馈也会汇总到这里：

![智能体仪表盘](3-testing-conversations.images/9-agent-dashboard-W.png){ .screenshot }

可观测性仪表盘让你深入了解智能体的表现。例如：

- **Business Intelligence**（商业智能）可以跟踪消耗指标、活跃用户、消息数、对话数，以及反馈随时间的变化趋势。查看最常用的工具和最活跃的用户，从中发现采用模式和优化机会。
- **Compliance and Auditability**（合规与可审计性）：完整的执行轨迹让你能够详细了解智能体的行为。AI Trust Layer Audit 会记录所有 LLM 调用，包括模型类型、数据驻留和 PII 脱敏状态，实现完整的合规可见性。
- **Feedback**（反馈）：用户可以用点赞/点踩为回答打分。管理员在 Instance Management 中查看这些反馈，并把洞察反哺到评估集里，实现持续改进。

最后：

<details ontoggle="if(this.open) { this.querySelector('iframe').src = this.querySelector('iframe').getAttribute('data-src'); }">
  <summary>你甚至可以把对话式智能体嵌入到自己的应用程序里！</summary>
  <div class="iframe-container">
    <iframe 
        data-src="https://cloud.uipath.com/tpenlabs/AgenticPractice/autopilotforeveryone_/conversational-agents/?agentId=418563&mode=embedded" 
        src="about:blank"
        width="100%" 
        height="500" 
        frameborder="0"
        allowfullscreen>
    </iframe>
  </div>
</details>

UiPath 对话式智能体很快将具备语音和 IVR 能力，支持客户端工具，并提供 WhatsApp 集成。但这个练习到此就完成了！前往总结页面，看看你都构建了什么。
