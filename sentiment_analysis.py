from tkinter import *
root = Tk()   


def start():
    mylabel1 = Label(root, text="Enter Product Name", height= 5)
    mylabel1.pack()
    
    e = Entry(root, width= 20, bd=3)
    e.pack()
    
    mylabel2 = Label(root, text=e.get)
    mylabel2.pack()

    


#title of the window
mylabel = Label(root, text="Customer Sentiment Analysis", height= 8, width= 80)
button = Button(root, text="Start" , fg="sky blue", bg="sea green", command=start)


#show the label
mylabel.pack()
button.pack()
root.mainloop()
