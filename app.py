from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import app_settings as settings

# Dictionary to store user data
user_data = {}

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title(settings.app_title)
        self.window.state('zoomed')
        self.window.geometry("1200x800")
        self.window.minsize(1000, 700)

        self.bg_image_loaded = False

        image_path = os.path.join("images", "I1.jpg")
        try:
            self.bg_image = Image.open(image_path)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = Label(self.window, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_image_loaded = True
            self.window.bind("<Configure>", self.resize_bg_image)
        except FileNotFoundError:
            print(f"File not found: {image_path}")
            self.bg_label = Label(self.window, bg='white')
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.top_frame = Frame(self.window, background=settings.primary_color, height=80)
        self.top_frame.pack(side=TOP, fill=X)

        mrgs_logo_path = os.path.join("images", "mrgs_logo.png")
        self.mrgs_logo = Image.open(mrgs_logo_path)
        self.mrgs_logo = self.mrgs_logo.resize((105, 75), Image.LANCZOS)
        self.mrgs_logo = ImageTk.PhotoImage(self.mrgs_logo)
        logo_label = Label(self.top_frame, image=self.mrgs_logo, bg=settings.primary_color)
        logo_label.pack(side=LEFT, padx=10, pady=10)

        title_label = Label(self.top_frame, text=settings.app_title, font=("Helvetica", 36, "bold"), bg=settings.primary_color, fg=settings.text_color)
        title_label.pack(side=LEFT, padx=10, pady=10)

        welcome_text_frame = Frame(self.window, bg='white', highlightbackground='#ffffff', highlightthickness=1, bd=0)
        welcome_text_frame.place(relx=0.25, rely=0.5, anchor=CENTER, width=500, height=200)  # Adjusted height

        welcome_text_section = Frame(welcome_text_frame, bg='white', padx=20, pady=10)  # Reduced pady
        welcome_text_section.pack(fill=BOTH, expand=True)

        subtitle = ("Welcome to Roskill Pulse! Engage with your school community, stay informed about events, and "
                    "access important resources with ease. Your hub for everything school-related.")
        subtitle_label = Label(welcome_text_section, text=subtitle, font=("Helvetica", 18), wraplength=460, justify=CENTER, bg='white')
        subtitle_label.pack(expand=True, fill=BOTH, pady=(10, 0))

        login_frame = Frame(self.window, bg='white', highlightbackground='#ffffff', highlightthickness=1, bd=0)
        login_frame.place(relx=0.75, rely=0.5, anchor=CENTER, width=500, height=450)

        login_section = Frame(login_frame, bg='white', padx=20, pady=20)
        login_section.pack(fill=BOTH, expand=True)

        discover_label = Label(login_section, text="Discover your school", font=("Helvetica", 24, "bold"), bg='white', anchor="w")
        discover_label.pack(pady=10, fill=X)

        self.email_entry = Entry(login_section, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.email_entry.pack(pady=10)
        self.email_entry.insert(0, "Email address")
        self.email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Email address"))
        self.email_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Email address"))

        self.password_entry = Entry(login_section, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.password_entry.pack(pady=10)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Password"))
        self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Password"))

        continue_button = Button(login_section, text="Continue", font=("Helvetica", 16), width=30, height=1, bg="#c8102e", fg=settings.text_color, command=self.login)
        continue_button.pack(pady=20)

        or_frame = Frame(login_section, bg='white')
        or_frame.pack(fill=X, pady=10)

        left_line = Frame(or_frame, bg=settings.primary_color, height=1)
        left_line.pack(side=LEFT, padx=5, expand=True, fill=X)

        or_label = Label(or_frame, text="OR", font=("Helvetica", 14), bg='white', fg=settings.text_color)
        or_label.pack(side=LEFT, padx=5)

        right_line = Frame(or_frame, bg=settings.primary_color, height=1)
        right_line.pack(side=LEFT, padx=5, expand=True, fill=X)

        guest_button = Button(login_section, text="Continue as Guest", font=("Helvetica", 16), width=30, height=1, bg="#c8102e", fg=settings.text_color, command=self.open_main_interface)
        guest_button.pack(pady=10)

        not_member_frame = Frame(login_section, bg='white')
        not_member_frame.pack(pady=(10, 10))

        not_member_label = Label(not_member_frame, text="Not a member yet? ", font=("Helvetica", 12), bg='white', fg='black')
        not_member_label.pack(side=LEFT)

        signup_label = Label(not_member_frame, text="Sign Up", font=("Helvetica", 12), bg='white', fg=settings.secondary_color, cursor="hand2")
        signup_label.pack(side=LEFT)
        signup_label.bind("<Button-1>", lambda e: self.open_signup_page())

        self.resize_bg_image()

        self.window.mainloop()

    def resize_bg_image(self, event=None):
        if self.bg_image_loaded:
            window_width = self.window.winfo_width()
            window_height = self.window.winfo_height()
            bg_aspect = self.bg_image.width / self.bg_image.height
            window_aspect = window_width / window_height

            if window_aspect > bg_aspect:
                new_width = window_width
                new_height = int(new_width / bg_aspect)
            else:
                new_height = window_height
                new_width = int(new_height * bg_aspect)

            resized_bg_image = self.bg_image.resize((new_width, new_height))
            self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg='black', show="*" if placeholder == "Password" else "")

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey', show="")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email in user_data and user_data[email] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.open_main_interface()
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def open_main_interface(self):
        self.window.destroy()
        MainInterface()

    def open_signup_page(self):
        self.window.destroy()
        SignUpPage()


class SignUpPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sign Up - Roskill Pulse")
        self.window.configure(bg=settings.primary_color)
        self.window.state('zoomed')

        outside_frame = Frame(self.window, bg='#c8102e')
        outside_frame.pack(expand=True, fill=BOTH)

        self.frame = Frame(outside_frame, bg='white')
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=700, height=600)  # Increased size

        signup_heading = Label(self.frame, text="One Step Away", font=("Helvetica", 24, "bold"), bg='white')
        signup_heading.pack(pady=20)

        content_frame = Frame(self.frame, bg='white')
        content_frame.pack(pady=10, padx=20, expand=True)  # Added padding and expansion

        self.username_entry = Entry(content_frame, font=("Helvetica", 18), width=35, fg='grey', bg='#f0f0f0')
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Username")
        self.username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Username"))
        self.username_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Username"))

        self.email_entry = Entry(content_frame, font=("Helvetica", 18), width=35, fg='grey', bg='#f0f0f0')
        self.email_entry.pack(pady=10)
        self.email_entry.insert(0, "Email address")
        self.email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Email address"))
        self.email_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Email address"))

        self.password_entry = Entry(content_frame, font=("Helvetica", 18), width=35, fg='grey', bg='#f0f0f0')
        self.password_entry.pack(pady=10)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Password"))
        self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Password"))

        self.confirm_password_entry = Entry(content_frame, font=("Helvetica", 18), width=35, fg='grey', bg='#f0f0f0')
        self.confirm_password_entry.pack(pady=10)
        self.confirm_password_entry.insert(0, "Confirm password")
        self.confirm_password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Confirm password"))
        self.confirm_password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Confirm password"))

        signup_button = Button(content_frame, text="Sign Up", font=("Helvetica", 18), width=35, height=1, bg="#c8102e", fg=settings.text_color, command=self.signup)
        signup_button.pack(pady=20)

        back_button = Button(self.frame, text="Back", font=("Helvetica", 18), width=10, height=1, bg="#c8102e", fg=settings.text_color, command=self.go_back)
        back_button.pack(pady=10, anchor=SE, padx=20, side=RIGHT)

        self.window.mainloop()

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg='black', show="*" if "password" in placeholder.lower() else "")

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey', show="")

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if email in user_data:
            messagebox.showerror("Error", "Email already registered.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            user_data[email] = password
            messagebox.showinfo("Success", "Sign up successful!")
            self.go_back()

    def go_back(self):
        self.window.destroy()
        App()


class MainInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Roskill Pulse - Main Interface")
        self.window.state('zoomed')
        self.window.geometry("1200x800")
        self.window.minsize(1000, 700)

        image_path = os.path.join("images", "I1.jpg")
        try:
            self.bg_image = Image.open(image_path)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = Label(self.window, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_image_loaded = True
            self.window.bind("<Configure>", self.resize_bg_image)
        except FileNotFoundError:
            print(f"File not found: {image_path}")
            self.bg_label = Label(self.window, bg='white')
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.top_frame = Frame(self.window, background=settings.primary_color, height=80)
        self.top_frame.pack(side=TOP, fill=X)

        mrgs_logo_path = os.path.join("images", "mrgs_logo.png")
        self.mrgs_logo = Image.open(mrgs_logo_path)
        self.mrgs_logo = self.mrgs_logo.resize((105, 75), Image.LANCZOS)
        self.mrgs_logo = ImageTk.PhotoImage(self.mrgs_logo)
        logo_label = Label(self.top_frame, image=self.mrgs_logo, bg=settings.primary_color)
        logo_label.pack(side=LEFT, padx=10, pady=10)

        title_label = Label(self.top_frame, text=settings.app_title, font=("Helvetica", 36, "bold"), bg=settings.primary_color, fg=settings.text_color)
        title_label.pack(side=LEFT, padx=10, pady=10)

        sidebar_frame = Frame(self.window, bg='white', width=250)
        sidebar_frame.pack(side=LEFT, fill=Y)

        self.sidebar_buttons = {}
        sidebar_options = ["Home", "Notices", "Profile", "Resources", "Settings"]

        for option in sidebar_options:
            button = Button(sidebar_frame, text=option, font=("Helvetica", 18), width=15, bg='white', fg='black', anchor='w', relief='flat', command=lambda opt=option: self.sidebar_button_click(opt))
            button.pack(pady=10, padx=10)
            self.sidebar_buttons[option] = button

        self.content_frame = Frame(self.window, bg='white')
        self.content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.sidebar_button_click("Home")

        self.window.mainloop()

    def resize_bg_image(self, event=None):
        if hasattr(self, 'bg_image'):
            window_width = self.window.winfo_width()
            window_height = self.window.winfo_height()
            bg_aspect = self.bg_image.width / self.bg_image.height
            window_aspect = window_width / window_height

            if window_aspect > bg_aspect:
                new_width = window_width
                new_height = int(new_width / bg_aspect)
            else:
                new_height = window_height
                new_width = int(new_height * bg_aspect)

            resized_bg_image = self.bg_image.resize((new_width, new_height))
            self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def sidebar_button_click(self, option):
        # Method to handle sidebar button clicks and update their appearance
        for btn in self.sidebar_buttons.values():
            btn.config(font=("Helvetica", 18), relief='flat', bg='white')  # Reset all buttons

        self.sidebar_buttons[option].config(font=("Helvetica", 18, "bold"), relief='sunken', bg='#f0f0f0')  # Highlight selected button
        self.update_content(option)

    def update_content(self, option):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if option == "Home":
            Label(self.content_frame, text="Welcome to Roskill Pulse Home!", font=("Helvetica", 24), bg='white').pack(side=TOP, fill=X, padx=20, pady=20)
        elif option == "Notices":
            Label(self.content_frame, text="Here are the latest notices.", font=("Helvetica", 24), bg='white').pack(side=TOP, fill=X, padx=20, pady=20)
        elif option == "Profile":
            Label(self.content_frame, text="Manage your profile here.", font=("Helvetica", 24), bg='white').pack(side=TOP, fill=X, padx=20, pady=20)
        elif option == "Resources":
            Label(self.content_frame, text="Access school resources here.", font=("Helvetica", 24), bg='white').pack(side=TOP, fill=X, padx=20, pady=20)
        elif option == "Settings":
            Label(self.content_frame, text="Adjust your settings here.", font=("Helvetica", 24), bg='white').pack(side=TOP, fill=X, padx=20, pady=20)

if __name__ == "__main__":
    App()
    