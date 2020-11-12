import tkinter as tk

class MyFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="BMI")
        self.l1 = tk.Label(self, text="輸入體重:")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.e1 = tk.Entry(self)
        self.e1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.l2 = tk.Label(self, text="輸入身高:")
        self.l2.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.e2 = tk.Entry(self)
        self.e2.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.b1 = tk.Button(self, text="計算", command=self.bmi)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.result = tk.Label(self, text="結果")
        self.result.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def bmi(self):
        w, h = float(self.e1.get()), float(self.e2.get())
        b = w / (h / 100) ** 2
        self.result["text"] = str(b)


window = tk.Tk()
window.geometry("500x500+250+250")

f1 = MyFrame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

window.mainloop()