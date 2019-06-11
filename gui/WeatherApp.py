import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=.1,relwidth=0.5, relheight=0.5)

button = tk.Button(frame, text="test button", bg='gray', fg='red')
button.grid(row=0, column=0)

label = tk.Label(frame, text='This is a label', bg='yellow')
label.grid(row=0, column=1)

entry = tk.Entry(frame, bg='green')
entry.grid(row=0, column=0)

root.mainloop()
 