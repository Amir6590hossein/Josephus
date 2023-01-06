#Gui
import tkinter as tk
from MyCanvus import Paint

class Gui:
    
 Input_frame=tk.Tk()
 Input_frame.geometry("1200x800")
 Input_frame.title("Input_Frame")
    
 Input_frame["bg"]="black"
 
 def Button(self,N,K):


        
        c=Paint(int(N),int(K))



 def first_frame(self):

    Josephus_lable=tk.Label(self.Input_frame,text="Josephus Problem",font=('calibre',35, 'bold'),fg="White",bg="black").place(x=360,y=180)
    guidance_Lable=tk.Label(self.Input_frame,text="guidance: \n N:Number of people \n K:number of people we pass at every step.",font=('calibre',10, 'bold')).place(x=430,y=250)
    N_lable = tk.Label(self.Input_frame, text = 'N:', font=('calibre',10, 'bold')).place(x=480,y=330)
    N = tk.Entry(self.Input_frame, font=('calibre',10,'normal'))
    N.place(x=500,y=330)
    K_lable=tk.Label(self.Input_frame,text="K:",font=('calibre',10, 'bold')).place(x=480,y=355)
    K = tk.Entry(self.Input_frame, font=('calibre',10,'normal'))
    K.place(x=500,y=355)


    
    btn = tk.Button(self.Input_frame, text = 'Solve Josephus Problem ', bd = '5',command =lambda : self.Button(N.get(),K.get())).place(x=490,y=380)
    self.Input_frame.mainloop()
 
 

# e=Gui()
# e.first_frame()
    # def Button():
    #     nonlocal N
    #     nonlocal K
        
    #     c=Paint(int(N.get()),int(K.get()))
    #     c.Show_Josephus() 