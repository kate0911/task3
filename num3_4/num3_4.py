f=open('text.txt','r')
text=f.read()
f.close()
stroki=text.split('\n')
print(len(stroki))
point=[]
Point=[]
for i in range (0,len(stroki)):
    P=(stroki[i]).split()
    for j in P:
        Point.append(float(j))
    point.append(Point)
    Point=[]
print (point)
check=0
c=0
if (len(point)>=4):
    for i in range(0,len(point)-2):
        if (check==0):
            for j in range(i+1,len(point)-1):
                if (check==0):
                    x0=(point[i])[0]
                    y0=(point[i])[1]
                    x1=(point[j])[0]
                    y1=(point[j])[1]
                    if (x1!=x0):
                        x2=(point[j+1])[0]
                        y2=(point[j+1])[1]
                        compare=int(((y1-y0)*x2-x0*y1+y0*x1)/(x1-x0)*100)/100
                        if (y2==compare):
                            print ("Невыпуклый")
                            check=1
                            break
                        else:
                            if (y2>compare):
                                c=1
                            else:
                                c=-1
                            for k in range(j+2,len(point)):
                                if (check==0):
                                    x2=(point[k])[0]
                                    y2=(point[k])[1]
                                    compare=int(((y1-y0)*x2-x0*y1+y0*x1)/(x1-x0)*100)/100
                                    if ((y2>compare)&(c==-1)):
                                        print ("Невыпуклый")
                                        check=1
                                        break
                                    elif ((y2<compare)&(c==1)):
                                        print ("Невыпуклый")
                                        check=1
                                        break
                                    elif (y2==compare):
                                        print ("Невыпуклый")
                                        check=1
                                        break
                    else:
                        for k in range(j+1,len(point)):
                            if (check==0):
                                x2=(point[k])[0]
                                if (c==0):
                                    if (x2>x1):
                                        c=1
                                    elif (x2<x1):
                                        c=-1
                                    else:
                                        print ("Невыпуклый")
                                        check=1
                                        break
                                if ((c==1)&(x2<x1)):
                                    print ("Невыпуклый")
                                    check=1
                                    break
                                if ((c==-1)&(x2>x1)):
                                    print ("Невыпуклый")
                                    check=1
                                    break
if (check==0):
    print ("Выпуклый")
maxX=(point[0])[0]
maxY=(point[0])[1]
minX=(point[0])[0]
minY=(point[0])[1]
for i in range(1,len(point)):
    if ((point[i])[0]>maxX):
        maxX=(point[i])[0]
    if ((point[i])[1]>maxY):
        maxY=(point[i])[1]
    if ((point[i])[0]<minX):
        minX=(point[i])[0]
    if ((point[i])[1]<minY):
        minY=(point[i])[1]
X=float(input("Введите x:"))
Y=float(input("Введите y:"))
if ((X>maxX)|(X<minX)|(Y>maxY)|(Y<minY)):
    print ("1")
    print ("Не принадлежит")
    print(maxX,minX,maxY,minY)
else:
    LeftRight=[]
    for i in range (0,len(point)-1):
        if ((((point[i])[1]>=Y)&((point[i+1])[1]<=Y))|(((point[i])[1]<=Y)&((point[i+1])[1]>=Y))):
            x0=(point[i])[0]
            y0=(point[i])[1]
            x1=(point[i+1])[0]
            y1=(point[i+1])[1]
            if (y1!=y0):
                print (y1,y0)
                LeftRight.append((Y*(x1-x0)+x0*y1-y0*x1)/(y1-y0))
        if ((((point[0])[1]>=Y)&((point[len(point)-1])[1]<=Y))|(((point[0])[1]<=Y)&((point[len(point)-1])[1]>=Y))):
            x0=(point[0])[0]
            y0=(point[0])[1]
            x1=(point[len(point)-1])[0]
            y1=(point[len(point)-1])[1]
            if (y1!=y0):
                print (y1,y0)
                LeftRight.append((Y*(x1-x0)+x0*y1-y0*x1)/(y1-y0))
    l=0
    r=0
    print (LeftRight)
    for i in range(0,len(LeftRight)):
        if (LeftRight[i]>X):
            r+=1
        elif (LeftRight[i]<X):
            l+=1
        else:
            print ("Точка принадлежит многоугольнику")
    if ((l%2==1)&(r%2==1)):
        print ("Точка принадлежит многоугольнику")
    else:
        print ("Точка не принадлежит многоугольнику")
        
        
    
                    
                        
                    
                
