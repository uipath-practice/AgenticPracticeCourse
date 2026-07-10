---
source_hash: b5ce2f54c7036f476dffb60531b8db61
---

# 사용 가능한 도구 이해하기

!!! tip "이번 레슨의 계획입니다:"

    1. **Studio Web**에서 **Orchestrator Tools** 템플릿 찾기
    2. 워크플로를 열어 유형과 구조, 내부에서 데이터가 처리되는 방식 이해하기
    3. 도구 인수(입력과 출력) 살펴보기
    4. 에이전트의 **Appearance**(모양) 설정에서 시작 프롬프트 구성하기

## 목표

이 레슨에서는 소스 코드를 직접 살펴보며 에이전트가 사용할 수 있는 도구를 탐색합니다. 우리가 추가한 도구들은 에이전트가 호출할 수 있는 사전 구축 자동화(**RPA 및 API 워크플로**)입니다. 각 도구가 무엇을 하는지, 어떤 데이터가 필요한지(입력), 어떤 데이터를 반환하는지(출력)를 이해하는 것이 에이전트를 올바르게 구성하고 사용하는 핵심입니다.

## 도구란 무엇인가요?

도구는 Studio Web에서 만들어 **Orchestrator**의 **Orchestrator Tools** 폴더에 게시된 재사용 가능한 자동화입니다. 에이전트가 무언가를 해야 할 때 — **Data Fabric**에서 인보이스 데이터를 조회하거나, **ServiceNow** 인시던트를 나열하거나, 인시던트에 노트를 추가할 때 — 설명을 기준으로 가장 알맞은 도구를 찾아 실행합니다. 여기서 보게 될 도구들은 단순하지만, 실제로는 UI 자동화나 Integration Service 액티비티를 포함해 챗봇에 노출하고 싶은 Orchestrator의 어떤 기존 컴포넌트든 도구가 될 수 있습니다.

어떤 경우든 각 도구에는 **Workflow**(내부의 자동화 로직), **Inputs**(도구 실행에 필요한 데이터), **Outputs**(도구가 에이전트에 반환하는 데이터)가 있습니다.

입력 인수의 데이터는 매번 **인수 설명(Argument Descriptions)**과 **프롬프트**를 바탕으로 생성됩니다 — 설명을 항상 써야 하는 이유가 바로 이것입니다. 도구를 호출하면 백엔드에서 Orchestrator Job이 생성되고, Job이 완료될 때까지 결과를 기다립니다. 그런 다음 에이전트가 결과를 검토하고 목표를 향해 계속 나아가거나, 목표를 달성하고 자신의 실행을 마무리합니다.

에이전트를 구성하기 전에 도구를 먼저 검토해 두면, 여러분의 문어 에이전트가 무엇을 할 수 있는지 알게 됩니다.

## 단계

### 1. Orchestrator Tools 템플릿 찾기

**Studio Web**에서 **Templates**(템플릿) 탭을 클릭해 사용 가능한 시작 템플릿을 둘러보세요.

"orchestrator tool"을 검색해 **Orchestrator Tools Template**을 찾으세요. 자주 쓰이는 자동화 도구가 담긴 사전 구축 솔루션입니다.

[[[
템플릿 카드의 점 세 개 메뉴를 열고 **New solution from template**(템플릿에서 새 솔루션)을 선택합니다. 도구는 이미 Orchestrator에 배포되어 있으므로 게시할 필요는 없습니다. 소스 코드만 검토하면 됩니다.
|30|
![Orchestrator Tools Template이 강조된 Studio Web의 Templates 탭](2-review-tools.images/1-find-orchestrator-tools-template.png){ .screenshot }
]]]

### 2. API 워크플로 살펴보기

템플릿 솔루션이 로드되면 왼쪽 Explorer 패널에서 **Orchestrator Tools** 폴더를 펼치세요.

사용 가능한 도구 목록이 보입니다. 먼저 **Get ServiceNow Incident Notes**라는 API 워크플로를 선택하세요.

[[[
![Get ServiceNow Incident Notes 워크플로가 열린 상태로 펼쳐진 Orchestrator Tools 폴더](2-review-tools.images/2-examine-tool-workflow.png){ .screenshot }
|70|
도구 폴더 아래의 **Workflow.json**을 선택하면 내부의 자동화 단계를 볼 수 있습니다.
]]]

ServiceNow 도구는 요청을 동적으로 만듭니다. **ServiceNow HTTP Request**에는 도구의 입력 인수로 API 쿼리 URL이 어떻게 조립되는지 정확히 보여 주는 JS 표현식이 있습니다. API 응답은 파싱되어 출력으로 전송되고, 이 출력이 에이전트에게 돌아갑니다.

![동적 요청 URL이 담긴 JS 표현식 편집기를 보여 주는 ServiceNow 인시던트 도구](2-review-tools.images/5-incidents-http-request-url-W.png){ .screenshot width="900" }

**Get Orchestrator Jobs** 같은 API 워크플로도 같은 방식으로 동작하지만, ServiceNow 대신 Orchestrator와 통신합니다. 프로세스 이름과 시간 범위로 잡을 필터링합니다. 특별한 날짜 형식과, 인수의 설명(description)에서 에이전트에게 지시하는 방식을 눈여겨보세요.

```text
Filter jobs after this date. Format: "2026-04-07T00%3A00%3A00.00Z". Default 30 days from today.
```

![Orchestrator API 연결과 요청 URL을 보여 주는 Get Orchestrator Jobs 워크플로](2-review-tools.images/6-orchestrator-jobs-workflow-W.png){ .screenshot width="900" }


### 3. RPA 도구 검토하기

Data Fabric에서 데이터를 읽는 RPA 워크플로인 **Get Approved Invoices**를 열어 보세요.

![Assign, Search, HTTP Request, Response 단계를 보여 주는 도구 워크플로](2-review-tools.images/3-review-tool-implementation.png){ .screenshot width="800" }

[[[
**Data Manager** 패널을 열어 도구의 구성을 확인하세요.

이 인수들은 에이전트가 이 도구를 호출할 때 무엇을 기대해야 하는지 정확히 알려 줍니다. 에이전트는 입력에 데이터를 전달하고 출력에서 데이터를 받습니다. 거의 같은 접근 방식입니다.
|70|
![도구의 입력과 출력을 보여 주는 Data Manager 패널](2-review-tools.images/4-configure-tool-arguments.png){ .screenshot }
]]]

### 4. 에이전트 모양 구성하기

실제 테스트를 실행하기 전에 환영 메시지를 추가하고, 에이전트가 답하도록 만들어진 프롬프트를 추천해 두는 것이 좋은 습관입니다. 에이전트 구성을 열고 **Appearance** 섹션을 채우세요.

[[[
**Welcome title**(환영 제목)과 **Welcome description**(환영 설명)을 설정한 다음, **Edit starting prompts**(시작 프롬프트 편집)를 클릭해 채팅 인터페이스에 표시될 추천 질문을 정의합니다.

시작 프롬프트는 채팅 인터페이스에 클릭 가능한 칩으로 나타납니다. 자주 쓰는 테스트 대화를 빠르게 시작하는 방법이자, 최종 사용자에게 유용한 출발점을 제공하는 방법입니다.
|50|
![환영 제목, 설명, Edit starting prompts 버튼을 보여 주는 에이전트 모양 설정](2-review-tools.images/7-agent-appearance-settings.png){ .screenshot }
]]]

각 행에는 두 개의 입력란이 있습니다. 사용자에게 보이는 짧은 **Display prompt**(표시 프롬프트)와 모델에 실제로 전송되는 전체 **Actual prompt**(실제 프롬프트)입니다. 표시 프롬프트는 짧고 친근하게 유지하고, 진짜 세부 내용은 실제 프롬프트에 담으세요.

다 되었으면 **Save**를 클릭합니다.

![저장 준비가 된 여섯 쌍의 사전 정의 프롬프트를 보여 주는 시작 프롬프트 빌더](2-review-tools.images/8-starting-prompts-builder-W.png){ .screenshot width="900" }

이제 에이전트가 이 도구들을 자신 있게 사용할 준비가 되었습니다 — 한번 시켜 봅시다!
