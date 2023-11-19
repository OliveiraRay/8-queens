from .environment import *
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Agente:
    def __init__(self, espaco):
        self.espaco = espaco
        self.spaces = []
        
    def search_pos(self, node=0, start_vertice=0):
        vertices_linha = [i for i in self.espaco.vertices if i.x_pos==node]
        for vertice in vertices_linha[start_vertice:]:
            if vertice.visitado == True:
                pass
            else:
                clear_screen()
                vertice.set_element(new_element='Q')
                self.queen_atack_pos(vertice_queen=vertice)
                self.espaco.print_space()
                time.sleep(0.5)
        if node < self.espaco.shape_x:
            self.search_pos(node=node+1)
        else:
            if len([i for i in self.espaco.vertices if i.elemento=='Q']) == 4:
                self.spaces.append(self.espaco)
            for i in self.espaco.vertices:
                if i.elemento == 'Q':
                    i.elemento = ' '
                if i.visitado == True:
                    i.visitado = False
    def queen_atack_pos(self, vertice_queen):
        x_pos = [i for i in self.espaco.vertices if i.x_pos == vertice_queen.x_pos]
        y_pos = [i for i in self.espaco.vertices if i.y_pos == vertice_queen.y_pos]
        diago = []
        for shape in range(0, self.espaco.shape_x):
            diago_new = [i for i in self.espaco.vertices if (i.x_pos == vertice_queen.x_pos+shape) and (i.y_pos == vertice_queen.y_pos+shape)]
            try:
                diago.append(diago_new[0])
            except:
                pass
            
        for i in x_pos:
            i.visitado = True
        for i in y_pos:
            i.visitado = True
        for i in diago:
            i.visitado = True
            
    def load_results(self):
        for shape in range(0, self.espaco.shape_x):
            self.search_pos(node=0, start_vertice=shape)
        print(f'solutions found: {len(self.spaces)}')
            
            