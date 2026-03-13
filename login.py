import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("350x450")
        self.window.configure(bg="pink")
        

        logo_label = tk.Label(
            self.window, 
            text="web", 
            font=("Arial", 40), 
            bg="pink"
        )
        logo_label.pack(pady=20)
        
        title_label = tk.Label(
            self.window,
            text="Sign in to web",
            font=("Arial", 18, "bold"),
            bg="pink"
        )
        title_label.pack(pady=10)
        
        tk.Label(self.window, text="Username:", bg="white").pack(pady=(20,5))
        self.username_entry = tk.Entry(self.window, width=25)
        self.username_entry.pack()
        
        tk.Label(self.window, text="Password:", bg="white").pack(pady=(15,5))
        self.password_entry = tk.Entry(self.window, width=25, show="*")
        self.password_entry.pack()
        
        login_btn = tk.Button(
            self.window,
            text="Login",
            bg="#1da1f2",
            fg="white",
            font=("Arial", 10, "bold"),
            width=20,
            height=2,
            command=self.login
        )
        login_btn.pack(pady=30)
        
        signup_label = tk.Label(
            self.window,
            text="Don't have an account? Sign up",
            fg="#1da1f2",
            bg="pink",
            cursor="hand2"
        )
        signup_label.pack()
        signup_label.bind("<Button-1>", lambda e: self.show_signup())
        
        self.window.mainloop()
    
    def login(self): # Not functional , just check if theres an input
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            messagebox.showinfo("Success", f"Welcome {username}!")# Not functional , should open main window
    
    def show_signup(self):# Not functional , just a new window
        signup_window = tk.Toplevel(self.window)
        signup_window.title("Sign Up")
        signup_window.geometry("350x500")
        
        tk.Label(signup_window, text="Create Account").pack(pady=20)

if __name__ == "__main__":
    Login()