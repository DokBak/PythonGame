# Project) 오락실 Pang 게임 만들기

# [게임 조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료 (실패)
# 8. FPS는 30으로 고정 (필요시 speed 값을 조정)

# [게임 이미지]
# 1. 배경 : 640 * 480(가로 * 세로) - background.png
# 2. 무대 : 640 * 50 - stage.png
# 3. 캐릭터 : 33 * 60 - character.png
# 4. 무기 : 20 * 430 - weapon.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

import pygame
import os

from pygame.constants import KEYDOWN
##################################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기 
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정 
pygame.display.set_caption("DokBak Pang")

# FPS
clock = pygame.time.Clock()
##################################################################################################################

# 1. 사용자 게임 초기화 (배경 화면 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "image") #image 폴더 위치 반환

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
charatcter_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기(4개 크기에 대해서 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3에 해당하는 값

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" :  0, # 공의 이미지 인덱스
    "to_x" : 3,  # x축 이동 방향, -3이면 왼쪽, 3이면 오른쪽으로 
    "to_y" : -6, # y축 이동 방향,
    "init_spd_y" : ball_speed_y[0]# y 최초 속도
})






# 배경 만들기 
background = pygame.image.load(os.path.join(image_path,"background.png")) # 폴더의 위치에서 이미지를 선택해서 배경변수에 넣기

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1] 
character_x_pos = ((screen_width / 2) - (character_width / 2))
character_y_pos = (screen_height - character_height - stage_height) # 스테이지 위에 캐릭터가 존재하기에 스테이지 높이까지 계산한다.

running = True 
while running:
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. 게임 캐릭터 위치 정의 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 
                character_to_x -= charatcter_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 
                character_to_x += charatcter_speed
            elif event.key == pygame.K_SPACE: # 무기를 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 4. 충돌처리(경계값 처리)
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [ [w[0],w[1] - weapon_speed] for w in weapons if w[1] > 0] # 무기 위치를 위로 

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 세로벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치 
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



    # 5. 화면에 그리기
    # 그리는 순서대로 위에 덮어씌우는 형식이라 사용자 위로 무기가 그려지지 않도록 무기를 제일먼저 작성한다.

    screen.blit(background,(0,0))

    for weapon_x_pos,weapon_y_pos in weapons:
       screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()
    
# pygame 종료
pygame.quit()