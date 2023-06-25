# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
## 紙芝居
img1 = pg.image.load("images/flower1.png")
img2 = pg.image.load("images/flower2.png")
img4 = pg.image.load("images/flower4.png")
## ボタン
next_img = pg.image.load("images/nextbtn.png")
#------------------------------------------------------------vvv
hitbtn_img = pg.image.load("images/UFO.png")
hitbtn_img = pg.transform.scale(hitbtn_img, (80,80))
ball_img = pg.image.load("images/uni.png")
ball_img = pg.transform.scale(ball_img, (30,30))
ball_rect = pg.Rect(-200,450,30,30)
hit_rect = pg.Rect(500,400,50,100)
#------------------------------------------------------------^^^

pushFlag = False
## btnを押したら、newpageにジャンプする
def button_to_jump(btn, newpage):
    global page, pushFlag
    # 4.ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
    else :
        pushFlag = False

#------------------------------------------------------------vvv
def page1():
    global page, pushFlag, ball_rect    
    # 3.画面を初期化する
    screen.blit(img1, (0,0))
    btn1 = screen.blit(hitbtn_img,(500, 500))
    #ヒットエリアを描く
    pg.draw.rect(screen, pg.Color("RED"), hit_rect)
    # ボールを右へ自動移動
    ball_rect.x += 8
    screen.blit(ball_img,ball_rect)
    # ボールが人に当たったらゲームオーバー
    if ball_rect.x > 600 :
        page = 2
        ball_rect = pg.Rect(0,450,30,30)
    # ボタンを押すタイミングを調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        #もしボタンを押したとき、
        if btn1.collidepoint(mx, my) and pushFlag == False:
            # ボールがヒットエリアにあったら成功
            if hit_rect.colliderect(ball_rect):
                page = 3
            else : #ヒットエリアの外なら失敗
                page = 2
            pushFlag = True
            ball_rect = pg.Rect(0,450,30,30)
    else :
        pushFlag = False
#------------------------------------------------------------^^^
        

def page2():
    # 3.画面を初期化する
    screen.blit(img2, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)
    
def page3():
    # 3.画面を初期化する
    screen.blit(img4, (0,0))
    btn1 = screen.blit(next_img,(600, 540))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)
    
page = 1
# 2.この下をずっとループする
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    elif page == 3:
        page3()
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()