from tkinter import *
class Window:
    def __init__(self,title):
        self.root = Tk()
        self.title = title
        self.root.title(title)
        self.fields={}
        self.labels={}
        self.buttons={}
    def Add_Field(self,title,column,row,width=None,height=None,columnspan=None,rowspan=None):
        #Let's make some fields for Entries
        columnspan=1 if columnspan == None else columnspan
        rowspan=1 if rowspan == None else rowspan
        width=30 if width == None else width
        height=8 if columnspan == None else columnspan
        self.fields[title]=Entry(self.root)
        self.labels[title]=Label(self.root,text=title).grid(column=column,row=row)
        self.fields[title].grid(column=(column+1),row=row,columnspan=columnspan,rowspan=rowspan)
    def Create_Window(self):
        #When you're done building the window, use this.
        self.root.mainloop()
    def Add_Button(self,title,column,row,command,width=None,height=None,columnspan=None,rowspan=None):
        pass
    def Get_Fields(self,*args):
        pass
        #Returns a dict populated with the content of all fields referenced
