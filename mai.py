import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('LOVE YOU')
    window.geometry("220x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
    text='Tôi nhớ bạn!',
    bg='pink',
    font=('usual scenario',18),
    width=25,height=4
    ).pack()
    window.mainloop()

threads =[]
for i in range(100):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    threads[i].start()