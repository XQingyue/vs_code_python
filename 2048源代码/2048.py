#2048
import pygame
import sys
import random
import time
from settings import Setting
from num_rect import Num_rect
def setup():
    '''
    初始化函数，包括
    初始化屏幕
    放置背景图像
    生成4*4二位矩阵的列表
    '''
    pygame.init()
    global screen
    global setting
    global img_matrix
    global pos_matrix
    global map_num
    global max_num
    map_num=0
    max_num=2
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_W,setting.screen_H))
    #二维图像矩阵
    img_matrix=[[0 for i in range(4)] for i in range(4)]
    #二维位置矩阵
    pos_matrix=[[(j*110+60,i*110+60) for j in range(4)] for i in range(4) ]

    pygame.display.set_caption('2048')
    update_function()
        
    

def run():
    '''
    初始化--
    （循环）--生成新数字--检查按键控制--执行按键控制---屏幕更新--
    '''
    while True:
        if map_num==16 or max_num==2048:
            pygame.quit()
            sys.exit()
        time.sleep(0.5)
        new(2)
        update_function();

        flag=1
        while flag:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type ==pygame.KEYUP:
                    flag=check_event(event)                
                    pass
                
        #a=Num_rect(2048,pos_matrix[2][0][0],pos_matrix[2][0][1],setting,screen)
        update_function()
        
        
def check_event(event):
    flag=0
    if event.key ==pygame.K_RIGHT:
        function_right()
        
    elif event.key ==pygame.K_LEFT:
        function_left()
        
    elif event.key ==pygame.K_UP:
        function_up()
        
    elif event.key ==pygame.K_DOWN:
        function_down()
        
    else :
        flag=1
    return flag

def function_up():
    global map_num
    for j in range(4):
        p1=0        
        for i in range(4):
            if img_matrix[p1][j]!=0:
                p1+=1
            elif img_matrix[i][j]==0:
                continue
            else:
                img_matrix[i][j],img_matrix[p1][j]=img_matrix[p1][j], img_matrix[i][j]                         
                img_matrix[p1][j].set_y(pos_matrix[p1][j][1])                
                p1+=1
                
    update_function()
    time.sleep(0.1)
    for j in range(4):
        m=[]        
        for i in range(4):
            if img_matrix[i][j] !=0:
                m.append(img_matrix[i][j].num)
            else:
                m.append(0)
        m_copy = m[:]
        mm = get_list(m)
        
        num1 = sum([ m_copy[i] and 1 for i in range(4)])
        num2 = sum([ mm[i] and 1 for i in range(4)])
        map_num=map_num - (num1 - num2)
        for i in range(4):
            if mm[i] != 0 :
                img_matrix[i][j].set_num(mm[i])
            else :
                img_matrix[i][j]=0
            
            
    pass


def function_down():
    global map_num
    for j in range(4):
        p1=3       
        for i in range(3,-1,-1):
            if img_matrix[p1][j]!=0:
                p1-=1
            elif img_matrix[i][j]==0:
                continue
            else:
                img_matrix[i][j],img_matrix[p1][j]=img_matrix[p1][j], img_matrix[i][j]                         
                img_matrix[p1][j].set_y(pos_matrix[p1][j][1])                
                p1-=1
                
    update_function()
    time.sleep(0.1)
    pass
    for j in range(4):
        m=[]        
        for i in range(3,-1,-1):
            if img_matrix[i][j] !=0:
                m.append(img_matrix[i][j].num)
            else:
                m.append(0)
        m_copy = m[:]
        mm = get_list(m)
        
        num1 = sum([ m_copy[i] and 1 for i in range(4)])
        num2 = sum([ mm[i] and 1 for i in range(4)])
        map_num=map_num - (num1 - num2)
        for i in range(3,-1,-1):
            if mm[3-i] != 0 :
                img_matrix[i][j].set_num(mm[3-i])
            else :
                img_matrix[i][j]=0    
        
def function_left():
    global map_num
    for i in range(4):
        p1=0    
        for j in range(4):
            if img_matrix[i][p1]!=0:
                p1+=1
            elif img_matrix[i][j]==0:
                continue
            else:
                img_matrix[i][j],img_matrix[i][p1]=img_matrix[i][p1], img_matrix[i][j]                         
                img_matrix[i][p1].set_x(pos_matrix[i][p1][0])                
                p1+=1
                
    update_function()
    time.sleep(0.1)
    for i in range(4):
        m=[]        
        for j in range(4):
            if img_matrix[i][j] !=0:
                m.append(img_matrix[i][j].num)
            else:
                m.append(0)
        m_copy = m[:]
        mm = get_list(m)
        
        num1 = sum([ m_copy[i] and 1 for i in range(4)])
        num2 = sum([ mm[i] and 1 for i in range(4)])
        map_num=map_num - (num1 - num2)
        for j in range(4):
            if mm[j] != 0 :
                img_matrix[i][j].set_num(mm[j])
            else :
                img_matrix[i][j]=0
    pass

def function_right():
    global map_num
    for i in range(4):
        p1=3    
        for j in range(3,-1,-1):
            if img_matrix[i][p1]!=0:
                p1-=1
            elif img_matrix[i][j]==0:
                continue
            else:
                img_matrix[i][j],img_matrix[i][p1]=img_matrix[i][p1], img_matrix[i][j]                         
                img_matrix[i][p1].set_x(pos_matrix[i][p1][0])                
                p1-=1
                
    update_function()
    time.sleep(0.1)
    for i in range(4):
        m=[]        
        for j in range(3,-1,-1):
            if img_matrix[i][j] !=0:
                m.append(img_matrix[i][j].num)
            else:
                m.append(0)
        m_copy = m[:]
        mm = get_list(m)
        
        num1 = sum([ m_copy[i] and 1 for i in range(4)])
        num2 = sum([ mm[i] and 1 for i in range(4)])
        map_num=map_num - (num1 - num2)
        for j in range(3,-1,-1):
            if mm[3-j] != 0 :
                img_matrix[i][j].set_num(mm[3-j])
            else :
                img_matrix[i][j]=0

def new(n):
    '''
    随机生成n个数字模块放置于空闲的矩阵位置
    '''
    global map_num
    for i in range(n):
        while True:
            a = random.randint(0,15)
            x = a//4
            y = a%4
            if img_matrix[x][y]==0:
                aa = Num_rect(2,pos_matrix[x][y][0],pos_matrix[x][y][1],setting,screen)
                img_matrix[x][y] = aa
                map_num+=1
                if map_num==16:
                    return
                break
            else:
                continue

def update_function():
    screen.blit(setting.screen_background,(0,0))
    for i in range(4):
        for j in range(4):
            if img_matrix[i][j]!=0:
                img_matrix[i][j].show()
    pygame.display.flip()
    

def list_right(m):
    for i in range(3):
        if m[i]==0:
            return 1
        elif m[i]==m[i+1]:
            return 0
    return 1


def get_list(m):
    global max_num
    while True:
        p1=0
        p2=0
        a = [0,0,0,0]
        if list_right(m):
            max_num = max_num if max_num > max(m) else max(m)
            return m
        else:
            while p1<=3:
                if m[p1]==0:
                    p1+=1
                    continue
                elif p1==3:
                    a[p2]=m[p1]
                    break
                elif m[p1]==m[p1+1]:
                    a[p2]=m[p1]*2
                    m[p1+1]=0
                    p2+=1
                else:
                    a[p2]=m[p1]
                    p2+=1
                p1+=1
            m = a
    pass
if __name__ == '__main__':
    setup()
    try:
        run()
    except :
        pygame.quit()
        sys.exit()


