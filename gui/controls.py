import tkinter as tk
from gui.main import GUI
from simulation import Simulation

BUTTON_Y_PAD = 5
class SimulationControls:
    def __init__(self,root,simulation, main:GUI) -> None:
       control_frame = tk.Frame(root)
       control_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
       self.__create_add_lecturer_btn(control_frame, main)
       self.__create_add_student_btn(control_frame, main)
       self.__create_reset_canvas_btn(control_frame, main)
       self.__create_simulate_btn(control_frame, simulation)
       self.__create_plot_btn(control_frame, simulation)


    def __create_add_lecturer_btn(self, root, main: GUI):
        btn = tk.Button(root, text="Add Lecturer", command= main.switch_to_add_lecturer_mode)
        btn.pack(pady=BUTTON_Y_PAD, expand=True)

    def __create_add_student_btn(self, root, main: GUI):
        btn = tk.Button(root, text="Add Student", command=main.switch_to_add_student_mode)
        btn.pack(pady=BUTTON_Y_PAD, expand=True)
    
    def __create_reset_canvas_btn(self, root, main:GUI):
        add_source_btn = tk.Button(root, text="Clear Room", command=main.clear_canvas)
        add_source_btn.pack(pady=BUTTON_Y_PAD, expand=True)
    
    def __create_simulate_btn(self, root, simulation: Simulation):
        btn = tk.Button(root, text="Simulate", command=simulation.simulate)
        btn.pack(pady=BUTTON_Y_PAD, expand=True)
    def __create_plot_btn(self, root, simulation: Simulation):
        btn = tk.Button(root, text="Plot Room", command=simulation.plot_room)
        btn.pack(pady=BUTTON_Y_PAD, expand=True)