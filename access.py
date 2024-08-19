import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class AccessEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.username = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")

        # form entries
        self.create_form_entry("Username", self.username)
        self.create_form_entry("Password", self.password)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Log in",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        print("Name:", self.username.get())
        print("Password:", self.password.get())
        return self.username.get(), self.password.get()

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("CRBC LOGIN", "litera", resizable=(False, False))
    app.iconbitmap(r"logo.ico")
    AccessEntryForm(app)
    app.mainloop()
