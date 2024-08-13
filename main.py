import tkinter as tk
from gui.main import GUI
from gui.console import SimulationConsole
from gui.controls import SimulationControls
from simulation import Simulation



if __name__ == '__main__':
    root = tk.Tk("UCSC Lecture Hall Acoustic Simulation")
    controlWindow = tk.Toplevel(root)
    controlWindow.title("Simulation Controls")
    SimulationConsole(controlWindow)
    simulation = Simulation()
    gui = GUI(root,simulation)
    SimulationControls(controlWindow,simulation,gui)
    
    tk.mainloop()
