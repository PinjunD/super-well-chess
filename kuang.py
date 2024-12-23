import pygame


class bound:
    def __init__(self, ai_game):
        self.l = 50
        self.screen = ai_game.screen
        self.color1 = ai_game.settings.bg_color
        self.color2 = ai_game.settings.line_color
        self.lline = []
        self.kkuai = []
        self.center = []
        self.wid = ai_game.settings.wid
        self.hei = ai_game.settings.hei
        for i in range(3):
            for j in range(3):
                self.lline.append(self.line(self.wid/2 - 13 * self.l / 2 + 5 * i * self.l,
                                           self.hei/2 - 13 * self.l / 2 + 5 * j * self.l))
                a = self.kuai(self.wid / 2 - 13 * self.l / 2 + 5 * i * self.l,
                          self.hei / 2 - 13 * self.l / 2 + 5 * j * self.l)
                self.kkuai.append(a)
                self.center.append(a[0][4][0].center)

    def line(self,m,n):
        kuang = []
        for i in range(4):
            kuang.append(pygame.Rect(m, n + i * self.l, 3*self.l, 1))
        for i in range(4):
            kuang.append(pygame.Rect(m + i * self.l, n, 1, 3*self.l))
        return kuang
    def kuai(self,m,n):
        k = []
        for i in range(3):
            for j in range(3):
                cell = [pygame.Rect(m + i * self.l, n + j * self.l, self.l, self.l), True, 3 * i + j]
                k.append(cell)
        kuang = [k, True]
        return kuang

    def draw_l(self):
        for lines in self.lline:
            for line in lines:
                pygame.draw.rect(self.screen, self.color2, line)
    def draw_k(self):
        for kuais in self.kkuai:
            for kuai in kuais[0]:
                if kuai[1]:
                    pygame.draw.rect(self.screen, (1, 230, 230), kuai[0])
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), kuai[0])

