from tkinter import *

root = Tk()
root.geometry('600x400+400+150')

# f_menu = Frame(root, bg='#1F252A', height=40)
# f_menu.pack(fill=X)
f_text = Frame(root, bg='white')
f_text.pack(fill=BOTH, expand=1)

# l_menu = Label(f_menu, text='Menu', bg='#2B3239', fg='#C6DEC1', font='Arial 10')
# l_menu.place(x=10, y=10)
#
#
# def add_str():
#     t.insert('2.4', 'Hello!')
#
#
# def del_str():
#     t.delete('1.0', END)
#
#
# def get_str():
#     print(t.get('1.0', END))
#
#
# btn_add = Button(root, text='Add', command=add_str).place(x=50, y=10)
# btn_del = Button(root, text='Delete', command=del_str).place(x=90, y=10)
# btn_get = Button(root, text='Get', command=get_str).place(x=140, y=10)

t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10, wrap=WORD,
         insertbackground='#EDA756', selectbackground='#4E5A65', spacing1=1, width=20)
t.pack(fill=BOTH, expand=1, side=LEFT)

scrollbar = Scrollbar(f_text, command=t.yview)
scrollbar.pack(side=LEFT, fill=Y)
t.config(yscrollcommand=scrollbar.set)

root.mainloop()
