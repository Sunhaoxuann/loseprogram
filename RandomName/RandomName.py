#导入模块
import random
import time
import pygame
import base64
#定义函数
def ifquit(eventlist):#判断是否退出
    for event in eventlist:
        if event.type == pygame.QUIT:
            return True
def clean1(windows):
    windows.fill(light_background)
    pygame.draw.rect(screen,deep_background,(0,0,385,27))
def draw_useable_circle(screen,state):
    if state == True:
        pygame.draw.circle(screen,green,(15,14),9,0)
    else:
        pygame.draw.circle(screen,red,(15,14),9,0)
def fonts(stringlist):
    for string in stringlist:
        font.render(string,True,red)
        font.render(string,True,green)
        font.render(string,True,black)
def button(screen,state,postion):
    if postion == True:
        pygame.draw.rect(screen,(201,201,201),(258,144,34,18))
        screen.blit(font.render(stringlist[3],True,green),(301,136))
        pygame.draw.rect(screen,green,(259,145,32,16))
        pygame.draw.rect(screen,deep_background,(259,145,16,16))
    elif postion == False:
        pygame.draw.rect(screen,(201,201,201),(258,144,34,18))
        screen.blit(font.render(stringlist[2],True,red),(301,136))
        pygame.draw.rect(screen,red,(259,145,32,16))
        pygame.draw.rect(screen,deep_background,(275,145,16,16))
    # if state == True and postion == False:
        # 
    # else:
        
def basicwindows(screen,state):
    clean1(screen)
    draw_useable_circle(screen,state)
    if state == True:
        screen.blit(font.render(stringlist[1],True,green),(30,0))
    else:
        screen.blit(font.render(stringlist[0],True,red),(30,0))
    button(screen,True,False)
    

#初始化
pygame.init()
#定义初始变量
windows_state = True #窗口状态
namelist = ['叶杨阳', '肖逸凡', '王沐恩', '黄皓轩', '项涵哲', '邹帆', '闻张依', '翁睿毅', '李御轩', '张峰铭', '韦思桐', '沈凯昕', '林浩', '吴珈栩', '袁晓晴', '于妙盈', '俞昭阳', '申屠绍越', '姚智宇', '陶奕畅', '孙昊轩', '高智杰', '严天浩', '李嘉怡', '何相南', '黄圣曦', '周炜昊', '吴文萱', '李乐山', '殷一铭', '蒋一凡', '孙周哲翊', '沈雨涵', '程天宇', '郑杰', '蒋哲聪', '徐书亚', '林馨雯', '方浩如', '刘翔', '边峻熙', '叶俊浩', '张可维', '李宏振', '高浩哲', '产洲俊', '王博辉', '陈沈捷'] #名字列表
stringlist = ['抽取中...','等待抽取','可以重复','不可重复']
green = (25,100,25)
red = (232,17,35)
black = (0,0,0)
light_background = (241,241,241)
deep_background = (220,220,220)
font = pygame.font.SysFont('华文楷体', 20)
#预渲染
fonts(stringlist)
fonts(namelist)
#窗口
screen = pygame.display.set_mode((385,168))
basicwindows(screen,False)
#主函数
while windows_state:
    events = pygame.event.get()#获取事件
    if ifquit(events): #判断是否退出
        windows_state = False
    else:#主体逻辑
        
        for event in events:
            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 258<=event.pos[0]<=292 and 144<=event.pos[1]<=162:
                ...
    pygame.display.update()