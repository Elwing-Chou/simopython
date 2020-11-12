import tkinter as tk

def bmi():
    global e1, e2, result
    w, h = float(e1.get()), float(e2.get())
    b = w / (h / 100) ** 2
    result["text"] = str(b)

window = tk.Tk()
window.geometry("500x500+250+250")

f1 = tk.Frame(window)
f1.pack()

l1 = tk.Label(f1, text="輸入體重:")
l1.pack()
e1 = tk.Entry(f1)
e1.pack()
l2 = tk.Label(f1, text="輸入身高:")
l2.pack()
e2 = tk.Entry(f1)
e2.pack()
b1 = tk.Button(f1, text="計算", command=bmi)
b1.pack()
result = tk.Label(f1, text="結果")
result.pack()

window.mainloop()