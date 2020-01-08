from tkinter import *

root=Tk()
cv=Canvas(root,bg='white')

rt3=cv.create_rectangle(30,30,70,70,tags=('y1','y2','y3'), fill='blue')
rt1=cv.create_rectangle(10,10,110,110,tags=('m0',))
rt2=cv.create_rectangle(20,20,80,80,tags=('m1',), fill='red')


# lst = cv.gettags(rt1)
# print(lst)

# print(rt1)
# print(rt2)
# print(rt3)
# print('-'*70)
# canvas_item_id = cv.find_overlapping(38, 38,45, 45)
# rt3=cv.create_rectangle(38, 38,45, 45, fill='red')
# print(canvas_item_id)
# to_delete_id = max(canvas_item_id)
# print(to_delete_id)
# cv.delete('m1')
# print(rt1)
# print(rt2)
# print(rt3)

# 1
# 2
# 3
# canvas_item_id = cv.find_overlapping(9, 9, 21, 21)
# print(canvas_item_id)
# canvas_item_id = (max(canvas_item_id))
# indice = len(cv.gettags(canvas_item_id))


cv.pack()

root.mainloop()

# from tkinter import *
#
# root=Tk()
#
# cv=Canvas(root,bg='white')
# rt1=cv.create_rectangle(10,10,110,110,tags=('r1','r2','r3'))
# rt2=cv.create_rectangle(20,20,80,80,tags=('s1','s2','s3'),fill='red')
# cv.delete(rt1)
# # cv.delete('s1')
# cv.pack()
#
# root.mainloop()