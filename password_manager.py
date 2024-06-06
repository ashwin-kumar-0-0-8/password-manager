import os
import random
import string
from cryptography.fernet import Fernet
import customtkinter as ctk
import tkinter as tk

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for i in range(length))
    return strong_password

# Function to load or generate encryption key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

# Function to add a new password entry
def add_password(username, password, fernet):
    encrypted_password = fernet.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as file:
        file.write(f"{username} | {encrypted_password}\n")

# Function to view all saved passwords
def view_passwords(fernet):
    passwords = []
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as file:
            for line in file:
                username, encrypted_password = line.strip().split(' | ')
                decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                passwords.append(f"Username: {username}, Password: {decrypted_password}")
    else:
        passwords.append("No passwords saved yet.")
    return passwords

def main():
    master_password = "YourMasterPassword"  # Set your master password here

    def ask_string(title, prompt, show='*'):
        dialog = ctk.CTkToplevel(root)
        dialog.title(title)
        dialog.geometry("300x150")

        label = ctk.CTkLabel(dialog, text=prompt)
        label.pack(pady=10)

        entry = ctk.CTkEntry(dialog, show=show)
        entry.pack(pady=10)

        def on_ok():
            dialog.result = entry.get()
            dialog.destroy()

        button = ctk.CTkButton(dialog, text="OK", command=on_ok)
        button.pack(pady=10)

        root.wait_window(dialog)
        return getattr(dialog, 'result', None)

    def show_info(title, message):
        info_dialog = ctk.CTkToplevel(root)
        info_dialog.title(title)
        info_dialog.geometry("300x150")

        label = ctk.CTkLabel(info_dialog, text=message)
        label.pack(pady=10)

        button = ctk.CTkButton(info_dialog, text="OK", command=info_dialog.destroy)
        button.pack(pady=10)

        root.wait_window(info_dialog)

    def show_error(title, message):
        error_dialog = ctk.CTkToplevel(root)
        error_dialog.title(title)
        error_dialog.geometry("300x150")

        label = ctk.CTkLabel(error_dialog, text=message)
        label.pack(pady=10)

        button = ctk.CTkButton(error_dialog, text="OK", command=error_dialog.destroy)
        button.pack(pady=10)

        root.wait_window(error_dialog)

    def on_copy():
        generated_password
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()  # required to ensure clipboard content is set immediately
        show_info("Copied", "Password copied to clipboard!")

    # Prompt the user for the master password using a GUI dialog
    root = ctk.CTk()
    root.withdraw()
    entered_password = ask_string("Master Password", "Enter the master password:")
    if entered_password != master_password:
        show_error("Error", "Incorrect master password!")
        return

    key = load_key()
    fernet = Fernet(key)

    def add_password_gui():
        username = ask_string("Input", "Enter the username:")
        password = ask_string("Input", "Enter the password:")
        if username and password:
            add_password(username, password, fernet)
            show_info("Success", "Password added successfully!")
        else:
            show_error("Input Error", "Username and password cannot be empty.")

    def view_passwords_gui():
        passwords = view_passwords(fernet)
        show_info("Saved Passwords", "\n".join(passwords))

    def generate_password_gui():
        def on_copy():
            nonlocal generated_password
            root.clipboard_clear()
            root.clipboard_append(generated_password)
            root.update()  # required to ensure clipboard content is set immediately
            show_info("Copied", "Password copied to clipboard!")

        length = ask_string("Input", "Enter the desired password length:")
        try:
            length = int(length)
            if 4 <= length <= 128:
                generated_password = generate_strong_password(length)
                dialog = ctk.CTkToplevel(root)
                dialog.title("Generated Password")
                dialog.geometry("300x200")

                label = ctk.CTkLabel(dialog, text=f"Generated strong password:\n{generated_password}")
                label.pack(pady=10)

                copy_button = ctk.CTkButton(dialog, text="Copy", command=on_copy)
                copy_button.pack(pady=10)

                button = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)
                button.pack(pady=10)

                root.wait_window(dialog)

            else:
                show_error("Input Error", "Password length must be between 4 and 128.")
        except ValueError:
            show_error("Input Error", "Invalid input. Please enter a number.")

    def exit_app():
        root.destroy()

    # Set up the main GUI window
    ctk.set_appearance_mode("dark")  # Set the theme to dark mode
    root = ctk.CTk()
    root.title("Password Manager")
    root.geometry("600x400")  # Set the window size

    ctk.CTkLabel(root, text="Password Manager", font=("Helvetica", 20)).pack(pady=20)

    ctk.CTkButton(root, text="Add New Password", command=add_password_gui).pack(pady=10)
    ctk.CTkButton(root, text="View Saved Passwords", command=view_passwords_gui).pack(pady=10)
    ctk.CTkButton(root, text="Generate Strong Password", command=generate_password_gui).pack(pady=10)
    ctk.CTkButton(root, text="Exit", command=exit_app).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
