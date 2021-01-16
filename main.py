import pygame, sys , random

#another size for small screens 288 x 512 you need to quit scale2x


def draw_floor():
    scren.blit(floor_surface, (floor_x_pos, 900))
    scren.blit(floor_surface, (floor_x_pos + 576,900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_suface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_suface.get_rect(midbottom=(700, random_pipe_pos - 300 ))
    return bottom_pipe , top_pipe

def move_pipes(pipes): #mueve los tubos
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=1024:
            scren.blit(pipe_suface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_suface,False,True)
            scren.blit(flip_pipe,pipe)
pygame.init()
scren =pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

#game variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))


pipe_suface = pygame.image.load('assets/pipe-green.png')
pipe_suface = pygame.transform.scale2x(pipe_suface)
pipe_list=[]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]  #todos los tamaños posiles de tubos



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    scren.blit(bg_surface,(0,0))

    #bird movement
    bird_movement += gravity
    bird_rect.centery += bird_movement
    scren.blit(bird_surface,bird_rect)

    #pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)                          #dibujar los rectangulos

    # floor
    floor_x_pos -=1
    draw_floor()
    if floor_x_pos <= -576:
            floor_x_pos = 0




    pygame.display.update()
    clock.tick(120) # este es el contador
