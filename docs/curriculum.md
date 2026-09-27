# 모듈별 상세 계획

각 모듈은 **① 무엇을 배우는지 → ② 할 일 → ③ 교재에서 고쳐야 할 점 → ④ 확인 포인트** 순서로 정리했습니다.
교재 코드를 그대로 옮기지 말고, 여기 적힌 "고쳐야 할 점"을 참고해 **직접 새로 작성**합니다.

## 공통: 옛날 문법 → Qiskit 2.x 대응표

| 교재(옛날 방식) | 지금 방식 | 비고 |
|---|---|---|
| `Aer.get_backend('aer_simulator')` | `from qiskit_aer import AerSimulator` → `AerSimulator()` | 옛 방식도 동작할 수 있으나 새 방식 권장 |
| `Aer.get_backend('qasm_simulator')`, `QasmSimulator()` | `AerSimulator()` | QasmSimulator는 사라짐 |
| `q.execute(...)` | `transpile()` 후 `backend.run()` | execute는 Qiskit 1.0에서 삭제 |
| `qiskit.tools.visualization`, `qiskit.tools.monitor.job_monitor` | `qiskit.visualization` / job_monitor는 없음 | `qiskit.tools` 모듈 삭제 |
| `qiskit.providers.fake_provider.FakeNairobi` | `qiskit_ibm_runtime.fake_provider`의 가짜 백엔드 | `qiskit-ibm-runtime` 설치 필요, 이름은 설치 후 확인 |
| `prov.get_backend(...)`, `prov.retrieve_job(...)` (IBMProvider) | `QiskitRuntimeService` | 모듈 9에서 공식 문서로 최신 방식 확인 |
| `backend.run()` (IBM 실제 기기) | `SamplerV2` 사용 | 모듈 9에서 확인 |
| `c_if` 조건부 게이트 | `with qc.if_test(...):` | Qiskit 2.0에서 c_if 삭제 |
| `routing_method='stochastic'` | `'sabre'` 등 | 최신 버전에서 없을 가능성 높음 → 실행해서 확인 |
| `layout_method='noise_adaptive'` | `'sabre'`, `'dense'`, `'trivial'` | 없을 가능성 높음 → 실행해서 확인 |
| `draw('mp1')` | `draw('mpl')` | 숫자 1이 아니라 소문자 L |

---

## 모듈 0. 환경 준비 (교재 p.188)

**할 일**
1. 가상환경 파이썬으로 `qiskit[visualization]`, `qiskit-aer` 설치
   - pip이 있으면: `.\.venv\Scripts\python.exe -m pip install "qiskit[visualization]" qiskit-aer`
   - pip이 없으면(uv 가상환경): `uv pip install --python .\.venv\Scripts\python.exe "qiskit[visualization]" qiskit-aer`
2. 설치 확인: `qiskit`, `qiskit_aer`, `matplotlib`를 import해서 버전 출력

**주의**
- 패키지 이름 오타 금지 (비슷한 이름의 악성 패키지 = 타이포스쿼팅)
- 그냥 `pip install` 말고 반드시 가상환경 파이썬으로 설치

---

## 모듈 1. 첫 양자회로: H → barrier → H (교재 p.188 [21])

**배우는 것**: 대각기저로 준비한 큐비트를 대각기저로 측정하면 원래 값(0)이 100% 나온다 → BB84의 핵심 원리

**할 일**
1. `aer_basics.py` 실행 → `{'0': 1024}` 확인
2. 교재 p.188 표 해석: 앨리스·밥 기저가 같은 1·3·6·8번째 자리만 남아 공유키 `0 1 0 1`
3. (응용) 두 번째 H를 빼면 결과가 어떻게 바뀌는지 실험 → 약 50:50

**교재에서 고칠 점**: `Aer.get_backend` → `AerSimulator()`, `import numpy as no` → `np`, `plot_bloch_multiverctor` 오타, `randint_` 오타

---

## 모듈 2. BB84 — 도청 없음 (교재 p.189~191, seed 0)

**배우는 것**: 앨리스 인코딩 → 밥 디코딩 → 기저 비교 → 같은 기저 자리만 키로 사용

**할 일**
1. 내 `BB84.py` 실행 (도청 없음 오류율 0% 예상)
2. 교재 방식 함수 3개를 Qiskit 2.x로 새로 작성: `encode_message`, `decode_message`, `generate_encryption_key`
3. n = 35, seed 0으로 실행 → 앨리스 키 == 밥 키 → "전송 성공!"
4. 내 `BB84.py`(StatevectorSampler)와 교재 방식(AerSimulator, shots=1, memory=True) 비교

**인코딩 규칙 (교재 기준)**: 기저 0 = 직교기저(+), 1 = 대각기저(×)
- 기저 0: 비트 0 → 아무것도 안 함 / 비트 1 → X
- 기저 1: 비트 0 → H / 비트 1 → X 후 H

**교재에서 고칠 점 (오타가 아닌 구조 문제)**
- [22]에서 `encode_message`를 정의하기도 전에 호출함 → 정의 먼저
- [26]에서 `bob_results`를 만들지 않고 출력함 → decode 먼저 실행
- 함수들이 `n`을 인자로 받지 않고 바깥 변수에 의존 → `len(bits)` 사용
- `decode_message`가 인자로 받은 회로에 측정을 직접 덧붙임 (원본 회로가 바뀜)

**교재 오타 목록**: `incode_message`, `select=0`(→ `seed=0`), `run decode_msg`(→ `return`), `ramge`, `apprnd`, `alise_bases`, `decode_,msg`, `result,get_memory`, `message[q], measure`(쉼표 → 점), `print("전송 송공!)` 따옴표 누락, `if alice_key == bob_key` 콜론 누락

---

## 모듈 3. BB84 — 도청 있음 (교재 p.191, seed 4)

**배우는 것**: 이브가 무작위 기저로 측정하면 상태가 망가져 밥의 키와 달라짐 → 도청 탐지

**할 일**
1. seed 4로 이브가 `decode_message(message, eve_bases)`로 가로챈 뒤 밥이 디코딩
2. 앨리스 키 ≠ 밥 키 → "도청감지, 전송실패!" 확인
3. 키가 다른 자리 비율(오류율) 계산 → 이론값 약 25%와 비교

**확인 포인트 (실험해볼 것)**
- 교재 코드는 이브가 측정한 **같은 회로 객체**에 밥의 게이트를 덧붙임 → 한 번 실행 안에서 이브 측정 → 밥 측정이 순서대로 일어나는 구조가 맞는지 확인
- 이브가 측정 후 **자기 기저로 다시 준비(재인코딩)하지 않음** → 재인코딩하는 버전과 오류율 비교
- 교재 오타: `nq.random`, `bod_results`, `generate__encryption_key`

---

## 모듈 4. 상태벡터·유니터리·블로흐 구·GHZ (교재 p.192~199)

> ⚠ p.194~199 사진은 아직 없음. 인수인계 요약 기준으로 계획함.

**할 일**
1. 벨 회로 `draw('mpl')`, `copy()` 후 `measure_all()`
2. 상태벡터 출력 → √2/2|00⟩ + √2/2|11⟩ (`Statevector`, `draw('latex')`)
3. 측정 시뮬레이션 (교재 QasmSimulator → AerSimulator)
4. 유니터리 행렬 보기, I⊗H 와 H⊗I 차이
5. 블로흐 구(`plot_bloch_multivector`)로 h, cx, x 게이트별 상태 변화
6. 일부러 에러 내보기: `cx(1)` → 제어·대상 큐비트 두 개가 필요하다는 TypeError
7. 3큐비트 GHZ 상태

**교재에서 고칠 점 (p.192~193)**: `sevice`, `ibm_quatum`, `service.backend()`(→ `backends()`), `Qidkit`, `AtatevectorAimulator`, `simullator`, `transfile`, `qiskit-ser`, `compiled_cirsuit`, `counte`

---

## 모듈 5. BV 알고리즘과 실제 기기의 한계 (교재 p.212~217)

> ⚠ BV 알고리즘을 처음 소개하는 부분(p.200~211)은 사진이 없음.

**배우는 것**
- **BV(Bernstein-Vazirani) 알고리즘**: 숨겨진 비밀 비트열을 한 번 실행으로 알아내는 알고리즘 (교재 결과상 비밀 문자열은 `1101`로 보임)
- **fidelity(충실도)**: 이상적인 결과와 실제 결과가 얼마나 비슷한지 0~1 점수 (`hellinger_fidelity`)
- 큐비트 수가 늘면 SWAP 게이트가 추가되어 fidelity가 급격히 떨어짐 (교재 그래프: 6큐비트부터 급락)

**할 일**
1. `bv_ones_circs(N)`: 비밀 문자열이 전부 1인 N큐비트 BV 회로 만들기
2. 2~10큐비트 회로 리스트 생성
3. 이상적 시뮬레이터(`AerSimulator()`) vs 잡음 시뮬레이터(`AerSimulator.from_backend(가짜백엔드)`) fidelity 비교 그래프
4. (모듈 9 이후) 실제 기기 결과도 같은 그래프에 추가

**교재에서 고칠 점**: `qiskit.tools.nomitor`(삭제됨), `prov.retrieve_job`(옛 방식), `QuantumCircuit(N, M-1)` 인자 혼동(M/N), `measuer`, `MAX_BITES`, `hellinger_fidelities`/`heeinger`, `Aer_cont`, `shots=1(0000)`, `label*'Aer'`, `ax.Legent`, `scheduling_method='a1ap'`(→ `'alap'`)

---

## 모듈 6. Transpile 깊이 파기 (교재 p.218~225)

**배우는 것**: transpile = 내 회로를 실제 기기가 알아듣는 기본 게이트로 바꾸고 배치를 최적화하는 과정

**할 일**
1. 최적화 레벨 0 vs 3 회로 비교, 가짜 백엔드로 10000번 실행 후 히스토그램 비교 (p.218~219)
2. `backend.operation_names`로 기본 게이트 집합 확인 (`rz`, `sx`, `x`, `cx` 등), `plot_gate_map`, `plot_error_map` (p.220)
3. **Layout**(논리 큐비트 → 실제 큐비트 배치): default / sabre / dense / 직접 지정(`initial_layout`) 4가지 결과 비교 (p.221~223)
4. **Routing**: 연결 안 된 큐비트 사이에 SWAP 삽입 — depth와 SWAP 개수 출력 (p.223)
5. **Translation**: `translation_method` 비교 (p.223~224)
6. **Optimization**: `PassManager` + `CommutativeCancellation`으로 cx 두 개가 사라지는 예제 (p.224~225)
7. **Scheduling**: `scheduling_method='alap'` / `'asap'`로 Delay가 삽입되는 모습 (p.225~226)

**교재에서 고칠 점**: `Fake Nairibi`, `goos_counts`, `result()get_counts()` 점 누락, `tr_circ.append{...}` 중괄호, `.sraw`, `layout_method+trivial`, `stodhastic`, `trandlator`, `Galse`, `trandpile`, `COmmunicativeCancellation`(→ `CommutativeCancellation`)

---

## 모듈 7. Dynamic Circuit (교재 p.225~227)

**배우는 것**: 회로 도중에 측정하고 그 결과로 다음 동작을 바꾸는 회로 → 큐비트 재사용으로 회로 크기·depth 감소

**할 일**
1. `reset(0)`으로 회로 중간에 큐비트를 |0⟩으로 초기화
2. `with qc.if_test(...)`로 측정 결과에 따른 조건부 게이트
3. **도전 과제**: 큐비트 2개(보조 큐비트 + 대상 큐비트)를 재사용하는 `dynamic_bv` 직접 구현
   - 교재에는 함수 정의가 없음! p.226 그림만 보고 만들어야 함
4. 일반 BV와 동적 BV의 회로 크기·depth 비교

---

## 모듈 8. 양자역학 이론 읽기 (교재 p.227~229, 코딩 없음)

**내용**: 양자화 가설, 슈뢰딩거 방정식 유도, 하이젠베르크 행렬역학, 디랙 표기법(브라-켓)

**교재 수식 오류 주의**
- p.228: `ħ = 6.63×10⁻³⁴ J·s` → 이 값은 **h**(플랑크 상수). ħ = h/2π ≈ 1.055×10⁻³⁴
- p.228 ④식: `Eψ = -ħ ∂ψ/∂t` → **`Eψ = iħ ∂ψ/∂t`**가 맞음
- ⑦식 ∂가 δ로 표기됨

**할 일**: 유도 과정을 손으로 따라 써보고 `notes/`에 정리

---

## 모듈 9. (나중에) IBM 실제 양자컴퓨터 (교재 p.191~192)

**할 일**
1. IBM Quantum Platform 가입, 최신 채널 이름·인증 방식은 **공식 문서로 확인**
2. 토큰은 `.env`에 저장하고 코드에서 불러오기 (`.gitignore`에 `.env` 등록 확인)
3. 사용 가능한 백엔드 목록 확인 (교재의 `ibm_kyoto`, `ibm_nairobi`, `ibm_auckland` 등은 퇴역했을 가능성 높음)
4. 벨 회로 또는 BV 회로를 실제 기기에서 실행 → 모듈 5 그래프에 Hardware 선 추가

**보안**: 토큰이 들어간 파일은 커밋 전에 `git status`로 한 번 더 확인
