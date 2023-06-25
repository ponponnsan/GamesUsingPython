import pgzrun
import math
 
WIDTH = 640
HEIGHT = 480
TITLE = "ゆらゆらした動き"
 
BG_COLOR = (0, 191, 255)    # 背景色
frame = 0                   # フレーム数カウント用
 
# キャラクタ生成
teki = Actor("teki")
teki.topleft = 0, 200
 
# 起動時の表示
def draw():
    screen.fill(BG_COLOR)
    teki.draw()
 
# フレーム処理
def update():
    global frame
    frame += 1
 
    teki.left += 2  # x方向の動き
    teki.top = teki.top + 4 * math.sin(frame/8);  # y方向の動き
 
    # 右端にいったら左端に戻す
    if teki.left > WIDTH:
        teki.left = 0
 
pgzrun.go()
