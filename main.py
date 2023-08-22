# умови завдання .Задано двумірний масив значення елементів якого 0 або 1

# визначити найбільший блок масиву з елементами 0 які дотикаються один до одного

# задаємо кількість строк и стовпців масиву

import random # ідключаємо модуль
import time
import copy



I = int (input( ' введи кількість строк масиву ' ))

J = int (input( ' введи кількисть стовпців масиву '))

# заповнюємо масив  значеннями 0 і 1

sp_1 = [ ] # водимо початкове значчення масиву
sp_2 = [ ]

sp_1 = [[random.randint(0,1) for x

         in range (J)] for y in range (I)]     # задаємо значення елемнтів масиву

# виводимо масив на екран

for x in range (I):
    for y in range (J):  
        print (sp_1[x][y], end=' ')
    print ()
sp_2 = copy.deepcopy(sp_1) # задаємо копію масива для подальшого виведення результату
#print (sp_2) 
pl_rez=[]   # задаємо список для блоку зі значенням 0
p2_rez=[]
#print (len(p2_rez))


poz = int(0)  # задаємо значення позиції в списку pl_rez
poz1 = int(0)
dl = int(0)    # задаємо значення для перевірки приросту в списку pl_rez

kol = int(0)


def poisk (p11, p12):     # задаємо функцію для пошуку дотичних комірок зі значенням 0
    p1=int(p11)
    p2=int(p12)
    global poz
    #global dl
    
    if p1 > 0   and sp_1[p1-1][p2]==0: 

              pl_rez.append([p1-1,p2])
              sp_1[p1-1][p2]=1
              poz+=1
                            
    elif  p2>0 and sp_1[p1][p2-1]==0:
        
              pl_rez.append([p1,p2-1])
              sp_1[p1][p2-1]=1
              poz+=1
       
    elif  p1<=I-2 and sp_1[p1+1][p2]==0:
        
              pl_rez.append([p1+1,p2])
              sp_1[p1+1][p2]=1
              poz+=1

    elif  p2<=J-2 and sp_1[p1][p2+1]==0:
        
              pl_rez.append([p1,p2+1])
              sp_1[p1][p2+1]=1
              poz+=1
              
  # задаємо основний цикл пошуку точки входу та визначення загального розміру блока з нулями

for x in range (I):
    
    for y in range (J):
        
        if sp_1[x][y]==0:
            
            pl_rez.append([x,y])
            sp_1[x][y]=1
            #print (pl_rez[poz])
            #poz=poz+1
            dl=poz
            while dl>=0:
                #print (pl_rez)
                #time.sleep(0)
                
                while  dl==poz:
                    #print (pl_rez[dl][0] , pl_rez[dl][1])
                    poisk (pl_rez[dl][0] , pl_rez[dl][1])
                    if dl<poz:
                        dl=poz
                    else:
                        poz1=poz
                        dl=dl-1
                        break
                    
                #dl=dl-1
                poisk (pl_rez[dl][0] , pl_rez[dl][1])
                if poz1<poz:
                        dl=poz
                        poz1=poz
                        
                        #poisk (pl_rez[dl][0] , pl_rez[dl][1])
                else:
                    dl=dl-1
                 #   poisk (pl_rez[dl][0] , pl_rez[dl][1])
        #print (pl_rez)
                #print ()
            dl=0
            #poz=0
            poz1=0
            #print (pl_rez)
            if len(pl_rez)>len(p2_rez):
               p2_rez=pl_rez
               kol=poz
               poz=0
               #print ("результат проміжний")
               #print (p2_rez)
               pl_rez=[]
            else:
               pl_rez=[]
               poz=0
               #dl=0
               #poz=0
               #poz1=0

print ()
print ()


# print(len (p2_rez))
for x in range (kol+1):
  t1 = int( p2_rez[x][0])
  t2 = int( p2_rez[x][1])
  sp_2[t1][t2]=8
#print (sp_2)  
  
for x in range (I):
    for y in range (J):  
        print (sp_2[x][y], end=' ')
    print ()
print ('Максимальна площа  ділянки з нулями', len(p2_rez))    
               
            

              
              
              
