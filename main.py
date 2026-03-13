import tkinter as tk

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("350x450")

def main():
    root = tk.Tk()
    root.title("web")
    root.geometry("1000x700")
    
    left_frame = tk.Frame(root, bg="#e8f5fe", width=250)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    main_frame = tk.Frame(root, bg="white", width=600)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    right_frame = tk.Frame(root, bg="#f5f8fa", width=350)
    right_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    tk.Label(left_frame, text="Sidebar", bg="#e8f5fe").pack(pady=20)
    tk.Label(main_frame, text="Timeline", bg="white").pack(pady=20)
    tk.Label(right_frame, text="Trends", bg="#f5f8fa").pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()