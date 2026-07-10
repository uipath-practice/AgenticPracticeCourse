---
source_hash: 9b876c1661efeee47194472f30ce7118
---

# 与外部服务打交道

!!! tip "本课的计划如下："

    1. 每当发票被拒绝时，使用验证步骤产出的回复文本和 **Gmail Connector**（Gmail 连接器）给供应商发送消息。
    2. 把批准的发票数据存入 **Data Fabric**，让财务团队用他们自己的自动化来处理付款。

## 目标

添加最后两个任务，完成端到端流程：在 **Reject** 路径上加一个拒绝邮件连接器，在 **Approve** 路径上加一个数据存储连接器。两者都使用 **AgenticPractice** 租户中已配置好的 **Integration Service** 连接器。

## Integration Service 与 Data Fabric

UiPath **Integration Service** 是自动化各类支持 API 的应用最快捷、最方便的方式。它负责处理授权和身份验证，集中管理 API 连接，让 SaaS 平台集成更快落地。

你的租户里已经配置好了两个连接：

- **Gmail**——用于发送自动邮件的共享邮箱
- **Data Fabric**——用于结构化记录（表格、文件等）的共享数据存储

平台管理员已经准备好了这些连接。你不需要配置身份验证。

![Integration Service 中可用的连接](5-configure-api.images/1-connections-W.png){ .screenshot width="900" }

!!! note "租户检查"
    确认你用的是正确的租户。如果连接有问题，请联系你的培训师。

## 步骤

### 1. 配置拒绝邮件任务

当发票未通过验证时，流程应该发送一封拒绝邮件。邮件内容用的是智能体生成、审核人有机会编辑过的草稿回复。


[[[
在你的 **Maestro Agentic Process** 中，选中 **Reject** 路径上的任务，把操作类型设为 **Execute Connector Activity**（执行连接器活动）。

使用“**Shared Gmail Connection**”连接，并选择“**Send Email**”活动。
|30|
![发送拒绝邮件任务的配置](5-configure-api.images/2-send-rejection.png){ .screenshot }
]]]


[[[

配置 **Send Email** 活动：把你自己的邮箱地址填为收件人地址，写一个合适的主题，然后把邮件正文映射到审核人编辑后的版本 `out_ApproverResponse`。

|50|
![Gmail Send Email 活动的配置](5-configure-api.images/3-gmail-configuration.png){ .screenshot }
]]]


### 2. 配置 Data Fabric 存储任务

现在我们知道被拒绝的发票会怎么处理了。对于批准的发票，把发票数据传给 **Data Fabric**，让财务团队自己的 UiPath 自动化接手并处理付款。他们的 UiPath 自动化连接的是同一个数据源，所以我们只需要把数据推送过去。

[[[
选中 **Approve** 路径上的任务，把操作类型设为 **Execute Connector Activity**。

把任务配置为使用 **Data Fabric** 连接器和共享连接，并对 **Payments Queue** 对象执行 **Create Entity Record** 活动。

|30|
![更新财务系统任务的配置](5-configure-api.images/4-update-financial-system.png){ .screenshot }
]]]

[[[
点击 **Manage Properties**（管理属性），把发票数据字段添加到 Payments Queue 实体。勾选 **InvoiceData** 字段来映射你的发票数据。

|50|
![选中 InvoiceData 字段](5-configure-api.images/4-update-records-fields.png){ .screenshot }
]]]

[[[
把智能体输出的发票 JSON 数据映射到 **InvoiceData** 输入字段。这样每张批准发票的信息都会进入付款队列，供下游处理。

|50|
![把发票数据映射到 InvoiceData 输入](5-configure-api.images/4-update-records-input.png){ .screenshot }
]]]



### 3. 测试两条路径

点击 **Debug**，让流程跑起来。记住，通过 RPA 自动化的 `in_FailureProbability` 参数，你可以控制被拒绝和被批准的发票出现的频率。

查看 **Data Fabric**，你会看到批准的发票在 Payments Queue 里不断累积：

![Data Fabric 的 Payments Queue 中已批准的发票](5-configure-api.images/5-payments-queue-W.png){ .screenshot width="900" }

再看看你的收件箱，里面会有来自共享 Gmail 账号的拒绝邮件。每封邮件都包含由智能体识别、经人工验证者审核过的差异：

![收到的拒绝邮件，包含生成的发票对比](5-configure-api.images/6-actual-email-received-W.png){ .screenshot width="600" }
