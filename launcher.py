from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton


class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.name = None
        self.host = None
        self.port = None

        self.title("Agario Launcher")
        self.geometry("300x400")

        self.title_label = CTkLabel(
            self,
            text="Connect to server:",
            font=("Comic Sans MS", 20, "bold"),
            pady=15,
            padx=20,
            anchor="w",
        )
        self.title_label.pack(fill="x")

        self.name_entry = CTkEntry(
            self,
            placeholder_text="Введіть ім'я:",
            height=50,
        )
        self.name_entry.pack(fill="x", padx=20)

        self.host_entry = CTkEntry(
            self,
            placeholder_text="Введіть хост:",
            height=50,
        )
        self.host_entry.pack(fill="x", padx=20, pady=15)

        self.port_entry = CTkEntry(
            self,
            placeholder_text="Введіть порт сервера:",
            height=50,
        )
        self.port_entry.pack(fill="x", padx=20)

        self.connect_button = CTkButton(
            self,
            text="Приєднатися",
            height=50,
            command=self.open_game,
        )
        self.connect_button.pack(fill="x", padx=20, pady=15)

    def open_game(self):
        self.name = self.name_entry.get()
        self.host = self.host_entry.get()
        self.port = int(self.port_entry.get())
        self.destroy()


if __name__ == "__main__":
    window = ConnectWindow()
    window.mainloop()