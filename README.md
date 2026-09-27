# qiskit-study

## ▶ 다음 할 일

**모듈 2-1** 교재 BB84 encode_message → 자세한 내용과 Claude용 프롬프트는 [NEXT-PROMPT.md](guide/NEXT-PROMPT.md)
(시간이 20\~30분뿐이면: QRNG 만들기)

---

양자 컴퓨팅 → 암호(RSA·PQC) → QKD → 위성 보안으로 이어지는 학습 저장소입니다.
교재(양자컴퓨팅 교재 p.188\~229)의 Qiskit 예제를 **Qiskit 2.x + qiskit-aer** 기준으로 고쳐가며 실습하고, 개념 로드맵(Q1\~Q6)을 함께 공부합니다.
PQC(양자내성암호) 커리큘럼 **Stage 7 (QKD · QRNG)** 의 BB84 실습에서 시작했고, Q1\~Q6은 그 양자 부분을 깊게 파고드는 가지입니다. (PQC 커리큘럼과의 관계는 [curriculum.md](guide/curriculum.md) 앞부분 참고)

> 교재 코드는 오타가 많고 Qiskit 1.0 이전의 옛날 문법이라 그대로는 실행되지 않습니다.
> 이 저장소에는 **교재를 그대로 옮기지 않고**, 직접 고친 코드와 학습 기록만 남깁니다.

## 📂 가이드 (guide 폴더)

| 파일 | 역할 |
|---|---|
| [guide/curriculum.md](guide/curriculum.md) | **전체 계획** — 개념 로드맵(Q1\~Q6) + 교재 실습 모듈(0\~9) |
| [guide/HOW-TO-RESUME.md](guide/HOW-TO-RESUME.md) | **시작하고 끝내는 법** — 환경 확인, 실행, 기록, 올리기 |
| [guide/NEXT-PROMPT.md](guide/NEXT-PROMPT.md) | **다음에 할 일 상세** — Claude에게 붙여넣을 프롬프트 |
| [notes/log.md](notes/log.md) | 날짜별 학습 기록 |

## 🛠 개발 환경

- Windows + VS Code
- 가상환경: `.venv` (파이썬 3.14.6, uv로 설치한 파이썬 기반)
- 패키지: `qiskit` 2.5.2, `qiskit-aer` 0.17.2, `matplotlib` 3.11.2 (모듈 5부터 `qiskit-ibm-runtime` 추가 예정)
- 실행: `.\.venv\Scripts\python.exe 파일이름.py`

## 🗺 커리큘럼 한눈에 보기

**개념 로드맵 (Q1~Q6)** — 자세한 개념 목록은 [curriculum.md Part 1](guide/curriculum.md#part-1-개념-로드맵-q1q6)

| 단계 | 주제 | 관련 실습 모듈 | 상태 |
|---|---|---|---|
| Q1 | 수학 언어 (디랙 표기법, 선형대수, 텐서곱) | 4, 8 | 🔄 진행 중 |
| Q2 | 물리 직관 (양자역학 가설, 측정, 광자, 블로흐 구) | 0~1, 4, 8 | ⬜ |
| Q3 | 게이트·얽힘·알고리즘 입문 (도이치, BV, 그로버) | 4, 5, 7 | ⬜ |
| Q4 | 쇼어 알고리즘과 양자 위협 (→ PQC는 Stage 6) | 새 모듈 추가 예정 | ⬜ |
| Q5 | 양자 오류와 오류 정정 | 5, 6, 7, 9 | ⬜ |
| Q6 | QKD·QRNG 심화와 위성 보안 | 2, 3 | ⬜ |

**교재 실습 모듈 (0~9)** — 자세한 할 일은 [curriculum.md Part 2](guide/curriculum.md#part-2-교재-실습-모듈-상세-모듈-09)

| 모듈 | 주제 | 교재 | 로드맵 | 상태 |
|---|---|---|---|---|
| 0 | 환경 준비 (시각화·Aer 설치) | p.188 | 준비 | ✅ |
| 1 | 첫 양자회로: H → barrier → H | p.188 | Q2 | ✅ |
| 2 | BB84 — 도청 없음 (seed 0) | p.189~191 | Q6 | 🔄 다음 |
| 3 | BB84 — 도청 있음 (seed 4) | p.191 | Q6 | ⬜ |
| 4 | 상태벡터·유니터리·블로흐 구·GHZ | p.192~199 | Q1~Q3 | ⬜ |
| 5 | BV 알고리즘과 fidelity 비교 | p.212~217 | Q3, Q5 | ⬜ |
| 6 | Transpile (layout / routing / optimization / scheduling) | p.218~225 | Q5 | ⬜ |
| 7 | Dynamic Circuit (reset, if_test, 동적 BV) | p.225~227 | Q3, Q5 | ⬜ |
| 8 | 양자역학 이론 읽기 (코딩 없음) | p.227~229 | Q1~Q2 | ⬜ |
| 9 | (나중에) IBM 실제 양자컴퓨터 | p.191~192 | Q5 | ⬜ |

상태 표시: ⬜ 시작 전 / 🔄 진행 중 / ✅ 완료

## ✅ 진행 체크리스트

**실습**
- [x] `step1_bell.py` — StatevectorSampler로 벨 상태 실행 (`{'00': 517, '11': 483}`)
- [x] 모듈 0 — `qiskit[visualization]`, `qiskit-aer` 설치 및 버전 확인
- [x] 모듈 1 — `aer_basics.py` 실행 (`{'0': 1024}`, 밥의 H 빼면 `{'0': 522, '1': 502}`)
- [x] 모듈 2 — 내 `BB84.py` 실행 결과 확인 (0.0% / 19.4%)
- [x] Q1 — `q1_gates.py` NumPy로 X, Z, H 게이트 행렬 만들고 Qiskit과 비교
- [ ] Q6 — QRNG 만들기 (H 게이트 측정으로 난수 생성)
- [ ] 모듈 2 — 교재 BB84 코드 수정·실행 (encode / decode / generate_encryption_key, seed 0)
- [ ] 모듈 3 — 도청 버전 실행, 교재 구조의 문제점 실험
- [ ] 모듈 4 — 상태벡터·유니터리·블로흐 구·GHZ
- [ ] 모듈 5 — BV 알고리즘 + fidelity 그래프
- [ ] 모듈 6 — Transpile 옵션 비교
- [ ] 모듈 7 — `dynamic_bv` 직접 구현
- [ ] 모듈 8 — 양자역학 이론 정리
- [ ] 모듈 9 — IBM 실제 기기 실행 (토큰 제외하고 기록)

**개념**
- [ ] Q1 — 수학 언어
- [ ] Q2 — 물리 직관
- [ ] Q3 — 게이트·얽힘·알고리즘 입문
- [ ] Q4 — 쇼어 알고리즘과 양자 위협 (실습 모듈 새로 추가)
- [ ] Q5 — 양자 오류와 오류 정정
- [ ] Q6 — QKD·QRNG 심화와 위성 보안

**자료**
- [ ] 교재 p.194~211 사진 확보 — 모듈 4·5 빈 부분 채우기
- [ ] 『프로그래밍으로 배우는 양자 컴퓨팅』, 『양자 컴퓨팅 및 정보: 스캐폴딩 접근 방식』 전체 목차 사진 확보 (국립중앙도서관)

## 🔐 보안 규칙

- IBM API 토큰은 **코드나 GitHub에 절대 넣지 않는다** → `.env` 파일에만 저장 (`.gitignore`에 등록됨)
- 교재 사진·교재 원문 코드는 올리지 않는다 (저작권)

## 🔗 관련 저장소

- [ten-infosec/rsa-from-scratch](https://github.com/ten-infosec/rsa-from-scratch) — RSA 직접 구현·공격·증명 (로드맵 Q4와 연계)
- [ten-infosec/linux-study](https://github.com/ten-infosec/linux-study) — 리눅스 독학
