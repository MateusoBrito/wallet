import customtkinter as ctk

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

campo_usuario = ctk.CTkLabel(app,text='Usuário')
campo_usuario.pack(pady=10)


ctk.CTkEntry(app,placeholder_text='Di')
app.mainloop()