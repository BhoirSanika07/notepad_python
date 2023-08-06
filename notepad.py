from tkinter import *
from tkinter import filedialog
def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    
def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not NONE:
        content=file.read()
  
    entry.insert(INSERT,content)
    
root =Tk()
root.title("notepad using python")
root.geometry("450x450")
root.config(bg='lightblue')
root.resizable(False,False)
b1=Button(root,width='20',height='2',bg="red",text="save_file",command=save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg="red",text="open_file",command=open_file).place(x=250,y=5)
Entry=Text(root,height='22',width='62',wrap=WORD)
Entry.place(x=10,y=60)


root.mainloop()