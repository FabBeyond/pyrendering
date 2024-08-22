import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Renderer")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        
    def renderCube(self, cameraPos, blockData):
        x, y, z, size, color = blockData
        self.canvas.create_rectangle(x-size/2, y-size/2, x+size/2, y+size/2, fill="black")
    
    def render(self):
        self.canvas.update()
        self.canvas.delete("all")
        
        

if __name__ == "__main__":
    renderer = Renderer()
    while True:
        renderer.renderCube([0, 0, 0], [0, 0, 0, 100, "black"])
        renderer.render()