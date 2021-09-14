# PythonGame
Python  Game Development

작업 환경 
    1. OS : macOS Big Sur 11.5.2 
    2. 언어 : Python 3.9.7 
    3. IDE(편집기) : VS CODE
    4. pygame : 21.2.4

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com

2021년 9월 15일
    배경 설정(2_background.py)
        1. 이미지 읽어오기(절대경로, 상대경로둘다 가능)
            pygame.image.load(경로)
        2. 이미지를 열어서 상단 탭 우클릭시 (상대)경로복사 기능이 있다.
        3. 화면 변수에 blit함수로 배경을 그린다.
            변수.blit(배경이미지변수, 좌표(0,0))
        4. 배경을 계속 그려주어야한다.
            pygame.display.update()
    캐릭터 설정(3_main_sprite.py)
        1. 이미지 읽어오기
            pygame.image.load(경로)
        2. 이미지 크기(사이즈)읽어오기. rect()이기 때문에 사각형 사이즈를 읽어온다. 배열로 저장되며 0번이 가로 1번이 세로 크기가 저장된다. 
            이미지변수.get_rect().size
        3. 배경의 좌표는 (0,0) 에서 시작하지만 캐릭터는 어디에 위치될지 모른다. 예로 초기위치(좌표)를 아래 중앙에 위치하게 설정은 (가로 :  (배경의 가로 / 2) - (캐릭터의 가로 / 2), 세로 : 배경의 세로길이 - 캐릭터의 세로길이)로 계산한다.
        4. 배경과 동일하게 화면변수에 blit함수로 캐릭터를 그린다.
2021년 9월 14일
    파이썬 게임 개발 환경 설정
        1. pygame패키지를 설치
            - 공식 사이트에서 파이썬을 설치 한 경우 : pip에서 pygame이 제대로 적용되지 않을 경우도 있다.
            - homebrew에서 파이썬을 설치 한 경우 : pip3 install pygame으로 설치한다.
    초기 설정(1_create_fram.py)
        1. 파이썬으로 게임을 작성하기 위한 pygame패키지 추가
            import pygame
        2. pygame을 import하고나면 반드시 초기화를 한번 진행해주어야 한다.
            pygame.init()
        3. 게임의 화면크기를 조정
            pygame.display.set_mode((가로크기,세로크기))
        4. 게임 타이틀 지정
            pygame.display.set_caption(게임이름)
        5. pygame사용시 설정
            설정에서  linting을 검색하고, python > linting : Bandit Enabled 옵션의 체크를 해제 한다. (처음부터 체크 해제인 경우도 있다.)
        6. 게임은 무엇인가의 이벤트가 있어야 게임이 꺼지지 않는다.
            for event in pygame.event.get()
                if event.type == pygmae.QUIT:
        7. 게임의 맨 마지막에는 pygame 패키지를 닫아주어야 한다
            pygame.quit()