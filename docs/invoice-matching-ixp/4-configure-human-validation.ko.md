---
source_hash: 300815cd671e260b015e86a398564f4a
---

# 꼭 필요할 때만 사람 개입시키기

!!! tip "이번 레슨의 계획입니다:"

    1. 검증용 Action App을 프로젝트로 가져옵니다.

    2. 에이전트가 인보이스와 PO 매칭에 실패하면 사람이 결정을 내릴 수 있도록 Action Center 작업이 생성되게 프로세스 흐름을 구성합니다.

    3. 앱 액션(Approve 또는 Reject)에 따라 흐름을 이어 갑니다.

    4. *(선택 사항)* 몇 가지 엣지 케이스를 처리하도록 에이전트의 프롬프트를 개선합니다.

## 목표

**Failed Match** 경로에 휴먼 검증 단계를 추가합니다. 에이전트가 불일치를 표시하면, **Action Center**에서 검토자가 두 문서가 담긴 요약을 보고 인보이스를 승인할지 반려할지 선택합니다. 워크플로는 그 결정에 따라 재개됩니다.

## 휴먼 인 더 루프

에이전트가 정확한 다음 행동을 판단할 수 없는 많은 경우에 사람의 개입이 필요합니다. 사람은 로봇과 에이전트가 보기 좋게 요약해 준 입력을 바탕으로 **Action Center**에서 작업을 처리합니다:

- 결정에 필요한 모든 입력이 한 화면에 표시되어야 합니다. 비즈니스 사용자가 애플리케이션을 열거나 실행 흐름을 되짚어 보게 만들지 않는 것이 이상적입니다.
- 에이전트의 역할은 모든 입력을 올바른 형식으로 준비해 두는 것입니다. 사용자 입력을 요청할 순간이 오면 데이터가 이미 준비되어 있도록 말이죠.
- 결정이 내려지면 프로세스 실행은 다음 단계로 이어집니다.

![휴먼 검증 단계 아키텍처](4-configure-human-validation.images/1-validation-arguments.png){ .screenshot width="700" }

!!! note "승인에 대한 참고"
    실제 상황이라면 구매 주문(PO)이 전혀 다른 내용인데 인보이스를 승인해 지불로 넘기는 일은 절대 용납되지 않습니다. 어떤 나라에서는 범죄입니다. 하지만 이 실습에서는 이 결정에 관한 한 사람이 아무 결과 걱정 없이 원하는 대로 할 수 있다고 가정합시다.

보기 좋은 검증 인터페이스를 만들려면, 문제와 함께 결정에 필요한 정보를 보여 주는 프런트엔드가 필요합니다:

- 인보이스와 구매 주문(PO)이 나란히 표시되어야 합니다. 불일치 항목은 빨간색으로 강조되면 이상적입니다.
- 문제가 사람에게 두어 문장으로 설명되어야 합니다.
- 인보이스를 반려하고 공급업체에 이메일을 보내기로 결정했다면, 초안 이메일이 시간을 아껴 줍니다. 이미 에이전트가 생성해 두었습니다!

이걸 처음부터 만드는 대신, 기존 Action App 템플릿을 재사용하겠습니다.

![인보이스와 PO 비교를 보여 주는 검증 앱 인터페이스](4-configure-human-validation.images/2-validation-app-draft-W.png){ .screenshot width="900"}

## 단계

### 1. 검증 앱 가져오기


[[[
솔루션에서 Explorer의 **+** 아이콘을 클릭해 프로젝트를 추가한 다음, **Import existing**을 선택해 새 프로젝트를 솔루션에 추가합니다. 검증 앱 템플릿을 찾아 가져오세요.
|50|
![가져오기 메뉴가 열린 Solution Explorer](4-configure-human-validation.images/3-import-action-app.png){ .screenshot }
]]]


[[[
목록에서 **2WM Validation App IXP Template**을 찾아 선택하고 **Add**를 클릭합니다.
|30|
![검증 템플릿이 선택된 프로젝트 추가 대화 상자](4-configure-human-validation.images/4-import-template.png){ .screenshot }
]]]

앱이 솔루션에 나타나면 구조를 살펴보면서 설계 접근 방식을 이해해 보세요. 

- 앱 **UI elements**의 구조 — 검증 작업이 사용자 앞에 표시되는 모습입니다.

- App Actions와 **Action Schema** — 사용자 결정이나 액션의 가능한 결과를 다룹니다.

- 앱의 **Inputs and Outputs** — 데이터가 어디서 오고, 어디에 쓰이고, 무엇이 나오는지.


앱 디자이너에서 **MainPage**를 엽니다:

![검증 인터페이스 레이아웃과 구성 요소를 보여 주는 앱 디자이너](4-configure-human-validation.images/5-app-structure-W.png){ .screenshot width="900" }

앱의 **input**과 **output** 구성을 살펴보세요. 에이전트가 어떤 데이터를 보내오고, 검토자의 결정이 무엇을 만들어 내는지 보여 줍니다.

![에이전트로부터의 입력과 출력 결정을 보여 주는 앱 구성](4-configure-human-validation.images/6-app-arguments-W.png){ .screenshot width="900" }

### 2. Maestro에서 휴먼 작업 구성하기

Maestro의 **Agentic Process**로 돌아가 **Failed Match** 경로의 검증 작업을 Action App 작업으로 구성합니다.


[[[
**Failed Match** 경로의 휴먼 작업 노드를 선택하고 액션 유형을 **Create action app task**로 설정합니다. 

그다음 Defined resources 목록에서 방금 가져온 **2WM Validation App IXP**를 선택합니다.

|30|
![Action App 선택이 표시된 Maestro 작업 속성](4-configure-human-validation.images/7-add-action-task.png){ .screenshot }
]]]


[[[
나중에 **Action Center**에서 쉽게 알아볼 수 있도록 작업 제목을 커스터마이징하세요. 예: **Invoice Validation (Your Name)**. 

**Advanced Options**에서 작업을 자신에게 할당하면, 미할당 작업 사이에서 찾아 헤맬 필요가 없습니다.

|50|
![제목과 담당자 옵션이 있는 작업 구성 패널](4-configure-human-validation.images/8-configure-action-task.png){ .screenshot }
]]]


[[[

에이전트에서 했던 것과 같은 방식으로, 에이전트의 출력을 앱의 입력에 매핑합니다.

Inputs 섹션에서 에이전트의 `out_DocumentsHTML`과 `out_SuggestedResponse`를 해당하는 앱 입력 필드에 연결합니다.

여기서 네이밍 컨벤션을 지키는 일의 진가를 다시 한번 실감할 수 있습니다!

|30|
![에이전트 출력이 앱 입력에 연결된 입력 매핑](4-configure-human-validation.images/9-configure-action-arguments.png){ .screenshot }
]]]

작업 구성을 저장하세요.

### 3. 게이트웨이 결정 구성하기

이제 검증 결정에 따른 이후 흐름을 구성합니다.

휴먼 작업 다음에 프로세스를 분기시키는 **Exclusive Gateway**를 선택합니다.

![Reject와 Approve 경로를 보여 주는 게이트웨이 속성](4-configure-human-validation.images/10-configure-gateway.png){ .screenshot width="800" }

**Reject**를 기본 경로로 설정합니다. 실제 비즈니스 프로세스라면 접근 방식이 다를 수 있다는 점은 기억해 두세요.

**Approve** 경로에서는 Expression Editor 버튼을 클릭해 조건을 구성합니다.

[[[
Expression editor에서 휴먼 작업의 Action 출력 변수를 삽입합니다.

Approve 경로의 조건을 입력하세요:

```css
vars.action=="Approve"
```

|30|
![변수 삽입 메뉴가 열린 표현식 편집기](4-configure-human-validation.images/11-gateway-variable.png){ .screenshot }
]]]


[[[
이렇게 하면 검토자가 인보이스를 승인했을 때 프로세스가 Approve 경로로 흘러갑니다.
|30|
![표현식이 표시된 게이트웨이 경로 조건](4-configure-human-validation.images/12-gateway-expression.png){ .screenshot }
]]]

### 4. 휴먼 검증 흐름 테스트하기

이제 휴먼 검증 흐름 전체를 테스트합니다. **Debug**를 클릭하고 실행을 지켜보세요. `in_FailureProbability`를 높은 값(예: 90)으로 설정해 두었다면 인보이스 매칭이 자주 실패하면서 휴먼 검증 작업이 트리거됩니다.

**Debug**를 클릭해 프로세스를 시작합니다. 불일치가 감지되면 실행이 **Manual Review and Validation** 작업에서 일시 정지합니다.

![휴먼 작업에서 일시 정지된 프로세스를 보여 주는 Maestro 실행 화면](4-configure-human-validation.images/13-validation-test-run-W.png){ .screenshot width="900" }

Details 패널에서 **Open app task**를 클릭해 액션 작업을 엽니다. 나란히 표시된 인보이스와 PO 비교를 검토하고 결정을 내리세요.

![인보이스 검증 인터페이스를 보여 주는 Action Center 작업](4-configure-human-validation.images/14-validation-action-W.png){ .screenshot width="900" }

에이전트가 일을 꽤 잘한 것 같습니다. 그런데 이 인보이스는 승인해야 할까요, 반려해야 할까요? **Approve and pay** 또는 **Reject**를 클릭하세요. 결정을 제출하는 순간 Maestro가 해당 경로를 따라 실행을 이어 갑니다.

엔드투엔드 프로세스를 살펴보면서 휴먼 검증 단계가 올바르게 통합되었는지, 여러분의 결정에 따라 분기하는지 확인하세요.

![휴먼 검증 단계가 강조된 전체 프로세스 다이어그램](4-configure-human-validation.images/15-end-to-end-flow-W.gif){ .screenshot width="900" }

Approve와 Reject를 모두 시도하면서 몇 번 더 테스트해, 두 경로가 모두 올바르게 분기하는지 확인하세요.

앱 디자인이 더 나아질 여지가 있다는 데는 동의합시다. 그래도 전반적으로 제 역할은 충분히 해냅니다.

테스트를 두어 번 더 실행하고 **[다음 레슨](5-configure-api.md)**으로 넘어가세요. 거의 다 왔습니다!
