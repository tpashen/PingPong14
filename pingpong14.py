from pygame import*

class GameSprite(sprite.Sprite):
    def _init_(self,player_image,player_x,player_y,player_speed,wight,height):
        super()._init_()
        self.image = transform.scale(image.load(player_image), (wight,height))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

        
        
#третья часть кода        
#флаги отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

#создание мяча и ракетки
racket1 = Player('racket.png',30,200,4,50,150) #при создании спрайта добавляется ещё два параметра
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSprite('tenis_ball.png',200,200,4,50,50)

font.init()
font = font.Font('Perfect DOS VGA 437.ttf',35)
lose1 = font.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_weight-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)


