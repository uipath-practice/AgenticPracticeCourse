---
source_hash: a2a3bbd398c7fe8982d1fffad16cf0c9
---

# 해냈습니다!

!!! tip "축하합니다!"

    실제 데이터에 근거하고, 실제 시스템에 연결되고, 모호한 케이스를 사람에게 라우팅할 수 있는 — 완전하게 동작하는 ServiceNow 인시던트 분류 에이전트를 완성했습니다.

---

## 무엇을 만들었나요

여러분의 에이전트는 Incident Number를 받아 **ServiceNow**에서 티켓 전체를 가져오고, 근거 있는 컨텍스트 소스로 분류하고, 알맞은 담당자를 조회하고, 결과를 다시 써넣습니다. 코드는 단 한 줄도 없이요. 티켓이 너무 모호해서 분류할 수 없을 때는 **Action Center**의 사람에게 에스컬레이션하고, 리뷰어가 결정하면 다시 이어서 진행합니다.

| 구성 요소 | 역할 |
|-----------|------|
| **에이전트** | 인시던트 설명을 분석하고, 컨텍스트로 분류하고, 엔드투엔드 워크플로를 조율합니다 |
| **Context Grounding** | 카테고리·하위 카테고리 결정을 유효한 데이터 소스에 고정해 할루시네이션을 없앱니다 |
| **Assignee Lookup 도구** | 주어진 카테고리/하위 카테고리 쌍에 대한 당직 전문가 이메일을 조회하는 RPA 워크플로 |
| **Search Incidents 도구** | Incident Number로 **ServiceNow**에서 실제 인시던트 상세 정보를 가져오는 Integration Service 액티비티 |
| **Update Incident 도구** | 분류 결과를 ServiceNow 티켓에 다시 써넣는 RPA 워크플로 |
| **에스컬레이션** | 분류할 수 없는 인시던트를 **Action Center**의 휴먼 리뷰어에게 라우팅하고, 리뷰어의 결정에 따라 이어서 진행합니다 |
| **Evaluations** | 여러 분류 시나리오를 기대 출력과 비교해 검증하는 회귀 테스트 |

---

## 다음 단계

### 1. 실제 인시던트로 에이전트 실행하기

에이전트는 이제 온디맨드로 실행할 준비가 되었습니다. 솔루션을 **Personal Workspace**에 게시하고, 실제 Incident Number를 입력으로 전달하며 **Orchestrator**에서 트리거하세요.

- **Studio Web**에서 솔루션을 엽니다
- **Personal Workspace**에 게시합니다
- **Orchestrator**에서 실행을 트리거하고 실제 인시던트 번호를 전달합니다
- **Agent Builder**에서 Execution Trace를 검토해 조회, 분류, 담당자 조회, 업데이트까지 모든 단계를 확인합니다

### 2. 자동 트리거에 연결하기

수동으로 실행하는 대신, 새 인시던트가 도착할 때마다 에이전트가 실행되도록 트리거에 연결하세요.

- **Orchestrator**에서 시간 기반 트리거나 큐를 설정합니다
- Incident Number를 큐 아이템 페이로드로 사용합니다
- 에이전트가 수동 입력 없이 티켓을 처리하는 모습을 지켜봅니다

---

## 계속 다듬어 보세요

**확신도 임곗값 조정하기**

- Context Grounding 설정을 열고 확신도 임곗값을 낮춰 보세요.
- 이전에는 확신 있게 분류되던 케이스가 에스컬레이션되기 시작하는 것을 관찰하세요.
- 임곗값을 올리면 자동 분류가 더 과감해집니다. 때로는 정확도를 대가로 치르면서요.
- 알맞은 균형을 찾는 일은 프로덕션 에이전트 설계의 핵심입니다.
- 카테고리 목록과 설명을 다듬어 모호함을 줄이세요.

**시스템 프롬프트 개선하기**

- 현재 프롬프트는 모호한 것을 모두 에스컬레이션합니다. 에스컬레이션 전에 폴백 규칙을 추가해 보세요. 예를 들어 가장 가까운 카테고리를 고르되 `ExecutionDetails`에 표시해 두는 식입니다.
- 혼동하기 쉬운 카테고리(예: *Software / Email* vs *Network / DNS*)에 대한 예시를 시스템 프롬프트에 추가하세요.
- 변경할 때마다 평가 세트를 다시 실행해 영향을 측정하세요.

**에이전트 확장하기**

- Change Requests처럼 다른 ServiceNow 테이블을 위한 두 번째 컨텍스트 소스를 추가하세요.
- 우선순위 라우팅을 도입하세요: 우선순위가 높은 인시던트는 일반 분류를 건너뛰고 즉시 에스컬레이션합니다.
- 사람이 개입해 수정한 내용을 모두 기록하는 에스컬레이션 사후 감사 단계를 추가하세요. 향후 프롬프트 개선에 유용한 학습 데이터가 됩니다.

여기서 연습한 기술 — 컨텍스트 그라운딩, 도구 통합, 에스컬레이션 설계, 프롬프트 반복 개선, Evaluations를 활용한 회귀 테스트 — 은 프로덕션급 에이전틱 자동화의 핵심 빌딩 블록입니다. 계속 실험하세요. 프롬프트를 바꿔 보세요. 망가뜨려 보세요. 그리고 고치세요.

---

## 더 알아보기

| 리소스 | 설명 |
|----------|-------------|
| [Studio Web에서 에이전트 만들기](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent-in-studio-web) | 에이전트를 만들고, 구성하고, 게시하는 단계별 레퍼런스 |
| [에이전트 도구](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-tools) | Integration Service 액티비티, RPA 워크플로, 기타 도구를 연결하는 방법 |
| [에이전트 컨텍스트](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts) | Context Grounding의 동작 방식과 데이터 소스 구성 방법 |
| [에이전트 평가](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-evaluations) | 여러 시나리오에서 에이전트 성능을 검증하는 회귀 테스트 실행 |
| [에이전트 에스컬레이션과 메모리](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-escalations-and-agent-memory) | 에스컬레이션 경로 구성과 휴먼 인 더 루프 의사 결정 처리 |
| [에이전트 프롬프트](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-prompts) | 시스템·사용자 프롬프트 구조, 베스트 프랙티스, 프롬프트 변수 |
