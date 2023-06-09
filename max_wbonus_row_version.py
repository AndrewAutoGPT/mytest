#import 
import numpy as py
import pandas as pd
import math
import copy
#import xlsxwriter
import xlwt

#workbook = xlsxwriter.Workbook("MaxCal.xls")
workbook = xlwt.Workbook()    
sheet1 = workbook.add_sheet("every step",cell_overwrite_ok=True)
sheet2 = workbook.add_sheet("step rate",cell_overwrite_ok=True)
sheet3 = workbook.add_sheet("rate avg",cell_overwrite_ok=True)
sheet4 = workbook.add_sheet("all ",cell_overwrite_ok=True)
sheet5 = workbook.add_sheet("gap ",cell_overwrite_ok=True)
sheet6 = workbook.add_sheet("list compare",cell_overwrite_ok=True)

x=0
one_roll=[0,0,0,0,0,0,0,0,0,0] #ten ball
wz=[0,0,0,0,0,0,0,0,0,0,1] #ten ball & one counter
total_w_n=[0,0,0,0,0]

#ball in string
wb=wz[:]
rb=wz[:]
bb=wz[:]
yb=wz[:]
gb=wz[:]

win_one=one_roll[:]
win_two=one_roll[:]
win_three=one_roll[:]
win_four=one_roll[:]
win_five=one_roll[:]

win_reset=py.array(py.arange(50).reshape(1,5,10))
win_all=py.array(py.arange(50).reshape(1,5,10))

#ball in number
n_wb=wz[:]
n_rb=wz[:]
n_bb=wz[:]
n_yb=wz[:]
n_gb=wz[:]


#setup the balls value in string and numbers
x=0
while x<10:
    
    #check count
    #print(wz[x])

    n_wb[x]=x+1
    n_rb[x]=x+11
    n_bb[x]=x+21
    n_yb[x]=x+31
    n_gb[x]=x+41

##    win_one[x]='wb'+str(x+1)
##    win_two[x]='rb'+str(x+11)
##    win_three[x]='bb'+str(x+21)
##    win_four[x]='yb'+str(x+31)
##    win_five[x]='gb'+str(x+41)
    x=x+1

#del gb[10]

#get file
file=r'max2.xls'

print(win_five)
game=pd.read_excel(file,index=0)
game_len=len(game.columns)
print("this is lenght of game"+str(game_len))
game_1=game.iloc[0:8,0:]
game_1=py.array(game_1)
#print(game_1)
#game_1.astype(int)
game_2=str(game.iloc[-1,1:]).replace("Bonus","")
game_2=py.array(game_2)

###############################################################
#-----------------START arrange wining # in 2D array---------##
###############################################################
print("allllllllllllllllllllllll")
x=0
xx=0
y=int(0)
y=int(game_len)
win_ball=(5,10,y)
win_b_reset=[]
y=0

all_num=py.array(py.arange(55).reshape(1,5,11))
win_b_reset=py.array(py.arange(55).reshape(1,5,11))
total_w_num=py.array(py.arange(5).reshape(1,1,5))
total_w_reset=py.array(py.arange(5).reshape(1,1,5))

zero_even_win=[0,0,0,0,0,0,0,0,0]
wb_123=zero_even_win[:]
rb_123=zero_even_win[:]
bb_123=zero_even_win[:]
yb_123=zero_even_win[:]
gb_123=zero_even_win[:]
reset_123=zero_even_win[:]
gap_ww=0   #counters for win
gap_wl=0
gap_rw=0
gap_rl=0
gap_bw=0
gap_bl=0
gap_yw=0
gap_yl=0
gap_gw=0
gap_gl=0   #counter for lose
reset_123=zero_even_win[:]
win_list=[0,0,0,0,0]

y=0
while y<game_len:

    #reset all the values
    print("this is y:"+ str(y))
    wb=[0,0,0,0,0,0,0,0,0,0,0]
    rb=[0,0,0,0,0,0,0,0,0,0,0]
    bb=[0,0,0,0,0,0,0,0,0,0,0]
    yb=[0,0,0,0,0,0,0,0,0,0,0]
    gb=[0,0,0,0,0,0,0,0,0,0,0]
    win_one=[0,0,0,0,0,0,0,0,0,0]
    win_two=[0,0,0,0,0,0,0,0,0,0]
    win_three=[0,0,0,0,0,0,0,0,0,0]
    win_four=[0,0,0,0,0,0,0,0,0,0]
    win_five=[0,0,0,0,0,0,0,0,0,0]

    w=0
    r=0
    b=0
    yy=0
    g=0
    # end of reset
    
#    print("this is y in game1")
#    print(str(y))
    x=int(0)
    while x<8:
#        print(game_1[x,y])
#        x=x+1
        win_ball=(game_1[x,y])
##        print("this is win_ball:"+str(win_ball))
##        print(win_ball)
        
        if win_ball>0 and win_ball<11:
            
            if win_ball==1:
                wb[0]=win_ball
                win_one[0]=1
            elif win_ball==2:
                wb[1]=win_ball
                win_one[1]=2
            elif win_ball==3:
                wb[2]=win_ball
                win_one[2]=3
            elif win_ball==4:
                wb[3]=win_ball
                win_one[3]=4
            elif win_ball==5:
                win_one[4]=5
                wb[4]=win_ball
            elif win_ball==6:
                wb[5]=win_ball
                win_one[5]=6
            elif win_ball==7:
                wb[6]=win_ball
                win_one[6]=7
            elif win_ball==8:
                wb[7]=win_ball
                win_one[7]=8
            elif win_ball==9:
                wb[8]=win_ball
                win_one[8]=9
            elif win_ball==10:
                wb[9]=win_ball
                win_one[9]=10
            else:
                print("some thing wrong in One")
#            wb[w]=win_ball
#            print(win_ball)
#            print(wb)
            
            wb[10]=w+1
            w=w+1
            
        elif win_ball>=11 and win_ball<=20:
        
            if win_ball==11:
                win_two[0]=11
                rb[0]=win_ball
            elif win_ball==12:
                win_two[1]=12
                rb[1]=win_ball
            elif win_ball==13:
                win_two[2]=13
                rb[2]=win_ball
            elif win_ball==14:
                win_two[3]=14
                rb[3]=win_ball
            elif win_ball==15:
                win_two[4]=15
                rb[4]=win_ball
            elif win_ball==16:
                win_two[5]=16
                rb[5]=win_ball
            elif win_ball==17:
                win_two[6]=17
                rb[6]=win_ball
            elif win_ball==18:
                win_two[7]=18
                rb[7]=win_ball
            elif win_ball==19:
                win_two[8]=19
                rb[8]=win_ball
            elif win_ball==20:
                win_two[9]=20
                rb[9]=win_ball
            else:
                print("some thing wrong in Ten")
#            rb[r]=win_ball
#            print(win_ball)
#            print(rb)
            win_reset=win_one
            
            rb[10]=r+1
            r=r+1
        elif win_ball>=21 and win_ball<=30:
            if win_ball==21:
                win_three[0]=21
                bb[0]=win_ball
            elif win_ball==22:
                win_three[1]=22
                bb[1]=win_ball
            elif win_ball==23:
                win_three[2]=23
                bb[2]=win_ball
            elif win_ball==24:
                win_three[3]=24
                bb[3]=win_ball
            elif win_ball==25:
                win_three[4]=25
                bb[4]=win_ball
            elif win_ball==26:
                win_three[5]=26
                bb[5]=win_ball
            elif win_ball==27:
                win_three[6]=27
                bb[6]=win_ball
            elif win_ball==28:
                win_three[7]=28
                bb[7]=win_ball
            elif win_ball==29:
                win_three[8]=29
                bb[8]=win_ball
            elif win_ball==30:
                win_three[9]=30
                bb[9]=win_ball
            else:
                print("some thing wrong in Tow")
#            bb[b]=win_ball
#            print(win_ball)
#            print(bb)
            b=b+1
            bb[10]=b
        elif win_ball>=31 and win_ball<=40:
            if win_ball==31:
                win_four[0]=31
                yb[0]=win_ball
            elif win_ball==32:
                win_four[1]=32
                yb[1]=win_ball
            elif win_ball==33:
                win_four[2]=33
                yb[2]=win_ball
            elif win_ball==34:
                win_four[3]=34
                yb[3]=win_ball
            elif win_ball==35:
                win_four[4]=35
                yb[4]=win_ball
            elif win_ball==36:
                win_four[5]=36
                yb[5]=win_ball
            elif win_ball==37:
                win_four[6]=37
                yb[6]=win_ball
            elif win_ball==38:
                win_four[7]=38
                yb[7]=win_ball
            elif win_ball==39:
                win_four[8]=39
                yb[8]=win_ball
            elif win_ball==40:
                win_four[9]=40
                yb[9]=win_ball
            else:
                print("some thing wrong in Three")
#            yb[yy]=win_ball
#            print(win_ball)
#            print(yb)
            yy=yy+1
            yb[10]=yy
        elif win_ball>=41 and win_ball<=50:
            if win_ball==41:
                win_five[0]=41
                gb[0]=win_ball
            elif win_ball==42:
                win_five[1]=42
                gb[1]=win_ball
            elif win_ball==43:
                win_five[2]=43
                gb[2]=win_ball
            elif win_ball==44:
                win_five[3]=44
                gb[3]=win_ball
            elif win_ball==45:
                win_five[4]=45
                gb[4]=win_ball
            elif win_ball==46:
                win_five[5]=46
                gb[5]=win_ball
            elif win_ball==47:
                win_five[6]=47
                gb[6]=win_ball
            elif win_ball==48:
                win_five[7]=48
                gb[7]=win_ball
            elif win_ball==49:
                win_five[8]=49
                gb[8]=win_ball
            elif win_ball==50:
                win_five[9]=50
                gb[9]=win_ball
            else:
                print("some thing wrong in Four")
#            gb[g]=win_ball
#            print(win_ball)
#            print(gb)
            g=g+1
            gb[10]=g
        else:
            print("some thing wrong")
        x=x+1
        
#start to check the time gap between win and lose
#    small=min(win_list)
#    big=max(win_list)
#    gap=0
#    win_all=py.array([[win_one,win_two,win_three,win_four,win_five]])
#    all_num=py.array([[wb,rb,bb,yb,gb]])
#    win_all=py.array([[win_one,win_two,win_four,win_five]])

#end of cehck the time gap
    wb_n=wb[10]
    rb_n=rb[10]
    bb_n=bb[10]
    yb_n=yb[10]
    gb_n=gb[10]
          
    if y==0:
        all_num=py.array([[wb,rb,bb,yb,gb]])
        win_all=py.array([[win_one,win_two,win_four,win_five]])
        total_w_num=py.array([[wb[10],rb[10],bb[10],yb[10],gb[10]]])
        print("*****all_num in y=0******")
        print(all_num)
        
        #set up count the winning time and gap
        win_list=py.array([[wb[10],rb[10],bb[10],yb[10],gb[10]]])
        small=py.min(win_list)
        big=py.max(win_list)
        #print("win list:"+str(win_list)+" y:"+str(y))
        print("max:"+str(big)+" min:"+str(small))
        
        if big==wb[10]:
            wb_123=([y,gap_ww,big,0,0,0,0,0,0])
            wb_123=py.array([[wb_123]])
            print(wb_123)
            gap_ww=y
        elif rb[10]==big:
            rb_123=[y,gap_rw,rb[10],0,0,0,0,0,0]
            gap_rw=y
        elif bb[10]==big:
            bb_123=[y,gap_bw,bb[10],0,0,0,0,0,0]
            gap_bw=y
        elif yb[10]==big:
            yb_123=[y,gap_yw,yb[10],0,0,0,0,0,0]
            gap_yw=y
        elif gb[10]==big:
            gb_123=[y,gap_rw,gb[10],0,0,0,0,0,0]
            gap_gw=y
            
        #for the small number
        elif wb[10]==small:
            wb_123=([0,0,0,0,0,0,y,gap_wl,small])
            wb_123=py.array([[wb_123]])
            print(wb_123)
            gap_wl=y
        elif gb[10]==big:
            rb_123=[0,0,0,0,0,0,0,y,gap_rl,rb[10]]
            gap_rl=y
        elif wb[10]==small:
            bb_123=[0,0,0,0,0,0,y,gap_bl,bb[10]]
            gap_bl=y
        elif gb[10]==big:
            yb_123=[0,0,0,0,0,0,y,gap_yl,gb[10]]
            gap_yl=y
        elif gb[10]==big:
            gb_123=[0,0,0,0,0,0,y,gap_gl,gb[10]]
            gap_gl=y
    else:
        win_b_reset=py.array([[wb,rb,bb,yb,gb]])
        win_reset=py.array([[win_one,win_two,win_four,win_five]])
        total_w_reset=py.array([[wb[10],rb[10],bb[10],yb[10],gb[10]]])
        #print("test")
        #print(win_b_reset)
        #print("all_num")
        all_num=py.append(all_num,win_b_reset,axis=0)
        win_all=py.append(win_all,win_reset,axis=0)
        total_w_num=py.append(total_w_num,total_w_reset,axis=0)
        
        #print(total_w_num)
        #print(all_num)
#       all_num=py.array(all_num)

        #set up count the winning time and gap
        win_list=total_w_num
        small=py.min(win_list)
        big=py.max(win_list)
        #print("win list: at y"+str(win_list)+" y:"+str(y))
        print("max:"+str(big)+" min:"+str(small))
        
        if big==wb[10]:
            print("y:"+str(y)+" gap_ww:"+str(gap_ww))
            gap_ww=y-gap_ww
            print(str(gap_ww))
            #zero_even_win=[y,gap_ww,big,0,0,0,0,0,0]
            #reset_123=([[zero_even_win]])
            reset_123=py.array([[y,gap_ww,big,0,0,0,0,0,0]])
            #wb_123=py.array(wb_123)
            #wb_123=py.insert(wb_123,[0,0],[y,gap_ww,big,0,0,0,0,0,0],axis=0)
            #wb_123=py.array([[wb_123]])
            print("this is wb_123 big:"+str(reset_123))
            gap_ww=y
            print("wb_123: gap"+str(gap_ww))
        elif rb[10]==big:
            gap_rw=y-gap_rw
            rb_123=[y,gap_rw,rb[10],0,0,0,0,0,0]
            gap_rw=y
        elif bb[10]==big:
            gap_bw=y-gap_bw
            bb_123=[y,gap_bw,bb[10],0,0,0,0,0,0]
            gap_bw=y
        elif yb[10]==big:
            gap_yw=y-gap_yw
            yb_123=[y,gap_yw,yb[10],0,0,0,0,0,0]
            gap_yw=y
        elif gb[10]==big:
            gap_gw=y-gap_gw
            gb_123=[y,gap_rw,gb[10],0,0,0,0,0,0]
            gap_gw=y
            
        #for the small number
        elif wb[10]==small:
            #reset_123=(wb_123)
            print("y:"+str(y)+" gap_wl:"+str(gap_wl))
            gap_wl=y-gap_wl
            print(str(gap_wl))
            #zero_even_win=[y,gap_ww,big,0,0,0,0,0,0]
            #reset_123=([[zero_even_win]])
            reset_123=py.array([[y,gap_wl,small,0,0,0,0,0,0]])
            wb_123=py.array(wb_123)
            #wb_123=py.append(wb_123,reset_123,axis=0)
            #wb_123=py.array([[wb_123]])
            print("this is small wb:"+str(reset_123))
            gap_wl=y
            print("wb_123: gap"+str(gap_wl))
        elif rb[10]==small:
            gap_rl=y-gap_rl
            rb_123=[0,0,0,0,0,0,0,y,gap_rl,rb[10]]
            gap_rl=y
        elif bb[10]==small:
            gap_bl=y-gap_bl
            bb_123=[0,0,0,0,0,0,y,gap_bl,bb[10]]
            gap_bl=y
        elif yb[10]==big:
            gap_yl=y-gap_yl
            yb_123=[0,0,0,0,0,0,y,gap_yl,gb[10]]
            gap_yl=y
        elif gb[10]==big:
            gap_gl=y-gap_gl
            gb_123=[0,0,0,0,0,0,y,gap_gl,gb[10]]
            gap_gl=y

        
    y=y+1    
# End of the while


print("#########################")
#all_num=py.reshape(63,5,11)
print("all_num[}")
print(win_all)
#print(all_num[61,1,5])

print("\n new line \n")
    

total_w_num=py.array(total_w_num,dtype=float)  #detail of each group
print("total_w_num")
print(total_w_num)

win_precetage=total_w_num/game_len
print("win_precentage:")
print(win_precetage)


big_small=py.array(total_w_num)
all_sum=all_num.sum(axis=0)
all_sum=all_sum.astype(float)

real_num=py.array([n_wb,n_rb,n_bb,n_yb,n_gb])

print("total win from big to small roll")
print(big_small.sum(axis=0))
      
print("49 # win times  all_sum:")
print(all_sum)
real_num=real_num.astype(float)
even_num=py.array(all_sum/real_num)
print("even_num")
print(even_num)
print("******* precetage of the winning********")
time_of_game=py.array(py.arange(55).reshape(1,5,11))
#py.time_of_game((5, 11), 48, dtype=float)
precent_ofWin=py.array(even_num/game_len)
print(precent_ofWin)

#game_2=py.array(game_2)
#game_2=game_2.replace("Bonus","")
print(game_2)


############ End of Arrange winning # in to 2D array ##########        

####################################################################
#-------------- END of arrange win number and counting-------------#
####################################################################

#*********************************************#
#******    began random visualize    *********#
#*********************************************#
import random as ra
win_all=[win_one,win_two,win_three,win_four,win_five]
#print(wb_123)
#ra.shuffle(win_all)
#win_all=py.array(win_all)
print(win_all)

print("*****************test wb_123 big")
print(wb_123)

SumWinRoll=py.array(py.arange(5).reshape(1,1,5))
SumWinReset=[0,0,0,0,0]
print("wining of 0-6")
x=0
while x<7:
    if x==0:
        SumWinRoll=[sum(total_w_num==int(x))]
    else:
        SumWinReset=[sum(total_w_num==int(x))]
        SumWinRoll=py.append(SumWinRoll,SumWinReset,axis=0)
    x=x+1

print(" this is SumWinRoll ")
print(SumWinRoll)
print(" this is even_num")
print(even_num)
##print("this is all_num")
##print(all_num)

x=0
y=0
k=0
step_cal=py.array(py.arange(55).reshape(1,5,11))
step_reset=py.array(py.arange(55).reshape(1,5,11))
step_every=py.array(py.arange(55).reshape(1,5,11))
step_every_reset=py.array(py.arange(55).reshape(1,5,11))
total_step=py.array(py.arange(55).reshape(1,5,11))


startK=game_len
x=0
while x<startK:
    step_cal=py.zeros((1,5,11),dtype=int)
    step_reset=py.zeros((1,5,11),dtype=int)
    y=x
    while y<game_len:
        if y==x:
            step_cal=py.array([all_num[y]])
            print("this is step cal in the first***c*******")
            print(step_cal)
        else:
            step_reset=py.array([all_num[y]])
            step_cal=py.append(step_cal,step_reset,axis=0)
        
        y=y+1
        #print("this is y"+str(y))
 
    

##    print("this is step_cal")    
##    print(step_cal)
        
    print("this is total step"+str(len(step_cal)))
    
    total_step=step_cal.sum(axis=0)
    num_total_step=total_step/real_num
    
    print("this is num_total_step")
    print(num_total_step)
    
    print("this is precentage of the step")
    precen_total_step=(num_total_step/50)*100
    print(precen_total_step)
    
    if x==0:
        step_every=py.array([num_total_step])
    elif x>0:
        step_every_reset=py.array([num_total_step])
        step_every=py.append(step_every,step_every_reset,axis=0)
        
    

    x=x+1

print("this is step_every")
print(step_every)

step_avg=step_every/startK
print("the step_avg")
print(step_avg)

print("total_w_num")
print(total_w_num)

print(" ")
all_roll_win_total=total_w_num.sum(axis=0)
print(all_roll_win_total)

min_total_w_num=min(all_roll_win_total)
print("this is the min of the win #")
print(min_total_w_num)

max_total_w_num=max(all_roll_win_total)
print("this is the max of the win #")
print(max_total_w_num)

total_w_num1=total_w_num[1:]
all_roll_win_total1=total_w_num1.sum(axis=0)
total_w_num2=total_w_num[2:]
all_roll_win_total2=total_w_num2.sum(axis=0)
total_w_num3=total_w_num[3:]
all_roll_win_total3=total_w_num3.sum(axis=0)
total_w_num4=total_w_num[4:]
all_roll_win_total4=total_w_num4.sum(axis=0)


print("total_w_num1")
print(total_w_num1)
print("the next total")

print(all_roll_win_total/game_len*100)
print(all_roll_win_total1/(game_len-1)*100)
print(all_roll_win_total2/(game_len-2)*100)
print(all_roll_win_total3/(game_len-3)*100)
print(all_roll_win_total4/(game_len-4)*100)

print(all_roll_win_total1)
print(all_roll_win_total2)
print(all_roll_win_total3)
print(all_roll_win_total4)

print(str(game_len))

differ=step_every[1]-step_every[2]
print("here is different")
print(step_every[2])
print("step 2")
print(step_every[3])
print("step 3")
print("difer")
print(differ)
print("all num:")
print(all_num)
print("                   ")
print(all_num[51,:,:])
print("                   ")
print(all_num[52,:,:])

all_num_1=py.array(all_num[1:,:,:])
all_num_2=py.array(all_num[2:,:,:])
all_num_3=py.array(all_num[3:,:,:])
all_num_4=py.array(all_num[4:,:,:])
all_num_5=py.array(all_num[5:,:,:])
all_num_6=py.array(all_num[6:,:,:])
all_num_7=py.array(all_num[7:,:,:])
all_num_8=py.array(all_num[8:,:,:])
all_num_9=py.array(all_num[9:,:,:])
all_num_10=py.array(all_num[10:,:,:])
all_num_11=py.array(all_num[11:,:,:])
all_num_12=py.array(all_num[12:,:,:])
##all_num_go=py.array(py.arange(55).reshape(1,5,11))


all_num_all=all_num.sum(axis=0)
all_num_1sum=all_num_1.sum(axis=0)
all_num_2sum=all_num_2.sum(axis=0)
all_num_3sum=all_num_3.sum(axis=0)
all_num_4sum=all_num_4.sum(axis=0)
all_num_5sum=all_num_5.sum(axis=0)
all_num_6sum=all_num_6.sum(axis=0)
all_num_7sum=all_num_7.sum(axis=0)
all_num_8sum=all_num_8.sum(axis=0)
all_num_9sum=all_num_9.sum(axis=0)
all_num_10sum=all_num_10.sum(axis=0)
all_num_11sum=all_num_11.sum(axis=0)
all_num_12sum=all_num_12.sum(axis=0)

print("this is  all_num_all  sum of all num")
##all_num_1sum=all_num_1.sum(axis=0)
##all_num_5sum=all_num_5.sum(axis=0)
##all_num_7sum=all_num_7.sum(axis=0)
##all_num_10sum=all_num_10.sum(axis=0)
##all_num_15sum=all_num_15.sum(axis=0)
##all_num_20sum=all_num_20.sum(axis=0)

##print(all_num_1sum)
##print(" ")
all_num_even=all_num_all/real_num
all_num_1even=all_num_1sum/real_num
all_num_2even=all_num_2sum/real_num
all_num_3even=all_num_3sum/real_num
all_num_4even=all_num_4sum/real_num
all_num_5even=all_num_5sum/real_num
all_num_6even=all_num_6sum/real_num
all_num_7even=all_num_7sum/real_num
all_num_8even=all_num_8sum/real_num
all_num_9even=all_num_9sum/real_num
all_num_10even=all_num_10sum/real_num
all_num_11even=all_num_11sum/real_num
all_num_12even=all_num_12sum/real_num


##all_num_1even=all_num_1sum/real_num
##all_num_5even=all_num_5sum/real_num
##all_num_7even=all_num_7sum/real_num
##all_num_10even=all_num_10sum/real_num
##all_num_15even=all_num_15sum/real_num
##all_num_20even=all_num_20sum/real_num

all_even_pre0=(all_num_even/(game_len*7))*100
all_even_pre1=(all_num_1even/((game_len-1)*7))*100
all_even_pre2=(all_num_2even/((game_len-2)*7))*100
all_even_pre3=(all_num_3even/((game_len-3)*7))*100
all_even_pre4=(all_num_4even/((game_len-4)*7))*100
all_even_pre5=(all_num_5even/((game_len-5)*7))*100
all_even_pre6=(all_num_6even/((game_len-6)*7))*100
all_even_pre7=(all_num_7even/((game_len-7)*7))*100
all_even_pre8=(all_num_8even/((game_len-8)*7))*100
all_even_pre9=(all_num_9even/((game_len-9)*7))*100
all_even_pre10=(all_num_10even/((game_len-10)*7))*100
all_even_pre11=(all_num_11even/((game_len-11)*7))*100
all_even_pre12=(all_num_12even/((game_len-12)*7))*100

#### average of the pre rate
all_even_pre_avg=all_even_pre0+all_even_pre1+all_even_pre2+all_even_pre3
all_even_pre_avg=all_even_pre_avg+all_even_pre4+all_even_pre5+all_even_pre6+all_even_pre7
all_even_pre_avg=all_even_pre_avg+all_even_pre8+all_even_pre9+all_even_pre10+all_even_pre11+all_even_pre12
all_even_pre_avg=all_even_pre_avg/13

##print("this is all_even_pre average")
##print(all_even_pre_avg)
##print("this is all num even_pre0")
##print(all_even_pre0)
##print("this is all num 1")
##print(all_even_pre1)
##print("this is all num 2")
##print(all_even_pre2)


##all_even_pre1=(all_num_1even/(game_len-1))*100
##all_even_pre5=(all_num_5even/(game_len-5))*100
##all_even_pre7=(all_num_7even/(game_len-7))*100
##all_even_pre10=(all_num_10even/(game_len-10))*100
##all_even_pre15=(all_num_15even/(game_len-15))*100
##all_even_pre20=(all_num_20even/(game_len-20))*100

##all_even_pre=py.array(py.arange(55).reshape(1,5,11))



##
##print("rate betweent avg to 1")
##print(all_even_pre_avg-all_even_pre1)
##print(" ")
##print("rate betweent avg to 2")
##print(all_even_pre_avg-all_even_pre2)
##print(" ")
##print("rate betweet avg-3 ")
##print(all_even_pre_avg-all_even_pre3)
##print(" ")
##print("rate from 1-5 ")
##print(all_even_pre1-all_even_pre5)
##print(" ")
##print("rate from 1-6 ")
##print(all_even_pre1-all_even_pre6)
##print(" ")
##print("rate from 1-7 ")
##print(all_even_pre1-all_even_pre7)
##print(" ")
##print("rate from 1-8 ")
##print(all_even_pre1-all_even_pre8)
##print(" ")
##print("rate from 1-9 ")
##print(all_even_pre1-all_even_pre9)
##print(" ")
##print("rate from 1-10 ")
##print(all_even_pre1-all_even_pre10)
##print(" ")
##print("rate from 1-11 ")
##print(all_even_pre1-all_even_pre11)
##print(" ")
##print("rate from 1-12 ")
##print(all_even_pre1-all_even_pre12)
##print(" ")
##print("rate from 1-2 ")
##print(all_even_pre1-all_even_pre2)
##print(" ")
##print("rate from 1-2 ")
##print(all_even_pre1-all_even_pre2)
##print(" ")
##
##print(all_even_pre7)
##print(" ")
##print(all_even_pre10)
##print(" ")
##print(all_even_pre15)
##print(" ")
##print(all_even_pre20)
##print(" ")
##print(all_even_pre20-all_even_pre1)
##print(" ")
##print(" ")




##print(even_num)
##differ_5=all_num_1even-all_num_5even
##differ_7=all_num_5even-all_num_7even
##differ_10=all_num_7even-all_num_10even
##differ_15=all_num_10even-all_num_15even
##differ_20=all_num_15even-all_num_20even
##
##print("this is the different 1-5")
##print(differ_5)
##
##print("this is the different 5-7")
##print(differ_7)
##
##print("this is the different 7-10")
##print(differ_10)
##
##print("this is the different 10-15")
##print(differ_15)
##
##print("this is the different 15-20")
##print(differ_20)
##
##print("total differ")
##total_differ=differ_5+differ_7+differ_10+differ_15+differ_20
##print(total_differ)

print("******* estimate shortage precetage of the winning********")
print("this is all_even_pre average")
print(all_even_pre_avg)
print(" ")
est0=all_even_pre_avg-all_even_pre0
print("estimatation 1 ")
print(est0)
est5=all_even_pre_avg-all_even_pre5
print(" ")
print("estimatation 5 ")
print(est5)
est10=all_even_pre_avg-all_even_pre10
print(" ")
print("estimatation 10 ")
print(est10)

print("\n out 10")
out5=est0+est5+est10
print(out5)

print(total_w_num1.sum(axis=0))
print("all_num_1sum")
print(all_num_1sum)


all_even_0=(all_num_even/(game_len*7))*100
all_even_1=(all_num_1even/(game_len*7))*100
all_even_2=(all_num_2even/(game_len*7))*100
all_even_3=(all_num_3even/(game_len*7))*100

print(" ")
print(all_even_0)
print(" ")
print(all_even_1)
print(" ")
print(all_even_2)
print(" ")
print(all_even_3)

print("all even 0-10")
print(all_num_even)
print(" ")
print(all_num_1even)
print(" ")
print(all_num_2even)
print(" ")
print(all_num_3even)
print(" ")
print(all_num_4even)
print(" ")
print(all_num_5even)
print(" ")
print(all_num_6even)
print(" ")
print(all_num_7even)
print(" ")
print(all_num_8even)
print(" ")
print(all_num_9even)
print(" ")

### print out all the winning time of all number
x=0
all_num_any=[]
all_num_anySum=[]
print("/n this is winning time......")
while x<game_len:
    all_num_any=py.array(all_num[x:,:,:])
    all_num_anySum=all_num_any.sum(axis=0)
    all_num_anyEven=all_num_anySum/real_num
    print(" ")
    #print("this is :"+str(x)+" even")
    #print(all_num_anyEven)
    #print("winning gap")
    a=((game_len-x)/all_num_anyEven)
    a=py.around(a, decimals=2)
    
    print(a)
    x=x+1

x=0
k=0
z=[0,0,0,0,0,0]
k0=z[:]
k1=z[:]
k2=z[:]
k3=z[:]
k4=z[:]


k00=py.array(py.arange(6).reshape(1,1,6))
k11=py.array(py.arange(6).reshape(1,1,6))
k22=py.array(py.arange(6).reshape(1,1,6))
k33=py.array(py.arange(6).reshape(1,1,6))
k44=py.array(py.arange(6).reshape(1,1,6))
zz=py.array(py.arange(6).reshape(1,1,6))

print(" ")
print("total_w_num")
x=game_len-1
while x>-1:
    
    #print(total_w_num[x])
    y=0
    while y<5:
        k=total_w_num[x,y]
        if y==0:
            if k==0:
                k0[0]=k0[0]+1
            elif k==1:
                k0[1]=k0[1]+1
            elif k==2:
                k0[2]=k0[2]+1
            elif k==3:
                k0[3]=k0[3]+1
            elif k==4:
                k0[4]=k0[4]+1
            elif k==5:
                k0[5]=k0[5]+1
            else:
                print("k0 over 6")
        elif y==1:
            if k==0:
                k1[0]=k1[0]+1
            elif k==1:
                k1[1]=k1[1]+1
            elif k==2:
                k1[2]=k1[2]+1
            elif k==3:
                k1[3]=k1[3]+1
            elif k==4:
                k1[4]=k1[4]+1
            elif k==5:
                k1[5]=k1[5]+1
            else:
                print("k1 over 6")
        elif y==2:
            if k==0:
                k2[0]=k2[0]+1
            elif k==1:
                k2[1]=k2[1]+1
            elif k==2:
                k2[2]=k2[2]+1
            elif k==3:
                k2[3]=k2[3]+1
            elif k==4:
                k2[4]=k2[4]+1
            elif k==5:
                k2[5]=k2[5]+1
            else:
                print("k2 over 6")
        elif y==3:
            if k==0:
                k3[0]=k3[0]+1
            elif k==1:
                k3[1]=k3[1]+1
            elif k==2:
                k3[2]=k3[2]+1
            elif k==3:
                k3[3]=k3[3]+1
            elif k==4:
                k3[4]=k3[4]+1
            elif k==5:
                k3[5]=k3[5]+1
            else:
                print("k3 over 6")
        elif y==4:
            if k==0:
                k4[0]=k4[0]+1
            elif k==1:
                k4[1]=k4[1]+1
            elif k==2:
                k4[2]=k4[2]+1
            elif k==3:
                k4[3]=k4[3]+1
            elif k==4:
                k4[4]=k4[4]+1
            elif k==5:
                k4[5]=k4[5]+1
            else:
                print("k4 over 6")
        y=y+1     

    

    x=x-1
    

print(" ")
print("win total's total time")
print(k0)
#print(" k1")
print(k1)
print(k2)
print(k3)
print(k4)
##k0=py.array(k0)
##print("average gap")
##print(k0/game_len*100)
##print(k1/game_len*100)
##print(k2/game_len*100)
##print(k3/game_len*100)
##print(k4/game_len*100)

def foo(x,y):
    y_len=len(y)
    k_y=py.zeros((y_len),dtype=int)
    count=0
    for a in y:
        if a==0:
            k_y[count]=0
            
        else:
            k_y[count]=x/a
        
        count=count+1
    return k_y

print("this is k0")
print(k0)
z=foo(game_len,k0)
print(z)

print("this is k1")
print(k1)
z=foo(game_len,k1)
print(z)

print("this is k2")
print(k2)
z=foo(game_len,k2)
print(z)

print("this is k3")
print(k3)
z=foo(game_len,k3)
print(z)

print("this is k44")
print(k44)
z=foo(game_len,k4)
print(z)
print(" ")


print(total_w_num)
print(" ")
for a in all_num:
    print(a)
    print(" ")



#################################################################
    ########## write to excel file #####################

#step_every_rate=copy.copy(step_every)
k=game_len
b=0
c=0

step_every_rate=py.array(py.arange(50*k).reshape(50,k))
step_every_rate=py.array(step_every_rate,dtype=float)

step_every_avg=py.array(py.arange(50*k).reshape(50,k))
step_every_avg=py.array(step_every_avg,dtype=float)

step_ink=py.array(py.arange(50*k).reshape(50,k))
step_ink=py.array(step_every_avg,dtype=float)

step_ture=py.array(py.arange(50*k).reshape(50,k))


row=0
col=0
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;') 
style2 = xlwt.easyxf('pattern: pattern solid, fore_colour blue;')
inkA= xlwt.easyxf('pattern: pattern solid, fore_colour red;')
style3 = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
style4 = style = xlwt.easyxf('font: bold 1')
print("start step_every  1234")

################## col and row values#########################
col=1
row=1
row4=1
k=game_len
x=1
while x<game_len+1:
    sheet1.write(row, 0, x, style1)
    sheet2.write(row, 0, x, style2)
    sheet3.write(row, 0, x, style3)
    sheet5.write(row, 0, x, style2)
    sheet4.write(row4, 0, x, style2)
    row4=row4+1
    sheet4.write(row4, 0, ' ', style2)
    row4=row4+1
    sheet4.write(row4, 0, ' ', style2)
    row4=row4+1
    sheet4.write(row4, 0, ' ', style1)
    
    row=row+1
    row4=row4+2
    x=x+1

x=1
col=1
k=game_len
while x<51:
    sheet1.write(0, col, k, style1)
    sheet2.write(0, col, k, style2)
    sheet3.write(0, col, k, style3)
    sheet5.write(0, col, k, style1)
    sheet4.write(0, col, k, style3)
    col=col+1
    k=k-1
    x=x+1
#########################################################

col=1
row=0
k=game_len
x=0
row=1
sh1=float
sh2=float
sh3=float

dif_avg_rate=py.array(py.arange(50*k).reshape(50,k))
dif_avg_rate=py.array(dif_avg_rate,dtype=float)

for a in step_every:
    x=0        
    row=1
    row4=1
    while x<5:
        y=0
        while y<10:
            step_ink[c,b]=a[x,y]
            
            step_ture[c,b]=0
            sh2=a[x,y]/k*100
            sh2=py.round(sh2,decimals=2)
            step_every_avg[c,b]=sh2
            #dif_avg_rate[c,b]=step_ink[c,b]-sh2
            
            if b==0:
                sheet1.write(row, col, a[x,y])
                sheet2.write(row, col, sh2)
                sheet4.write(row4, col, a[x,y])
                row4=row4+1
                sheet4.write(row4, col, sh2)
                row4=row4+2
                #sheet4.write(row4, col, dif_avg_rate[c,b],style1)
                
                #sheet3.write(row, col, sh2)
            elif b>0:
                if step_ink[c,b-1]>step_ink[c,b]:
                    sh1=step_ink[c,b-1]
                    step_ture[c,b]=1
                    sh3=step_every_avg[c,b-1]                    
                    
                    sheet1.write(row, col, a[x,y],inkA)
                    sheet2.write(row, col, sh2,inkA)
                    
                    #sheet3.write(row, col, sh2,inkA)
                    sheet4.write(row4, col, a[x,y],inkA)
                    row4=row4+1
                    sheet4.write(row4, col, sh2,inkA)
                    row4=row4+2
                    #sheet4.write(row4, col, dif_avg_rate[c,b],inkA)
                    #row4=row4+1
                else:
                    sheet1.write(row, col, a[x,y])
                    sheet2.write(row, col, sh2)
                    
                    sheet4.write(row4, col, a[x,y])
                    row4=row4+1
                    sheet4.write(row4, col, sh2)
                    row4=row4+2
                    #sheet4.write(row4, col, dif_avg_rate[c,b],style1)
                    #row4=row4+1
                    #sheet3.write(row, col, sh2,inkA)
            c=c+1
            #print(a[x,y])
            col=col+1
            row4=row4+2
            y=y+1
        x=x+1
        #print("Next "+ str(x)+" num")
    b=b+1
    c=0
    k=k-1
    row=row+1

###########################################

print("this is test on line 1289")

x=0
y=0
b=1
c=1
cell_sum=float
cell_sum=0
cell_sum_reset=float
cell_sum_reset=0
step_every_aSum=copy.copy(step_every_avg)
            
col=1
row=0
k=game_len
x=0
row=1
row4=3
while x<50:
    col=game_len
    y=game_len
    while y>0:
        y=y-1
        if y==(game_len-1):
            cell_sum=step_every_avg[x,y]
            cell_sum_reset=cell_sum
            step_every_aSum[x,y]=cell_sum/c
            b=step_every_aSum[x,y]/100
            
            step_every_aSum[x,y]=b
            
            b=py.round(b,decimals=2)
            dif_avg_rate[x,y]=b-step_every_avg[x,y]
            sh3=dif_avg_rate[x,y]
            
            if step_ture[x,y]==1:
                sheet3.write(row, col, b,inkA)
                sheet5.write(row, col, sh3,inkA)
                sheet4.write(row4, col, b,inkA)
                #row4=row+1
                sheet4.write(row4+1,col,sh3,style1)
                #row4=row4-1
                
            else:
                sheet3.write(row, col, b)
                sheet5.write(row, col, sh3)
                sheet4.write(row4, col, b)
                #row4=row4+1
                sheet4.write(row4+1,col,sh3,style1)
                #row4=row4-1
                   
                #row4=row4+3
        
            #c=c+1
                #print(cell_sum)
        else:
            cell_sum=step_every_avg[x,y]+cell_sum_reset
            cell_sum_reset=cell_sum
            step_every_aSum[x,y]=cell_sum/c
            b=step_every_aSum[x,y]
            b=py.round(b,decimals=2)
            b=step_every_aSum[x,y]/100
            
            step_every_aSum[x,y]=b
            
            b=py.round(b,decimals=2)
            dif_avg_rate[x,y]=b-step_every_avg[x,y]
            sh3=dif_avg_rate[x,y]
            
            if step_ture[x,y]==1:
                sheet3.write(row, col, b,inkA)
                sheet5.write(row, col, sh3,inkA)
                sheet4.write(row4, col, b,inkA)
                
                sheet4.write(row4+1,col,sh3,style1)
   
                #row4=row4+3
            else:
                sheet3.write(row, col, b)
                sheet4.write(row4, col, b)
                sheet5.write(row, col, sh3)
                sheet4.write(row4+1,col,sh3,style1)
   
                #row4=row4+3
                
        col=col-1
            #c=c+1
        
    
    row=row+1
    row4=row4+5
    #print("row: "+str(row)+" row4: "+ str(row4))
    x=x+1
#################################     
            
 
    
workbook.save("sample_row.xls")

#print("the end")
#print(step_every)
#print(step_ture)

############### end of write excel file ######################
##############################################################

############### Sort winning time board ######################
sort_step_ink=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_step_avg=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_step_aSum=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_dif_rate=py.array(py.arange(200).reshape(50,4), dtype=float)

sort_step_ink_reset=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_step_avg_reset=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_step_aSum_reset=py.array(py.arange(200).reshape(50,4), dtype=float)
sort_dif_rate_reset=py.array(py.arange(200).reshape(50,4), dtype=float)

print("this test on line 1406")

print("here")
for a in step_ink:
    print(a)
print("after step_ink")

y=0
x=0
a=0
b=0

# check the total winning times in every number, from 1 to 50
for a in step_ink:
    x=x+1
    y=0
    while y<game_len:
        print(a[y])
        y=y+1
        
    
    
y=0
x=0
a=0
b=0

while y<game_len:
    a=0
    while a<50:
        sort_step_ink_reset[a,0]=0
        sort_step_avg_reset[a,0]=0
        sort_step_aSum_reset[a,0]=0
        sort_dif_rate_reset[a,0]=0

        sort_step_ink_reset[a,1]=a+1
        sort_step_avg_reset[a,1]=a+1
        sort_step_aSum_reset[a,1]=a+1
        sort_dif_rate_reset[a,1]=a+1
        
        sort_step_ink_reset[a,2]=step_ink[a,y]
        sort_step_avg_reset[a,2]=step_every_avg[a,y]
        sort_step_aSum_reset[a,2]=step_every_aSum[a,y]
        sort_dif_rate_reset[a,2]=dif_avg_rate[a,y]
        
        if step_ture[a,y]==1:
            sort_step_ink_reset[a,3]=1
            sort_step_avg_reset[a,3]=1
            sort_step_aSum_reset[a,3]=1
            sort_dif_rate_reset[a,3]=1
        elif step_ture[a,y]==0:
            sort_step_ink_reset[a,3]=0
            sort_step_avg_reset[a,3]=0
            sort_step_aSum_reset[a,3]=0
            sort_dif_rate_reset[a,3]=0
        a=a+1

    arr1=sort_step_ink_reset[sort_step_ink_reset[ :, 2].argsort()]
    arr2=sort_step_avg_reset[sort_step_avg_reset[ :, 2].argsort()]
    arr3=sort_step_aSum_reset[sort_step_aSum_reset[ :, 2].argsort()]
    arr4=sort_dif_rate_reset[sort_dif_rate_reset[ :, 2].argsort()]
    
    k=0
    while k<50:
        arr1[k,0]=k+1
        arr2[k,0]=k+1
        arr3[k,0]=k+1
        arr4[k,0]=k+1
        k=k+1
                
    if y==0:
        sort_step_ink=py.array(arr1)
        sort_step_avg=py.array(arr2)
        sort_step_aSum=py.array(arr3)
        sort_dif_rate=py.array(arr4)
    else:
        sort_step_ink=py.append(sort_step_ink,arr1,axis=0)
        sort_step_avg=py.append(sort_step_avg,arr2,axis=0)
        sort_step_aSum=py.append(sort_step_aSum,arr3,axis=0)
        sort_dif_rate=py.append(sort_dif_rate,arr4,axis=0)
            
    y=y+1
k=game_len

sort_step_ink=py.reshape(sort_step_ink,(k,50,4))
sort_step_avg=py.reshape(sort_step_avg,(k,50,4))
sort_step_aSum=py.reshape(sort_step_aSum,(k,50,4))
sort_dif_rate=py.reshape(sort_dif_rate,(k,50,4))
    
 
print("this line of 1492")

col=1
row=0
x=0
y=0
z=0
print("this is the value")
print(sort_step_ink[0,1,2])
print(sort_step_ink[0,2,2])
print(sort_step_ink[0,1,0])
print(sort_step_ink[0,2,0])

      
while y<50:
    row=row+1
    col=1
    while z<game_len:
        a=sort_step_ink[z,y,1]
        a2=sort_step_ink[z,y,2]
        a3=sort_step_ink[z,y,3]
        
##        b=sort_step_aSum[z,y,1]
##        b2=sort_step_aSum[z,y,2]
##        b3=sort_step_aSum[z,y,3]
##        
##        c=sort_dif_rate[z,y,1]
##        c2=sort_dif_rate[z,y,2]
##        c3=sort_dif_rate[z,y,3]
        print(a, "  ", a2, "  ", a3)
        
##        sheet6.write(row, col, a)
##        col=col+1
##        sheet6.write(row, col, a2)
        col=col+1
##        sheet6.write(row, col, b)
##        col=col+1
##        sheet6.write(row, col, b2)
##        col=col+1
##        sheet6.write(row, col, c)
##        col=col+1
##        sheet6.write(row, col, c2)
##        print(a)

        z=z+1
##    print("next")
    y=y+1

        

################## sort_step_aSum #####################
##col=1
##row=53
##x=0
##y=0
##for a in sort_step_aSum:
##    y=0    
##    while y<50:
##        k=int(a[y,3])
##        e=py.round(a[y,1],decimals=2)
##        f=py.round(a[y,2],decimals=2)
##        
##        if k==1:
##            #print(b)
##            sheet6.write(row, col, e,inkA)
##            col=col+1
##            sheet6.write(row, col, f)
##            col=col-1
##        elif k==0:
##            sheet6.write(row, col, e,style3)
##            col=col+1
##            sheet6.write(row, col, f)
##            if y==49:
##                col=col+1
##            else:
##                col=col-1
##        row=row+1
####        print("this is row"+str(row))
##        y=y+1
##    row=53
##    x=x+1
##
##
##
################### sort_dif_rate ###########################
##    
##col=1
##row=106
##x=0
##y=0
##while x<100:
##    x=x+1
##    while y<100:
##        y=y+1
##x=0
##y=0
##col=1
##row=106
##for a in sort_dif_rate:
##    y=0    
##    while y<50:
##        k=int(a[y,3])
##        b=py.round(a[y,1],decimals=2)
##        c=py.round(a[y,2],decimals=2)
##        
##        if k==1:
##            #print(b)
##            sheet6.write(row, col, b,inkA)
##            col=col+1
##            sheet6.write(row, col, c)
##            col=col-1
##        elif k==0:
##            sheet6.write(row, col, b,style2)
##            col=col+1
##            sheet6.write(row, col, c)
##            if y==49:
##                col=col+1
##            else:
##                col=col-1
##        row=row+1
####        print("this is row"+str(row))
##        y=y+1
##    row=106
##    x=x+1









