from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill((210, 255, 255))
clock = time.Clock()
FPS = 60

game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.witgh = player_width
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_rocet1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_rpcet2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite('tennis.png', 300, 250, 4, 50, 50)
player1 = Player('Rocket.png', win_width - 25, 400, 4, 20, 100)
player2 = Player('Rocket.png', 10, 4, 4, 20, 100)

speed_y = 3
speed_x = 3

font.init()
font = font.Font(None, 50)
lose1 = font.render("Игрок номер 1 проиграл!", True, (180, 0, 0))
lose2 = font.render("Игрок номер 2 проиграл!", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill((210, 255, 255))
        player1.update_rocet1()
        player2.update_rpcet2()
        ball.reset()
        player1.reset()
        player2.reset()
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose1, (250, 250))
        if ball.rect.x < -50:
            finish = True
            window.blit(lose2, (250, 250))

    display.update()
    clock.tick(FPS)
