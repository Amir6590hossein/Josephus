#Canvus
from LinkedList import CreateList
import tkinter as tk
import math
from playsound import playsound



class Paint:


  def __init__(self,N,K) :
    self.K=K
    self.N=N
    self.circle=CreateList()
    self.ShowFram=tk.Tk()
    # self.ShowFram.title="Josephus"
    self.ShowFram["bg"]="cyan"
    self.myCanvas = tk.Canvas(self.ShowFram, bg="yellow", height=1300, width=1500)
    self.Show_Josephus()
     
  
  

  def XY_to_PolarCoordinates(self,r,o):
    return [r*math.cos(math.radians(o) ),r*math.sin(math.radians(o))]
  
  def Josephus (self,n):
    
    
    if n.next==n :
        
        self.myCanvas.itemconfig(n.data,fill="green")
        playsound("345299__scrampunk__okay.wav")
        return
    else:
     for i in range(self.K-1):
        n=n.next
     self.myCanvas.itemconfig(n.next.data,fill="red")
     playsound("244657__greenvwbeetle__pop-5.mp3")
     n.next=n.next.next
   
     self.myCanvas.after(500,func=lambda : self.Josephus(n.next))
    
  def j(self):
    return self.Josephus(self.circle.head)

  
  def Next_Button(self):
    if self.circle.head.next==self.circle.head :
        self.myCanvas.itemconfig(self.circle.head.data,fill="green")
        playsound("345299__scrampunk__okay.wav")
        return
    else:
     for i in range(self.K-1):
        self.circle.head=self.circle.head.next
     self.myCanvas.itemconfig(self.circle.head.next.data,fill="red")
     playsound("244657__greenvwbeetle__pop-5.mp3")
      
     self.circle.head.next=self.circle.head.next.next
     self.circle.head=self.circle.head.next


  def J2(self):
    self.Next_Button(self.circle.head)
  

  
  
  def Show_Josephus(self):

   deg=360/self.N
   for i in range (self.N):
     X0=320

     X=700+self.XY_to_PolarCoordinates(X0,i*deg)[0]
     Y=370+self.XY_to_PolarCoordinates(X0,i*deg)[1]
     r2=(50/self.N)*20
     f=math.floor((10/self.N)*70)+1
     z=self.myCanvas.create_oval(X,Y+r2,X+2*r2,Y-r2,fill="blue")
     self.circle.add(z) 
     self.myCanvas.create_text(X+r2, Y, text=i+1, fill="White", font=(f'Helvetica {f} bold'))
   btn=tk.Button(self.ShowFram,text="Solve",command=self.j,bg="green",fg="white",font=('calibre',15, 'bold'))
   btn2=tk.Button(self.ShowFram,text="Next Kill",command=self.Next_Button,bg="green",fg="white",font=('calibre',15, 'bold'))
  
   btn.pack(side="top")
   btn2.pack(side= "top")
   
   self.myCanvas.pack()
   self.ShowFram.mainloop()
   
   
# e=Paint(2,2)


