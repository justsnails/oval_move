import tkinter as tk

# 創造視窗
root = tk.Tk()
root.title('Oval Move')
root.geometry('600x600')

# 創造畫布
canvas = tk.Canvas(root, width = 600, height = 600, bg = 'white')
canvas.place(x = 0, y = 0)

x = 300
y = 300

# 設定圓形: 中心點在 (300, 300) 半徑為 25  fill 內部著色   width 線條寬度
# 使用bind 連結 「事件名」以及「想執行的函式」 canvas.bind(事件名,函示名) 
# 若要指定事件名 < 按鍵修飾 - 事件 - 種類 >  
# < Button - 1 >   Button : 按下滑鼠    1: 滑鼠左鍵
def click(event):
    global x, y
    r = 20
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = 'white', width = 0)
    x = event.x # 存取點擊的位置x
    y = event.y # 存取點擊的位置y
    canvas.create_oval(x - r, y - r, x + r, y + r, fill = 'red', width = 0)



canvas.bind('<Button - 1>', click) # click 自行設定



root.mainloop()