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