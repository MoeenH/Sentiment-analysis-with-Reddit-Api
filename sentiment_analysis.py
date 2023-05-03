from tkinter import *
import reddit_api

root = Tk()   
mylabel = Label(root, text="Customer Sentiment Analysis", height= 5, width= 80)
mylabel.pack()

  
def keyword():
    def send ():
        reddit_api.get_submission(clicked.get(),e.get())    
  
    mybutton2 = Button(root, text="Enter Keyword", height= 5, command= send)
    mybutton2.pack(side = RIGHT)
        
    e = Entry(root, width= 20, bd=3)
    e.pack()
       
        
        #reddit_api.get_submission(subreddit,e.get())



  
  
    #drop box menu

clicked = StringVar()

clicked.set("food")


drop = OptionMenu(root, clicked,"politics", "food", "Games", "amazon","ebay","startups","pakistan")
drop.pack()

    
clickedbutton = Button(root,text="Press to continue", command= keyword)
clickedbutton.pack()

    
    
   
    
    
    
   
    



#title of the window




#show the label



root.mainloop()
