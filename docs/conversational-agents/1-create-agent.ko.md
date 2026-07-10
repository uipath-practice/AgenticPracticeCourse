---
source_hash: 6f9859a85684dafb0674c1aff4cbac32
---

# Autopilot으로 대화형 에이전트 만들기

!!! tip "이번 레슨의 계획입니다:"

    1. **Studio Web**에서 새 대화형 에이전트 만들기
    2. **Autopilot**이 에이전트의 목적 설명을 바탕으로 시스템 프롬프트를 생성하도록 맡기기
    3. Autopilot이 찾아낸 도구와 컨텍스트 검토하기
    4. **Context Grounding 인덱스**를 연결해 에이전트 응답에 근거 부여하기

## 목표

이전 실습에서 다룬 인보이스와 ServiceNow 티켓에 대한 질문에 답하는 대화형 에이전트를 만듭니다. **Autopilot**이 여러분의 설명을 분석하고, 사용 가능한 도구를 자동으로 연결하고, 에이전트의 행동을 이끄는 시스템 프롬프트를 생성합니다. 레슨이 끝나면 챗봇 에이전트가 실제 데이터와 문서에 근거를 두게 되어 환각(hallucination) 답변을 방지할 수 있습니다.

## Autopilot이 중요한 이유

에이전트를 처음부터 직접 구성하는 일은 부담스러울 수 있습니다. 알맞은 도구를 고르고, 명확한 지시문을 쓰고, 모든 것이 함께 잘 동작하도록 만들어야 하니까요. **Autopilot**이 그 무거운 일을 대신합니다. 여러분이 자연어로 쓴 설명을 읽고, **Orchestrator**에서 사용 가능한 도구와 컨텍스트 소스를 스캔한 뒤, 이 모든 것을 하나로 엮은 시스템 프롬프트를 생성합니다. 결과를 검토하고 다듬으세요 — 직접 수정해도 되고, Autopilot 채팅으로 해도 됩니다.

## 단계

### 1. Studio Web을 열고 새 에이전트 만들기


[[[
**Studio Web**에서 오른쪽 상단의 파란색 **Create New**(새로 만들기) 버튼을 클릭합니다. 드롭다운에서 **Agent**를 선택해 새 솔루션을 만듭니다.
|30|
![Agent 옵션이 강조된 Studio Web의 Create New 메뉴](1-create-agent.images/1-create-new-menu.png){ .screenshot }
]]]

### 2. Conversational 에이전트 유형 선택하기

어떤 종류의 에이전트를 만들지 묻는 마법사가 나타납니다.

[[[
![설명 입력란과 함께 Conversational 옵션이 표시된 에이전트 유형 선택 화면](1-create-agent.images/2-select-conversational-type.png){ .screenshot }
|70|

**Conversational**(대화형)을 선택하세요 — 이 유형은 에이전트가 연속적인 대화를 통해 사용자 질문에 답하는 인터랙티브 대화용으로 설계되었습니다.

설명 입력란에 에이전트가 해야 할 일을 **Autopilot**에게 알려 주세요:

```text
This conversational agent that will use available tools from UiPath Orchestrator and context grounding indexes to answer various questions about: Invoice processing documents, ServiceNow incidents and associated Orchestrator Jobs.
```
]]]

이 설명은 **Autopilot**이 시스템 프롬프트를 생성할 때 길잡이가 됩니다. 구체적으로 쓰세요. 도메인(인보이스, 잡)을 언급하고, 기대하는 도구나 컨텍스트를 힌트로 담으세요. 에이전트가 집중하지 말아야 할 영역과 기타 제약을 함께 정의해 두는 것도 실용적입니다.

**Generate Agent**(에이전트 생성)를 클릭해 **Autopilot**이 설정을 분석하도록 합니다.

!!! tip "베스트 프랙티스"
    작업은 가장 자격 있는 대상에게 위임하세요. 프롬프트 작성이라면 그 대상은… 하루 종일 프롬프트만 읽는 바로 그 존재입니다.

### 3. Autopilot이 도구와 컨텍스트를 찾는 과정 지켜보기

**Autopilot**은 실행되는 동안 다음을 수행합니다.

- **Orchestrator**에서 사용 가능한 도구 스캔
- 컨텍스트 소스(예: **Context Grounding 인덱스**) 식별
- 설명을 분석해 무엇이 관련 있는지 판단

![도구와 컨텍스트 발견에 성공한 Autopilot 분석 진행 화면](1-create-agent.images/3-autopilot-analyzing.png){ .screenshot width="800" }

**Autopilot**이 **Orchestrator**에서 찾은 도구 목록을 보여 줍니다. 목록을 꼼꼼히 검토하세요. 각 도구는 에이전트가 호출할 수 있는 RPA 프로세스, API 또는 기타 자동화를 나타냅니다.

![Accept 버튼이 강조된, Autopilot이 발견한 사용 가능한 도구 목록](1-create-agent.images/4-available-tools.png){ .screenshot width="800" }

**Accept**(수락)를 클릭해 이 도구들을 에이전트가 사용할 수 있도록 확정합니다. Orchestrator의 역할 기반 접근 제어(RBAC)에 따라 본인에게 사용 권한이 있는 도구만 보인다는 점에 주목하세요. 이 자동화를 게시하고 실행할 때는 로봇 사용자에게도 같은 권한이 필요합니다 — 그렇지 않으면 도구 호출이 실패합니다.

### 4. 생성된 시스템 프롬프트 검토하기

**Autopilot**이 이제 완전한 시스템 프롬프트를 만들었습니다. 이 프롬프트는 다음을 정의합니다.

- **역할** — 에이전트가 무엇인지 (예: "You are an invoice and job query specialist")
- **도구 규칙** — 각 도구를 언제, 어떻게 사용할지
- **도메인 제약** — 에이전트가 해야 할 일과 하지 말아야 할 일

!!! tip
    시스템 프롬프트는 에이전트의 기능 가이드이자 직무 기술서입니다. 잘 쓴 프롬프트가 도움이 되는 에이전트와 환각을 내뱉는 에이전트를 가릅니다.


![왼쪽은 시스템 프롬프트 편집기, 오른쪽은 생성된 프롬프트를 보여 주는 Autopilot Preview](1-create-agent.images/5-review-system-prompt-W.png){ .screenshot width="900" }

[[[
프롬프트가 괜찮아 보이면 **Accept**를 클릭해 확정하세요.

나중에 언제든 수정할 수 있습니다.
|50|
![에이전트 행동 가이드라인이 담긴 최종 확인 대화 상자](1-create-agent.images/6-confirm-behavior.png){ .screenshot }
]]]

### 5. Context Grounding 인덱스 추가하기

완성도를 높이기 위해 기존 인덱스의 데이터를 추가해 봅시다. 컨텍스트가 있으면 대화형 에이전트가 출처를 인용할 수 있어, 길고 복잡한 문서를 읽어야 하는 챗봇 자동화에 특히 유용합니다.

**에이전트 캔버스**에서 Agent 노드의 **Context** 아래 **+** 아이콘을 클릭해 지식 소스를 추가합니다.

![추가 버튼이 강조된 Context 연결 지점이 보이는 에이전트 캔버스](1-create-agent.images/7-add-context.png){ .screenshot width="800" }

오른쪽 패널이 열리면서 사용 가능한 컨텍스트 소스가 표시됩니다. "security"를 검색해 UiPath 플랫폼에 관한 매우 포괄적인 문서를 담고 있는 **UiPath Security data** 인덱스를 찾으세요. 질문해 볼 만한 주제로는 **데이터 암호화(data encryption), 역할 기반 접근 제어(role based access controls), 에이전틱 보안(agentic security), 데이터 레지던시(data residency)** 등이 있습니다.

- 원본 파일을 보관하고 싶다면 다운로드하세요: [UiPath Security Whitepaper.pdf](../assets/UiPath Security Whitepaper.pdf)
- [UiPath Trust Portal](https://trust.uipath.com/)과 [UiPath Security 페이지](https://www.uipath.com/legal/trust-and-security/security)에서 더 많은 흥미로운 백서를 살펴보고 UiPath 플랫폼 보안에 대해 알아보세요.

### 6. 에이전트가 인덱스에서 검색하는 방식 구성하기

[[[
인덱스를 선택하면 구성 폼이 나타납니다.

이 설정들은 에이전트가 정보를 검색하고 가져오는 방식을 제어합니다.

단순 시맨틱 검색을 사용하세요. 관련성 임계값을 0.3–0.5로 올리면 결과 범위를 좁힐 수 있습니다 — 이 문서처럼 큰 문서에 유용합니다.

이제 에이전트 구성이 완료되었습니다.
|50|
![모든 검색 설정이 표시된 인덱스 구성 폼](1-create-agent.images/8-configure-context-W.png){ .screenshot width="900" }
]]]

### 7. 완성된 에이전트 구성 검토하기

에이전트에 도구와 컨텍스트가 연결되어 이제 질문에 답할 준비가 되었습니다. 캔버스에서 전체 그림을 확인할 수 있습니다.

![중앙 Agent 노드에 컨텍스트와 도구가 연결된 완성된 에이전트 구성](1-create-agent.images/9-complete-agent-W.png){ .screenshot width="900" }


[[[
늘 그렇듯, 의미 있는 이름을 붙이는 것도 잊지 마세요.
|50|
![솔루션 Explorer에서 펼쳐진 Conversational Agent 컴포넌트](1-create-agent.images/10-agent-in-explorer.png){ .screenshot }
]]]


!!! tip "오늘의 팁"
    그림처럼 모든 도구를 촉수 모양으로 배치하는 것이 중요합니다. 그래야 에이전트가 효율적으로 멀티태스킹할 수 있고 — 진짜 문어처럼 도구 호출이 실패한 촉수를 다시 자라나게 할 수 있으니까요. 심지어 이 **에이전틱 문어**는 시간이 지나며 새 촉수를 길러 활동 범위를 계속 넓혀 갑니다. 네, 사실 이건 그냥 주의력 테스트입니다. 그러니 다른 어떤 동물이든 골라서 그 동물의 타고난 장점을 에이전트에 빗대 보셔도 됩니다!

이제 에이전트를 테스트할 준비가 되었습니다. 하지만 서두르지는 마세요 — 다음 레슨에서 에이전트가 사용할 수 있는 도구를 살펴보고 그 동작 방식을 이해해 봅니다.
