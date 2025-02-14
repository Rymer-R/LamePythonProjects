import customtkinter

#setting appearance to dark
customtkinter.set_appearance_mode("dark")
#setting colors of elements
customtkinter.set_default_color_theme("green")
#setting the gui dimentions
root = customtkinter.CTk()
root.geometry("500x450")
#defining a pseudo login function
def login():
    print("Logged In...")
#the frame
frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
#displays Login on top of the screen
label = customtkinter.CTkLabel(master = frame, text = "Login System", font=("Roboto", 42))
label.pack(pady = 20, padx = 10)
#displays an input box with "Username" as a placeholder
entry1 = customtkinter.CTkEntry(master = frame, placeholder_text= "Username", width= 350, height = 40, font = ("Roboto", 20))
entry1.pack(pady = 12, padx = 10)
#displays another input box with "Password" as a placeholder
entry2 = customtkinter.CTkEntry(master = frame, placeholder_text= "Password", width= 350, height = 40, font = ("Roboto", 20), show = "*")
entry2.pack(pady = 12, padx = 10)
#creates a button which executes the login function if triggered
button = customtkinter.CTkButton(master = frame, text = "Login", command = login, height = 40, width = 200, font = ("Roboto", 20))
button.pack(pady = 40, padx = 10)
#a "remember me" checkbox
checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember me", font = ("Roboto", 20))
checkbox.pack(pady = 12, padx = 10)
#running the gui
root.mainloop()
