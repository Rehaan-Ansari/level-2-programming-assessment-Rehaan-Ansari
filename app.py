from tkinter import *
from tkinter import messagebox  
from PIL import Image, ImageTk
import os
import app_settings as settings


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
        self.mrgs_logo = self.mrgs_logo.resize((150, 75), Image.LANCZOS)
        self.mrgs_logo = ImageTk.PhotoImage(self.mrgs_logo)
        logo_label = Label(self.top_frame, image=self.mrgs_logo, bg=settings.primary_color)
        logo_label.pack(side=LEFT, padx=10, pady=10)

        title_label = Label(self.top_frame, text=settings.app_title, font=("Helvetica", 36, "bold"), bg=settings.primary_color, fg=settings.text_color)
        title_label.pack(side=LEFT, padx=10, pady=10)

        welcome_text_frame = Frame(self.window, bg='white', highlightbackground='#ffffff', highlightthickness=1, bd=0)
        welcome_text_frame.place(relx=0.25, rely=0.5, anchor=CENTER, width=500, height=300)

        welcome_text_section = Frame(welcome_text_frame, bg='white', padx=20, pady=20)
        welcome_text_section.pack(fill=BOTH, expand=True)

        subtitle = ("Welcome to Roskill Roundup, your hub for local connections and collaboration! Stay in the loop with "
                    "upcoming events, chat with classmates, and join exciting school projects. Get involved, stay "
                    "informed, and make a difference in your school community today!")
        subtitle_label = Label(welcome_text_section, text=subtitle, font=("Helvetica", 18), wraplength=460, justify=CENTER, bg='white')
        subtitle_label.pack(expand=True, fill=BOTH, pady=(10, 10))

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

        continue_button = Button(login_section, text="Continue", font=("Helvetica", 16), width=30, height=1, bg="#c8102e", fg=settings.text_color, command=self.open_main_interface)
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

        self.signup_label = Label(not_member_frame, text="Sign Up", font=("Helvetica", 12), bg='white', fg=settings.secondary_color, cursor="hand2")
        self.signup_label.pack(side=LEFT)
        self.signup_label.bind("<Button-1>", lambda e: self.open_signup_page())

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

    def open_main_interface(self):
        self.window.withdraw()  # Hide the current window instead of destroying it
        root = Tk()
        MainInterface(root)
        root.mainloop()

    def open_signup_page(self):
        self.window.destroy()
        root = Tk()
        SignUpPage(root)
        root.mainloop()


class SignUpPage:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up - Roskill Roundup")
        self.window.configure(bg=settings.primary_color)

        # Maximize the window to fullscreen
        self.window.state('zoomed')

        # Creating a red background outside the frame
        outside_frame = Frame(self.window, bg='#c8102e')
        outside_frame.pack(expand=True, fill=BOTH)

        # Creating a white frame for the signup section
        self.frame = Frame(outside_frame, bg='white')
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=450)

        # Heading for the sign-up page
        signup_heading = Label(self.frame, text="Sign Up Page", font=("Helvetica", 24, "bold"), bg='white')
        signup_heading.pack(pady=20)

        # Username entry
        self.username_entry = Entry(self.frame, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Username")
        self.username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Username"))
        self.username_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Username"))

        # Email entry
        self.email_entry = Entry(self.frame, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.email_entry.pack(pady=10)
        self.email_entry.insert(0, "Email address")
        self.email_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Email address"))
        self.email_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Email address"))

        # Password entry
        self.password_entry = Entry(self.frame, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.password_entry.pack(pady=10)
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Password"))
        self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Password"))

        # Confirm password entry
        self.confirm_password_entry = Entry(self.frame, font=("Helvetica", 16), width=30, fg='grey', bg='#f0f0f0')
        self.confirm_password_entry.pack(pady=10)
        self.confirm_password_entry.insert(0, "Confirm Password")
        self.confirm_password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Confirm Password"))
        self.confirm_password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, "Confirm Password"))

        # Sign up button
        signup_button = Button(self.frame, text="Sign Up", font=("Helvetica", 16), width=30, height=1, bg="#c8102e", fg=settings.text_color, command=self.signup)
        signup_button.pack(pady=20)

        # Back to login link
        login_link = Label(self.frame, text="Back to Login", font=("Helvetica", 12), bg='white', fg=settings.secondary_color, cursor="hand2")
        login_link.pack()
        login_link.bind("<Button-1>", lambda e: self.go_to_login())

        self.window.mainloop()

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg='black', show="*" if placeholder in ["Password", "Confirm Password"] else "")

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey', show="")

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Perform signup actions here, like saving the user data

        messagebox.showinfo("Success", f"Account created successfully for {username}!")
        self.window.destroy()
        root = Tk()
        App()
        root.mainloop()

    def go_to_login(self):
        self.window.destroy()
        root = Tk()
        App()
        root.mainloop()

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg='black', show="*" if placeholder in ["Password", "Confirm Password"] else "")

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey', show="")

    def signup(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Perform signup actions here, like saving the user data

        messagebox.showinfo("Success", "Account created successfully!")
        self.window.destroy()
        root = Tk()
        App()
        root.mainloop()


class MainInterface:
    def __init__(self, root):
        self.window = root
        self.window.title("Roskill Roundup Main Interface")
        self.window.geometry("1200x800")
        self.window.state('zoomed')

        self.window.configure(bg='white')

        self.top_frame = Frame(self.window, background=settings.primary_color, height=80)
        self.top_frame.pack(side=TOP, fill=X)

        mrgs_logo_path = os.path.join("images", "mrgs_logo.png")
        self.mrgs_logo = Image.open(mrgs_logo_path)
        self.mrgs_logo = self.mrgs_logo.resize((150, 75), Image.LANCZOS)
        self.mrgs_logo = ImageTk.PhotoImage(self.mrgs_logo)
        logo_label = Label(self.top_frame, image=self.mrgs_logo, bg=settings.primary_color)
        logo_label.pack(side=LEFT, padx=10, pady=10)

        title_label = Label(self.top_frame, text=settings.app_title, font=("Helvetica", 36, "bold"), bg=settings.primary_color, fg=settings.text_color)
        title_label.pack(side=LEFT, padx=10, pady=10)

        self.sidebar = Frame(self.window, width=200, bg=settings.primary_color, height=600, relief="sunken", borderwidth=2)
        self.sidebar.pack(expand=False, fill='y', side='left', anchor='nw')

        self.sidebar_options = [
            {"label": "Home", "command": self.show_home},
            {"label": "Classrooms", "command": self.show_classrooms},
            {"label": "Assignments", "command": self.show_assignments},
            {"label": "Calendar", "command": self.show_calendar},
        ]

        self.sidebar_buttons = {}
        for option in self.sidebar_options:
            button = Button(self.sidebar, text=option["label"], font=("Helvetica", 16), bg=settings.primary_color, fg='white', command=option["command"])
            button.pack(fill=X, pady=2)
            self.sidebar_buttons[option["label"]] = button

        self.content_frame = Frame(self.window, bg='white')
        self.content_frame.pack(expand=True, fill=BOTH, side=RIGHT)

        self.show_home()

    def show_home(self):
        self.clear_content_frame()
        self.sidebar_buttons["Home"].config(font=("Helvetica", 16, "bold"))
        home_label = Label(self.content_frame, text="Home", font=("Helvetica", 24), bg='white')
        home_label.pack(pady=10)

    def show_classrooms(self):
        self.clear_content_frame()
        self.sidebar_buttons["Classrooms"].config(font=("Helvetica", 16, "bold"))
        classrooms_label = Label(self.content_frame, text="Classrooms", font=("Helvetica", 24), bg='white')
        classrooms_label.pack(pady=10)

    def show_assignments(self):
        self.clear_content_frame()
        self.sidebar_buttons["Assignments"].config(font=("Helvetica", 16, "bold"))
        assignments_label = Label(self.content_frame, text="Assignments", font=("Helvetica", 24), bg='white')
        assignments_label.pack(pady=10)

    def show_calendar(self):
        self.clear_content_frame()
        self.sidebar_buttons["Calendar"].config(font=("Helvetica", 16, "bold"))
        calendar_label = Label(self.content_frame, text="Calendar", font=("Helvetica", 24), bg='white')
        calendar_label.pack(pady=10)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        for button in self.sidebar_buttons.values():
            button.config(font=("Helvetica", 16))


if __name__ == "__main__":
    app = App()