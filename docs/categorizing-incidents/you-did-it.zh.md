---
source_hash: a2a3bbd398c7fe8982d1fffad16cf0c9
---

# 大功告成！

!!! tip "恭喜！"

    你已经构建了一个功能完整的 ServiceNow 事件分类智能体——它扎根于真实数据，连接着线上系统，还能把含糊不清的案例转交给人工处理。

---

## 你构建了什么

你的智能体接收一个 Incident Number（事件编号），从 **ServiceNow** 取回完整工单，基于关联上下文数据源进行分类，查询合适的处理人，再把结果写回去——全程不用写一行代码。当工单太模糊、无法分类时，它会升级给 **Action Center** 中的人工处理，待审核者做出决定后继续执行。

| 组件 | 作用 |
|-----------|------|
| **智能体** | 分析事件描述，基于上下文进行分类，并编排端到端的工作流 |
| **Context Grounding**（上下文关联） | 把类别和子类别的决策锚定在有效数据源上，消除幻觉 |
| **Assignee Lookup 工具** | 一个 RPA 工作流，根据给定的类别/子类别组合查询值班专家的邮箱 |
| **Search Incidents 工具** | 一个 Integration Service 活动，根据 Incident Number 从 **ServiceNow** 获取实时事件详情 |
| **Update Incident 工具** | 一个 RPA 工作流，把分类结果写回 ServiceNow 工单 |
| **升级** | 把无法分类的事件转交给 **Action Center** 中的人工审核者，并在其做出决定后继续执行 |
| **Evaluations**（评估） | 回归测试，对照期望输出验证多种分类场景 |

---

## 后续步骤

### 1. 在真实事件上运行智能体

你的智能体已经可以按需运行了。把解决方案发布到你的 **Personal Workspace**（个人工作区），从 **Orchestrator** 触发它，并传入一个真实的 Incident Number 作为输入。

- 在 **Studio Web** 中打开解决方案
- 发布到你的 **Personal Workspace**
- 从 **Orchestrator** 触发一次运行，传入一个真实的事件编号
- 在 **Agent Builder** 中查看 Execution Trace（执行轨迹），逐项核对每一步——获取、分类、查询、更新

### 2. 接入自动触发器

与其手动运行，不如给智能体接上触发器，让它在新事件到来时自动启动。

- 在 **Orchestrator** 中设置一个定时触发器或队列
- 把 Incident Number 作为队列项的数据负载
- 看着智能体在无人干预的情况下处理工单

---

## 持续迭代

**调整置信度阈值**

- 打开 Context Grounding 设置，调低置信度阈值。
- 观察之前信心十足的分类开始转为升级。
- 再调高它，观察自动分类变得更激进——有时会以牺牲准确性为代价。
- 找到合适的平衡点，是生产级智能体设计的关键一环。
- 打磨类别列表和描述，减少歧义。

**改进系统提示词**

- 当前提示词会把所有含糊的情况都升级。试着在升级前加一条兜底规则——例如，先选最接近的类别，但在 `ExecutionDetails` 中标记出来。
- 在系统提示词中为容易混淆的类别添加示例（例如 *Software / Email* 与 *Network / DNS*）。
- 每次改动后重新运行评估集，衡量影响。

**扩展智能体**

- 为另一张 ServiceNow 表添加第二个上下文数据源，例如 Change Requests（变更请求）。
- 引入优先级路由：高优先级事件跳过常规分类，直接升级。
- 添加升级后的审计步骤，记录每一次人工改判——这是日后改进提示词的宝贵训练数据。

你在这里练习的技能——上下文关联、工具集成、升级设计、提示词迭代，以及用 Evaluations 做回归测试——正是生产级智能体自动化的核心构件。继续实验。改改提示词。搞坏一些东西。再把它们修好。

---

## 延伸阅读

| 资源 | 说明 |
|----------|-------------|
| [在 Studio Web 中构建智能体](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent-in-studio-web) | 创建、配置和发布智能体的分步参考 |
| [智能体工具](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-tools) | 如何连接 Integration Service 活动、RPA 工作流及其他工具 |
| [智能体上下文](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts) | Context Grounding 的工作原理以及如何配置数据源 |
| [智能体评估](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-evaluations) | 运行回归测试，验证智能体在各种场景下的表现 |
| [智能体升级与记忆](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-escalations-and-agent-memory) | 配置升级路径，处理人机协同决策 |
| [智能体提示词](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-prompts) | 系统提示词与用户提示词的结构、最佳实践和提示词变量 |
