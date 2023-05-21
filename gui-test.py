import tkinter as tk 
import tkinter.font as tkFont
from tkinter import *
import reddit_api
import config
from PIL import ImageTk, Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import test

            
                        
class App:


    def __init__(self, root):
        #setting title
        root.title("Analysis")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_413=tk.Message(root)
        ft = tkFont.Font(family='Times',size=17)
        GMessage_413["font"] = ft
        GMessage_413["fg"] = "#333333"
        
        GMessage_413["text"] = "Sentiment Analysis"
        GMessage_413["relief"] = "sunken"
        GMessage_413.place(x=140,y=70,width=298,height=90)
        
        

        GButton_508=tk.Button(root, command=self.start)
        GButton_508["activebackground"] = "#934e4e"
        GButton_508["activeforeground"] = "#d0b3b3"
        GButton_508["anchor"] = "w"
        GButton_508["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_508["font"] = ft
        GButton_508["fg"] = "#000000"
        GButton_508["justify"] = "center"
        GButton_508["text"] = "Start"
        GButton_508.place(x=240,y=230,width=105,height=30)
        
        
        


    def start(self):
        print("Clearing Frame")
        self.clear_frame()
        
        GLabel_168=tk.Label(root)
    
        ft = tkFont.Font(family='Tibetan machine uni',size=25)
        GLabel_168["font"] = ft
        GLabel_168["fg"] = "#333333"
        GLabel_168["text"] = "Select  a topic"
    
        GLabel_168.place(x=200,y=5,height=70)
        
            
        def keyword():
                def send ():
                        
                    reddit_api.call_all(clicked.get(),e.get())
                    def make_wordcloud():
                        test
                        test.show_cloud()

                     # this is the line that calls the reddit_api
                    #reddit_api.call_all()
                    print("Clicked")
                    self.clear_frame()
                    GLabel_170=tk.Label(root)
                    ft = tkFont.Font(family='Tibetan machine uni',size=25)
                    GLabel_170["font"] = ft
                    GLabel_170["fg"] = "#333333"
                    GLabel_170["text"] = "Working On It..."
                   
                    GLabel_170.place(x=200,y=5,height=70)
                    
                    self.clear_frame()
                    GLabel_169=tk.Label(root)
                    ft = tkFont.Font(family='Tibetan machine uni',size=25)
                    GLabel_169["font"] = ft
                    GLabel_169["fg"] = "#333333"
                    GLabel_169["text"] = "Data Created"
                
                    GLabel_169.place(x=200,y=5,height=70)
                    
                                
                    GButton_507=tk.Button(root, command=reddit_api.print_Positive_Submission)
                    GButton_507["activebackground"] = "#934e4e"
                    GButton_507["activeforeground"] = "#d0b3b3"
                    GButton_507["anchor"] = "w"
                    GButton_507["bg"] = "#efefef"
                    ft = tkFont.Font(family='Times',size=10)
                    GButton_507["font"] = ft
                    GButton_507["fg"] = "#000000"
                    GButton_507["justify"] = "center"
                    GButton_507["text"] = "Positive comments"
                    GButton_507.place(x=150,y=230,width=105,height=30)
                    
                    
                    GButton_506=tk.Button(root, command=reddit_api.print_Negative_Submission)
                    GButton_506["activebackground"] = "#934e4e"
                    GButton_506["activeforeground"] = "#d0b3b3"
                    GButton_506["anchor"] = "w"
                    GButton_506["bg"] = "#efefef"
                    ft = tkFont.Font(family='Times',size=10)
                    GButton_506["font"] = ft
                    GButton_506["fg"] = "#000000"
                    GButton_506["justify"] = "center"
                    GButton_506["text"] = "Negative comments"
                    GButton_506.place(x=350,y=230,width=105,height=30)

                   
                   
                    GButton_505=tk.Button(root, command=make_wordcloud)
                    GButton_505["activebackground"] = "#934e4e"
                    GButton_505["activeforeground"] = "#d0b3b3"
                    GButton_505["anchor"] = "w"
                    GButton_505["bg"] = "#efefef"
                    ft = tkFont.Font(family='Times',size=10)
                    GButton_505["font"] = ft
                    GButton_505["fg"] = "#000000"
                    GButton_505["justify"] = "center"
                    GButton_505["text"] = "Most common words"
                    GButton_505.place(x=240,y=350,width=105,height=30)
                    
                
                e = Entry(root, width= 20, bd=3)
                e.pack()
                e.place(x=240,y=160,width=105,height=30)
                mybutton2 = Button(root, text="Enter Keyword", height= 5, command= send)
                mybutton2.pack()
                mybutton2.place(x=240,y=230,width=105,height=30)
                mybutton2.justify = "center"
        
                
        clicked = StringVar()
        clicked.set("food")        
        drop = OptionMenu(root, clicked,"politics", "food", "Games", "amazon","ebay","startups","pakistan")
        drop.pack()
        drop.place(x=180,y=75,width=105,height=30)

    
        clickedbutton = Button(root,text="Press to continue", command= keyword)
        clickedbutton.pack()
        clickedbutton.place(x=340,y=75,width = 150,height=30)
        clickedbutton.justify = "center"
        

        
        
        
        
    def clear_frame(self):
        for widgets in root.winfo_children():
            widgets.destroy()
        
    
        
        
            


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

