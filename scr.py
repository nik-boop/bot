from pyautogui import *
from PIL import Image
from random import randint, choices
import keyboard

def serch(img, fun=None, args = None, f = 0):
    '''imj fun args->[] f=0'''
    loc = None
    while loc is None:
        loc = locateCenterOnScreen(img, region=(276, 245, 491, 945), grayscale=False)
    if f == 1:
        if fun is not None:
            if args is not None:
                fun(loc, *args)
            else:
                fun(loc)
    else:
        if fun is not None:
            if args is not None:
                fun(loc, *args)
            else:
                fun(loc)

def pr(var):
    keyboard.write(str(var))
def cloc(loc):
    moveTo(loc)
    click()


op1 = Image.open('imj/1/img.png')
img1 = [Image.open('imj/1/img_1.png'), Image.open('imj/1/img_2.png'),
        Image.open('imj/1/img_3.png'), Image.open('imj/1/img_4.png'),
        Image.open('imj/1/img_5.png'), Image.open('imj/1/img_6.png')
        ]
img2 = [Image.open('imj/2/img_1.png'), Image.open('imj/2/img_2.png'),
        Image.open('imj/2/img_3.png'), Image.open('imj/2/img_4.png'),
        Image.open('imj/2/img_5.png'), Image.open('imj/2/img_6.png')
        ]
op3 = Image.open('imj/3/img_0.png')
op4 = Image.open('imj/4/img_8.png')
img5 = [Image.open('imj/5/img_9.png'), Image.open('imj/5/img.png'),
        Image.open('imj/5/img_10.png'), Image.open('imj/5/img_11.png'),
        Image.open('imj/5/img_12.png')
        ]
img6 = [Image.open('imj/6/img.png'), Image.open('imj/6/img_1.png')]
end = Image.open('imj/end/img.png')
eres = Image.open('imj/eras/img.png')
k = 1
while k <= 123:
    i1 = choices([1,2,3,4,5,6], weights=[35,16,28,1,2,13])[0]

    i2o = choices([1,2,3,4,5,6], weights=[5,14,7,16,19,39])[0]
    if i2o == 6:
        i2 = choices([1,2,3,4,5], weights=[5,14,7,16,19])[0]
    else:
        i2 = i2o

    d3 = {1: choices([6,7,8,9,10], weights=[10,14,32,25,20])[0],
          2: choices([6,7,8,9,10], weights=[7,10,26,38,22])[0],
          3: choices([7,8,9,10,11,12], weights=[7,10,26,28,22,10])[0],
          4: choices([8,9,10,11,12,13,14], weights=[6,9,10,28,30,13,10])[0],
          5: choices([8,9,10,11,12,13,14,15], weights=[1,4,10,22,23,21,15,6])[0]}
    i3 = d3[i2]
    if i2 < 2:
        i4 = choices([1,2], weights=[40,60])[0]
    elif 2 <= i2 and i2<4:
        i4 = choices([1,2], weights=[65,35])[0]
    elif i2 >= 4:
        i4 = choices([1,2], weights=[85,15])[0]

    dsc = {1: 8, 2: 9, 3: 11, 4: 13, 5: 14}
    ver = i3 / dsc[i2] + randint(-5, 5) / 100

    if ver > 1:
        if i4 > 1:
            ver *= 0.85

    i51 = round(ver * 100)
    if round((i51%10)/10):
        i51 += (10-i51%10)
    else:
        i51 -= (i51 % 10)
    i52 = randint(93, 100)
    if round((i52%10)/10):
        i52 += (10-i52%10)
    else:
        i52 -= (i52 % 10)
    if i4 > 1:
        i6 = choices([1, 2], weights=[65, 35])[0]
    else:
        i6 = 0

    if i6 == 0:
        i6=1
    else:
        i6=0

    if i52>100:
        i52 = 100
    if i51>100:
        i51 = 100

    if i51>50 and i51 < 70:
        i51 = 70
    if i51<50:
        i51 = 50

    d5 = {5:5,7:4,8:3,9:2,10:1}

    print(f'marc:{i1} em:{i2} tim:{i3} col:{i4} arz:{i51}-{i52} pb:{i6}')
    k += 1
    serch(op1,click,f=1)
    serch(img1[i1-1],click,f=1)
    serch(img2[i2o-1],click,f=1)
    serch(op3, click, f=1)
    pr(i3)
    serch(op4, click, f=1)
    pr(i4)
    if i51!=i52:
        serch(img5[d5[i51//10]-1], click, f=1)
        serch(img5[d5[i52//10]-1], click, f=1)
    else:
        serch(img5[d5[i51 // 10]-1], click, f=1)
    serch(img6[i6], click, f=1)
    serch(end, click, f=1)
    serch(eres, click, f=1)

