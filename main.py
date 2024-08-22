import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Renderer")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600)

        self.root.mainloop()
    def renderCube(self, data):
        x, y, z, size, color = data
        print(data)


if __name__ == "__main__":
    renderer = Renderer()
    renderer.renderCube([0, 0, 0, 100, "000000"])