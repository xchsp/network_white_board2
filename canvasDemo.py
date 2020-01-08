from tkinter import *
from tkinter import font

root=Tk()

cv=Canvas(root,bg='white')
# lefttop = (100,100)
# edge_size = 150
# rt1=cv.create_rectangle(lefttop[0],lefttop[1],lefttop[0]+edge_size,lefttop[1]+edge_size,tags=('r1','r2','r3'))

text = 'hello'
text_font = font.Font(family='Helvetica',size=50, weight='bold', slant='italic')
cv.create_text(200,200,fill='red',font=text_font,text=text)


cv.pack()

root.mainloop()

#

