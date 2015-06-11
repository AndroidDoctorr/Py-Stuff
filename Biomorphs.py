from tkinter import Tk, Canvas, Frame, BOTH
import random
import math

global bio1, bio2, bio3, bio4, bio5, bio6, bio7, bio8, bio9 #The Biomorphs
global bgenes, CoM, ShM, RoM, SpM, LnM                      #Base genes, mutation rates
b_d = 5                                                     #Branch depth, i.e. # of genes (x4+1)

class Biomorph(Frame):
    def __init__(self,parent,x,y):
        self.parent = parent
        self.x=x
        self.y=y
        Frame.__init__(self,parent)
        self.grow()
        #Each generation, each biomorph redraws itself based on its genes
        
    def grow(self):
        #Create empty list of genes, populate with new genes based on the base genes +/- some
        #amount of mutation
        genes = []
        for i in range(b_d):
            colr=-1
            colg=-1
            colb=-1
            while not((0<colr<256) and (0<colg<256) and (0<colg<256)):
                colr = bgenes[i*4][0]+random.randint(-CoM,CoM)
                colg = bgenes[i*4][1]+random.randint(-CoM,CoM)
                colb = bgenes[i*4][2]+random.randint(-CoM,CoM)
            genes += ['#'+'%02x'%colr+'%02x'%colg+'%02x'%colb]      #Color genes
            genes += [bgenes[4*i+1]+random.randint(-RoM,RoM)]       #Rotation angle genes
            genes += [bgenes[4*i+2]+random.randint(-SpM,SpM)]       #Separation angle genes
            genes += [bgenes[4*i+3]+random.randint(-LnM,LnM)]       #Length genes

        self.genes = genes

        #TURN THIS INTO A RECURSIVE ALGORITHM!!!!!
        #create a list of coordinates? lists within lists?  [[x,y],[[b1x,b1y],[b2x,b2y]],[[[b1ax,b1ay],[b1bx,b1by]],[[b2ax...
        #def branch(self):

        #Trunk (rotation angle, separation angle ignored - automatically set to 0 and 0???)
        
        self.body=[canvas.create_line(self.x,self.y,self.x,self.y+genes[3],fill=genes[0])]
        self.y = self.y + genes[3]

        #Branch layer 1 (rotation angle ignored, or set to 0)
        
        br1x=self.x+genes[7]*math.sin(genes[6]/360*math.pi)
        br1y=self.y+genes[7]*math.cos(genes[6]/360*math.pi)
        self.body+=[canvas.create_line(self.x,self.y,br1x,br1y,fill=genes[4])]
        br2x=self.x+genes[7]*-math.sin(genes[6]/360*math.pi)
        br2y=self.y+genes[7]*math.cos(genes[6]/360*math.pi)
        self.body+=[canvas.create_line(self.x,self.y,br2x,br2y,fill=genes[4])]

        #Branch layer 2 (INCLUDE ROTATION ANGLE)

        br1ax=br1x+genes[11]*math.sin(genes[10]/360*math.pi)*math.sin(genes[9]/360*math.pi)
        br1ay=br1y+genes[11]*math.cos(genes[10]/360*math.pi)*math.cos(genes[9]/360*math.pi)
        self.body+=[canvas.create_line(br1x,br1y,br1ax,br1ay,fill=genes[8])]
        br1bx=br1x+genes[11]*-math.sin(genes[10]/360*math.pi)*math.sin(genes[9]/360*math.pi)
        br1by=br1y+genes[11]*math.cos(genes[10]/360*math.pi)*math.cos(genes[9]/360*math.pi)
        self.body+=[canvas.create_line(br1x,br1y,br1bx,br1by,fill=genes[8])]

        br2ax=br2x+genes[11]*math.sin(genes[10]/360*math.pi)*math.sin(-genes[9]/360*math.pi)
        br2ay=br2y+genes[11]*math.cos(genes[10]/360*math.pi)*math.cos(-genes[9]/360*math.pi)
        self.body+=[canvas.create_line(br2x,br2y,br2ax,br2ay,fill=genes[8])]
        br2bx=br2x+genes[11]*-math.sin(genes[10]/360*math.pi)*math.sin(-genes[9]/360*math.pi)
        br2by=br2y+genes[11]*math.cos(genes[10]/360*math.pi)*math.cos(-genes[9]/360*math.pi)
        self.body+=[canvas.create_line(br2x,br2y,br2bx,br2by,fill=genes[8])]

        #Branch layer 3   
        
        

def loadgenes(bio):
    #Genes of selected biomorph become base genes for next generation
    bgenes = bio.genes
    for i in range(b_d):
        color=bgenes[i*4]
        bgenes[i*4]=[]
        bgenes[i*4]+=[int(color[1:3],base=16)]
        bgenes[i*4]+=[int(color[3:5],base=16)]
        bgenes[i*4]+=[int(color[5:7],base=16)]

def key(event):
    #Refresh biomorphs when one is selected by key
    biokey = event.keysym
    loadgenes(eval('bio'+str(biokey)))
    refresh()

def click(event):
    #Refresh biomorphs when one is clicked
    if 50<event.y<150:
        if 50<event.x<150:
            loadgenes(bio1)
        elif 150<event.x<250:
            loadgenes(bio2)
        elif 250<event.x<350:
            loadgenes(bio3)
    elif 150<event.y<250:
        if 50<event.x<150:
            loadgenes(bio4)
        elif 150<event.x<250:
            loadgenes(bio5)
        elif 250<event.x<350:
            loadgenes(bio6)
    elif 250<event.y<350:
        if 50<event.x<150:
            loadgenes(bio7)
        elif 150<event.x<250:
            loadgenes(bio8)
        elif 250<event.x<350:
            loadgenes(bio9)
    refresh()

def refresh():
    global bio1, bio2, bio3, bio4, bio5, bio6, bio7, bio8, bio9 #I thought these were already global...
    for i in range(7):                  #This 7 - Create a variable that calculates the # of objects in the body!!!!!
        #Kill all the old biomorphs
        canvas.delete(bio1.body[i])     
        canvas.delete(bio1.body[i])
        canvas.delete(bio2.body[i])
        canvas.delete(bio3.body[i])
        canvas.delete(bio4.body[i])
        canvas.delete(bio5.body[i])
        canvas.delete(bio6.body[i])
        canvas.delete(bio7.body[i])
        canvas.delete(bio8.body[i])
        canvas.delete(bio9.body[i])
    #Generate a new generation of biomorphs
    bio1 = Biomorph(root,100,100)       
    bio2 = Biomorph(root,200,100)
    bio3 = Biomorph(root,300,100)
    bio4 = Biomorph(root,100,200)
    bio5 = Biomorph(root,200,200)
    bio6 = Biomorph(root,300,200)
    bio7 = Biomorph(root,100,300)
    bio8 = Biomorph(root,200,300)
    bio9 = Biomorph(root,300,300)

#---End Definitions/Begin Script---#

#Base gene ranges, mutation rates    
CoB = 100
ShB = 100
RoB = 120
SpB = 120
LnB = 20
CoM = 10
ShM = 5
RoM = 2
SpM = 2
LnM = 3

#Create base genes
bgenes=[]
for i in range(b_d):
    bgenes += [[random.randint(0,255),random.randint(0,255),random.randint(0,255)]]
    bgenes += [random.randint(-RoB,RoB)]
    bgenes += [random.randint(-SpB,SpB)]
    bgenes += [random.randint(-LnB,LnB)]

#GUI
root = Tk()
root.geometry('400x400')
root.title('Biomorphs')
root.resizable(0,0)


canvas = Canvas(root)
canvas.create_rectangle(50,50,150,150, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(150,50,250,150, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(250,50,350,150, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(50,150,150,250, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(150,150,250,250, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(250,150,350,250, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(50,250,150,350, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(150,250,250,350, outline='#000000', fill='#aaaaaa')
canvas.create_rectangle(250,250,350,350, outline='#000000', fill='#aaaaaa')
        
canvas.pack(fill=BOTH, expand=1)

#Create generation 1 of biomorphs
bio1 = Biomorph(root,100,100)
bio2 = Biomorph(root,200,100)
bio3 = Biomorph(root,300,100)
bio4 = Biomorph(root,100,200)
bio5 = Biomorph(root,200,200)
bio6 = Biomorph(root,300,200)
bio7 = Biomorph(root,100,300)
bio8 = Biomorph(root,200,300)
bio9 = Biomorph(root,300,300)

#Key bindings
root.bind('<Button-1>', click)
root.bind('<Key-1>', key)
root.bind('<Key-2>', key)
root.bind('<Key-3>', key)
root.bind('<Key-4>', key)
root.bind('<Key-5>', key)
root.bind('<Key-6>', key)
root.bind('<Key-7>', key)
root.bind('<Key-8>', key)
root.bind('<Key-9>', key)
