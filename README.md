# Password Manager

A simple password manager application built with Python, `customtkinter`, and `cryptography`. This password manager allows users to add, view, and generate strong passwords, all stored securely in an encrypted format.No database instead uses a text file which the inforamtion is encrypted and uses only python 

## Features

- **Add New Password**: Save a new username and password pair securely.
- **View Saved Passwords**: Display all saved usernames and their decrypted passwords.
- **Generate Strong Password**: Generate a strong password of a specified length.
- **Copy to Clipboard**: Copy generated passwords to the clipboard for easy use.
- **Secure Storage**: Passwords are encrypted using the AES encryption standard.

## Prerequisites

- Python 3.7 or later
- `cryptography` library
- `customtkinter` library

## Installation

1. Clone the repository or download the source code.
2. Install the required Python libraries:

```sh
pip install cryptography 
pip install customtkinter
