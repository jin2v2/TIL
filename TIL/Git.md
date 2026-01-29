# CLI
- Command Line Interface
- 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

## CLI에서 가장 중요한 것.
- 내가 어디 있는지(경로) 알아야 한다.
    - 루트(root) 디렉토리(/)
    - 홈 디렉토리(~)

    - 절대경로 : 루트 부터 목적지까지의 전체주소
    - 상대경로 : 현재 내 위치를 기준으로 한 주소

## 기초 문법 정리
| 문법 | 역할 | 예시 |
| -- | -- | -- |
|.|현재 디렉토리| -- |
|..|상위 디렉토리| -- |
|touch|파일 생성| touch ../bar |
|mkdir|폴더(디렉) 생성| -- |
|ls|폴더/파일 목록을 출력| -- |
|cd|작업 위치 이동| -- |
|start|폴더 / 파일을 열기| -- |
|rm|파일 삭제| -- |
|rm -r|폴더(디렉) 삭제| -- |
|pwd|디렉의 절대 경로를 출력| -- |

# Git
- 분산 버전 관리 시스템
    - 중앙 집중식 : 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
    - 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리

- 코드의 버전을 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

### Git의 3가지 영역
1. Working Directory : 실제 작업 중인 파일들이 위치하는 영역

2. Staging Area : WD에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

3. Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역 모든 버전과 변경 이력이 기록됨


## Git의 동작
### git init
    - git init
    - 로컬 저장소 설정(초기화)
    - git의 버전 관리를 시작할 디렉토리에서 진행
    - <주의사항> : Git 로컬 저장소 내에 또다른 Git 로컬 저장소를 만들지 말 것.

### git add
    - git add .
    - git add sample.txt
    - 변경사항이 있는 파일을 staging area에 추가

### git commit
    - git commit -m "first commit"
    - staging area에 있는 파일들을 저장소에 기록
    - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것

### git status
    - git status
    - 로컬 저장소의 파일 상태 확인

### git config
    - git config --global user.email " "
    - git config --global user.name " "
    - git 사용자 정보 등록

### git log
    - git log
    - git log --oneline : commit 목록 한 줄로 보기
    - git config --global -l : git global 설정 정보 보기
    - commit history 목록 확인

## 로컬
- 현재 사요자가 직접 접속하고 있는 기기

## 원격 저장소(Remote Repository)
- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장공간

## GitHub Repository & Local Repository
  ### git remote add origin remote_repo_url
    - 로컬 저장소에 원격 저장소 추가
    - origin : 추가하는 원격 저장소 별칭
    - remote_repo_url : 추가하는 원격 저장소 주소(url)
    
  ### git remote -v
    - 등록된 원격 저장소 목록 확인

  ### git remote rm
    - 현재 로컬 저장소에 등록된 원격 저장소 삭제

  ### git push
    - git push origin master
    - git push -u origin master : master 브렌치의 원본 브렌치를 origin의 master를 원본으로 기록
    - 원격 저장소에 commit 목록을 업로드

  ### git pull
    - git pull origin master
    - 원격 저장소의 변경사항만을 받아옴(업데이트)

  ### git clone
    - git clone <remote_repo_url>
    - 원격 저장소 전체를 복제(다운로드)

  ## git ignore
    - git에서 특정 파일이나 디렉을 추적하지 않도록 설정하는 데 사용되는 텍스트 파일(공유하지 않을 문서 저장소)
    - .gitignore 파일 생성
    - .gitignore에 파일 작성
    - git init
    - git status

    <주의사항> : 이미 git의 관리를 받은 이력이 있는 파일이나 디렉은 나중에 gitignore 적용되지 않음 --> git rm --cached 명령어를 통해 git 캐시에서 삭제 필요

  ## git revert
    - git log --oneline
    - git revert <commit id>
    - vim 편집기 실행 - 저장 후 종료
    - 특정 commit을 없었던 일로 만드는 작업
    - 재설정
    - 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업
    - commit 기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 commit을 생성
    - git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임

  ## git reset
    - git log --oneline
    - git reset --soft <id>
    - git status

    <Remote에 올라간 commit은 절대 reset해서는 안됨>

    - git reset [옵션] <commit id>
    - 특정 commit으로 되돌아가는 작업
    - 되돌리기
    - 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제
    
    - [옵션] 1. --soft 2. --mixed 3. --hard

    - 삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지 옵션을 활용해 조정
    
    - --soft : 삭제된 commit들의 기록을 staging area에 남김
    
    - --mixed : 삭제된 commit들의 기록을 working directory 에 남김 (기본값) : untracked 된다.

    - --hard : 삭제된 commit들의 기록을 남기지 않음
  
  ## git restore
    - Modified 상태 파일 되돌리기
    - working directory에서 파일을 수정했을 때 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업
    - 원래 파일로 덮어쓰는 원리이기 때문에 수정한 내용은 전부 사라짐
    - git restore를 통해 수정 취소 후에는 해당 내용을 복원할 수 없음

  ## Unstage
    - git restore -staged
      : staging area에서 working directory로 되돌리기

    - git rm --cached
      : 