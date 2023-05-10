import tkinter
canvas=tkinter.Canvas(bg = "pink",height = "400",width = 600)
canvas.pack()


slovo=["S","A","M","A"]
slovo1=["_","_","_","_"]
slovo2=["S","A","M","A"]
pokus=0
       
while pokus<10 and slovo2!=slovo1:
    pismeno=input('Hadaj pismeno:')
    if pismeno in slovo:
        print("ok")
        slovo1[slovo.index(pismeno)]= pismeno
        if slovo.count(pismeno)>1:
            for i in range(slovo.count(pismeno)):
                slovo1[slovo.index(pismeno)]= pismeno
                slovo[slovo.index(pismeno)]= ""
        print(slovo1)
    else:
        if pokus!=10:
            pokus+=1
            print("Máš ešte",10-pokus,"pokusov.")
        if pokus==9:
            canvas.create_line(65,205,55,260,fill="orange",width=10)
        if pokus==8:
            canvas.create_line(90,205,100,260,fill="orange",width=10)
        if pokus==7:
            canvas.create_line(110,130,95,150,fill="orange",width=10)
        if pokus==6:
            canvas.create_line(35,130,55,145,fill="orange",width=10)
        if pokus==5:
            canvas.create_oval(50,130,100,210,fill="orange")
        if pokus==4:
            canvas.create_line(75,110,75,130,fill="orange",width=5)
        if pokus==3:
            canvas.create_oval(50,40,100,110,fill="orange",tag="si")
        if pokus==2:
            canvas.create_line(20,2,20,270,width=7)
        if pokus==1:
            canvas.create_line(80,2,80,110,width=7)
        if pokus==0:
            canvas.create_line(20,2,80,2,width=7)
if slovo==slovo1:
    print("Si super :)")
else:
    print("Nemáš pokusy:(")

canvas.mainloop()
