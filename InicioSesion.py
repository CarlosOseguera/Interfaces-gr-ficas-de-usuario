import tkinter as tk

class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Inicio de Sesión")

        # Etiqueta de Usuario
        self.label_user = tk.Label(master, text="Usuario:")
        self.label_user.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.entry_user = tk.Entry(master)
        self.entry_user.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.entry_user.focus_set()
        self.entry_user.bind("<Return>", lambda event: self.switch_focus(event, self.entry_pass))

        # Etiqueta de Contraseña
        self.label_pass = tk.Label(master, text="Contraseña:")
        self.label_pass.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.entry_pass = tk.Entry(master, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.entry_pass.bind("<Return>", lambda event: self.switch_focus(event, self.btn_ingresar))

        # Botón de Ingresar
        self.btn_ingresar = tk.Button(master, text="Ingresar", command=self.print_values)
        self.btn_ingresar.grid(row=2, column=1, padx=10, pady=10, sticky="SE")
        self.btn_ingresar.bind("<Return>", self.print_values)

        # Ajustar tamaño de la ventana
        master.geometry("240x150")

    def switch_focus(self, event, next_widget):
        next_widget.focus_set()

    def print_values(self, event=None):
        usuario = self.entry_user.get()
        contrasena = self.entry_pass.get()
        print("Usuario:", usuario)
        print("Contraseña:", contrasena)

root = tk.Tk()
gui = LoginGUI(root)
root.mainloop()