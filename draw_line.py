"""
File: 
Name: Bill
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE =10
window = GWindow()
click_memory = None

def main():

    onmouseclicked(draw_line)


def draw_line(event):
    global click_memory
    if click_memory is None:
        hole = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        hole.filled = False
        window.add(hole)
        click_memory = hole
    else:
        # 步驟 A: 取得起點 (從剛剛存下來的 click_memory 拿座標)
        x1 = click_memory.x
        y1 = click_memory.y

        # 步驟 B: 畫線 (GLine 需要四個參數: x0, y0, x1, y1)
        # 起點是 x1, y1; 終點是現在滑鼠的位置 event.x, event.y
        line = GLine(x1, y1, event.x, event.y)
        window.add(line)

        # 步驟 C: 移除舊的圓球
        window.remove(click_memory)
        # 步驟 d: 清空click_memory
        click_memory = None


if __name__ == "__main__":
    main()
