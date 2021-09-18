# PythonGame
Python  Game Development

작업 환경 
    1. OS : macOS Big Sur 11.5.2 
    2. 언어 : Python 3.9.7 
    3. IDE(편집기) : VS CODE
    4. pygame : 21.2.4

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com
2021년 9월 18일 
    충돌(6_collision.py)
        1. 3_main_sprite.py에서 작성하였던 캐릭터와 마찬가지로 충돌할 대상즉 적 캐릭터를 생성해 준다.
            1) 이미지 로드
                pygame.imae.load()
            2) 사이즈
                1)에서의변수.get_rect().size 
            3) 현재 위치 계산
        2. 충돌 처리를 위한 rect정보 업데이트)
            변수_rect = 변수.get_rect()
            변수_rect.left = 변수_x_pos
            변수_rect.top = 변수_y_pos
        3. 충돌 처리
            rect변수의 colliderect함수를 활용 
            변수_rect.colliderect(충돌할 대상)
            결과는 bool 형태이므로 if으로 사용하며 충돌시 작업내용을 작성해준다.
    텍스트(7_text.py)
        1. 폰트정의
            폰트를 지정하지 않을때는 None으로 작성하면 디폴트 폰트로 적용된다.
            pygame.font.Font(폰트,크기)
        2. 시간 정보 취득
            시간정보 중 시작 tick 정보를 받는다.
            시간정보의 단위는 ms로 받아진다.
            pygame.time.get_ticks() 
        3. 게임 내 시간 계산
            게임 시작시 start_ticks으로 먼저 취득 한 상태에서, 새로운 경과시간 게임 변수를 만들어 다시 시간 정보를 취득해 시작 시간정보를 빼준 뒤, 1000으로 나누어 단위를 ms에서 s로 변경한다.
        4. 텍스트표시
            1.에서 정의한 폰트변수의 함수를 사용한다.
            game_font.render(출력할 글자, True, 글자색상)
            다른 것들과 마찬가지로 screen.blit(변수, 위치)함수를 이용해 게임내 화면에 그려준다.
        5. 게임내 딜레이주기
            pygame.time.delay(ms)
            ms단위의 시간을 작성해주면 해당시간동안 딜레이를 줄 수 있다.
            2000 = 2초
2021년 9월 16일
    FPS(5_frame_per_second.py)
        1. FPS를 설정하기 위해서는 clock변수를 선언해야 한다.
            clock = pygame.time.Clock()
        2. 이벤트 루프에 게임화면의 초당 프레임 수를 설정한다.
            dt = clock.tick(60) # 지금은 : 60프레임
        3. 1과 2만 추가한상태에서 프레임수를 변경하면 프레임에 따라 캐릭터의 이동속도가 다르게된다. 게임내의 이동속도는 프레임이 얼마가 되었든 일정해야한다.
        4. 기존 소스의 이동량(5)이 공통된 부분이므로                
            character_speed로 변수로 사용한다.
        5. 프레임이 변화하더라도 이동속도가 비슷하기 위해서는 캐릭터 이동을 조정하는 부분에서 프레임 값을 곱해주면된다.
            character_x_pos += to_x * dt
        6. 프레임에 관한 부가 설명
            #캐릭터가 100만큼 이동을 해야함 
            # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
            # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5 * 20 = 100
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
    키보드 이벤트 설정(4_keyboard_event.py)
        1. 게임을 진행할 때 필요한 입력 이벤트를 설정
        2. 이벤트 타입이 키보드를 누를때(KEYDOWN : 대문자로)
            event.type == pygame.KEYDOWN
        3. 이벤트 타입이 키보드에서 손을 뗄때(KEYUP : 대문자로)
            event.type == pygame.KEYUP
        4. 어떤 키가 눌렸는지는 아래와 같이 작성(Key이름 : 대문자로)
            event.key == pygame.K_LEFT
        5. 이동시 캐릭터의 좌표를 변경해줄 이동좌표를 선언후 이벤트 별로 이동 좌표 값을 조정
        6. 캐릭터의 좌표를 현재좌표 - 이동좌표로 현재좌표를 갱신한다.
        7. 화면크기에 맞게 경계값 처리를 한다.

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
        6. 게임은 무엇인가의 이벤트가 있어야 게임이 꺼지지 않는다.(QUIT : 대문자로)
            for event in pygame.event.get()
                if event.type == pygmae.QUIT:
        7. 게임의 맨 마지막에는 pygame 패키지를 닫아주어야 한다
            pygame.quit()