import pygame
import math
class Num_rect():
    '''
    数字图像类
    '''
    def __init__(self,num,x,y,setting,screen):
        self.num = num
        self.setting =setting
        self.image = setting.num_image[int(math.log2(num))-1]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.screen = screen
        pass

    def set_x(self,x):
        self.rect.centerx = x

    def set_y(self,y):
        self.rect.centery = y

    def show(self):
        self.screen.blit(self.image,self.rect)
        
    def set_num(self,num):
        self.num = num
        self.image =self.setting.num_image[int(math.log2(num))-1]
