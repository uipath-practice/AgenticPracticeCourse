---
source_hash: 034a3bbdb1913877dcec7a6dd471c54d
---

# 使用 IXP 进行发票匹配

**使用 IXP、机器人、AI 智能体和人工审核，构建端到端的双向匹配（2-way matching）流程。**

## 概览

**UiPath Maestro** 支持智能体编排——在不同的记录系统和交互系统之间，协调人、机器人和 AI 智能体共同完成长时间运行的企业流程。本练习在此基础上加入 **IXP**（Intelligent eXtraction & Processing），用它从 PDF 文档中提取结构化的发票数据。

| 步骤 | 重点 |
| ---: | :--- |
| [**创建 BPMN 流程**](1-create-bpmn.md) | 为整个流程设计端到端的工作流 |
| [**配置机器人**](2-configure-robot.md) | 获取发票 PDF 文档的 RPA 任务 |
| [**配置智能体**](3-configure-agent.md) | 用 IXP 提取发票数据，查询采购订单，并执行双向匹配 |
| [**配置人工验证**](4-configure-human-validation.md) | 在 Action Center 中用 Action App 对发票异常进行人工审核 |
| [**配置 API 集成**](5-configure-api.md) | 发送拒绝邮件，并存储批准的发票以供付款处理 |

!!! tip "训练环境"
    登录 **[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)**，并记得在本练习中使用 **AgenticPractice** 租户。
