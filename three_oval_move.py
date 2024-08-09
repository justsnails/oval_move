import tkinter as tk

# 創造視窗
root = tk.Tk()
root.title('Oval Move')
root.geometry('600x600')

# 創造畫布
canvas = tk.Canvas(root, width = 600, height = 600, bg = 'white')
canvas.place(x = 0, y = 0)

# 設定清單放入字典 : 用來存放圓形的資料
balls = [{'x': 300, 'y': 300, 'dx': 5, 'dy': 3, 'color': 'red'}, {'x': 200, 'y': 200, 'dx': 6, 'dy': -3, 'color': 'blue'}, {'x': 100, 'y': 100, 'dx': 4, 'dy': 6, 'color': 'green'}]
x = 300
y = 300

r = 20 # 圓形半徑

def move():
    global  x, y, r, balls
    for b in balls:
        canvas.create_oval(b['x'] - r, b['y'] - r, b['x'] + r, b['y'] + r, fill = 'white', width = 0) # 設定圓形: 中心點在 (300, 300) 半徑為 25  fill 內部著色   width 線條寬度
        b['x'] += b['dx'] # x軸移動速度
        b['y'] += b['dy'] # y軸移動速度
        canvas.create_oval(b['x'] - r, b['y'] - r, b['x'] + r, b['y'] + r, fill = b['color'], width = 0)
        
        if b['x'] >= canvas.winfo_width() - r: # 超過右邊界。 winfo_width() 取得畫布寬度
            b['dx'] = -b['dx']
        elif b['x'] <= r:
            b['dx'] = -b['dx'] # 超過左邊界 內部的值變成負的 所以是 -(-5) = 5
        if b['y'] >= canvas.winfo_height() - r: # 超過下邊界。 winfo_height() 取得畫布高度
            b['dy'] = -b['dy']
        elif b['y'] <= r:
            b['dy'] = -b['dy'] # 超過上邊界 內部的值變成負的 所以是 -(-3) = 3

    root.after(10, move) # 0.01秒之後再次執行 move 函式

root.after(10, move) # 0.01秒之後執行 move 函式


root.mainloop()