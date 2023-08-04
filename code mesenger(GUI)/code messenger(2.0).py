import customtkinter as ctk
import code_converter as c
import os

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()

root.title('Code converter')
root.geometry(f"{500}x{550}")

#coding
pcode = ''
def code():
    try:
        global pcode
        message = c_entry.get()
        passcode = c_passcode.get()
        f_message,passcode = c.coding(message=message,passcode=passcode)
        pcode = f_message
        f_message = 'Code:' + f_message + '\n' + 'passcode:' + passcode 
        print(f_message)
        c_output.configure(text=f_message,font=('Roboto',16))
    except:
        c_output.configure(text= 'Invalid passcode or message!')

def copy():
    command = 'echo ' + pcode + '| clip'
    os.system(command)

frame = ctk.CTkFrame(master = root,height=500,width=450,border_color='#ccc',border_width=2)
frame.place(anchor = 'center', relx = 0.5,rely = 0.5)

c_lable = ctk.CTkLabel(master=frame,text='Code your message here',font=('Roboto',16),bg_color='#444',width=400)
c_lable.place(relx = 0.5,rely = 0.1,anchor = 'center')

c_entry = ctk.CTkEntry(root,placeholder_text='Type your message here', width=400)
c_entry.pack(padx=50,pady=(100,50),anchor='center')

c_passcode = ctk.CTkEntry(root,placeholder_text='Type your custom code here', width=400)
c_passcode.place(relx= 0.5,rely = 0.27,anchor='center')


c_button = ctk.CTkButton(root,text='Code the message',command=code)
c_button.place(relx= 0.3,rely = 0.35,anchor='center')

copy_button = ctk.CTkButton(root,text='Copy code',command=copy)
copy_button.place(relx= 0.7,rely = 0.35,anchor='center')


c_output = ctk.CTkLabel(master=root,text='',font=('Roboto',16),bg_color='transparent')
c_output.place(relx = 0.5,rely = 0.45,anchor = 'center')

#decode

def decode(passcode):
    message = dc_entry.get()
    

    if '\n' in message:
        message = message[0:len(message)-1]
    code = passcode
    f_message = c.decoding(passcode=code,message=message)
    print(f_message)
    dc_output.configure(text = f_message,font=('Roboto', 16))


def open_dialog():
        dialog = ctk.CTkInputDialog(text="Type the passcode:", title="Passcode")
        decode(dialog.get_input())
        
dc_lable = ctk.CTkLabel(master=root,text='Decode your message here',font=('Roboto',16),bg_color='#444',width=400)
dc_lable.place(relx = 0.5,rely = 0.55,anchor = 'center')

dc_entry = ctk.CTkEntry(root,placeholder_text='Type your code here', width=400)
dc_entry.place(relx = 0.5,rely = 0.65,anchor = 'center')

dc_button = ctk.CTkButton(root,text='decode the message',command=open_dialog)
dc_button.place(relx = 0.5,rely = 0.75,anchor='center')

dc_output = ctk.CTkLabel(root,text='',font = ('Roboto', 16))
dc_output.place(relx = 0.5,rely = 0.85, anchor = 'center')
root.mainloop()


