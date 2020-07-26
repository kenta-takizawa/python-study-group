import tkinter as tk 

root = tk.Tk() 
root.title("hello") 

tk.Message(root, text=48*'xxxxx ').grid(row=0, column=0, columnspan=3) 

tk.Label(root, text='Name:',padding=).grid(row=1, column=0) 
tk.Entry(root, width=50,padding=True).grid(row=1, column=1) 
tk.Button(root, text="?",padding=True).grid(row=1, column=2) 

tk.Button(root, text="Left").grid(row=2, column=0) 
tk.Button(root, text="Center").grid(row=2, column=1) 
tk.Button(root, text="Right").grid(row=2, column=2) 

root.mainloop() 