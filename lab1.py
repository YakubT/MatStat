import numpy
import math
import turtle
import time



def findN(x,l,r):
    count = 0
    for i in range(len(x)):
        if (x[i]>l and x[i]<r):
            count = count+1
    return count


height = 500
width = 400
start = (-60,-200)
def drawCoordSystem(char1, char2):
    turtle.up()
    turtle.setpos(0,0)
    turtle.up()
    turtle.forward(start[0])
    turtle.left(90)
    turtle.forward(start[1])
    turtle.down()
    turtle.forward(height)
    turtle.up()
    turtle.setpos(start[0],start[1])
    turtle.right(90)
    turtle.down()
    turtle.forward(width)
    turtle.right(135)
    turtle.forward(10)
    turtle.up()
    turtle.setpos(start[0]+width,start[1])
    turtle.down()
    turtle.left(270)
    turtle.forward(10)
    turtle.left(-135)
    turtle.up()
    turtle.setpos(start[0],start[1]+height)
    turtle.down()
    turtle.right(135)
    turtle.forward(10)
    turtle.forward(-10)
    turtle.left(-270)
    turtle.forward(10)
    turtle.right(-135)
    turtle.right(90)
    turtle.up()
    turtle.forward(10)
    turtle.write(char1,font=('arial',15,'normal'))
    turtle.setpos(start[0]+width+10,start[1])
    turtle.write(char2,font=('arial',15,'normal'))
    turtle.setpos(start[0]-300,start[1])
    turtle.down()
    turtle.forward(width)
    turtle.up()

def plotFunc(x,y,color,r,size):
    turtle.setpos(start[0],start[1])
    turtle.left(90)
    h = height
    turtle.right(90)
    maxim = y[0];
    for i in range(len(x)):
        maxim = max(maxim,y[i])
    turtle.width(3)
    for i in range(len(y)):
        turtle.setpos(start[0],start[1]+0.92*height*y[i]/maxim)
        turtle.down()
        turtle.forward(10)
        turtle.forward(-20)
        turtle.up()
        turtle.forward(-20)
        turtle.setpos(start[0]-40,start[1]+0.92*height*y[i]/maxim-4)
        turtle.write(y[i],font=('arial',size,'normal'))
    turtle.setpos(start[0],start[1])
    turtle.left(90)
    turtle.forward(-20)
    turtle.write("0")
    for i in range(len(x)):
        turtle.setpos(start[0]+10+0.75*(x[i]-x[0])*width/(x[len(x)-1]-x[0]),start[1])
        turtle.down()
        turtle.forward(10)
        turtle.forward(-20)
        turtle.up()
        turtle.forward(-20)
        turtle.write(x[i],font=('arial',size,'normal'),align='center')
    turtle.pencolor(color)
    for i in range(len(x)-1):
        turtle.setpos(start[0]+10+0.75*(x[i]-x[0])*width/(x[len(x)-1]-x[0]),start[1]+0.92*height*y[i]/maxim)
        turtle.down()
        turtle.setpos(start[0]+10+0.75*(x[i+1]-x[0])*width/(x[len(x)-1]-x[0]),start[1]+0.92*height*y[i+1]/maxim)
    turtle.up()
    turtle.pencolor("black")
    for i in range(len(x)):
        turtle.setpos(start[0]+10+0.75*(x[i]-x[0])*width/(x[len(x)-1]-x[0])+r,start[1]+0.92*height*y[i]/maxim)
        turtle.down()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()
        turtle.up()
    turtle.width(1)
  
def drawPoligon(table,n):
    turtle.setheading(0)
    turtle.Screen().title("Полігон частот")
    turtle.clear()
    drawCoordSystem("\u03C9","xi")
    turtle.setpos(start[0]-100,start[1]-100)
    turtle.write("Полігон частот",font=('arial',20,'bold'))
    x = []
    y = []
    for i in range(len(table)):
        x.append(table[i][0])
        y.append(table[i][1]/n)
    plotFunc(x,y,"lightseagreen",4,10)
    
    
def drawCumuliata(table,y,n):
    turtle.clear()
    maxim = y[0];
    for i in range(len(y)):
        maxim = max(maxim,y[i])
    x = []
    for i in range(len(table)):
        x.append(table[i][0])
    turtle.setheading(0)
    turtle.Screen().title("Кумулята")
    turtle.clear()
    drawCoordSystem("\u03C9","xi")
    turtle.setpos(start[0]-50,start[1]-100)
    turtle.write("Кумулята",font=('arial',20,'bold'))
    turtle.up()
    turtle.setpos(start[0]-25,start[1]+0.92*height*0.5/maxim-6)
    turtle.color('red')
    turtle.write("0.5",font=('arial',9,'bold'))
    turtle.color('black')
    medIndex = 0
    for i in range(len(x)-1):
        if (y[i]<0.5 and y[i+1]>0.5):
            medIndex = i
    xC = (0.5-y[medIndex]+x[medIndex]*(y[medIndex+1]-y[medIndex])/(x[medIndex+1]-x[medIndex]))/((y[medIndex+1]-y[medIndex])/(x[medIndex+1]-x[medIndex]))
    yC = 0.5
    pMedDraw = (start[0]+10+0.75*width*(xC-x[0])/(x[len(x)-1]-x[0]),start[1]+0.92*height*yC/maxim)
    turtle.width(3)
    turtle.pencolor("orange")
    pR = (start[0],start[1]+0.92*height*yC/maxim)
    pl = (start[0]+10+0.75*width*(xC-x[0])/(x[len(x)-1]-x[0]),start[1])
    drawDashedLine(pMedDraw,pR,5)
    drawDashedLine(pMedDraw,pl,5)
    turtle.pencolor("black")
    turtle.width(1)
    plotFunc(x,y,"deeppink",3,7)
    turtle.setpos(start[0]+0.75*width*xC/x[len(x)-1]-10,start[1])
    turtle.forward(40)
    char = ""
    if (xC<0):
        char="\u2013"
    turtle.write("Медіана = "+char+str(abs(round(xC*10)/10)),font=('cambria math',15,'normal'))
    turtle.setheading(0)
    

def drawDashedLine(a,b,h):
    turtle.setheading(0)
    leng = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    k = round(leng/h)
    turtle.setpos(a[0],a[1])
    for i in range(k):
        turtle.up()
        p = (a[0]+((i+1)/k)*(b[0]-a[0]),a[1]+((i+1)/k)*(b[1]-a[1]))
        if (i%2==1):
            turtle.down()
        turtle.setpos(p[0],p[1])
    turtle.up()
            
def drawHistograma(table,ends,n):
    turtle.Screen().title("Гістограма")
    turtle.clear()
    turtle.up()
    turtle.setheading(0)
    turtle.setpos(start[0],start[1])
    maxim = table[0][1];
    for i in range(len(table)):
        maxim = max(table[i][1],maxim)
    y = []
    for i in range(len(table)):
        y.append(table[i][1])
        xCoord = start[0]-70+0.75*width*(table[i][0]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0])
        turtle.up()
        turtle.setpos(xCoord,start[1]-20)
        turtle.write(table[i][0],font=('arial',8,'normal'),align='center')
        l = start[0]-70+0.75*width*(ends[i][0]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0])
        turtle.setpos(l,start[1])
        turtle.fillcolor("yellowgreen")
        turtle.begin_fill()
        turtle.pencolor("forestgreen")
        turtle.down()
        r = start[0]-70+0.75*width*(ends[i][1]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0])
        turtle.setpos(r,start[1])
        turtle.left(90)
        h = y[i]*height/maxim
        turtle.forward(h)
        turtle.setpos(l,start[1]+h)
        turtle.setpos(l,start[1])
        turtle.end_fill()
        turtle.right(90)
        turtle.pencolor("black")
        turtle.up()
        turtle.setpos(xCoord,start[1]+h+5)
        turtle.write(table[i][1],font=('arial',10,'normal'),align='center')
    maximIndex = 0;
    for i in range(len(table)):
        if (table[i][1]>table[maximIndex][1]):
            maximIndex = i
    rMod = start[0]-70+0.75*width*(ends[maximIndex][1]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0])
    modR = (rMod,start[1]+y[maximIndex]*height/maxim)
    modR1 = (ends[maximIndex][1],y[maximIndex])
    beforeMode = (start[0]-70+0.75*width*(ends[maximIndex-1][1]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),
                  start[1]+y[maximIndex-1]*height/maxim)
    beforeMode1 = (ends[maximIndex-1][1],y[maximIndex-1])
    drawDashedLine(modR,beforeMode,3)
    modL = (start[0]-70+0.75*width*(ends[maximIndex][0]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),start[1]+y[maximIndex]*height/maxim)
    modL1  = (ends[maximIndex][0],y[maximIndex])
    afterMode = (start[0]-70+0.75*width*(ends[maximIndex+1][0]-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),
                  start[1]+y[maximIndex+1]*height/maxim)
    afterMode1 = (ends[maximIndex+1][0],y[maximIndex+1])
    drawDashedLine(modL,afterMode,3)
    k1 = (beforeMode1[1]-modR1[1])/(beforeMode1[0]-modR1[0])
    b1 = modR1[1]-modR1[0]*(beforeMode1[1]-modR1[1])/(beforeMode1[0]-modR1[0])
    k2 = (afterMode1[1]-modL1[1])/(afterMode1[0]-modL1[0])
    b2 = modL1[1]-modL1[0]*(afterMode1[1]-modL1[1])/(afterMode1[0]-modL1[0])
    xPer = (b2-b1)/(k1-k2)
    yPer = k1*xPer+b1
    turtle.setpos(start[0]-70+0.75*width*(xPer-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),start[1]+yPer*height/maxim)
    turtle.setheading(0)
    turtle.right(90)
    turtle.down()
    turtle.setpos(start[0]-70+0.75*width*(xPer-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),start[1])
    turtle.right(35)
    turtle.forward(-6)
    turtle.up()
    turtle.setpos(start[0]-70+0.75*width*(xPer-ends[0][0])/(ends[len(table)-1][1]-ends[0][0]),start[1])
    turtle.setheading(0)
    turtle.down()
    turtle.left(125)
    turtle.forward(6)
    turtle.up()
    turtle.setpos(start[0]-70+0.75*width*(xPer-ends[0][0])/(ends[len(table)-1][1]-ends[0][0])+30,start[1])
    turtle.forward(40)
    char = ""
    if (xPer<0):
        char="\u2013"
    turtle.write("Мода = "+char+str(abs(round(xPer*10)/10)),font=('cambria math',15,'normal'))
    turtle.setpos(start[0]-30,start[1]-100)
    turtle.write("Гістограма",font=('arial',20,'bold'))
    turtle.setheading(0)
    
def solve(x):
    n = len(x)
    print("Якубишин КП-12 Співідношення євро до долара у відсотках")
    print("Згенерована вибірка")
    print(x,"\n")
    x.sort()
    print("Ранжована вибірка:")
    print(x,"\n")
    r = x[n-1]-x[0]
    print("Розмах вибірки",r)
    m = round(1+3.3221*math.log(n,10))
    k = r/m
    print("Ширина інтервалу:",k)
    k = round(k)
    print("Візьмемо k =",k)
    xStart = round(x[0]-k/2)
    m = m+1
    print("x початкове =", xStart)
    table = []
    ends = []
    for i in range(m):
        avg = xStart+i*k+k/2;
        count = findN(x, xStart+i*k,xStart+(i+1)*k)
        table.append((avg,count))
        ends.append((xStart+i*k,xStart+(i+1)*k))
    if (table[0][1]<5):
        table[1] = ((table[0][0]+table[1][0])/2,table[0][1]+table[1][1])
        table.pop(0)
        ends.pop(0)
        ends[0] = (table[0][0]-k,table[0][0]+k)
    m = len(table)
    if (table[m-1][1]<5):
        table[m-2] = ((table[m-1][0]+table[m-2][0])/2,table[m-1][1]+table[m-2][1])
        table.pop(m-1)
        ends.pop(m-1)
        ends[m-2] = (table[m-2][0]-k,table[m-2][0]+k)
    m = len(table)
    print(table)
    print("******************")
    print("Згрупований ранжований ряд зведемо в таблицю")
    print("|i  |Кінці інтервалів| Середини інтервалів (xi)| Частота ni|Частість| Накопичена частота ni_нак|Накопичена частість|")
    niNak = 0
    chastNakArr = []
    res = []
    ser = 0
    for i in range(m):
        niNak = table[i][1]+niNak
        chastNakArr.append(niNak/n)
        ser+=table[i][1]*table[i][0]
        print(str(i+1).center(3),str("("+str(ends[i][0])+")-("+str(ends[i][1])+")").center(20),str(table[i][0]).center(15),str(table[i][1]).center(20),
              str(table[i][1]/n).center(5),str(niNak).center(15),
              str(niNak/n).center(35))
    ser = ser/n;
    ser = round(ser*10)/10
    print("Середнє = ",ser)
    sKv = 0
    for i in range(m):
        sKv +=((table[i][0]-ser)**2)*table[i][1]
    sKv = sKv/n
    s = math.sqrt(sKv)
    print("Дисперсія",sKv)
    print("Середнє квадратичне відхилення",s)
    v = s/abs(ser)*100
    print("Коефіцієнт варіцації",v,"%")
    print("Введіть у вікні 1 - для побудови полігона частот, 2 - для побудови гістограми,3 -для побудови кумуляти")
    turtle.Screen().listen()
    turtle.Screen().onkey(lambda: drawPoligon(table,n),'1')
    turtle.Screen().onkey(lambda: drawHistograma(table,ends,n),'2')
    turtle.Screen().onkey(lambda: drawCumuliata(table,chastNakArr,n),'3')
    turtle.Screen().mainloop()

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)
n = 100
f = open("data.txt", "r")
x = []
for i in range(n):
    x.append(float(f.readline()))
    x[i]*=100
solve(x)
f.close()




