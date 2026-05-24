import tkinter as tk
import time
import random
class tic_tac_toe:
 def __init__(self):
    self.win_v = None
    self.win_z = None
    self.win = None
    self.canvas = None
    self.center_p = None
    self.left_p = None
    self.ridht_p = None
    self.bottom_p = None
    self.top_p = None
    self.horizon_l_p = None
    self.horizon_r_p = None
    self.horizon_l_b_p = None
    self.horizon_r_b_p = None
    self.check = None
    self.varible = [[0,0,0],[0,0,0],[0,0,0]]
    self.p = None
 def zer(self):
   self.p = 1
   self.zero()
 def cross(self):
   self.p = 2
   self.zero()
 def return_com(self):
    if self.check == None:
       self.win_z.destroy()
    else:
       self.win_v.destroy()
    self.win_v = None
    self.win_z = None
    self.win = None
    self.canvas = None
    self.center_p = None
    self.left_p = None
    self.ridht_p = None
    self.bottom_p = None
    self.top_p = None
    self.horizon_l_p = None
    self.horizon_r_p = None
    self.horizon_l_b_p = None
    self.horizon_r_b_p = None
    self.check = None
    self.p = None
    self.varible = [[0,0,0],[0,0,0],[0,0,0]]
    self.choise()
 def win_com(self):
    if self.check == 1:
      self.win_z.destroy()
      self.win_v = tk.Tk()
      self.win_v.title('Выигрышное окно')
      self.win_v.geometry('300x300+100+100')
      label = tk.Label(self.win_v,text='Вы выиграли',font=('arial',20))
      label.pack(side='top')
      button1 = tk.Button(self.win_v,text='Выйти',width=15,height=1,command=self.win_v.destroy)
      button1.pack()
      button2 = tk.Button(self.win_v,text='Заново',width=15,height=1,command=self.return_com)
      button2.pack()
    elif self.check == 2:
      self.win_z.destroy()
      self.win_v = tk.Tk()
      self.win_v.title('Проиграшное окно')
      self.win_v.geometry('300x300+100+100')
      label = tk.Label(self.win_v,text='Вы проиграли',font=('arial',20))
      label.pack(side='top')
      button1 = tk.Button(self.win_v,text='Выйти',width=15,height=1,command=self.win_v.destroy)
      button1.pack()
      button2 = tk.Button(self.win_v,text='Заново',width=15,height=1,command=self.return_com)
      button2.pack()
 def robot(self):
    total = False
    if self.p == 1:
     while total == False:
      choise = random.randint(1,9)
      if self.check == 1 or self.check == 2:
       total = True
      elif total == False and self.center_p in self.canvas.find_all() and choise == 1:
       self.canvas.create_line(150,100,225,198)
       self.canvas.create_line(225,100,150,198)
       self.varible[1][1] = 2
       self.canvas.delete(self.center_p)
       self.if_com()
       total = True
      elif  total == False and self.left_p in self.canvas.find_all() and choise == 2:
       self.canvas.create_line(100,100,30,200)
       self.canvas.create_line(30,100,100,200)
       self.varible[1][0] = 2
       self.canvas.delete(self.left_p)
       self.if_com()
       total = True
      elif  total == False and self.ridht_p in  self.canvas.find_all() and choise == 3:
       self.canvas.create_line(275,100,340,200)
       self.canvas.create_line(340,100,270,200)
       self.varible[1][2] = 2
       self.canvas.delete(self.ridht_p)
       self.if_com()
       total = True
      elif total == False and self.top_p in  self.canvas.find_all() and choise == 4:
       self.canvas.create_line(150,0,225,100)
       self.canvas.create_line(225,0,150,100)
       self.varible[0][1] = 2
       self.canvas.delete(self.top_p)
       self.if_com()
       total = True
      elif total == False and self.bottom_p in  self.canvas.find_all() and choise == 5:
       self.canvas.create_line(150,200,223,300)
       self.canvas.create_line(225,200,150,300)
       self.varible[2][1] = 2
       self. canvas.delete(self.bottom_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_l_p in  self.canvas.find_all() and choise == 6:
       self. canvas.create_line(30,100,100,0)
       self. canvas.create_line(100,100,30,0)
       self. varible[0][0] = 2
       self. canvas.delete(self.horizon_l_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_r_p in  self.canvas.find_all() and choise == 7:
       self. canvas.create_line(275,100,340,0)
       self. canvas.create_line(340,100,275,0)
       self. varible[0][2] = 2
       self. canvas.delete(self.horizon_r_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_l_b_p in  self.canvas.find_all() and choise == 8:
       self. canvas.create_line(30,200,100,300)
       self. canvas.create_line(100,200,30,300)
       self. varible[2][0] = 2
       self. canvas.delete(self.horizon_l_b_p)
       self.if_com()
       total = True
      elif  total == False and self.horizon_r_b_p in  self.canvas.find_all() and choise == 9:
       self. canvas.create_line(270,200,340,300)
       self. canvas.create_line(340,200,270,300)
       self. varible[2][2] = 2
       self. canvas.delete(self.horizon_r_b_p)
       self.if_com()
       total = True
      elif total == False and 0 not in self.varible[0] and 0 not in self.varible[1] and 0 not in self.varible[2]:
       total = True
    if self.p == 2:
     while total == False:
      choise = random.randint(1,9)
      if self.check == 1 or self.check == 2:
       total = True
      elif total == False and self.center_p in self.canvas.find_all() and choise == 1:
       self.canvas.create_oval(136,105,236,196)
       self.varible[1][1] = 2
       self.canvas.delete(self.center_p)
       self.if_com()
       total = True
      elif  total == False and self.left_p in self.canvas.find_all() and choise == 2:
       self.canvas.create_oval(25,105,120,196)
       self.varible[1][0] = 2
       self.canvas.delete(self.left_p)
       self.if_com()
       total = True
      elif  total == False and self.ridht_p in  self.canvas.find_all() and choise == 3:
       self.canvas.create_oval(254,105,352,196)
       self.varible[1][2] = 2
       self.canvas.delete(self.ridht_p)
       self.if_com()
       total = True
      elif total == False and self.top_p in  self.canvas.find_all() and choise == 4:
       self.canvas.create_oval(136,5,236,96)
       self.varible[0][1] = 2
       self.canvas.delete(self.top_p)
       self.if_com()
       total = True
      elif total == False and self.bottom_p in  self.canvas.find_all() and choise == 5:
       self.canvas.create_oval(133,202,240,295)
       self.varible[2][1] = 2
       self.canvas.delete(self.bottom_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_l_p in  self.canvas.find_all() and choise == 6:
       self.canvas.create_oval(25,5,120,96)
       self. varible[0][0] = 2
       self. canvas.delete(self.horizon_l_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_r_p in  self.canvas.find_all() and choise == 7:
       self.canvas.create_oval(260,5,358,95)
       self. varible[0][2] = 2
       self. canvas.delete(self.horizon_r_p)
       self.if_com()
       total = True
      elif total == False and self.horizon_l_b_p in  self.canvas.find_all() and choise == 8:
       self.canvas.create_oval(118,203,18,294)
       self. varible[2][0] = 2
       self. canvas.delete(self.horizon_l_b_p)
       self.if_com()
       total = True
      elif  total == False and self.horizon_r_b_p in  self.canvas.find_all() and choise == 9:
       self.canvas.create_oval(253,203,352,294)
       self. varible[2][2] = 2
       self. canvas.delete(self.horizon_r_b_p)
       self.if_com()
       total = True
      elif total == False and 0 not in self.varible[0] and 0 not in self.varible[1] and 0 not in self.varible[2]:
       total = True
 def if_com(self): 
  if  self.varible[0][0] == 1 and  self.varible[1][0] == 1 and  self.varible[2][0] == 1:
    self.canvas.create_line(72,0,72,305)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][1] == 1 and  self.varible[1][1] == 1 and  self.varible[2][1] == 1:
    self.canvas.create_line(184,0,184,305)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][2] == 1 and  self.varible[1][2] == 1 and  self.varible[2][2] == 1:
    self. canvas.create_line(307,0,307,305)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][0] == 1 and  self.varible[0][1] == 1 and  self.varible[0][2] == 1:
    self.canvas.create_line(15,50,365,50)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[1][0] == 1 and  self.varible[1][1] == 1 and  self.varible[1][2] == 1:
    self.canvas.create_line(15,148,365,148)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[2][0] == 1 and  self.varible[2][1] == 1 and  self.varible[2][2] == 1:
    self.canvas.create_line(15,245,365,245)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][0] == 1 and  self.varible[1][1] == 1 and  self.varible[2][2] == 1:
    self.canvas.create_line(20,0,365,310)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][2] == 1 and  self.varible[1][1] == 1 and  self.varible[2][0] == 1:
    self.canvas.create_line(360,0,10,288)
    self.canvas.update()
    self.check = 1
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][0] == 2 and  self.varible[1][0] == 2 and  self.varible[2][0] == 2:
    self.canvas.create_line(72,0,72,305)
    self.canvas.update()
    self.check = 2
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][1] == 2 and  self.varible[1][1] == 2 and  self.varible[2][1] == 2:
    self.canvas.create_line(184,0,184,305)
    self.canvas.update()
    self.check = 2
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][2] == 2 and  self.varible[1][2] == 2 and  self.varible[2][2] == 2:
    self.canvas.create_line(307,0,307,305)
    self.canvas.update()
    self.check = 2
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[0][0] == 2 and  self.varible[0][1] == 2 and  self.varible[0][2] == 2:
    self.canvas.create_line(15,50,365,50)
    self.canvas.update()
    self.check = 2
    for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
    time.sleep(1)
    self.win_com()
  elif  self.varible[1][0] == 2 and  self.varible[1][1] == 2 and  self.varible[1][2] == 2:
     self.canvas.create_line(15,148,365,148)
     self.canvas.update()
     self.check = 2
     for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
     time.sleep(1)
     self.win_com()
  elif  self.varible[2][0] == 2 and  self.varible[2][1] == 2 and  self.varible[2][2] == 2:
      self.canvas.create_line(15,245,365,245)
      self.canvas.update()
      self.check = 2
      for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
      time.sleep(1)
      self.win_com()
  elif  self.varible[0][0] == 2 and  self.varible[1][1] == 2 and  self.varible[2][2] == 2:
      self.canvas.create_line(20,0,365,310)
      self.canvas.update()
      self.check = 2
      for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
      time.sleep(1)
      self.win_com()
  elif  self.varible[0][2] == 2 and  self.varible[1][1] == 2 and  self.varible[2][0] == 2:
      self.canvas.create_line(360,0,10,288)
      self.canvas.update()
      self.check = 2
      for x in self.canvas.find_all():
       if self.canvas.type(x) == "window":
         self.canvas.delete(x)
      time.sleep(1)
      self.win_com()
  elif self.check == None and 0 not in self.varible[0] and 0 not in self.varible[1] and 0 not in self.varible[2]:
      self.canvas.create_window(100,350,width=150,height=45,window=tk.Button(self.canvas,text='Выйти',command=self.win_z.destroy))
      self.canvas.create_window(300,350,width=150,height=45,window=tk.Button(self.canvas,text='Заново',command=self.return_com))
 def center(self):
   if self.p == 1:
    self.varible[1][1] = 1
    self.canvas.delete(self.center_p)
    self.canvas.create_oval(136,105,236,196)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[1][1] = 1
    self.canvas.delete(self.center_p)
    self.canvas.create_line(150,100,225,198)
    self.canvas.create_line(225,100,150,198)
    self.if_com()
    self.robot()
 def left(self):
   if self.p == 1:
    self.varible[1][0] = 1
    self.canvas.delete(self.left_p)
    self.canvas.create_oval(25,105,120,196)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[1][0] = 1
    self.canvas.delete(self.left_p)
    self.canvas.create_line(100,100,30,200)
    self.canvas.create_line(30,100,100,200)
    self.if_com()
    self.robot()
 def ridht(self):
   if self.p == 1:
    self.varible[1][2] = 1
    self.canvas.delete(self.ridht_p)
    self.canvas.create_oval(254,105,352,196)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[1][2] = 1
    self.canvas.delete(self.ridht_p)
    self.canvas.create_line(275,100,340,200)
    self.canvas.create_line(340,100,270,200)
    self.if_com()
    self.robot()
 def botomm(self):
   if self.p == 1:
    self.varible[2][1] = 1
    self.canvas.delete(self.bottom_p)
    self.canvas.create_oval(133,202,240,295)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[2][1] = 1
    self.canvas.delete(self.bottom_p)
    self.canvas.create_line(150,200,223,300)
    self.canvas.create_line(225,200,150,300)
    self.if_com()
    self.robot()
 def top(self):
   if self.p == 1:
    self.varible[0][1] = 1
    self.canvas.delete(self.top_p)
    self.canvas.create_oval(136,5,236,96)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[0][1] = 1
    self.canvas.delete(self.top_p)
    self.canvas.create_line(150,0,225,100)
    self.canvas.create_line(225,0,150,100)
    self.if_com()
    self.robot()
 def horizon_l(self):
   if self.p == 1:
    self.varible[0][0] = 1
    self.canvas.delete(self.horizon_l_p)
    self.canvas.create_oval(25,5,120,96)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[0][0] = 1
    self.canvas.delete(self.horizon_l_p)
    self. canvas.create_line(30,100,100,0)
    self. canvas.create_line(100,100,30,0)
    self.if_com()
    self.robot()
 def horizon_r(self):
   if self.p == 1:
    self.varible[0][2] = 1
    self.canvas.delete(self.horizon_r_p)
    self.canvas.create_oval(260,5,358,95)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[0][2] = 1
    self.canvas.delete(self.horizon_r_p)
    self. canvas.create_line(275,100,340,0)
    self. canvas.create_line(340,100,275,0)
    self.if_com()
    self.robot()
 def horizon_l_b(self):
   if self.p == 1:
    self.varible[2][0] = 1
    self.canvas.delete(self.horizon_l_b_p)
    self.canvas.create_oval(118,203,18,294)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[2][0] = 1
    self.canvas.delete(self.horizon_l_b_p)
    self. canvas.create_line(30,200,100,300)
    self. canvas.create_line(100,200,30,300)
    self.if_com()
    self.robot()
 def horizon_r_b(self):
   if self.p == 1:
    self.varible[2][2] = 1
    self.canvas.delete(self.horizon_r_b_p)
    self.canvas.create_oval(253,203,352,294)
    self.if_com()
    self.robot()
   elif self.p == 2:
    self.varible[2][2] = 1
    self.canvas.delete(self.horizon_r_b_p)
    self. canvas.create_line(270,200,340,300)
    self. canvas.create_line(340,200,270,300)
    self.if_com()
    self.robot()
 def zero(self):
    self.win.destroy()
    self.win_z = tk.Tk()
    self.win_z.title('Крестики-Нолики')
    self.win_z.geometry("400x400+100+100")
    self.win_z.attributes("-toolwindow", True)
    self.canvas = tk.Canvas(self.win_z,width=500,height=500,bg='white')
    self.canvas.pack()
    self.canvas.create_line(20,100,355,100)
    self.canvas.create_line(20,200,355,200)
    self.canvas.create_line(125,0,125,300)
    self.canvas.create_line(250,0,250,300)
    self.center_p = self.canvas.create_window(188,150,width=120,height=97,window=tk.Button(self.canvas,text='',command=self.center,bg='white',bd=0))
    self.left_p = self.canvas.create_window(70,150,width=105,height=98,window=tk.Button(self.canvas,text='',command=self.left,bg='white',bd=0))
    self.ridht_p = self.canvas.create_window(303,150,width=105,height=98,window=tk.Button(self.canvas,text='',command=self.ridht,bg='white',bd=0))
    self.bottom_p = self.canvas.create_window(187,250,width=122,height=98,window=tk.Button(self.canvas,text='',command=self.botomm,bg='white',bd=0))
    self.top_p = self.canvas.create_window(188,51,width=121,height=98,window=tk.Button(self.canvas,text='',command=self.top,bg='white',bd=0))
    self.horizon_l_p = self.canvas.create_window(71,50,width=105,height=98,window=tk.Button(self.canvas,text='',command=self.horizon_l,bg='white',bd=0))
    self.horizon_r_p = self.canvas.create_window(305,51,width=105,height=98,window=tk.Button(self.canvas,text='',command=self.horizon_r,bg='white',bd=0))
    self.horizon_l_b_p = self.canvas.create_window(71,250,width=105,height=97,window=tk.Button(self.canvas,text='',command=self.horizon_l_b,bg='white',bd=0))
    self.horizon_r_b_p = self.canvas.create_window(303,250,width=105,height=98,window=tk.Button(self.canvas,text='',command=self.horizon_r_b,bg='white',bd=0))
    tk.mainloop()
 def choise(self):
    self.win= tk.Tk()
    self.win.title('Крестики-Нолики')
    self.win.geometry('300x300+100+100')
    self.win.attributes("-toolwindow", True)
    frame_1 = tk.Frame(self.win)
    frame_2 = tk.Frame(self.win)
    frame_1.pack()
    frame_2.pack()
    label = tk.Label(frame_1,text='За кого вы будете играть?',font=('arial black',15))
    label.pack(side='top')
    button_red = tk.Button(frame_2,text='крестики',bg="#C90000",command=self.cross,width=15,height=1,font=('arial black',15,))
    button_red.pack(side='top')
    button_blue = tk.Button(frame_2,text='нолики',bg="#001FCF",command=self.zer,width=15,height=1,font=('arial black',15))
    button_blue.pack(side='top')
    button_exit = tk.Button(self.win,text='Выйти',command=self.win.destroy,width=10,height=1,font=('arial black',15))
    button_exit.pack(side='bottom')
    tk.mainloop()
gui = tic_tac_toe()
gui.choise()