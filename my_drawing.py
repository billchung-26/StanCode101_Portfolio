"""
File: 
Name: Bill
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def main():
    """
    Title: 神奇寶貝中的地鼠！
    """
    window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    # 1. Body

    body = GOval(100, 160)
    body.filled = True
    body.fill_color = 'sienna'
    body.color = 'sienna' #邊框
    window.add(body, x=(window.width - body.width) / 2, y=(window.height - body.height) / 2)

    # 2. Eyes
    # Hint: 眼睛是兩個黑色的小長橢圓
    # Eye Left

    l_eye = GOval (10,25)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye, x=175, y = 150)

    r_eye = GOval(10, 25)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye, x=215, y=150)

    # 3. Nose
    nose = GOval(40, 20)
    nose.filled = True
    nose.fill_color = 'hotpink'
    nose.color = 'hotpink'
    window.add(nose, x=180, y=185)

    # 4. Ground/Shadow
    shadow = GOval(200, 70)
    shadow.filled = True
    shadow.fill_color = 'darkgray'
    shadow.color = 'darkgray'
    # 算出置中的 X: (400 - 120) / 2 = 140
    # Y 設在 270，剛好蓋住身體底部
    window.add(shadow, x=100, y=230)
    # 5. label
    label = GLabel('Diglett ver 1.0')
    label.font = '-20'
    window.add(label, x=250, y=380)
"""
Title: Diglett ver 1.0
用簡單的四個橢圓形，畫出神奇寶貝的三地鼠。參考了原版的顏色，也發現原來原版的神奇寶貝，雖然百分百難以達成，但要做的7-80%像並不難！
"""

if __name__ == '__main__':
    main()
