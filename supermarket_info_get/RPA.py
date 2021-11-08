import pyautogui as pg
import time
import webbrowser
import pyperclip as pp

url='https://www.aeon.com/store/list/%E9%96%A2%E6%9D%B1%E5%9C%B0%E6%96%B9/%E6%9D%B1%E4%BA%AC%E9%83%BD/?q=aeoncom'

#csvファイル作成
csv=open('testRPA.csv','w')

#brouser起動
webbrowser.open(url)
time.sleep(5)
pg.hotkey('winleft','up')
pg.moveTo(216,850)
pg.scroll(-160)

mouse_b=[660,850,1550,1320,965]
mouse_a=[380,910,1150,910]

for i in range(10):
    #マウスの位置移動してドラッグ、コピー
    pg.moveTo(mouse_b[0],mouse_b[1])
    pg.dragTo(mouse_b[2],mouse_b[1],0.5)
    pg.hotkey('ctrlleft','c')

    #リンク前のもの貼り付け
    csv.write(pp.paste()+",")
    
    #リンクをクリック
    pg.moveTo(mouse_b[3],mouse_b[4])
    pg.click()
    time.sleep(5)
    pg.moveTo(mouse_a[0],mouse_a[1])
    pg.dragTo(mouse_a[2],mouse_a[3],0.5)
    pg.hotkey('ctrlleft','c')
    #リンク後のもの貼り付け、改行
    csv.write(pp.paste()+"\n")

    #リンク前に戻る
    pg.hotkey('altleft','left')
    time.sleep(5)
    pg.scroll(-234)

#csv閉じる
csv.close()