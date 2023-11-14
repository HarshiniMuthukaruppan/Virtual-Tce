import tkinter as tk 
import cvzone
import cv2 
from tkinter.tix import *
import numpy as np
import datetime
from cvzone.SelfiSegmentationModule import SelfiSegmentation
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
top = Tk()  
#top.title("SNAP CHAT CLONE")
top.geometry("700x820")
top.resizable(width=0,height=0)
tip= Balloon(top)

#l = Label(top, text = "SIMPLE SNAP APPLICATION",font =("Courier", 24)).place(x = 50,y = 60)
#l.config(font =("Courier", 14))
#l.pack()
top.title("SNAP CHAT CLONE")
bgimg= tk.PhotoImage(file = "1234.ppm")
limg= Label(top, i=bgimg)
limg.pack()
l = Label(top, text = "TCE SNAP",font =("Courier", 24)).place(x = 250,y = 60)
#pane = Frame(top)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#hs, ws = int(120 * 2), int(213 * 2)
#pane.pack(fill = BOTH, expand = True)
def normal():  
	vid = cv2.VideoCapture(0)
	key = cv2. waitKey(1)
	while(True):
		ret, frame = vid.read()
		frame = cv2.flip(frame, 1)
		cv2.imshow('normal', frame)
		key = cv2. waitKey(1)
		#k = cv2.waitKey(0)
		if key == ord('q'): 
			break
		elif key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=frame)
			vid.release()
			img_new = cv2.imread('saved_img.jpg')
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(400)
			cv2.destroyAllWindows()
			break
	
	vid.release()
	cv2.destroyAllWindows()

def garyscale():  
    vid = cv2.VideoCapture(0)
    key = cv2. waitKey(1)
    while(True):
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('BLACK AND WHITE', frame)
        key = cv2. waitKey(1)
        if key == ord('q'): 
            break
        elif key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            vid.release()
            img_new = cv2.imread('saved_img.jpg')
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(400)
            cv2.destroyAllWindows()
            break        
    vid.release()
    cv2.destroyAllWindows()

def blur():  
    vid = cv2.VideoCapture(0)
    key = cv2. waitKey(1)
    while(True):
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.blur(frame,(10,10))
        cv2.imshow('BLURRY', frame)
        key = cv2. waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            vid.release()
            img_new = cv2.imread('saved_img.jpg')
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            break        
    vid.release()
    cv2.destroyAllWindows()

def border():
    #m,dx 	  
	border = cv2.imread('/home/shiv/Downloads/frame-gbe77724c1_1280.png')
    #der = cv2.resize(border, (0, 0), fx = 0.1, fy = 0.1)
    #border = cv2.resize(border, (1050, 1610))
	down_points = (1280,720)
	border = cv2.resize(border, down_points, interpolation= cv2.INTER_LINEAR)
    #cv2.imshow('bor', border)
	#cv2.imshow('BORDER', border)	    
	vid = cv2.VideoCapture(0)
	key = cv2. waitKey(1)
	while(True):
		ret, frame = vid.read()
		frame = cv2.flip(frame, 1)
		frame = cv2.resize(frame, (848, 474))
		h, w, _ = border.shape
		border[126:600, 215:1063] = frame
		cv2.imshow('Leaf BORDER', border)
		key = cv2. waitKey(1)
	#215 126   
	#cv2.imshow("image",img)
	#cv2.imshow("imagep",imgp)
		#cv2.imshow('border', frame)
		if key == ord('q'):
			break
		elif key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=border)
			vid.release()
			img_new = cv2.imread('saved_img.jpg')
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(400)
			cv2.destroyAllWindows()
	vid.release()
	cv2.destroyAllWindows()


def tce():  
	vid = cv2.VideoCapture(0)
	logo = cv2.imread('logo.png')
	size = 150
	logo = cv2.resize(logo, (size, size))
	img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
	key = cv2. waitKey(1)
	while(True):
		ret, frame = vid.read()
		frame = cv2.flip(frame, 1)
		roi = frame[-size-10:-10, -size-10:-10]
		roi[np.where(mask)] = 0
		roi += logo
		cv2.imshow('normal', frame)
		key = cv2. waitKey(1)
		#k = cv2.waitKey(0)
		if key == ord('q'): 
			break
		elif key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=frame)
			vid.release()
			img_new = cv2.imread('saved_img.jpg')
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(400)
			cv2.destroyAllWindows()
			break
	
	vid.release()
	cv2.destroyAllWindows()


def glass():  
	try:
		vid = cv2.VideoCapture(0)
		key = cv2. waitKey(1)
		overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
		while(True):
			_, frame = vid.read()
			frame = cv2.flip(frame, 1)
			gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = cascade.detectMultiScale(gray_scale)
			for (x, y, w, h) in faces:
			#cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
				overlay_resize = cv2.resize(overlay, (w,h))
				frame = cvzone.overlayPNG(frame, overlay_resize, [x, y-5])
			cv2.imshow('Snap Dude', frame)
			key = cv2. waitKey(1)
			if key == ord('q'):
				break
			elif key == ord('s'):
				cv2.imwrite(filename='saved_img.jpg', img=frame)
				vid.release()
				img_new = cv2.imread('saved_img.jpg')
				img_new = cv2.imshow("Captured Image", img_new)
				cv2.waitKey(1000)
				cv2.destroyAllWindows()
				break        
		vid.release()
		cv2.destroyAllWindows()
		
		
	except:
		glass()



def star():  
	try:
		vid = cv2.VideoCapture(0)
		key = cv2. waitKey(1)
		overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
		while(True):
			_, frame = vid.read()
			frame = cv2.flip(frame, 1)
			gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = cascade.detectMultiScale(gray_scale)
			for (x, y, w, h) in faces:
			#cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
				overlay_resize = cv2.resize(overlay, (w,h))
				frame = cvzone.overlayPNG(frame, overlay_resize, [x, y-15])
			cv2.imshow('Snap Dude', frame)
			key = cv2. waitKey(1)
			if key == ord('q'):
				break
			elif key == ord('s'):
				cv2.imwrite(filename='saved_img.jpg', img=frame)
				vid.release()
				img_new = cv2.imread('saved_img.jpg')
				img_new = cv2.imshow("Captured Image", img_new)
				cv2.waitKey(1000)
				cv2.destroyAllWindows()
				break        
		vid.release()
		cv2.destroyAllWindows()
		
		
	except:
		star()
		
		
		
def timestamp():  
	vid = cv2.VideoCapture(0)
	key = cv2. waitKey(1)
	font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
	while(True):
		ret, frame = vid.read()
		dt = datetime.datetime.now()
		x = dt.strftime("%Y-%m-%d %H:%M:%S")
		frame = cv2.flip(frame, 1)
		frame = cv2.putText(frame, x,(100, 425),font, 1,(255, 255, 255),4, cv2.LINE_8)
		cv2.imshow('normal timestamp', frame)
		key = cv2. waitKey(1)
		#k = cv2.waitKey(0)
		if key == ord('q'): 
			break
		elif key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=frame)
			vid.release()
			img_new = cv2.imread('saved_img.jpg')
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(400)
			cv2.destroyAllWindows()
			break
		elif key == ord('1'):
			font = cv2.FONT_HERSHEY_DUPLEX
		elif key == ord('2'): 
			font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
		elif key == ord('3'): 
			font = cv2.FONT_HERSHEY_TRIPLEX
		elif key == ord('4'): 
			font = cv2.FONT_HERSHEY_SIMPLEX	
	vid.release()
	cv2.destroyAllWindows()
		

def bg():  
	vid = cv2.VideoCapture(0)
	vid.set(3, 640)
	vid.set(4, 480)
	segmentor = SelfiSegmentation()
	fpsReader = cvzone.FPS()
	imgBG = cv2.imread("tce.png")
	key = cv2. waitKey(1)
	while(True):
		ret, frame = vid.read()
		frame = cv2.flip(frame, 1)
		imgOut = segmentor.removeBG(frame, imgBG, threshold=0.8)
		#imgStack = cvzone.stackImages([frame, imgOut], 2,1)
		#_, imgStack = fpsReader.update(imgStack)
		cv2.imshow("image", imgOut)
		key = cv2. waitKey(1)
		#k = cv2.waitKey(0)
		if key == ord('q'): 
			break
		elif key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=imgOut)
			vid.release()
			img_new = cv2.imread('saved_img.jpg')
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(400)
			cv2.destroyAllWindows()
			break
	
	vid.release()
	cv2.destroyAllWindows()

def bh1(e):
	photo = PhotoImage(file="n.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="TAKES NORMAL IMAGE!!")
def bh2(e):
	photo = PhotoImage(file="image(1).png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="GIVES GRAYSCALE IMAGE!!")
def bh3(e):
	photo = PhotoImage(file="image.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="GIVES BLUR IMAGE!!")
def bh4(e):
	photo = PhotoImage(file="f1.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="A LEAF THEMED FRAME IMAGE!!")
def bh5(e):
	photo = PhotoImage(file="f2.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="GET TCE LOGO IN IMAGE!!")
def bh6(e):
	photo = PhotoImage(file="f4.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="WEAR NORMAL GLASS FILTER!!")
def bh7(e):
	photo = PhotoImage(file="f5.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="WEAR STAR GLASS FILTER!!")
def bh8(e):
	photo = PhotoImage(file="f3.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)

	sl.config(text="TAKES IMAGE WITH TIME!!")
def bh9(e):
	photo = PhotoImage(file="f6.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	sl.config(text="GET TCE BACKGROUND IN IMAGE!!")
	
def bhl(e):
	photo = PhotoImage(file="Fstival-22.png")
	label1 = tkinter.Label(image=photo)
	label1.image=photo
	label1.place(x=350,y=250)
	photo = PhotoImage(file="logotce.png")
	label2 = tkinter.Label(image=photo)
	label2.image=photo
	label2.place(x=400,y=600)
	sl.config(text="")
		
b1 = Button(top,text = "normal",width = 25,command = normal,activeforeground = "red",activebackground = "pink",pady=10)
  
b2 = Button(top, text = "grayscale",width = 25,command = garyscale,activeforeground = "blue",activebackground = "pink",pady=10)
  
b3 = Button(top, text = "blur",width = 25,command = blur,activeforeground = "green",activebackground = "pink",pady = 10)
  
b4 = Button(top, text = "frame",width = 25,command = border,activeforeground = "yellow",activebackground = "pink",pady = 10)

b5 = Button(top, text = "tce",width = 25,command = tce,activeforeground = "red",activebackground = "pink",pady = 10)

b6 = Button(top, text = "glass",width = 25,command = glass,activeforeground = "blue",activebackground = "pink",pady = 10)

b7 = Button(top, text = "star glass",width = 25,command = star,activeforeground = "green",activebackground = "pink",pady = 10)

b8 = Button(top, text = "normal timestamp",width = 25,command = timestamp,activeforeground = "yellow",activebackground = "pink",pady = 10)

b9 = Button(top,text = "bg",width = 25,command = bg,activeforeground = "red",activebackground = "pink",pady=10)




#photo = PhotoImage(file="cool.png")


#label1 = tkinter.Label(image=photo)
#label1.image=photo
#label1.place(x=150,y=250)


#label.place(relx=0.0,rely=1.0,anchor=E)



sl=Label(top,text='',bd=1,relief=SUNKEN,anchor=E)

photo = PhotoImage(file="Fstival-22.png")
label1 = tkinter.Label(image=photo)
label1.image=photo
label1.place(x=350,y=250)
photo = PhotoImage(file="logotce.png")
label2 = tkinter.Label(image=photo)
label2.image=photo
label2.place(x=400,y=600)
sl.config(text="")

sl.pack(fill=X, side=BOTTOM, ipady=2)
tip.bind_widget(b1,balloonmsg="TAKES NORMAL IMAGE!!")
tip.bind_widget(b2,balloonmsg="GIVES GRAYSCALE IMAGE!!")
tip.bind_widget(b3,balloonmsg="GIVES BLUR IMAGE!!")
tip.bind_widget(b4,balloonmsg="A LEAF THEMED FRAME IMAGE!!")
tip.bind_widget(b5,balloonmsg="GET TCE LOGO IN IMAGE!!")
tip.bind_widget(b6,balloonmsg="WEAR NORMAL GLASS FILTER!!")
tip.bind_widget(b7,balloonmsg="WEAR STAR GLASS FILTER!!")
tip.bind_widget(b8,balloonmsg="TAKES IMAGE WITH TIME!!")
tip.bind_widget(b9,balloonmsg="GET TCE BACKGROUND IN IMAGE!!")

b1.bind("<Enter>",bh1)
b1.bind("<Leave>",bhl)
b2.bind("<Enter>",bh2)
b2.bind("<Leave>",bhl)
b3.bind("<Enter>",bh3)
b3.bind("<Leave>",bhl)
b4.bind("<Enter>",bh4)
b4.bind("<Leave>",bhl)
b5.bind("<Enter>",bh5)
b5.bind("<Leave>",bhl)
b6.bind("<Enter>",bh6)
b6.bind("<Leave>",bhl)
b7.bind("<Enter>",bh7)
b7.bind("<Leave>",bhl)
b8.bind("<Enter>",bh8)
b8.bind("<Leave>",bhl)
b9.bind("<Enter>",bh9)
b9.bind("<Leave>",bhl)

b1.place(x=100, y=200)

b2.place(x=100, y=250)

b3.place(x=100, y=300)

b4.place(x=100, y=350)

b5.place(x=100, y=400)

b6.place(x=100, y=450)

b7.place(x=100, y=500)

b8.place(x=100, y=550)

b9.place(x=100, y=600)


top.mainloop()



