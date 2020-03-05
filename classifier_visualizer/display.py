import tkinter as tk

class Display(tk.Frame):

    def __init__(self, master, w=500, h=500):
        super().__init__(master, highlightbackground="black", highlightcolor="red", highlightthickness=1, width=w, height=h, bd= 0)
        self.master = master
        self.width = w
        self.height = h
        self.canvas = tk.Canvas(self, width=w, height=h)
        self.canvas.bind("<Button-1>",  self.left_click_callback)
        self.canvas.bind("<Button-3>", self.right_click_callback)
        self.canvas.pack()
        #self.grid = Grid(50,50, width, height)

    def draw_point(self, x, y, width, color): self.canvas.create_oval(x-1, y-1, x+1, y+1, width=width, outline= "red" if color else "blue")

    def left_click_callback(self, e):
        self.master.generate_points_at(e.x, e.y, 0)


    def right_click_callback(self, e):
        self.master.generate_points_at(e.x, e.y, 1)