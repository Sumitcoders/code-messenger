from tkinter import *
import code_converter as c
import os

def copy():
    global code
    command = 'echo ' + code + '| clip'
    os.system(command)



root = Tk()
root.geometry("1000x600")

bg_color = '#A3E4D7'

root.configure(bg=bg_color)

code = ''

def code():
    global code
    a,b = c.coding(c_entry.get())
    code = a
    a = 'Code:'+ a
    b = 'Passocde:' + b
    coder_code.config(text= a,font= 'Helvetica 16')
    coder_passcode.config(text= b,font= 'Helvetica 16')
    
    print(a)
    print(b)
def decode():
    entry = dc_entry.get()
    if '\n' in entry:
        entry = entry[0:len(entry)-1]
    a = c.decoding(dp_entry.get(),entry)
    

    print(a)
    decoder_code.config(text=a,font='Helvetica 16')
coder = Label(root,text= 'Coding the message',font= 'Helvetica 16')
coder.pack()

c_entry = Entry(root,wid=42)
c_entry.place(relx= .5, rely= 0.1, anchor= CENTER)


coder_button = Button(root, text= "Click to Show code ", command= code).place(relx= .65, rely= .1, anchor= CENTER)

coder_code = Label(root,text= '',font= 'Helvetica 16')
coder_passcode = Label(root,text= '',font= 'Helvetica 16')
coder_code.place(relx=.5,rely=.15,anchor=CENTER)
coder_passcode.place(relx=.5,rely=.25,anchor=CENTER)
code_copy = Button(root,command=copy,text='Copy code')
code_copy.place(relx= .65, rely= .2, anchor= CENTER)



decoder = Label(root,text= 'Decoding the message',font= 'Helvetica 16')
decoder.place(relx= .5, rely= 0.5, anchor= CENTER)

dc_entry = Entry(root,wid=42)
dc_entry.place(relx= .5, rely= 0.55, anchor= CENTER)
dp_entry = Entry(root,wid=40)
dp_entry.place(relx= .5, rely= 0.61, anchor= CENTER)

decoder_button = Button(root, text= "Click to Show decode ", command= decode).place(relx= .65, rely= .55, anchor= CENTER)

decoder_code = Label(root,text= '',font= 'Helvetica 16')
decoder_passcode = Label(root,text= '',font= 'Helvetica 16')
decoder_code.place(relx=.5,rely=.65,anchor=CENTER)




coder_code.configure(bg=bg_color)
coder_passcode.configure(bg=bg_color)
decoder_code.configure(bg=bg_color)





root.mainloop()
