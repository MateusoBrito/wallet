import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.title('Wallet')
app.geometry("1000x650")

app.configure(fg_color="#1F1F1F") 

#menu frame
menu_frame = ctk.CTkFrame(app,  width=200, height=630, fg_color="#2C2C2C", corner_radius=10)
menu_frame.pack(side="left", padx=10, pady=10)

logo = ctk.CTkLabel(menu_frame,text='wallet', font=("Nickels", 30, "bold"), text_color="#FFFFFF")
logo.pack(pady=20)
logo.place(x=15, y=10)

#main frame
main_frame = ctk.CTkFrame(app,  width=550, height=630, fg_color="#2C2C2C", corner_radius=10)
main_frame.pack(side="left", padx=0, pady=10)

#result frame
result_frame = ctk.CTkFrame(app,  width=50, height=50, fg_color="#2C2C2C", corner_radius=10)
result_frame.pack(side="left", anchor="ne", padx=10, pady=10)

#category frame
category_frame = ctk.CTkFrame(app, width=50, height=50, fg_color="#2C2C2C", corner_radius=10)
result_frame.pack(side="left", anchor="ne", padx=10, pady=10)
app.mainloop()