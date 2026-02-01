"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = 0
    dy = 0
    lives = NUM_LIVES
    num_bricks = graphics.brick_rows * graphics.brick_cols


    # Add the animation loop here!
    while True:
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()

        graphics.ball.move(dx, dy)

        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy
        if graphics.ball.y >= graphics.window.height - graphics.ball.width:
            lives -= 1
            # 通知圖形介面更新文字
            graphics.set_lives(lives)
            if lives == 0:
                graphics.draw_end_message("You Lose!")
                break
            else:
                graphics.reset_ball()
                # 這樣下一圈迴圈才會進入「等待模式」(if dx == 0 ...)
                dx = 0
                dy = 0

        obj = None
        r =  graphics.ball_radius
        ball_x = graphics.ball.x
        ball_y = graphics.ball.y

        if obj is None:
            obj = graphics.window.get_object_at(ball_x, ball_y)
        if obj is None:
            obj = graphics.window.get_object_at(ball_x + 2*r, ball_y)
        if obj is None:
            obj = graphics.window.get_object_at(ball_x + 2*r, ball_y + 2*r)
        if obj is None:
            obj = graphics.window.get_object_at(ball_x, ball_y + 2*r)
        if obj is not None:
            if obj is graphics.paddle:
                if dy > 0:
                    dy = -dy
            else:
                if obj is not graphics.lives_label:
                    dy = -dy
                    graphics.window.remove(obj)
                    num_bricks -=1
                    if num_bricks == 0:
                        graphics.draw_end_message("You Win!")

                        break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
