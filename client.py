import time
from threading import Thread

from connection import Connection
from whiteboard import WhiteBoard
from UserDialog import UserDialog

class Client(Thread,WhiteBoard):
    Objects = {'line': 'L', 'oval': 'O', 'circle': 'C', 'rectangle': 'R', 'square': 'S', 'drag': 'DR'}

    def __init__(self):
        self.conn = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None
        self.last_time = None
        self.last_click_obj = None

        self.line_x1,self.line_y1,self.line_x2,self.line_y2 = None, None, None, None

    def _init_mouse_event(self):
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

    def send_del_msg(self,event):
        canvas_item_tuple = self.drawing_area.find_overlapping(event.x + 2, event.y + 2, event.x - 2, event.y - 2)
        print(canvas_item_tuple)
        if len(canvas_item_tuple) > 0:
            to_delete_id = max(canvas_item_tuple)
            tags = self.drawing_area.gettags(to_delete_id)
            msgid = tags[0]
            msg = ('Z', msgid)
            self.conn.send_message(msg)


    #(tpye，startx,starty,endx,endy,color)
    #('D',startx,starty,endx,endy,'red')
    def left_but_down(self,event=None):
        self.isMouseDown = True
        self.x_pos = event.x
        self.y_pos = event.y
        self.last_time = time.time()
        self.line_x1, self.line_y1 = event.x,event.y

        if self.isMouseDown == True and self.drawing_tool == 'eraser':
            self.send_del_msg(event)

        try:
            self.last_click_obj = self.drawing_area.gettags('current')[0]
            print(self.last_click_obj)
        except Exception:
            pass



    def left_but_up(self,event=None):
        self.isMouseDown = False
        print(event.x,event.y)
        self.last_time = None
        self.line_x2, self.line_y2 = event.x, event.y
        if self.drawing_tool == 'text':
            self.draw_text()
        elif self.drawing_tool == 'drag':
            self.do_drag()
        else:
            self.draw_one_obj()


    def do_drag(self):
        msg = ('DR', self.last_click_obj, self.line_x2 - self.line_x1, self.line_y2 - self.line_y1)
        self.conn.send_message(msg)

    def draw_text(self):
        text_to_draw = UserDialog._Text
        msg = ('T', self.line_x1, self.line_y1, 'red',text_to_draw)
        self.conn.send_message(msg)

    def draw_one_obj(self):
        tool = self.drawing_tool
        if tool not in Client.Objects.keys():
            return
        else:
            cmd_type = Client.Objects[tool]
            msg = (cmd_type, self.line_x1, self.line_y1, self.line_x2, self.line_y2, 'red')
            self.conn.send_message(msg)

    # (tpye，startx,starty,endx,endy,color)
    # ('D',startx,starty,endx,endy,'red')
    def motion(self,event=None):
        if self.isMouseDown == True and self.drawing_tool == 'pencil':
            now = time.time()
            if now - self.last_time < 0.02:
                print('too fast')
                return
            self.last_time = now
            msg = ('D',self.x_pos,self.y_pos,event.x,event.y,'red')
            self.conn.send_message(msg)
            self.x_pos = event.x
            self.y_pos = event.y
        elif self.isMouseDown == True and self.drawing_tool == 'eraser':
            self.send_del_msg(event)




    def run(self):
        # print('run')aa
        while True:
            msg = self.conn.receive_msg()
            self.draw_from_msg(msg)
            print(msg)
            if msg == 'xxx':
                pass
            # print('i am running')
            # time.sleep(0.1)

if __name__ == '__main__':
    client = Client()
    print('startt')
    client.start()
    client.show_window()




