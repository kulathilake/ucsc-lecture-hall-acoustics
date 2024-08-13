# Graphical Interface for the Simulation
import tkinter as tk
import numpy as np
from simulation import Simulation
import time
CANVAS_W = 950
CANVAS_H = 950
PADDING_W = 0
PADDING_H = 0

class GUI:
    def __init__(self,root,simulation: Simulation):
        self.root = root
        # Canvas
        self.canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="grey")
        self.canvas.pack()
        self.scaleX = 1
        self.scaleY = 1
        # Functional Attributes 
        self.simulation = simulation
        self.receivers = []
        self.last_receiver_id = 0
        self.source = None
        self.clickMode = "Add Lecturer"

        # Lecture Hall label
        self.hall_label = tk.Label(self.canvas, text="Lecture Hall: S10", bg="grey")
        self.hall_label.place(x=0,y=0)
        # Cursor Label
        self.cursor_label = tk.Label(self.canvas, text=self.clickMode, bg="lightblue")
        self.cursor_label.place(x=0,y=0)
        

        # Init Calls
        self.__draw_room()

        # Event Binders
        self.canvas.bind("<Button-1>", self.__on_canvas_click)
        self.canvas.bind('<Motion>', self.__on_mouse_move)

    def clear_canvas(self):
        self.receivers = []
        self.last_receiver_id = 0
        self.source = None
        self.simulation.reset_sim_state()
        self.canvas.delete('all')
        self.__draw_room()
        print("CANVAS: room cleared")

    def switch_to_add_lecturer_mode(self):
        if self.source != None:
            print("CANVS_ERR: Max number of lecturers added")
        else:
            self.clickMode = "Add Lecturer"
            print("CANVAS: switched add mode to 'lecturer'")
    def switch_to_add_student_mode(self):
        self.clickMode = "Add Student"
        print("CANVAS: switched add mode to 'student'")

    # Event Handlers
    def __on_mouse_move(self,event):
        roomX, roomY = self.__transform_canvas_coords_to_room(event.x,event.y)
        self.cursor_label.config(text=f"{self.clickMode} (X:{roomX:2f}m,Y:{roomY:2f})")
        self.cursor_label.place(x=event.x+10, y=event.y+10)

    def __on_canvas_click(self, event):
        x,y = event.x, event.y
        roomX, roomY = self.__transform_canvas_coords_to_room(x,y)
        pointObject = {'x': x, 'y':y, 'roomX': roomX, 'roomY': roomY}
        if self.clickMode == 'Add Student':
            pointObject['id'] = self.last_receiver_id
            self.last_receiver_id += 1
            self.receivers.append(pointObject)
            self.__draw_circle(pointObject,"student")
            self.simulation.add_reciever(roomX,roomY)
            print(f"CANVAS: student added at {x:2f},{y:2f}")
        elif self.source != None:
            print("CANVAS_ERR: Max number of lecturers added")
        else:
            try:
                self.simulation.add_source(roomX,roomY)
                self.source = pointObject
                self.__draw_circle(pointObject,"lecturer")
                print(f"CANVAS: lecturer added at {x:2f},{y:2f}")
                self.switch_to_add_student_mode()
            except Exception as e:
                print(f"CANVAS_ERR: could not add lecturer")
                print("---->",e)

            

    def __on_mouse_drag(self, event):
        pass

    def __on_right_click(self, event):
        pass

    def __transform_coorners(self):
        bbox = self.simulation.room.get_bbox()
        corners = self.simulation.corners
        x_max = bbox[0][1]
        y_max = bbox[1][1]
        x_scale = (CANVAS_W - 2*PADDING_W) / x_max
        y_scale = (CANVAS_H - 2* PADDING_H) / y_max
        self.scaleX = x_scale
        self.scaleY = y_scale
        print(f"CANVAS: Scale Factors: {x_scale:2f},{y_scale:2f}")
        scaled_coordinates = corners * [x_scale, y_scale] + [PADDING_W,PADDING_H]
        return scaled_coordinates
    
    def __transform_canvas_coords_to_room(self,x,y):
        return[x/self.scaleX,y/self.scaleY]
    
    def __draw_room(self):
        corners = self.__transform_coorners()
        self.canvas.create_polygon(corners.flatten().tolist(),fill="white", outline="black")

    def __draw_circle(self,pointObject,type):
        if type == "student":
            color = "red"
            radius = 10
            label = str(pointObject['id'])
        else:
            color = "yellow"
            radius = 20
            label = "Lecturer"
        # bbox = self.simulation.room.get_bbox()
        # xFromMax = bbox[0][1] - pointObject['roomX']
        # yFromMax = bbox[1][1] - pointObject['roomY']
        self.canvas.create_oval(pointObject['x']-radius, pointObject['y']-radius, pointObject['x'] + radius, pointObject['y'] + radius, outline="black", fill=color)
        self.canvas.create_text(pointObject['x'] + radius + 5, pointObject['y'], text=label, anchor=tk.W, font=('Arial', 12), fill='black')


