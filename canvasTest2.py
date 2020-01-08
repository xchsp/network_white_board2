from tkinter import *

root=Tk()

cv=Canvas(root,bg='white')


rt1=cv.create_rectangle(10,10,110,110,tags=('r1','r2','r3'))
cv.create_rectangle(10,10,110,110,tags=('r1','r2','r3'),outline='red')

cv.move(rt1,20,-5)

cv.pack()

root.mainloop()
