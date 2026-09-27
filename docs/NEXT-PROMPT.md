# 다음에 이어서 할 때 Claude에게 보낼 프롬프트

> 새 대화를 열고 아래 회색 상자 안 내용을 **통째로 복사해서** 붙여넣으면 됩니다.
> 시작 전 준비와 끝난 뒤 정리 절차는 [HOW-TO-RESUME.md](HOW-TO-RESUME.md)를 따릅니다.
> 공부를 마칠 때마다 아래 **[로드맵 위치] [현재 진행 상황] [이번에 할 것]** 세 곳을 업데이트해 두기.

## 프롬프트 (복사해서 붙여넣기)

```
qiskit-study 저장소로 양자 컴퓨팅 학습과 교재 Qiskit 실습을 이어서 하고 있어.
저장소: github.com/ten-infosec/qiskit-study
(README에 진행 상황, docs/curriculum.md에 전체 커리큘럼 — 개념 로드맵 Q1~Q6 + 교재 실습 모듈 0~9 — 있음)

[답변 방식]
- 한국어로, 전문 용어는 처음 나올 때 쉬운 말로 풀어서 설명
- 명령어·옵션은 "왜 이렇게 하는지"까지 설명, 한 번에 너무 많은 단계 말고 차근차근
- 코드 형식: 한 코드 블록 안에 "제목 주석 → 2줄 띄우기 → 코드 → 2줄 띄우기 → '→ ~하겠다' 해석 주석"
- 여러 단계 코드는 "코드 블록 → 해석"을 단계별로 반복
- 답변 맨 아래에 "📌 남은 할 일" 체크리스트 계속 유지

[환경]
- Windows + VS Code, 바탕화면 qiskit-study 폴더
- 가상환경 .venv (파이썬 3.14.6, uv 기반) — pip 대신 uv pip install --python .\.venv\Scripts\python.exe 사용
- qiskit 2.5.2 / qiskit-aer 0.17.2 / matplotlib 3.11.2 설치 완료
- 실행: .\.venv\Scripts\python.exe 파일이름.py
- VS Code 자동 저장 켜져 있음

[로드맵 위치]
- 실습: 모듈 2 진행 중 (로드맵 Q6 — QKD)
- 개념: Q1(수학 언어) 시작 — 디랙 표기법, 선형대수, 텐서곱

[현재 진행 상황]
- 모듈 0 완료: Aer·시각화 도구 설치
- 모듈 1 완료: aer_basics.py (H-barrier-H → {'0': 1024}, 밥의 H 빼면 {'0': 522, '1': 502})
- 내 BB84.py(StatevectorSampler) 실행 완료: 도청 없음 QBER 0.0% / 도청 있음 19.4%
- 교재는 오타가 많고 옛날 Qiskit 문법이라 Qiskit 2.x로 고쳐가며 실습 중
- 교재 사진은 저작권 때문에 GitHub에 안 올림

[이번에 할 것]
모듈 2: 교재 BB84 코드(p.189~191)를 Qiskit 2.x로 고쳐서 seed 0으로 실행
  2-1. encode_message (앨리스 인코딩)
  2-2. decode_message (밥 측정, AerSimulator shots=1 memory=True)
  2-3. generate_encryption_key (기저 같은 자리만 키로)
  2-4. seed 0 전체 실행 → "전송 성공!" 확인
교재의 구조적 버그(정의 전에 호출, bob_results 없이 출력, n을 전역 변수에 의존,
decode가 원본 회로를 직접 바꿈)도 짚어줘.
실습 중 나오는 개념(브라켓 표기, 기저, 측정)은 Q1~Q2 개념과 연결해서 설명해줘.
교재 p.189~191 사진을 같이 보낼게. 2-1부터 차근차근 안내해줘.
```
