# qiskit-study

교재(양자컴퓨팅 교재 p.188~229)의 Qiskit 예제를 **Qiskit 2.x + qiskit-aer** 기준으로 고쳐가며 실습하는 저장소입니다.
PQC(양자내성암호) 커리큘럼 **Stage 7 (QKD, 양자키분배)** 의 BB84 실습에서 시작했습니다.

> 교재 코드는 오타가 많고 Qiskit 1.0 이전의 옛날 문법이라 그대로는 실행되지 않습니다.
> 이 저장소에는 **교재를 그대로 옮기지 않고**, 직접 고친 코드와 학습 기록만 남깁니다.

## 📂 문서 안내

| 파일 | 내용 |
|---|---|
| [docs/HOW-TO-RESUME.md](docs/HOW-TO-RESUME.md) | **다음에 이어서 공부할 때 여기부터 보기** (환경 확인, 실행 방법, Claude에게 줄 프롬프트) |
| [docs/curriculum.md](docs/curriculum.md) | 모듈별 상세 계획 — 교재 페이지, 할 일, 고쳐야 할 점, 확인 포인트 |
| [notes/log.md](notes/log.md) | 날짜별 학습 기록 |

## 🛠 개발 환경

- Windows + VS Code
- 가상환경: `.venv` (파이썬 3.14.6, uv로 설치한 파이썬 기반)
- 패키지: `qiskit` 2.5.2, `qiskit[visualization]`, `qiskit-aer` (모듈 5부터 `qiskit-ibm-runtime` 추가 예정)
- 실행: `.\.venv\Scripts\python.exe 파일이름.py`

## 🗺 커리큘럼 한눈에 보기

| 모듈 | 주제 | 교재 | 상태 |
|---|---|---|---|
| 0 | 환경 준비 (시각화·Aer 설치) | p.188 | 🔄 진행 중 |
| 1 | 첫 양자회로: H → barrier → H | p.188 | ⬜ |
| 2 | BB84 — 도청 없음 (seed 0) | p.189~191 | ⬜ |
| 3 | BB84 — 도청 있음 (seed 4) | p.191 | ⬜ |
| 4 | 상태벡터·유니터리·블로흐 구·GHZ | p.192~199 | ⬜ |
| 5 | BV 알고리즘과 fidelity 비교 | p.212~217 | ⬜ |
| 6 | Transpile (layout / routing / optimization / scheduling) | p.218~225 | ⬜ |
| 7 | Dynamic Circuit (reset, if_test, 동적 BV) | p.225~227 | ⬜ |
| 8 | 양자역학 이론 읽기 (코딩 없음) | p.227~229 | ⬜ |
| 9 | (나중에) IBM 실제 양자컴퓨터 | p.191~192 | ⬜ |

상태 표시: ⬜ 시작 전 / 🔄 진행 중 / ✅ 완료

## ✅ 진행 체크리스트

- [x] `step1_bell.py` — StatevectorSampler로 벨 상태 실행 (`{'00': 517, '11': 483}`)
- [ ] 모듈 0 — `qiskit[visualization]`, `qiskit-aer` 설치 및 버전 확인
- [ ] 모듈 1 — `aer_basics.py` 실행 (`{'0': 1024}` 확인)
- [ ] 모듈 2 — 내 `BB84.py` 실행 결과 확인 + 교재 BB84 코드 수정·실행
- [ ] 모듈 3 — 도청 버전 실행, 교재 구조의 문제점 실험
- [ ] 모듈 4 — 상태벡터·유니터리·블로흐 구·GHZ
- [ ] 모듈 5 — BV 알고리즘 + fidelity 그래프
- [ ] 모듈 6 — Transpile 옵션 비교
- [ ] 모듈 7 — `dynamic_bv` 직접 구현
- [ ] 모듈 8 — 양자역학 이론 정리
- [ ] 모듈 9 — IBM 실제 기기 실행 (토큰 제외하고 기록)
- [ ] (자료) 교재 p.194~211 사진 확보 — 모듈 4·5 빈 부분 채우기

## 🔐 보안 규칙

- IBM API 토큰은 **코드나 GitHub에 절대 넣지 않는다** → `.env` 파일에만 저장 (`.gitignore`에 등록됨)
- 교재 사진·교재 원문 코드는 올리지 않는다 (저작권)

## 🔗 관련 저장소

- [ten-infosec/rsa-from-scratch](https://github.com/ten-infosec/rsa-from-scratch) — RSA 직접 구현·공격·증명
- [ten-infosec/linux-study](https://github.com/ten-infosec/linux-study) — 리눅스 독학
