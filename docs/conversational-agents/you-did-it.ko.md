---
source_hash: f5dace92b48b8305fc193ea1106a663e
---

# 해냈습니다!

!!! tip "축하합니다!"

    실제 문서에 근거한 대화형 에이전트를 만들고, 실제 자동화 도구에 연결하고, 네 가지 유형의 실제 대화로 검증까지 마쳤습니다.

---

## 무엇을 만들었나요

**Agent Builder**에서 인보이스와 ServiceNow 티켓에 대한 질문에 실시간으로 답하는 대화형 에이전트를 만들었습니다. **Context Grounding** 인덱스로 UiPath Security 문서에 근거를 두게 한 다음, **Orchestrator**에 게시된 RPA 도구와 API 도구를 모두 연결했습니다. 마지막으로 데이터 조회, 인시던트 조회, 쓰기 작업, 지식 질문에 걸쳐 테스트하며 각 도구 호출이 실시간으로 일어나는 모습을 지켜봤습니다.

| 구성 요소 | 역할 |
|-----------|------|
| **대화형 에이전트** | 근거 지식과 연결된 도구 범위 안에서 실시간으로 질문에 답변 |
| **Context Grounding** | 인용 가능한 출처와 함께 응답을 UiPath Security 문서에 고정 |
| **Orchestrator Tools** | 에이전트가 필요할 때 인보이스 데이터와 ServiceNow 인시던트 상세 정보를 조회하도록 지원 |
| **프롬프트** | 에이전트가 답하도록 만들어진 질문으로 사용자를 안내 |

---

## 다음은 무엇일까요?

어떤 에이전트 유형을 언제 써야 할까요?

| | 자율형(Autonomous) | 대화형(Conversational) |
|-|------------|----------------|
| **상호작용 모델** | 최초 프롬프트에 기반한 싱글턴 작업 실행 | 멀티턴으로 주고받는 대화 |
| **주요 유스 케이스** | 정의된 구조화 프롬프트로 복잡한 작업 실행 | 실시간 사용자 지원과 도움, 인터랙티브한 정보 수집 |
| **사용자 입력** | 단일한 구조화 프롬프트 또는 명령 | 모호함이 섞이기도 하는 연속적인 채팅 메시지 |
| **핵심 강점** | 사전 정의된 프로세스와 자동화 워크플로 실행 | 대화 유지, 맥락 이해, 뉘앙스 처리 |

### 1. 에이전트 배포하고 공유하기

**Agent Builder**에서 에이전트를 게시하고 엔드포인트를 동료와 공유해 보세요. 근거 범위 밖의 질문도 던져 보고 — 답하면 안 되는 주제를 어떻게 다루는지 살펴보세요.

### 2. 옵저버빌리티 데이터 검토하기

Agent Builder에서 옵저버빌리티 대시보드를 열어 보세요. 대화 로그, 도구 호출 빈도, 사용자 피드백을 확인하고 다음에 무엇을 개선할지 결정하세요.

---

## 계속 다듬어 보세요

**지식 베이스 넓히기**

- 컨텍스트 그라운딩 소스에 문서 인덱스를 더 추가하고 에이전트의 커버리지가 어떻게 달라지는지 관찰해 보세요.

**Orchestrator 도구 더 추가하기**

- 추가 도구와 연결(예: MCP 서버)을 연결해 보세요.

**시스템 프롬프트 다듬기**

- 데이터와 피드백을 바탕으로 시스템 프롬프트를 주기적으로 다시 살펴보세요. 도메인 제약을 조이고, 도구 사용 규칙을 조정하고, 에이전트의 행동이 어떻게 달라지는지 확인해 보세요.

---

## 더 알아보기

| 리소스 | 설명 |
|----------|-------------|
| [대화형 에이전트](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents) | UiPath Agent Builder의 대화형 에이전트 개요 |
| [시작하기](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-getting-started) | 첫 대화형 에이전트를 만드는 단계별 가이드 |
| [에이전트 설계](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-design) | 프롬프트 구성, 도구, 그라운딩 옵션 |
| [배포](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-deployment) | 대화형 에이전트를 게시하고 공유하는 방법 |
| [옵저버빌리티](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-observability) | 대화와 도구 사용 모니터링 |
| [인덱스 관리](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes) | 컨텍스트 그라운딩을 위한 문서 인덱스 설정 |
