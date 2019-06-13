#coding=utf-8
from tkinter import *
def image_change(aFrame):
	bm1 = PhotoImage(file='1.gif')
	bm2 = PhotoImage(file='2.gif')
	bm3 = PhotoImage(file='3.gif')
	bm4 = PhotoImage(file='4.gif')
	label = Label(aFrame,width = 300,height = 200, image=bm1,bg="#B0C4DE LightSteelBlue 亮钢蓝")
	label.bm = bm1
	i = 1
	def changeImage(i):
		if i % 3 == 1:
			label.configure(image = bm1)
			i = i + 1
			label.after(2000,changeImage,i)
		elif i % 3 == 2:
			label.configure(image=bm2)
			i = i + 1
			label.after(1000, changeImage,i)
		else:
			label.configure(image=bm3)
			i = i + 1
			label.after(6000, changeImage, i)
	label.pack(fill=BOTH,side=TOP)
	i = i + 1
	label.after(2000,changeImage,i)
	"""aFrame.update_idletasks()
	aFrame.deiconify()    #now window size was calculated
	aFrame.withdraw()     #hide window again
	#aFrame.geometry('%sx%s+%s+%s' % (aFrame.winfo_width() + 10, aFrame.winfo_height() + 10, (screenwidth - aFrame.winfo_width())/2,
 	#(screenheight - aFrame.winfo_height())/2) )    #center window on desktop

	aFrame.deiconify()"""
	pass