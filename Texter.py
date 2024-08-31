import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog

def text_editor():
    def New():
        root.destroy()
        text_editor()
    
    def New_window():
        text_editor()
    
    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
                                           
        if file_path:
            with open(file_path, 'w') as file:
                file.write(txt.get("1.0", tk.END))
    
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                txt.delete("1.0", tk.END)
                with open(file_path, 'r') as file:
                    txt.insert(tk.END, file.read())
                print(f"File opened successfully from {file_path}")
            except Exception as e:
                print(f"Error opening file: {e}")
    
    def cut(event = None):
        txt.event_generate("<<Cut>>")

    def copy(event = None):
        txt.event_generate("<<Copy>>")

    def paste(event = None):
        txt.event_generate("<<Paste>>")

    def undo(event = None):
        txt.edit_undo()

    def redo(event = None):
        txt.edit_redo()
    
    def ask():
        text_content = txt.get("1.0", tk.END).strip()
        if text_content:
            def xclose():
                def b1():
                    save_file()
                    closing_window.destroy()
                    root.destroy()
                def b2():
                    closing_window.destroy()
                    root.destroy()
                def b3():
                    closing_window.destroy()    
                
                closing_window = ttk.Window()
                closing_window.geometry("400x120")
                closing_window.title("")

                label = ttk.Label(closing_window , text = "Do you want to save changes?" , font = "bold")
                label.pack()

                frame_close = ttk.Frame(closing_window)
                frame_close.pack()
            
                button1 = ttk.Button(frame_close , text = "Save" , command = b1)
                button1.pack(side = ttk.LEFT , padx = 5 ,)
                
                button2 = ttk.Button(frame_close , text = "Don't save" , command = b2)
                button2.pack(side = ttk.LEFT , padx = 5)
                
                button3 = ttk.Button(frame_close , text = "Close" , command = b3)
                button3.pack(side = ttk.RIGHT , padx = 5)
                
                closing_window.mainloop()
            xclose()
        else:
            root.destroy()
    #window
    root = ttk.Window()
    root.geometry("1500x800")
    root.title("Texter")
    #text
    txt = ttk.Text(root , font = ("Times New Roman" , 12) , undo = True)
    txt.pack(expand= True , fill= "both")

    #menu_bar
    menu_bar = ttk.Menu(root)
    root.config(menu = menu_bar)

    #file_menu
    file_menu = ttk.Menu(menu_bar , tearoff = 0, )
    menu_bar.add_cascade(label = 'File', menu = file_menu)

    #file_menu_commands
    file_menu.add_command(label = "New" , command = New)
    file_menu.add_command(label = "New window" , command = New_window)
    file_menu.add_command(label = "Open" , command = open_file)
    file_menu.add_command(label = "Save" , command = save_file)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit" , command = root.destroy)

    #edit_menu
    edit_menu = ttk.Menu(menu_bar)
    menu_bar.add_cascade(label = "Edit" , menu = edit_menu)

    #edit_menu_commands
    edit_menu.add_command(label = "Undo" , command = undo)
    edit_menu.add_command(label = "Redo" , command = redo)
    edit_menu.add_separator()
    edit_menu.add_command(label = "Cut" , command = cut)
    edit_menu.add_command(label = "Copy" , command = copy)
    edit_menu.add_command(label = "Paste" , command = paste)

    root.protocol("WM_DELETE_WINDOW" , ask)
    #run
    root.mainloop()
text_editor()