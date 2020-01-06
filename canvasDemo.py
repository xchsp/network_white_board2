from tkinter import *

root=Tk()

cv=Canvas(root,bg='white')

rt1=cv.create_oval(10,10,110,110,tags=('r1','r2','r3'))
rt2=cv.create_rectangle(20,20,80,80,tags=('s1','s2','s3'))
line = cv.create_line(20,20,80,80)
# cv.delete(rt1)
# cv.delete('s1')
cv.pack()

root.mainloop()