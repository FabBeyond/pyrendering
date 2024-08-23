import tkinter as tk

class Renderer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Renderer")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.focalLength = 1000
        
    def renderGameObject(self, blockData):
        type, x, y, z, size, color, attributes = blockData
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
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7]
            ]

        for vertex in vertecies:
            xProj = (self.focalLength*vertex[0])/(self.focalLength+vertex[2])
            yProj = (self.focalLength*vertex[1])/(self.focalLength+vertex[2])
            proj_list.append([xProj, yProj])
        
        for index in indices:
            self.canvas.create_polygon(proj_list[index[0]][0], proj_list[index[0]][1], proj_list[index[1]][0], proj_list[index[1]][1], proj_list[index[2]][0],
                                       proj_list[index[2]][1], proj_list[index[3]][0], proj_list[index[3]][1], fill=color)
    
    def render(self):
        self.canvas.update()
        self.canvas.delete("all")

class GameObject():
    def __init__(self, type="cube", x=0, y=0, z=0, size=100, color="black", **attributes):
        self.type = type
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.color = color
        self.attributes = attributes
    def data(self):
        return [self.type, self.x, self.y, self.z, self.size, self.color, self.attributes]

if __name__ == "__main__":
    renderer = Renderer()
    block = GameObject("cube", 500, 500, 0, 100, "black").data()
    while True:
        renderer.renderGameObject(block)
        renderer.render()