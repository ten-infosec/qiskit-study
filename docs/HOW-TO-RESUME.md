# 다음에 이어서 공부하는 방법

시간이 날 때 이 순서대로 하면 바로 이어서 시작할 수 있습니다.

## 1단계. 작업 폴더 열기

1. VS Code에서 바탕화면의 `qiskit-study` 폴더 열기 (파일 → 폴더 열기)
2. 터미널 열기 (메뉴 → 터미널 → 새 터미널)

## 2단계. 최신 상태로 맞추기 (다른 컴퓨터에서 작업했을 경우)

```powershell
git pull
```
→ GitHub에 올라간 최신 내용을 내 컴퓨터로 가져온다. 한 컴퓨터에서만 작업했다면 "Already up to date."가 나오고 끝.

## 3단계. 가상환경 확인

```powershell
.\.venv\Scripts\python.exe -c "import qiskit, qiskit_aer; print(qiskit.__version__, qiskit_aer.__version__)"
```
→ 버전 두 개가 나오면 정상.

**`.venv` 폴더가 없다면** (새 컴퓨터이거나 지웠을 경우 — `.venv`는 GitHub에 안 올리기 때문):
```powershell
uv venv .venv --python 3.14
uv pip install --python .\.venv\Scripts\python.exe qiskit "qiskit[visualization]" qiskit-aer
```
→ 가상환경을 새로 만들고 필요한 패키지를 다시 설치한다.

**VS Code 인터프리터 확인**: 오른쪽 아래 파이썬 버전 표시 클릭 → `.venv` 선택

## 4단계. 어디까지 했는지 확인

1. [README.md](../README.md)의 **진행 체크리스트**에서 체크 안 된 첫 항목 찾기
2. [curriculum.md](curriculum.md)에서 해당 모듈의 "할 일" 읽기
3. [notes/log.md](../notes/log.md)에서 마지막 기록 읽기

## 5단계. Claude에게 이어서 부탁하기

새 대화를 열고 아래 내용을 복사해서 붙여넣기 (`모듈 N`만 바꾸기):

```
qiskit-study 저장소로 교재 Qiskit 실습 중이야. (github.com/ten-infosec/qiskit-study)
환경: Windows + VS Code, .venv (파이썬 3.14.6), qiskit 2.5.2 + qiskit-aer.
실행은 .\.venv\Scripts\python.exe 파일이름.py 로 해.
교재 코드는 오타가 많고 옛날 Qiskit 문법이라 Qiskit 2.x로 고쳐가며 실습 중이야.
지금 할 차례는 [모듈 N]이야. docs/curriculum.md 내용을 붙여줄게:
(여기에 curriculum.md의 해당 모듈 부분 붙여넣기)
교재 해당 페이지 사진도 같이 보낼게. 차근차근 안내해줘.
```
→ 교재 사진은 저장소에 없으니(저작권) 휴대폰 사진첩에서 해당 페이지를 함께 보내기.

## 6단계. 공부 끝나면 기록하고 올리기

1. `notes/log.md`에 오늘 한 것, 막힌 것, 다음 할 것 적기
2. README 체크리스트 업데이트 (`- [ ]` → `- [x]`, 상태 표 ⬜ → ✅)
3. 올리기:

```powershell
git status
git add .
git commit -m "모듈 N: 한 일 요약"
git push
```
→ `git status`: 올라갈 파일 목록 확인. **`.venv`나 `.env`가 목록에 보이면 멈추기!**
→ `git add .`: 바뀐 파일 전부를 커밋 대상으로 담기
→ `git commit -m`: 담은 내용을 설명과 함께 저장 (내 컴퓨터에만 저장됨)
→ `git push`: 저장한 내용을 GitHub로 보내기

## 🔐 올리기 전 체크

- [ ] IBM API 토큰이 코드에 없는가?
- [ ] `.env` 파일이 `git status` 목록에 없는가?
- [ ] 교재 사진이나 교재 원문을 그대로 옮긴 파일이 없는가?
