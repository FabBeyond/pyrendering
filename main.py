import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Renderer")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        
    def renderCube(self, focalLength, blockData):
        x, y, z, size, color = blockData
        proj_list = []
        vertecies = [
            [x-size/2, y-size/2, z-size/2],
            [x-size/2, y+size/2, z-size/2],
            [x+size/2, y+size/2, z-size/2],
            [x+size/2, y-size/2, z-size/2],
            [x-size/2, y-size/2, z+size/2],
            [x-size/2, y+size/2, z+size/2],
            [x+size/2, y+size/2, z+size/2],
            [x+size/2, y-size/2, z+size/2]
        ]
        indices = [
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [1, 5], [5, 6], [6, 2], [2, 1],
            [0, 4], [4, 7], [7, 3], [3, 0],
            [0, 1], [1, 5], [5, 4], [4, 0],
            [3, 2], [2, 6], [6, 7], [7, 3]
        ]

        for vertex in vertecies:
            xProj = (focalLength*vertex[0])/(focalLength+vertex[2])
            yProj = (focalLength*vertex[1])/(focalLength+vertex[2])
            proj_list.append([xProj, yProj])
        
        for index in indices:
            self.canvas.create_line(proj_list[index[0]][0], proj_list[index[0]][1], proj_list[index[1]][0], proj_list[index[1]][1])
    
    def render(self):
        self.canvas.update()
        self.canvas.delete("all")
        
if __name__ == "__main__":
    renderer = Renderer()
    idx = 0
    while True:
        renderer.renderCube(1000, [100, 100, 0, 100, "black"])
        renderer.render()
        idx += 1