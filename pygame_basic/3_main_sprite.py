import pygame

pygame.init() # 초기화 (반드시 필요한 작업)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 화면 타이틀 설정 
pygame.display.set_caption("DokBak Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("pygame_basic/background.png") # 절대 경로

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("pygame_basic/character.png") # 절대 경로
character_size = character.get_rect().size # 이미지의 크기(사이즈)를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 가로의 절반 크기에 해당하는 곳에 위치 (가로) # 가로의 절반 크기에서 캐릭터의 절반 크기만큼 빼주어야 캐릭터가 중앙으로 간다.
character_y_pos = screen_height - character_height # 화면 세로크기 가# 화면장 아래에 해당하는 곳에 위치 (세로) # 전체 높이에서 캐릭터 높이만큼 빼주어야 캐릭터의 높이 위치가 계산된다.


# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()