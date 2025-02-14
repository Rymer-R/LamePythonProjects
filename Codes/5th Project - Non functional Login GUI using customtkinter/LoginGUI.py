import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x450")

def login():
    print("Logged In...")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Login System", font=("Roboto", 42))
label.pack(pady = 20, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text= "Username", width= 350, height = 40, font = ("Roboto", 20))
entry1.pack(pady = 12, padx = 10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text= "Password", width= 350, height = 40, font = ("Roboto", 20), show = "*")
entry2.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "Login", command = login, height = 40, width = 200, font = ("Roboto", 20))
button.pack(pady = 40, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember me", font = ("Roboto", 20))
checkbox.pack(pady = 12, padx = 10)

root.mainloop()