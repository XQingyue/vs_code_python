import pygame
class Setting():
    def __init__(self):
        #屏幕参数
        
        self.screen_W = 450
        self.screen_H = 450
        self.screen_background = pygame.image.load('photo/1.1.jpg')

        
        
        #相关的图片资源
        self.num_2 =pygame.image.load('photo/2.jpg')
        self.num_4 =pygame.image.load('photo/4.jpg')
        self.num_8 =pygame.image.load('photo/8.jpg')
        self.num_16 =pygame.image.load('photo/16.jpg')
        self.num_32 =pygame.image.load('photo/32.jpg')
        self.num_64 =pygame.image.load('photo/64.jpg')
        self.num_128 =pygame.image.load('photo/128.jpg')
        self.num_256 =pygame.image.load('photo/256.jpg')
        self.num_512 =pygame.image.load('photo/512.jpg')
        self.num_1024 =pygame.image.load('photo/1024.jpg')
        self.num_2048 =pygame.image.load('photo/2048.jpg')  

        self.num_image = [self.num_2,self.num_4,self.num_8,self.num_16,
                          self.num_32,self.num_64,self.num_128,self.num_256,
                          self.num_512,self.num_1024,self.num_2048]
        
        
        
        

        

        
      
