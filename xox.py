from tkinter import *

window = Tk()

window.geometry("500x500")

window.title("XOX")

row_1 = Frame(window,bg="#fff",)
row_1.pack(expand=True,fill="both")

row_2 = Frame(window)
row_2.pack(expand=True,fill="both",)

row_3 = Frame(window,bg="#fff",)
row_3.pack(expand=True,fill="both")
click = True
def logic(buttons):
    
    global click
    
    if buttons["text"]=="" and click==True:
        buttons["text"]="X"
        click = False 
        

    elif buttons["text"]=="" and click==False:
        buttons["text"]="O"
        click = True
        
    if(btn_1["text"]=="O" and btn_2["text"]=="O" and btn_3["text"]=="O" or
    btn_4["text"]=="O" and btn_5["text"]=="O" and btn_6["text"]=="O" or
    btn_7["text"]=="O" and btn_8["text"]=="O" and btn_9["text"]=="O" or
    btn_1["text"]=="O" and btn_5["text"]=="O" and btn_9["text"]=="O" or
    btn_1["text"]=="O" and btn_7["text"]=="O" and btn_4["text"]=="O" or
    btn_5["text"]=="O" and btn_2["text"]=="O" and btn_6["text"]=="O" or
    btn_9["text"]=="O" and btn_6["text"]=="O" and btn_3["text"]=="O" or 
    btn_3["text"]=="O" and btn_5["text"]=="O" and btn_7["text"]=="O"):
         print("win O")
    if (btn_1["text"]=="X" and btn_2["text"]=="X" and btn_3["text"]=="X" or btn_4["text"]=="X" and btn_5["text"]=="X" and btn_6["text"]=="X" or btn_7["text"]=="X" and btn_8["text"]=="X" and btn_9["text"]=="X" or btn_1["text"]=="X" and btn_5["text"]=="X" and btn_9["text"]=="X" or btn_1["text"]=="X" and btn_7["text"]=="X" and btn_4["text"]=="X" or btn_5["text"]=="X" and btn_2["text"]=="X" and btn_6["text"]=="X" or btn_9["text"]=="X" and btn_6["text"]=="X" and btn_3["text"]=="X" or btn_3["text"]=="X" and btn_5["text"]=="X" and btn_7["text"]=="X"):
            print("winX")
            END
btn_1=Button(
    row_1,
    command=lambda:logic(btn_1)

)
btn_1.pack(side=LEFT,

expand=True,

fill="both",
)

btn_2=Button(
    row_1,
    command= lambda:logic(btn_2)
    )
btn_2.pack(side=LEFT,expand=True,fill="both",)

btn_3=Button(row_1,command=lambda:logic(btn_3))
btn_3.pack(side=LEFT,expand=True,fill="both")

btn_4=Button(row_2,command=lambda:logic(btn_4))
btn_4.pack(side=LEFT,expand=True,fill="both")

btn_5=Button(row_2,command=lambda:logic(btn_5))
btn_5.pack(side=LEFT,expand=True,fill="both")

btn_6=Button(row_2,command=lambda:logic(btn_6))
btn_6.pack(side=LEFT,expand=True,fill="both")

btn_7=Button(row_3,command=lambda:logic(btn_7))
btn_7.pack(side=LEFT,expand=True,fill="both")

btn_8=Button(row_3,command=lambda:logic(btn_8))
btn_8.pack(side=LEFT,expand=True,fill="both")

btn_9=Button(row_3,command=lambda:logic(btn_9))
btn_9.pack(side=LEFT,expand=True,fill="both")




window.mainloop()