# умови завдання .Задано двумірний масив значення елементів якого 0 або 1

#   

# задаємо кількість строк и стовпців масиву

import random # ідключаємо модуль
import time
import copy



ROW = int (input( ' введи кількість строк масиву ' ))

COL = int (input( ' введи кількисть стовпців масиву '))

# заповнюємо масив  значеннями 0 і 1

MAS_1 = [ ] # задаємо початкове значення масиву
MAS_2 = [ ]

MAS_1 = [[random.randint(0,1) for x

         in range (COL)] for y in range (ROW)]     # задаємо значення елементів масиву

# виводимо масив на екран

for x in range (ROW):
    for y in range (COL):  
        print (MAS_1[x][y], end=' ')
    print ()
MAS_2 = copy.deepcopy(MAS_1) # задаємо копію масива для подальшого виведення результату
#print (sp_2) 
listl_rez=[]   # задаємо список для блоку зі значенням 0
list2_rez=[]
#print (len(p2_rez))


poz = int(0)  # задаємо значення позиції в списку listl_rez
poz1 = int(0)
dl = int(0)    # задаємо значення для перевірки приросту в списку listl_rez

kol = int(0)


def poisk (x11, y11):     # задаємо функцію для пошуку дотичних комірок зі значенням 0
    x1=int(x11)
    y1=int(y11)
    global poz
    #global dl
    
    if x1 > 0   and MAS_1[x1-1][y1]==0: 

              listl_rez.append([x1-1,y1])
              MAS_1[x1-1][y1]=1
              poz+=1
                            
    elif  y1>0 and MAS_1[x1][y1-1]==0:
        
              listl_rez.append([x1,y1-1])
              MAS_1[x1][y1-1]=1
              poz+=1
       
    elif  x1<=ROW-2 and MAS_1[x1+1][y1]==0:
        
              listl_rez.append([x1+1,y1])
              MAS_1[x1+1][y1]=1
              poz+=1

    elif  y1<=COL-2 and MAS_1[x1][y1+1]==0:
        
              listl_rez.append([x1,y1+1])
              MAS_1[x1][y1+1]=1
              poz+=1
              
  # задаємо основний цикл пошуку точки входу та визначення загального розміру блока з нулями

for x in range (ROW):
    
    for y in range (COL):
        
        if MAS_1[x][y]==0:
            
            listl_rez.append([x,y])
            MAS_1[x][y]=1
            #print (pl_rez[poz])
            #poz=poz+1
            dl=poz
            while dl>=0:
                #print (pl_rez)
                #time.sleep(0)
                
                while  dl==poz:
                    #print (pl_rez[dl][0] , pl_rez[dl][1])
                    poisk (listl_rez[dl][0] , listl_rez[dl][1])
                    if dl<poz:
                        dl=poz
                    else:
                        poz1=poz
                        dl=dl-1
                        break
                    
                #dl=dl-1
                poisk (listl_rez[dl][0] , listl_rez[dl][1])
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
            if len(listl_rez)>len(list2_rez):
               list2_rez=listl_rez
               kol=poz
               poz=0
               #print ("результат проміжний")
               #print (p2_rez)
               listl_rez=[]
            else:
               listl_rez=[]
               poz=0
               #dl=0
               #poz=0
               #poz1=0

print ()
print ()


# print(len (p2_rez))
for x in range (kol+1):
  t1 = int( list2_rez[x][0])
  t2 = int( list2_rez[x][1])
  MAS_2[t1][t2]=8
#print (sp_2)  
  
for x in range (ROW):
    for y in range (COL):  
        print (MAS_2[x][y], end=' ')
    print ()
print ('Максимальна площа  ділянки з нулями', len(list2_rez))    
               
            

              
              
              
