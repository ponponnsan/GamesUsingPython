# 1.ゲームの準備をする
import pygame as pg, sys
import random #randomをインポート
pg.init()
screen = pg.display.set_mode((800, 600))
## 紙芝居
img1 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/タイトル図.JPG")
img1 = pg.transform.scale(img1, (800, 600))

img2 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/説明文.JPG")
img2 = pg.transform.scale(img2, (800, 600))

img3 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/腹痛.JPG")
img3 = pg.transform.scale(img3, (800, 600))

img4 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/生理痛.JPG")
img4 = pg.transform.scale(img4, (800, 600))

img5 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/パソコン.JPG")
img5 = pg.transform.scale(img5, (800, 600))

img6 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/二日酔い.JPG")
img6 = pg.transform.scale(img6, (800, 600))

img7 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/熱中症.JPG")
img7 = pg.transform.scale(img7, (800, 600))

kaiketujo8 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/解決.JPG")
kaiketujo8 = pg.transform.scale(kaiketujo8, (800, 600))

hijo9 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/非解決.JPG")
hijo9 = pg.transform.scale(hijo9, (800, 600))

kaiketudan10 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/解決 (2).JPG")
kaiketudan10 = pg.transform.scale(kaiketudan10, (800, 600))

hidan11 = pg.image.load("mygame/mygame/images/かけてけていシーン集3/非解決 (2).JPG")
hidan11 = pg.transform.scale(hidan11, (800, 600))



toumei = pg.image.load("mygame/mygame/images/透明1.png")
toumei = pg.transform.scale(toumei, (143 , 130))





## ボタン
next_img = pg.image.load("mygame/mygame/images/nextbtn.png")
replay_img = pg.image.load("mygame/mygame/images/replaybtn.png")


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

def page1():
    # 3.画面を初期化する
    screen.blit(img1, (0,0))
    btn1 = screen.blit(next_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 2)

def page2():
    # 3.画面を初期化する
    screen.blit(img2, (0,0))
    btn1 = screen.blit(next_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    num = random.randint(3,7)
    button_to_jump(btn1, num)

    
    
def page3():
    # 3.画面を初期化する
    screen.blit(img3, (0,0))
    btn1 = screen.blit(toumei,(139, 365))
    btn2 = screen.blit(toumei,(341, 365))
    btn3 = screen.blit(toumei,(544, 365))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 9)
    button_to_jump(btn2, 8)
    button_to_jump(btn3, 9)



def page4():
    # 3.画面を初期化する
    screen.blit(img4, (0,0))
    btn1 = screen.blit(toumei,(146, 365))
    btn2 = screen.blit(toumei,(329, 365))
    btn3 = screen.blit(toumei,(510, 365))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 8)
    button_to_jump(btn2, 9)
    button_to_jump(btn3, 9)


def page5():
    # 3.画面を初期化する
    screen.blit(img5, (0,0))
    btn1 = screen.blit(toumei,(129, 373))
    btn2 = screen.blit(toumei,(335, 373))
    btn3 = screen.blit(toumei,(529, 365))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 9)
    button_to_jump(btn2, 9)
    button_to_jump(btn3, 8)


def page6():
    # 3.画面を初期化する
    screen.blit(img7, (0,0))
    btn1 = screen.blit(toumei,(138, 369))
    btn2 = screen.blit(toumei,(337, 368))
    btn3 = screen.blit(toumei,(550, 367))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 11)
    button_to_jump(btn2, 11)
    button_to_jump(btn3, 10)

def page7():
    # 3.画面を初期化する
    screen.blit(img6, (0,0))
    btn1 = screen.blit(toumei,(144, 369))
    btn2 = screen.blit(toumei,(345, 372))
    btn3 = screen.blit(toumei,(544, 367))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 11)
    button_to_jump(btn2, 10)
    button_to_jump(btn3, 11)

def page8():
    # 3.画面を初期化する
    screen.blit(kaiketujo8 , (0,0))
    btn1 = screen.blit(replay_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

def page9():
    # 3.画面を初期化する
    screen.blit(hijo9, (0,0))
    btn1 = screen.blit(replay_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

def page10():
    # 3.画面を初期化する
    screen.blit(kaiketudan10, (0,0))
    btn1 = screen.blit(replay_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

def page11():
    # 3.画面を初期化する
    screen.blit(hidan11, (0,0))
    btn1 = screen.blit(replay_img,(600, 550))
    # 5.絵を描いたり、判定したりする
    button_to_jump(btn1, 1)




page = 1
### 2.この下をずっとループする
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    elif page == 3:
        page3()
    elif page == 4:
        page4()
    elif page == 5:
        page5()
    elif page == 6:
        page6()
    elif page == 7:
        page7()
    elif page == 8:
        page8()
    elif page == 9:
        page9()
    elif page == 10:
        page10()
    elif page == 11:
        page11()

    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
