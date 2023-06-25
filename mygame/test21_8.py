# 1.ゲームの準備をする
import pygame as pg, sys
import math
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images/ika.png")
img1 = pg.transform.scale(img1, (100, 100))
myrect = pg.Rect(100,100,50,50)

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    frame = 0
    # 5.絵を描いたり、判定したりする
    myrect.x= myrect.x + 2
    frame += 1
    myrect.y = myrect.y - 4 * math.sin(frame/5)
    # y方向の動き 
    screen.blit(img1, myrect)
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
