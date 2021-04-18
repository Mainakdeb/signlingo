from tkinter import *
from custom_button import TkinterCustomButton
import numpy as np
import cv2
import torch
from model import Net
import random
def run_inference_on_frame(frame, model):
    res = cv2.resize(frame, dsize=(28, 28), interpolation = cv2.INTER_CUBIC)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    res1 = np.reshape(res, (1, 1, 28, 28)) / 255
    res1 = torch.from_numpy(res1)
    res1 = res1.type(torch.FloatTensor)
    out = model(res1)
    probs, label = torch.topk(out, 25)
    probs = torch.nn.functional.softmax(probs, 1)
    pred = out.max(1, keepdim=True)[1]
    return(pred, probs)
def clicked():
    cap = cv2.VideoCapture(0)
    font =cv2.FONT_HERSHEY_PLAIN

    cap.set(3, 700)
    cap.set(4, 480)

    modelo = torch.load('model_trained.pt')
    modelo.eval()

    signs = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I','9':'J',
            '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R',
            '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y' , '25':'Z'}
    
    prompt = 11
    score=0

    while True:
        ret, frame = cap.read()
        
        img = frame[20:250, 20:250]
        frame = cv2.rectangle(frame, (20, 20), (250, 250), (0, 255, 0), 3)
        frame = cv2.putText(frame, "Target: "+list(signs.values())[prompt], (60,385), font, 1, (255,255,0), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, "Current Score: "+str(score), (60,355), font, 1, (255,0,0), 2, cv2.LINE_AA)
        k = cv2. waitKey(1)
        
        if k%256 == 32:
            #space - run inference
            pred, probs =run_inference_on_frame(img, modelo)
        
            if float(probs[0,0]) < 0.0:
                text_ = 'Sign not detected'
            else:
                text_ = signs[str(int(pred))] + ': ' + '{:.2f}'.format(float(probs[0,0])*100) + '%'

            font = cv2.FONT_HERSHEY_SIMPLEX
            frame = cv2.putText(frame, text_, (60,285), font, 1, (255,255,255), 2, cv2.LINE_AA)
            
            cv2.imshow('Cam', frame)
            #print(text_, "index:", pred.item(), prompt)
            if pred.item() == prompt:
                prompt = random.randint(0,24)
                score+=1

        elif k%256 == 27:
            #escape - exit
            break
            
        else:
            cv2.imshow('Cam', frame)

    cap.release()
    cv2.destroyAllWindows()
def hide_button(widget):
    # This will remove the widget from toplevel
    widget.pack_forget()
  
  
# Method to make Button(widget) visible
def show_button(widget):
    # This will recover the widget from toplevel
    widget.pack()
def openLevelWindow():
    hide_button(btn)
    btn1 = TkinterCustomButton(text="Level 1", corner_radius=10, command=openLevel1)
    btn2 = TkinterCustomButton(text="Level 2", corner_radius=10, command=openLevel2)
    btn3 = TkinterCustomButton(text="Level 3", corner_radius=10, command=openLevel3)
    btn1.grid(column=2, row=0)
    btn2.grid(column=3, row=0)
    btn3.grid(column=4, row=0)

    btn1.place(x=450, y=100)
    btn2.place(x=450, y=200)
    btn3.place(x=450, y=300)


def openLevel1():
    newWindow = Toplevel(window)
    Fact = "Know which hand to use. In the British, Australian and New Zealand Sign Languages, your dominant hand is used to sign onto the fingers of your non-dominant hand, which is forms the “base” for your vowels. If you are left handed, use your right hand as your base hand.If you are right handed, use your left hand as your base hand to sign the vowels.To sign vowels, you are required to point with your index finger onto the fingers on your other hand, so ensure that you have enough dexterity to carry out these signs"
    # sets the title of the
    # Toplevel widget
    newWindow.title("ASL - Level 1")
  
    # sets the geometry of toplevel
    newWindow.geometry("1000x800")
    lbl1 = Label(newWindow, text="Level-1!",font=("Arial Bold", 50))

    lbl1.grid(column=10, row=10)
    lbl1.place(x=500, y=50, anchor="center")
    lbl2 = Label(newWindow, text="Let's talk about vowels today!")

    lbl2.grid(column=10, row=10)
    lbl2.place(x=490, y=100, anchor="center")
    lbl3 = Label(newWindow, text="Vowels in English are A,E,I,O,U")

    lbl3.grid(column=10, row=10)
    lbl3.place(x=490, y=150, anchor="center")
    T = Text(newWindow, height = 20, width = 100)
    T.insert(INSERT, Fact)
    T.place(x=490, y=200, anchor="center")
    
    btn1 = Button(newWindow, text="Start Level1!",command=clicked)
    btn1.grid(column=2, row=0)
    btn1.place(x=450, y=300)


def openLevel2():
    newWindow1 = Toplevel(window)
    Fact = "Know which hand to use. In the British, Australian and New Zealand Sign Languages, your dominant hand is used to sign onto the fingers of your non-dominant hand, which is forms the “base” for your vowels. If you are left handed, use your right hand as your base hand.If you are right handed, use your left hand as your base hand to sign the vowels.To sign vowels, you are required to point with your index finger onto the fingers on your other hand, so ensure that you have enough dexterity to carry out these signs"
    # sets the title of the
    # Toplevel widget
    newWindow1.title("ASL - Level 2")
  
    # sets the geometry of toplevel
    newWindow1.geometry("1000x800")
    lbl1 = Label(newWindow1, text="Level-2!",font=("Arial Bold", 50))

    lbl1.grid(column=10, row=10)
    lbl1.place(x=500, y=50, anchor="center")
    lbl2 = Label(newWindow1, text="Let's talk about vowels today!")

    lbl2.grid(column=10, row=10)
    lbl2.place(x=490, y=100, anchor="center")
    lbl3 = Label(newWindow1, text="Vowels in English are A,E,I,O,U")

    lbl3.grid(column=10, row=10)
    lbl3.place(x=490, y=150, anchor="center")
    T = Text(newWindow1, height = 20, width = 100)
    T.insert(INSERT, Fact)
    T.place(x=490, y=200, anchor="center")
    
    btn1 = Button(newWindow1, text="Start Level2!",command=clicked)
    btn1.grid(column=2, row=0)
    btn1.place(x=450, y=300)

def openLevel3():
    newWindow2 = Toplevel(window)
    Fact = "Know which hand to use. In the British, Australian and New Zealand Sign Languages, your dominant hand is used to sign onto the fingers of your non-dominant hand, which is forms the “base” for your vowels. If you are left handed, use your right hand as your base hand.If you are right handed, use your left hand as your base hand to sign the vowels.To sign vowels, you are required to point with your index finger onto the fingers on your other hand, so ensure that you have enough dexterity to carry out these signs"
    # sets the title of the
    # Toplevel widget
    newWindow2.title("ASL - Level 3")
  
    # sets the geometry of toplevel
    newWindow2.geometry("1000x800")
    lbl1 = Label(newWindow2, text="Level-3!",font=("Arial Bold", 50))

    lbl1.grid(column=10, row=10)
    lbl1.place(x=500, y=50, anchor="center")
    lbl2 = Label(newWindow2, text="Let's talk about vowels today!")

    lbl2.grid(column=10, row=10)
    lbl2.place(x=490, y=100, anchor="center")
    lbl3 = Label(newWindow2, text="Vowels in English are A,E,I,O,U")

    lbl3.grid(column=10, row=10)
    lbl3.place(x=490, y=150, anchor="center")
    T = Text(newWindow2, height = 20, width = 100)
    T.insert(INSERT, Fact)
    T.place(x=490, y=200, anchor="center")
    
    btn1 = Button(newWindow2, text="Start Level3!",command=clicked)
    btn1.grid(column=2, row=0)
    btn1.place(x=450, y=300)


  
window = Tk()

window.title("Learn-ASL")

window.geometry('1000x800')
bg = PhotoImage(file = "asls.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)
lbl = Label(window, text="Learn-ASL!",font=("Arial Bold", 50))
btn = Button(window, text="Click Me", bg="orange", fg="red")
lbl.grid(column=10, row=10)
lbl.place(x=500, y=50, anchor="center")
btn = Button(window, text="Start Playing",command=openLevelWindow)
btn.grid(column=2, row=0)
btn.place(x=450, y=100)
window.mainloop()




