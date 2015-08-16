from Tkinter import *
root = Tk()

root.title("Tick")
root.geometry("320x400")

def tick():
	print "Tick"
	root.after(1000, tick)

#root.after(1000, tick)
tick()
root.mainloop()
