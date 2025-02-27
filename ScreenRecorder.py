from tkinter import *
import pyscreenrec

root=Tk()
root.geometry("400x600")
root.title("SCREEN RECORDER")
root.config(bg="black")
root.resizable(False,False)

def start():
    file=filename.get()
    rec.start_recording(str(file+".mp4"),30)

def pause():
    rec.pause_recording()

def resume():
    rec.resume_recording()

def stop():
    rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#bg images

photo1=PhotoImage(file="yelllow.png")
Label(root,image=photo1,bg="black").place(x=-2,y=35)


photo2=PhotoImage(file="blue.png")
Label(root,image=photo2,bg="black").place(x=223,y=200)


lbl=Label(root,text="Screen Recorder",font="arial 15 bold",bg="black",fg="white")
lbl.pack(pady=20)


photo3=PhotoImage(file="recording.png")
Label(root,image=photo3,bd=0,bg="black").pack(pady=30)

filename=StringVar()
entry=Entry(root,textvariable=filename,width=18,font="arial 15")
entry.place(x=100,y=350)
filename.set("recording25")

start=Button(root,text="start",font="arial 22",bd=0,bg="black",fg="white",command=start)
start.place(x=140,y=250)

photo4=PhotoImage(file="pause.png")
pause=Button(root,image=photo4,bd=0,bg="black",command=pause)
pause.place(x=50,y=450)

photo5=PhotoImage(file="resume.png")
resume=Button(root,image=photo5,bd=0,bg="black",command=resume)
resume.place(x=150,y=450)

photo6=PhotoImage(file="stop.png")
stop=Button(root,image=photo6,bd=0,bg="black",command=stop)
stop.place(x=250,y=450)


root.mainloop()
