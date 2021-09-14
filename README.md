# PythonGame
Python  Game Development

작업 환경 
    1. OS : macOS Big Sur 11.5.2 
    2. 언어 : Python 3.9.7 
    3. IDE(편집기) : VS CODE
    4. pygame : 21.2.4

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com


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
        5. 게임은 무엇인가의 이벤트가 있어야 게임이 꺼지지 않는다.
            for event in pygame.event.get()
                if event.type == pygmae.QUIT:
        6. 게임의 맨 마지막에는 pygame 패키지를 닫아주어야 한다
            pygame.quit()