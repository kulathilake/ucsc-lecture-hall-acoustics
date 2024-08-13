import matplotlib.pyplot as plt
import pyroomacoustics as pra
import numpy as np
from room_coordinates import s104

class Simulation:
    def __init__(self):
       self.room:pra.Room = None
       self.room, self.corners = self.create_room()
       self.source = None
       self.recievers = []

    def create_room(self, corners = s104):
        room = pra.Room.from_corners(corners.T)
        print("SIMUL: room created with corners", corners.tolist())
        return [room,corners]
    
    def plot_room(self):
        self.room.plot()
        plt.show()

    def reset_sim_state(self):
        self.source = []
        self.recievers = []
        self.room = self.create_room()[0]

    def add_source(self,x,y):
        self.source = {x,y}
        self.room.add_source([x,y])
        print(f"SIMUL: source added at {x:.2f}, {y:.2f}")
    
    def add_reciever(self,x,y):
        self.recievers.append([x,y])
        print(f"SIMUL: reciever added at {x:.2f}, {y:.2f}")
    
    def simulate(self):
        print("SIMUL: begin simulation")
        try:
            if(self.room.mic_array == None):
                self.room.add_microphone_array(pra.MicrophoneArray(np.transpose(self.recievers),fs=self.room.fs))
            self.room.compute_rir()
            self.room.plot_rir()
            plt.show()
        except Exception as e:
            print("SIMUL_ERR: failed to run simulation")
            print("--->",e)
