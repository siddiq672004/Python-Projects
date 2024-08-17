import tkinter
import PIL.Image, PIL.ImageTk#pip install pillow
import cv2 #pip install opencv-python
from functools import partial #to get arguments which can not done in command 
import threading
import imutils #for resize image 
import time

#width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368
stream = cv2.VideoCapture("playback.mp4")
flag = True
def play(speed):
  global flag
  print(f"you clicked on play.speed is {speed}")
  frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
  stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

  grabbed, frame = stream.read()
  if not grabbed:
    exit()
  frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
  frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
  canvas.image = frame
  canvas.create_image(0,0, image=frame,anchor=tkinter.NW)
  if flag:
    canvas.create_text(120,25,fill="red",font="Times 20 italic bold",text="Decision Pending")
  flag = not flag

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("decision.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    time.sleep(1.5)
    if decision == 'out':
      decisionImg = "out.jpg"
    else:
        decisionImg = "not out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)    
    print("")
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
def not_out():
     thread = threading.Thread(target=pending, args=("not out",))
     thread.daemon = 1
     thread.start()
     print("Player is not out")



#tkinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("umpire.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho = tkinter.NW, image =photo)
canvas.pack()


#buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)",width=50, command = partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (slow)",width=50, command = partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Next (fast) >>",width=50, command = partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Next (slow) >>",width=50, command = partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text=" Give Out ",width=50, command = out)
btn.pack()
btn = tkinter.Button(window, text=" Give Not Out ",width=50, command = not_out )
btn.pack()

# btn = tkinter.Button(window, text="<<Previous ()")

window.mainloop()
