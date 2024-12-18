---
layout: post
title: "소프트웨어 생명주기에서의 검증 및 확인 활동"
#date: 2024-11-23
categories: [v&v]
tags: [sdlc,v&v]

---
### 소프트웨어 생명주기에서의 검증 및 확인 활동

---

#### **1. 검증 및 확인 관리 (Management of V&V)**

##### **1.1 소프트웨어 검증 및 확인 계획 생성**
- 소프트웨어 생명주기의 각 단계에서 수행할 검증 및 확인 활동을 정의합니다. 
- 검증 및 확인 활동의 목표, 범위, 일정, 필요 자원(인력, 도구 등)을 명확히 문서화합니다.
- 계획은 요구사항 변화에 따라 동적으로 업데이트되며, 모든 관련 이해관계자에게 공유되어야 합니다.

##### **1.2 한계선 기준선 변경 평가**
- 소프트웨어 요구사항, 설계 또는 구현이 변경될 때 변경된 항목이 기존 시스템에 미치는 영향을 평가합니다.
- 변경으로 인해 기존 요구사항, 테스트 케이스 또는 설계가 영향을 받는지 추적성을 통해 확인합니다.

##### **1.3 검증 및 확인 리뷰 관리**
- 주요 산출물(요구사항, 설계 문서, 코드 등)에 대한 리뷰 일정을 수립하고, 리뷰 활동을 체계적으로 관리합니다.
- 리뷰 결과는 모든 이해관계자에게 전달되며, 리뷰 후 개선 사항을 추적하고 재검토합니다.

##### **1.4 리뷰 검증**
- 리뷰를 통해 확인된 결함 및 개선 사항이 적절히 반영되었는지 재검토합니다.
- 리뷰 후 수정된 문서, 코드 및 테스트 케이스의 품질을 보장하기 위한 활동입니다.

---

#### **2. 구상 단계의 검증 및 확인 (Concept Phase V&V)**

##### **2.1 초기 요구사항 분석**
- 프로젝트의 목적과 고수준 요구사항이 소프트웨어로 실현 가능한지 검토합니다.
- 비즈니스 및 기술적 요구사항의 적합성을 평가합니다.

##### **2.2 개념 설계 평가**
- 초기 설계 단계에서 시스템 아키텍처와 구현 가능성을 분석합니다.
- 개념 설계가 프로젝트의 목표와 일치하는지 확인하며, 이 과정에서 주요 리스크를 식별합니다.

##### **2.3 주요 이해관계자와의 검토**
- 주요 이해관계자(사용자, 고객 등)와 함께 검증 및 확인을 수행하여 초기 단계에서 오해나 누락된 요구사항을 줄입니다.

---

#### **3. 요구사항 도출 단계의 검증 및 확인 (Requirement Phase V&V)**

##### **3.1 소프트웨어 요구사항 추적성 분석**
- 각 요구사항이 시스템 설계, 코드, 테스트 케이스에 적절히 매핑되었는지 확인합니다.
- 누락되거나 중복된 요구사항을 식별합니다.

##### **3.2 소프트웨어 요구사항 평가**
- 요구사항의 명확성, 일관성, 완전성, 테스트 가능성을 검토합니다.
- 비기능적 요구사항(성능, 보안 등)이 적절히 정의되었는지 확인합니다.

##### **3.3 소프트웨어 요구사항 인터페이스 분석**
- 시스템 및 소프트웨어 컴포넌트 간의 상호작용 및 데이터 교환 방식을 검토합니다.
- 외부 시스템과의 인터페이스 요구사항도 포함됩니다.

##### **3.4 테스트 계획 생성**
- 요구사항 기반 테스트 계획을 수립합니다.
  - **시스템 테스트**: 전체 시스템의 기능과 성능 검증.
  - **인수 테스트**: 사용자 요구사항 만족 여부 확인.

---

#### **4. 설계 단계의 검증 및 확인 (Design Phase V&V)**

##### **4.1 소프트웨어 설계 추적성 분석**
- 요구사항이 설계 문서에 적절히 반영되었는지 추적성을 확인합니다.

##### **4.2 소프트웨어 설계 평가**
- 설계가 요구사항을 충족하고 기술적 제약 조건을 준수하는지 검토합니다.
- 설계 품질 메트릭(복잡도, 재사용성 등)을 평가합니다.

##### **4.3 소프트웨어 설계 인터페이스 분석**
- 설계된 시스템 모듈 간의 인터페이스 정의와 데이터 흐름을 검토합니다.
- 모듈 간 상호작용에서 발생할 수 있는 잠재적 문제를 사전에 식별합니다.

##### **4.4 테스트 계획 및 설계 생성**
- 각 설계 단계에서 테스트를 위해 필요한 계획 및 테스트 케이스를 작성합니다.
  - **컴포넌트 테스트**: 개별 모듈 단위 테스트.
  - **통합 테스트**: 모듈 간 상호작용 검증.
  - **시스템 테스트**: 전체 시스템의 동작 검증.
  - **인수 테스트**: 최종 사용자 요구사항 기반 테스트.

---

#### **5. 구현 단계의 검증 및 확인 (Implementation Phase V&V)**

##### **5.1 소스코드 추적성 분석**
- 소스코드와 설계 문서가 연계되어 있는지 확인합니다.

##### **5.2 소스코드 평가**
- 코드 품질 표준(코딩 스타일, 복잡도 등)을 준수하는지 자동화 도구를 통해 검토합니다.
- 정적 분석 도구(예: SonarQube)를 사용하여 잠재적 결함을 식별합니다.

##### **5.3 소스코드 인터페이스 분석**
- 모듈 간 데이터 전송 및 호출 방식의 적합성을 확인합니다.

##### **5.4 테스트 케이스 및 절차 생성**
- 구현된 기능을 검증하기 위한 테스트 케이스를 작성합니다.
  - 컴포넌트 테스트, 통합 테스트, 시스템 테스트, 인수 테스트 포함.

##### **5.5 컴포넌트 테스트 실행**
- 구현된 모듈을 단독으로 테스트하여 초기 결함을 식별하고 수정합니다.

---

#### **6. 테스트 단계의 검증 및 확인 (Test Phase V&V)**

##### **6.1 인수 테스트 케이스 생성**
- 최종 사용자 요구사항을 기준으로 테스트 케이스를 설계합니다.

##### **6.2 테스트 실행**
- 각 수준의 테스트를 실행합니다.
  - **통합 테스트**: 모듈 간 상호작용 확인.
  - **시스템 테스트**: 전체 시스템의 기능과 성능 검증.
  - **인수 테스트**: 사용자가 요구한 기능이 적합하게 구현되었는지 확인.

---

#### **7. 설치 및 검사 단계의 검증 및 확인 (Installation and Checkout Phase V&V)**

##### **7.1 설치 구성 감사**
- 배포 프로세스와 설치된 시스템의 구성 요소가 요구사항을 충족하는지 검토합니다.

##### **7.2 최종 검증 및 확인 보고서 생성**
- 모든 검증 및 확인 활동의 결과를 종합하여 최종 보고서를 작성하고, 이를 기반으로 시스템 인수를 결정합니다.

---

#### **8. 작동 및 유지보수 단계의 검증 및 확인 (Operation and Maintenance Phase V&V)**

##### **8.1 소프트웨어 검증 및 확인 계획 수정**
- 운영 중 발견된 결함 및 요구사항 변경을 반영하여 계획을 업데이트합니다.

##### **8.2 예외 처리 평가**
- 소프트웨어가 비정상 상황(예: 네트워크 장애, 데이터 손실)에서도 적절히 작동하는지 검증합니다.

##### **8.3 제안된 수정 평가**
- 시스템 수정 후 검증 테스트를 반복하여 수정 사항이 기존 기능에 영향을 미치지 않는지 확인합니다.

##### **8.4 단계 태스크 반복**
- 필요 시 이전 단계의 검증 및 확인 활동을 반복하여 품질을 보장합니다.

---

### 결론
각 단계에서 체계적이고 세부적인 검증 및 확인 활동을 수행하면 소프트웨어 품질을 보장하고, 결함을 조기에 발견하여 비용과 시간을 절감할 수 있습니다. 각 단계의 문서화와 추적성을 확보하는 것이 성공적인 V&V의 핵심입니다.
