import sys
import pygame
from settings import Settings
from kuang import bound
from qi import qi
import time
class Super_Game:
    def __init__(self):
        self.type = 1
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.wid, self.settings.hei))
        pygame.display.set_caption("Super#TicTacToe")
        self.bou = bound(self)
        self.qi1 = []
        self.qi2 = []
        self.daqi1 = []
        self.daqi2 = []
        self.choose = 9

    def run_game(self):
        while True:
            self.screen.fill(self.settings.bg_color)
            self.check_event()
            self.zhanling()
            self.bou.draw_k()
            self.bou.draw_l()
            self.updata()
            pygame.display.flip()
            self.shengfu()


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    sys.exit()
                if event.key == pygame.K_b:
                    self.chehui()
                if event.key == pygame.K_SPACE:
                    self.shualai()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.xiaqi(pos)

#绘制棋子
    def updata(self):
        for qi in self.qi1:
            qi.draw()
        for qi in self.qi2:
            qi.draw()
        for qi in self.daqi1:
            qi.draw()
        for qi in self.daqi2:
            qi.draw()

#下棋判定
    def xiaqi(self, p):
        if self.choose == 9 or not self.bou.kkuai[self.choose][1]:
            kkuai = self.bou.kkuai
        else:
            kkuai = [self.bou.kkuai[self.choose]]
        for kuai in kkuai:
            for celll in kuai[0]:
                cell = celll[0]
                if cell.collidepoint(p) and celll[1]:
                    celll[1] = False
                    self.choose = celll[2]
                    if self.type == 1:
                        new_qi = qi(self, cell.center)
                        self.qi1.append(new_qi)
                    else:
                        new_qi = qi(self, cell.center)
                        self.qi2.append(new_qi)
                    self.type += 1
                    self.type %= 2


#占领判断
    def zhanling(self):
        for Qi1 in self.qi1:
            for Qi2 in self.qi1:
                for Qi3 in self.qi1:
                    #oa0 = Qi1.rect.center != Qi2.rect.center and Qi3.rect.center != Qi2.rect.center and Qi1.rect.center != Qi3.rect.center
                    a = Qi1.rect.centerx - Qi2.rect.centerx == self.bou.l and Qi2.rect.centerx - Qi3.rect.centerx == self.bou.l
                    b = Qi1.rect.centery - Qi2.rect.centery == self.bou.l and Qi2.rect.centery - Qi3.rect.centery == self.bou.l
                    a2 = Qi3.rect.centerx - Qi2.rect.centerx == self.bou.l and Qi2.rect.centerx - Qi1.rect.centerx == self.bou.l
                    b2 = Qi1.rect.centery - Qi2.rect.centery == self.bou.l and Qi2.rect.centery - Qi3.rect.centery == self.bou.l
                    a1 = Qi1.rect.centery == Qi2.rect.centery and Qi3.rect.centery == Qi2.rect.centery
                    b1 = Qi1.rect.centerx == Qi2.rect.centerx and Qi3.rect.centerx == Qi2.rect.centerx
                    if (a and b) or (a and a1) or (b and b1) or (a2 and b2):
                        for kuai in self.bou.kkuai:
                            if kuai[1]:
                                for celll in kuai[0]:
                                    cell = celll[0]
                                    if Qi1.rect.center == cell.center:
                                        new_daqi = qi(self, kuai[0][4][0].center, 1)
                                        self.daqi1.append(new_daqi)
                                        for celll in kuai[0]:
                                            celll[1] = False


        for Qi1 in self.qi2:
            for Qi2 in self.qi2:
                for Qi3 in self.qi2:
                    a = Qi1.rect.centerx - Qi2.rect.centerx == self.bou.l and Qi2.rect.centerx - Qi3.rect.centerx == self.bou.l
                    b = Qi1.rect.centery - Qi2.rect.centery == self.bou.l and Qi2.rect.centery - Qi3.rect.centery == self.bou.l
                    a2 = Qi3.rect.centerx - Qi2.rect.centerx == self.bou.l and Qi2.rect.centerx - Qi1.rect.centerx == self.bou.l
                    b2 = Qi1.rect.centery - Qi2.rect.centery == self.bou.l and Qi2.rect.centery - Qi3.rect.centery == self.bou.l
                    a1 = Qi1.rect.centery == Qi2.rect.centery and Qi3.rect.centery == Qi2.rect.centery
                    b1 = Qi1.rect.centerx == Qi2.rect.centerx and Qi3.rect.centerx == Qi2.rect.centerx
                    if (a and b) or (a and a1) or (b and b1) or (a2 and b2):
                        for kuai in self.bou.kkuai:
                            if kuai[1]:
                                for celll in kuai[0]:
                                    cell = celll[0]
                                    if Qi1.rect.center == cell.center:
                                        new_daqi = qi(self, kuai[0][4][0].center, 1)
                                        self.daqi2.append(new_daqi)
                                        for celll in kuai[0]:
                                            celll[1] = False

        for kuai in self.bou.kkuai:
            aa = 1
            for cell in kuai[0]:
                aa = aa and not cell[1]
            if aa:
                kuai[1] = False





# 胜负判定
    def shengfu(self):
        if len(self.daqi1) >= 3:
            L = 5 * self.bou.l
            for Qi1 in self.daqi1:
                for Qi2 in self.daqi1:
                    for Qi3 in self.daqi1:
                        a = Qi1.rect.centerx - Qi2.rect.centerx == L and Qi2.rect.centerx - Qi3.rect.centerx == L
                        b = Qi1.rect.centery - Qi2.rect.centery == L and Qi2.rect.centery - Qi3.rect.centery == L
                        a2 = Qi3.rect.centerx - Qi2.rect.centerx == L and Qi2.rect.centerx - Qi1.rect.centerx == L
                        b2 = Qi1.rect.centery - Qi2.rect.centery == L and Qi2.rect.centery - Qi3.rect.centery == L
                        a1 = Qi1.rect.centery == Qi2.rect.centery and Qi3.rect.centery == Qi2.rect.centery
                        b1 = Qi1.rect.centerx == Qi2.rect.centerx and Qi3.rect.centerx == Qi2.rect.centerx
                        if (a and b) or (a and a1) or (b and b1) or (a2 and b2):
                            print("黑棋胜利")
                            time.sleep(1)
                            sys.exit()


        if len(self.daqi2) >= 3:
            L = 5 * self.bou.l
            for Qi1 in self.daqi2:
                for Qi2 in self.daqi2:
                    for Qi3 in self.daqi2:
                        a = Qi1.rect.centerx - Qi2.rect.centerx == L and Qi2.rect.centerx - Qi3.rect.centerx == L
                        b = Qi1.rect.centery - Qi2.rect.centery == L and Qi2.rect.centery - Qi3.rect.centery == L
                        a2 = Qi3.rect.centerx - Qi2.rect.centerx == L and Qi2.rect.centerx - Qi1.rect.centerx == L
                        b2 = Qi1.rect.centery - Qi2.rect.centery == L and Qi2.rect.centery - Qi3.rect.centery == L
                        a1 = Qi1.rect.centery == Qi2.rect.centery and Qi3.rect.centery == Qi2.rect.centery
                        b1 = Qi1.rect.centerx == Qi2.rect.centerx and Qi3.rect.centerx == Qi2.rect.centerx
                        if (a and b) or (a and a1) or (b and b1) or (a2 and b2):
                            print("白棋胜利")
                            time.sleep(1)
                            sys.exit()
#悔棋
    def chehui(self):
        if self.type == 1:
            if len(self.qi2) != 0:
                self.qi2.remove(self.qi2[-1])
                self.type = 0
        else:
            if len(self.qi1) != 0:
                self.qi1.remove(self.qi1[-1])
                self.type = 1

#耍赖
    def shualai(self):
        self.choose = 9

if __name__ == '__main__':
    ai = Super_Game()
    ai.run_game()


