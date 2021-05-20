import tkinter as tk
from PIL import ImageTk
from PIL import Image
import time


class Env:
    def __init__(self):
        self.grid_size = 100
        self.win = tk.Tk()
        self.pic_player, self.pic_diamond, self.pic_boom1, self.pic_boom2, self.pic_boom3, self.pic_boom4,self.pic_boom5,self.pic_boom6,self.pic_boom7,self.pic_boom8,self.pic_boom9,self.pic_boom10= self.__load_img()
        self.__init_win()
        self.canvas = self.__init_rc()
        self.texts = self.__produce_text()
        self.canvas.pack()
        # self._init_test_case()
        # self.win.mainloop()

    def __init_win(self):
        self.win.title('Grid World')
        # self.win.geometry("500x300")

    def __init_rc(self):
        canvas = tk.Canvas(self.win, width=500, height=720, bg='white')
        for h in range(5):
            for v in range(5):
                canvas.create_rectangle(self.grid_size * v, self.grid_size * h, self.grid_size * (v + 1),
                                        self.grid_size * (h + 1))
        trans_pixel = int(self.grid_size / 2)
        self.player = canvas.create_image(trans_pixel + self.grid_size * 0, trans_pixel + self.grid_size * 0,
                                          image=self.pic_player)
        self.diamond = canvas.create_image(trans_pixel + self.grid_size * 4, trans_pixel + self.grid_size * 4,
                                           image=self.pic_diamond)
        self.boom1 = canvas.create_image(trans_pixel + self.grid_size * 1, trans_pixel + self.grid_size * 1,
                                         image=self.pic_boom1)
        self.boom2 = canvas.create_image(trans_pixel + self.grid_size * 3, trans_pixel + self.grid_size * 1,
                                         image=self.pic_boom2)
        self.boom3 = canvas.create_image(trans_pixel + self.grid_size * 1, trans_pixel + self.grid_size * 3,
                                         image=self.pic_boom3)
        self.boom4 = canvas.create_image(trans_pixel + self.grid_size * 3, trans_pixel + self.grid_size * 3,
                                         image=self.pic_boom4)
        self.boom5 = canvas.create_image(trans_pixel + self.grid_size * 1, trans_pixel + self.grid_size * 2,
                                         image=self.pic_boom5)
        self.boom6 = canvas.create_image(trans_pixel + self.grid_size * 3, trans_pixel + self.grid_size * 2,
                                         image=self.pic_boom6)
        self.boom7 = canvas.create_image(trans_pixel + self.grid_size * 0, trans_pixel + self.grid_size * 2,
                                         image=self.pic_boom7)
        self.boom8 = canvas.create_image(trans_pixel + self.grid_size * 1, trans_pixel + self.grid_size * 4,
                                         image=self.pic_boom8)
        self.boom9 = canvas.create_image(trans_pixel + self.grid_size * 2, trans_pixel + self.grid_size * 3,
                                         image=self.pic_boom9)
        self.boom10 = canvas.create_image(trans_pixel + self.grid_size * 3, trans_pixel + self.grid_size * 4,
                                         image=self.pic_boom10)
        return canvas

    def __load_img(self):
        pic_resize = int(self.grid_size / 2)
        player = ImageTk.PhotoImage(Image.open("p.png").resize((pic_resize, pic_resize)))
        diamond = ImageTk.PhotoImage(Image.open("captured.png").resize((pic_resize, pic_resize)))
        boom1 = ImageTk.PhotoImage(Image.open('z.png').resize((pic_resize, pic_resize)))
        boom2 = ImageTk.PhotoImage(Image.open('z.png').resize((pic_resize, pic_resize)))
        boom3 = ImageTk.PhotoImage(Image.open('z.png').resize((pic_resize, pic_resize)))
        boom4 = ImageTk.PhotoImage(Image.open('z.png').resize((pic_resize, pic_resize)))
        boom5 = ImageTk.PhotoImage(Image.open('l.png').resize((pic_resize, pic_resize)))
        boom6= ImageTk.PhotoImage(Image.open('f.png').resize((pic_resize, pic_resize)))
        boom7 = ImageTk.PhotoImage(Image.open('g.png').resize((pic_resize, pic_resize)))
        boom8 = ImageTk.PhotoImage(Image.open('x.png').resize((pic_resize, pic_resize)))
        boom9 = ImageTk.PhotoImage(Image.open('xz.png').resize((pic_resize, pic_resize)))
        boom10 = ImageTk.PhotoImage(Image.open('s.png').resize((pic_resize, pic_resize)))
        return player, diamond, boom1, boom2, boom3, boom4,boom5,boom6,boom7,boom8,boom9,boom10

    def __produce_text(self):
        texts = []
        x = self.grid_size / 2
        y = self.grid_size / 6
        for h in range(5):
            for v in range(5):
                up = self.canvas.create_text(x + h * self.grid_size, y + v * self.grid_size, text=0)
                down = self.canvas.create_text(x + h * self.grid_size, self.grid_size - y + v * self.grid_size, text=0)
                left = self.canvas.create_text(y + h * self.grid_size, x + v * self.grid_size, text=0)
                right = self.canvas.create_text(self.grid_size - y + h * self.grid_size, x + v * self.grid_size, text=0)
                texts.append({"up": up, "down": down, "left": left, "right": right})
        return texts

    def _win_d_update(self):
        self.win.update()
        time.sleep(0.1)


class GridWorld(Env):
    def __init__(self):
        super().__init__()
        self._win_d_update()

    def player_move(self, x, y):
        # x横向移动向右,y纵向移动向下
        self.canvas.move(self.player, x * self.grid_size, y * self.grid_size)
        self._win_d_update()

    def reset(self):
        # 重置为起始位置
        x, y = self.canvas.coords(self.player)
        self.canvas.move(self.player, -x + self.grid_size / 2, -y + self.grid_size / 2)
        self._win_d_update()
        return self.get_state(self.player)

    def get_state(self, who):
        x, y = self.canvas.coords(who)
        state = [int(x / self.grid_size), int(y / self.grid_size)]
        return state

    def update_val(self, num, arrow, val):
        pos = num[0] * 5 + num[1]
        x, y = self.canvas.coords(self.texts[pos][arrow])
        self.canvas.delete(self.texts[pos][arrow])
        self.texts[pos][arrow] = self.canvas.create_text(x, y, text=val)
        # self._win_d_update()

    def exec_calc(self, action):
        # 执行一次决策
        feedback = 'alive'  # alive, stop, dead 分别对应通过，撞墙，炸死
        next_state = []
        next_h, next_v, reward = 0.0, 0.0, 0.0
        h, v = self.get_state(self.player)
        if action == 0:  # up
            next_h = h
            next_v = v - 1
            # self.player_move(0, -1)
        elif action == 1:  # down
            next_h = h
            next_v = v + 1
            # self.player_move(0, 1)
        elif action == 2:  # left
            next_h = h - 1
            next_v = v
            # self.player_move(-1, 0)
        elif action == 3:  # right
            next_h = h + 1
            next_v = v
            # self.player_move(1, 0)
        else:
            print('programmer bug ...')
        next_state = [next_h, next_v]
        boom1, boom2, boom3, boom4 = self.get_state(self.boom1), self.get_state(self.boom2), self.get_state(
            self.boom3), self.get_state(self.boom4)
        diamond = self.get_state(self.diamond)
        if next_h < 0 or next_v < 0 or next_h > 4 or next_v > 4:  # 超过边界
            reward = -1
            feedback = 'stop'
        elif next_state == boom1 or next_state == boom2 or next_state == boom3 or next_state == boom4:  # 炸弹区域
            reward = -100
            feedback = 'dead'
        elif next_state == diamond:  # 获得的通关物品
            reward = 500
        else:
            reward = 0
        return feedback, next_state, reward

    def update_view(self, state, action, next_state, q_val):
        action_list = ['up', 'down', 'left', 'right']
        self.player_move(next_state[0] - state[0], next_state[1] - state[1])
        self.update_val(state, action_list[action], round(q_val, 2))

    def attach(self):
        # 到达终点，返回True , 未到达，返回False
        return str(self.get_state(self.player)) == str(self.get_state(self.diamond))


