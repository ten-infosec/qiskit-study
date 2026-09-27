# 공부 전에 읽기: 어떤 파일을 어떤 순서로 보나

| 파일 | 역할 | 비유 |
|---|---|---|
| `README.md` 맨 위 "▶ 다음 할 일" | 오늘 할 일 한 줄 | 표지판 |
| `guide/NEXT-PROMPT.md` | 오늘 할 일 상세 + Claude용 프롬프트 | 할 일 쪽지 |
| `guide/HOW-TO-RESUME.md` | 시작하고 끝내는 절차 | 사용 설명서 |
| `guide/curriculum.md` | 전체 계획 | 전체 지도 |

---

## 공부 시작할 때

```
① README.md 맨 위 "▶ 다음 할 일"
   → "아, 오늘은 모듈 2-1이구나" (5초)
        ↓
② guide/NEXT-PROMPT.md
   → 오늘 할 일 상세 확인 + 프롬프트 복사해서 Claude에게
        ↓
③ guide/HOW-TO-RESUME.md 1~3단계
   → git pull, 가상환경 확인 (익숙해지면 안 봐도 됨)
```

## 공부 끝날 때

```
guide/HOW-TO-RESUME.md 6단계
   → 기록 → NEXT-PROMPT 업데이트 → README "▶ 다음 할 일" 한 줄 수정 → push
```

## 가끔 볼 때

```
guide/curriculum.md
   → "지금 전체에서 어디쯤이지?", "이 모듈 다음엔 뭐지?" 할 때
```

---

> 표지판 보고 쪽지 꺼내서 시작하고, 설명서는 헷갈릴 때만, 지도는 길을 잃었을 때만 펴본다.
