from tkinter import *

root = Tk()
root.geometry('600x400+400+150')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    print('About')


# Menu File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Create')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as...')
file_menu.add_separator()
file_menu.add_command(label='Quit')
main_menu.add_cascade(label='File', menu=file_menu)

# Menu About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Online')
help_menu_sub.add_command(label='Offline')
help_menu.add_cascade(label='Help', menu=help_menu_sub)
help_menu.add_command(label='About', command=about_program)
main_menu.add_cascade(label='About', menu=help_menu)

f_text = Frame(root, bg='white')
f_text.pack(fill=BOTH, expand=1)

t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10, wrap=WORD,
         insertbackground='#EDA756', selectbackground='#4E5A65', spacing1=1, width=20)
t.pack(fill=BOTH, expand=1, side=LEFT)

scrollbar = Scrollbar(f_text, command=t.yview)
scrollbar.pack(side=LEFT, fill=Y)
t.config(yscrollcommand=scrollbar.set)

root.mainloop()
