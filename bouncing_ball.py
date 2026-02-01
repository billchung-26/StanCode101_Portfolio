"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
is_running = False #程式的開關
bounce_counter = 0


def main():
    global is_running # 先宣告這個開關避免被認為是local 變數
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)

    onmouseclicked(start_game) #開關打開

    VY = 0 # 宣告vy的速度
    while True:
        if is_running:
            VY += GRAVITY
            ball.move(VX, VY)

            # 地板反彈
            if ball.y + SIZE >= window.height:
                VY = -VY * REDUCE
                ball.y = window.height - SIZE
            # 超出右邊界，重新設定x, y 的位置以及vy的速度，同時把開關關上
            if ball.x + SIZE >= window.width:
                ball.x = START_X
                ball.y = START_Y
                VY = 0
                is_running = False

        pause(DELAY)


def start_game(mouse):

    global is_running # 告訴 Python 我們要改外面那個變數
    global bounce_counter

    if not is_running and bounce_counter < 3:
        bounce_counter +=1
        is_running = True


if __name__ == "__main__":
    main()
