# wallet
    def screen_new_spent(self):
        new_screen = ctk.CTkToplevel(self)
        new_screen.title = ("New Spent")
        new_screen.geometry("300x350")

        ctk.CTkLabel(new_screen, text="Value:").pack(pady=5)
        entry_value = ctk.CTkEntry(new_screen)
        entry_value.pack(pady=5)

        ctk.CTkLabel(new_screen, text="Category:").pack(pady=5)
        entry_category = ctk.CTkEntry(new_screen)
        entry_category.pack(pady=5)

        ctk.CTkLabel(new_screen, text="Date (dd/mm/yyyy):").pack(pady=5)
        entry_date = ctk.CTkEntry(new_screen)
        entry_date.pack(pady=5)

        def save_data():
            spent = Spent(value=entry_value.get(), category=entry_category.get(), date=entry_date.get())

            if write_data(spent):
                new_screen.destroy()
            else:
                error_label = ctk.CTkLabel(new_screen, text="Erro ao salvar o arquivo!", text_color="red")
                error_label.pack(pady=10)

        ctk.CTkButton(new_screen, text="Save", command=save_data).pack(pady=20)