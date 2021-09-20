# PythonGame
Python  Game Development

작업 환경 
    1. OS : macOS Big Sur 11.5.2 
    2. 언어 : Python 3.9.7 
    3. IDE(편집기) : VS CODE
    4. pygame : 21.2.4

공부 자료 출처 : 유투브 "나도코딩" nadocoding.tistory.com

pygame_basic폴더의 파일의 소스를 순차적으로 확인해보면 어떤식으로 게임을 개발하여야 하는지 도움될 수 있다.

2021년 9월 20일
    팡 게임 만들기_공 움직임(3_ball_movement.py)
        1. 공 만들기
            공은 크기에 따라 따로 처리할 예정, 각각의 크기에 맞는 이미지를 로드할때 리스트로 관리한다.
                ball_images = [pygame.image.load(os.path.join(image_path,"파일명")),...]

        2. 공의 크기에 따른 최초 속도
            공 크기에 따라 각각의 공이 튀어 오를때의 최초듸 속도를 지정, 공이 지면(경계면)에 닿았을 때의 속도를 의미한다.
                balls_speed_y = [-18, -15, -12, -9]            
        3. 공 관리
            무기와 마찬가지로 큰공에서 작은공으로 갈때는 2개씩 늘어나며, 공의 종류 또한 4종류나 되기에 리스트로 관리한다.
                balls = []
        4. 최초 발생하는 큰공의 정보 추가
            공 하나를 정의 하기 위해서는 다양한 정보를 정의해주어야 하므로 사전형으로 정의를 하도록한다.
            balls.append({
                "pos_x" : 공의 x 좌표 
                "pos_y" : 공의 y 좌표
                "img_idx" : # 공의 이미지 인덱스
                "to_x" : x축 이동 방향, -방향이면 왼쪽으로, +방향이면 오른쪽으로 이동
                "to_y" : y축 이동 방향, -방향이면 위로, +방향이면 아래로 이동
                "init_spd_y" : ball_speed_y[i]   # 2.에서 말하는 최초 속도 (y 최초 속도)
            })
        5. 리스트의 인덱스, 값을 출력하는 enumerate 연습 예제 
            practice_enumerate.py에서 연습예를 확인한다.
        6. 공의 위치를 정의
            4.에서 정의한 pos_x, pos_y, pos_img_idx를 그대로 각각의 balls의 변수에 넣는다.
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]
            그 다음부터는 캐릭터와 비슷하게 ball의 크기를 취득 
            ball_size = ball_images[ball_img_idx].get_rect().size
        7. x축 이동 설정 : 세로 벽에 닿았을 때 공 이동 위치 변경
            캐릭터의 경계벽 처리와 비슷하게 처리, 다만 벽에 부딛히면 방향이 만대로 튕기는 효과를 주어야 한다.
                if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
                    ball_val["to_x"] = ball_val["to_x"] * -1
        8. y축 이동 설정 
            y축에서의 이동은 스테이지(stage)에 닿았을 때와 그 이외의 동작 모두로 2패턴으로 나뉜다.
                a. 튕겨져 올라갈 때(스테이지에 닿았을 때)
                    if ball_pos_y >= screen_height - statge_height - ball_height:
                        ball_val["to_y"] = ball_val["init_spd_y"]
                b. 그 이외 의 경우
                    else: 
                        ball_val["to_y"] += 0.5
        9. 볼의 좌표를 갱신 
            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]
        10. 화면에 그리기
            화면에 그릴때도 5.의 enumerate함수를 이용하여 작성 
                for idx, val in enumerate(balls):
                    ball_pos_x = val["pos_x"]
                    ball_pos_y = val["pos_y"]
                    ball_img_idx = val["img_idx"]
                    screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
    리스트 항목 추출함수(practice_enumerate.py)
        리스트의 인덱스와 값을 추출한다. 리스트_idx에 인덱스 값, 리스트_val에 데이터 값을 추출
            for 리스트_idx, 리스트_val in enumerate(리스트):
    충돌(4_collision.py)
        1. 캐릭터가 공에 닿았을 경우에는 이전 basic에서 진행하였듯이 진행
            캐릭터의 rect 정보를 취득 및 갱신
                character_rect = character.get_rect()
                character_rect.left = character_x_pos
                character_rect.top = character_y_pos
            공의 rect 정보를 취득 및 갱신 각각의 공에 대해서 취득해야 함으로 for문 사용 
                for ball_idx, ball_val in enumerate(balls):
                    ball_pos_x = ball_val["pos_x"]
                    ball_pos_y = ball_val["pos_y"]
                    ball_img_idx = ball_val["img_idx"]
                    ball_rect = ball_images[ball_img_idx].get_rect()
                    ball_rect.left = ball_pos_x
                    ball_rect.top = ball_pos_y
            공과 캐릭터의 충돌처리(colliderect())
                if character_rect.colliderect(ball_rect):
                    running = False
                    break
        2. 공들과 무기들의 충돌 처리
            무기들도 리스트로 관리하고 있으므로 공과 동일하게 rect정보를 취득후 충돌처리(colliderect())
                for weapon_idx, weapon_val in enumerate(weapons):
                    weapon_pos_x = weapon_val[0]
                    weapon_pos_y = weapon_val[1]
                    
                    weapon_rect = weapon.get_rect()
                    weapon_rect.left = weapon_pos_x
                    weapon_rect.top = weapon_pos_y
            공들과 무기의 충돌처리(coliderect())
                if weapon_rect.colliderect(ball_rect):
                    weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                    ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정
                    break
        3. 무기와 공의 충돌시 해당 항목 지우기
            충돌한 공과 무기를 없애기 위한 변수 설정
                weapon_to_remove = -1
                ball_to_remove = -1
            충돌한 공과 무기 없애는 처리
                if ball_to_remove > -1:
                    del balls[ball_to_remove]
                    ball_to_remove = -1
                if weapon_to_remove > -1:
                    del weapons[weapon_to_remove]
                    weapon_to_remove = -1
    공 쪼개기(5_ball_division.py)
        무기와 공이 부딫혔을때 의 if문에서 추가작업
            가장 작은 공이 아니라면 공을 두 개 추가하며 서로 반대 방향으로 나오도록 진행
                if ball_img_idx < 3:
                    # 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보 
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                        "img_idx" :  ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : -3,  # x축 이동 방향, -3이면 왼쪽, 3이면 오른쪽으로 
                        "to_y" : -6, # y축 이동 방향,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]# y 최초 속도
                    })
                    # 오른쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                        "img_idx" :  ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : 3,  # x축 이동 방향, -3이면 왼쪽, 3이면 오른쪽으로 
                        "to_y" : -6, # y축 이동 방향,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]# y 최초 속도
                    })

2021년 9월 19일
    게임 개발 기본 프레임(8_game_frame.py)
        게임개발시 기본 구성만 남겨두었다. 앞으로 게임 개발을 할 경우  8_game_frame.py를 기본 폼으로써 사용하자.
    똥 피하기 게임_직접 코딩(quiz.py)
        1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
        2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
        3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐 
        4. 캐릭터가 똥과 충돌하면 게임 종료
        5. FPS는 30으로 고정 
    똥 피하기 게임_코드 첨삭(quiz_answer.py)
        1. random 함수임포트 
            재 확인 내용 : from random import * 로 추가하면 randint()형식으로 [random.]은  생략가능한데 import random으로 추가하게되면 임포트 하는 패키지까지 포함해서 작성해주어야 한다. random.randint()로...
        2. 거의 정답
    팡 게임 만들기_배경,스테이지,캐릭터(1_frame_background_stage_character.py)
        1. 게임 이미지 생성
            배경, 스테이지, 캐릭터, 무기, 공1~4
        2. 전체경로가 아닌 지정 폴더, 파일을 지정하기
            os패키지 기능을 사용하기 위해 추가
                import os
            현재 파일의 위치를 반환
                current_path = os.path.dirname(__file__)
            현재 파일 경로에서 다른 파일/폴더를 지정해서  load()에 넣기
                os.path.join(current_path,"폴더/파일명")
        3. 배경설정, 스테이지설정, 캐릭터설정
            게임개발 기본 프레임에서 배경, 스테이지, 캐릭터그리기 까지 완료 
    팡 게임 만들기_무기, 이벤트(2_weapon_keyevent.py)
        1. 무기 객체 생성
            캐릭터 객체, 적 객체와 마찬가지로 load를 이용해서 생성, 무기의 이동 속도도 선언
        2. 무기의 경우 여러발을 발사할 수 있기 때문에 리스트로 선언
            weapons = []
        3. 무기를 발사 했을 때 무기가 발사가 되어야 하므로 key이벤트에서 무기의 위치를 지정해 준다. 무기는 캐릭터의 위치[character_x_pos]에서 캐릭터의 절반[character_width]크기만큼 더한값에 무기 이미지의 절반[weapon_width]을 빼주어 무기의 x좌표를 계산한다.
            또한 무기 발사시마다 리스트에 넣어주어야 한다.
            weapons.append([무기x좌표, 무기y좌표])
        4. 무기의 위치를 조정
            무기는 리스트로 저장햇는데 x좌표는 고정이면서, y좌표만 변한다. 이것을 기존 weapons에 다시 넣는 작업을 한 줄 for문을 이용해서 작성하면 다음과 같다. y좌표인 w[1]만 무기의 이동속도만큼 빼주는 처리를 해준다.
                weapons = [ [ w[0], w[1] - weapon_speed] for w in weapons ]
        5. 무기가 화면 제일 상단에 닿게되었을 때 무기를 안보이게 하려면 4.의 코드에서 조건을 추가한다.
                weapons = [ [ w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0]
        6. 무기를 화면에 그리기
            for문을 이용해서 weapons에서 weapon_x_pos,weapon_y_pos을 하나씩 빼서 화면에 그려준다.
        7. 화면에 그릴 경우 코딩 순서에 따라 그려지기 때문에 출력 순서를 조절해 주어야 한다. 무기를 캐릭터 아래에 그리도록 작성하면 화면에서는 캐릭터 위로 무기 이미지가 나오게된다.

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