from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x400+300+150')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    messagebox.showinfo(title='About notepad', message='Program NotePad Version 0.0.1')


def notepad_quit():
    answer = messagebox.askokcancel(title='Quit', message='A You Sure?')
    # print(answer)
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Choose the file',
                                           filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Documents", "*.*")))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path, encoding='utf-8').read())


# def save_file():
#     file_path = filedialog.asksaveasfile(title='Choose the file', filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Documents", "*.*")))


def save_file_name():
    file_path = filedialog.asksaveasfilename(title='Enter the name of file', filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Documents", "*.*")))
    f = open(file_path , 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()

def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


# Menu File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Create')
file_menu.add_command(label='Open', command=open_file)
# file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save as...', command=save_file_name)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=notepad_quit)
main_menu.add_cascade(label='File', menu=file_menu)

# Menu About
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light Theme', command=lambda: change_theme('light'))
theme_menu_sub.add_command(label='Dark Theme', command=lambda: change_theme('dark'))
theme_menu.add_cascade(label='Decor', menu=theme_menu_sub)
theme_menu.add_command(label='About', command=about_program)
main_menu.add_cascade(label='Other', menu=theme_menu)

f_text = Frame(root, bg='white')
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#C6DEC1", "cursor": "#EDA756", "select_bg": "#4E5A65"
    },
    "light": {
        "text_bg": "#fff", "text_fg": "#000", "cursor": "#8000FF", "select_bg": "#777"
    }
}

t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']['select_bg'],
         spacing1=1, width=20, font=("Courier New", 11))
t.pack(fill=BOTH, expand=1, side=LEFT)

scrollbar = Scrollbar(f_text, command=t.yview)
scrollbar.pack(side=LEFT, fill=Y)
t.config(yscrollcommand=scrollbar.set)

root.mainloop()
