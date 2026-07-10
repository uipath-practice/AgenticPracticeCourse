---
source_hash: 034a3bbdb1913877dcec7a6dd471c54d
---

# IXP로 인보이스 매칭하기

**IXP, 로봇, AI 에이전트, 휴먼 검토를 결합해 엔드투엔드 2-way 매칭 프로세스를 만듭니다.**

## 개요

**UiPath Maestro**는 에이전틱 오케스트레이션을 지원합니다. 서로 다른 기록 시스템과 업무 시스템에 걸쳐 사람, 로봇, AI 에이전트 사이의 장기 실행 엔터프라이즈 프로세스를 조율하는 것입니다. 이번 실습에서는 여기에 **IXP**(Intelligent eXtraction & Processing)를 더해, PDF 문서에서 구조화된 인보이스 데이터를 추출합니다.

| 단계 | 핵심 내용 |
| ---: | :--- |
| [**BPMN 프로세스 만들기**](1-create-bpmn.md) | 프로세스의 엔드투엔드 워크플로 설계 |
| [**로봇 구성하기**](2-configure-robot.md) | 인보이스 PDF 문서를 가져오는 RPA 작업 |
| [**에이전트 구성하기**](3-configure-agent.md) | IXP로 인보이스 데이터를 추출하고, 구매 주문(PO)을 조회한 뒤, 2-way 매칭 실행 |
| [**휴먼 검증 구성하기**](4-configure-human-validation.md) | 인보이스 예외를 사람이 검토하는 Action Center의 Action App |
| [**API 통합 구성하기**](5-configure-api.md) | 반려 이메일 발송과 결제 처리를 위한 승인 인보이스 저장 |

!!! tip "실습 환경"
    **[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)**에 로그인하고, 이 실습에서는 **AgenticPractice** 테넌트를 사용해야 한다는 점을 기억하세요.
