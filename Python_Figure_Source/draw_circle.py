from turtle import *    #図形を描くツールを呼び出す

#circle関数をつくる
#円の描画はrangeとleftの積が360のなればよい
def circle():
    for count in range(36):
        forward(20)     #20前に描画カーソルを進める、円の大きさを決める
        left(10)    #10度左に傾ける

for cnt in range(10):
    circle()    #関数を呼び出す
    left(36)    #36度左に傾ける

input('type to exit')