# 다음에 이어서 할 때 Claude에게 보낼 프롬프트

> 공부를 마칠 때마다 이 파일의 "현재 진행 상황"과 "이번에 할 것"을 업데이트해 두기.
> 새 대화를 열고 아래 회색 상자 안 내용을 **통째로 복사해서** 붙여넣으면 됨.

## 사용 방법

1. VS Code에서 `qiskit-study` 폴더 열기 → 터미널에서 `git pull`
2. 새 Claude 대화 열기
3. 아래 프롬프트 복사 → 붙여넣기
4. 교재 해당 페이지 사진 함께 보내기 (휴대폰 사진첩 / 바탕화면 `qiskit_image.zip`)
5. 필요하면 `docs/curriculum.md`의 해당 모듈 부분도 복사해서 같이 보내기

## 프롬프트 (복사해서 붙여넣기)

```
qiskit-study 저장소로 교재 Qiskit 실습을 이어서 하고 있어.
저장소: github.com/ten-infosec/qiskit-study (README, docs/curriculum.md에 커리큘럼 있음)

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
교재 p.189~191 사진을 같이 보낼게. 2-1부터 차근차근 안내해줘.
```

## 공부 끝날 때 할 일

1. `notes/log.md`에 오늘 기록 추가
2. `README.md` 체크리스트·상태 표 업데이트
3. **이 파일의 [현재 진행 상황]과 [이번에 할 것] 업데이트** (다음 모듈로 바꾸기)
4. `git add .` → `git commit -m "..."` → `git push`