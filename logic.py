import sys
from tkinter import *
import tkinter as tk
import threading
from tkinter import messagebox
import math

def me():
    def open_new_window():
        if get_field.get()=="1":
            window = tk.Toplevel(root)
            window.title("RSA Encryption")
            window.geometry("540x400")
            window.config(bg="#1F2041")
            tk.Label(window, text="RSA Encryption/Decryption Tool", font=("Arial", 16),fg="white",bg="#1F2041",pady=40).grid(row=0, columnspan=2,)
            tk.Label(window, text="Encryption Key:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=1, column=0)
            global new_entry
            new_entry = tk.Entry(window, width=50)
            new_entry.grid(row=1, column=1)
            tk.Label(window, text="N",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=2, column=0)
            global private_key_entry
            private_key_entry = tk.Entry(window, width=50)
            private_key_entry.grid(row=2, column=1)
            tk.Label(window, text="Message:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=4, column=0)
            global message_entry
            message_entry = tk.Entry(window, width=50)
            message_entry.grid(row=4, column=1)
            tk.Button(window, text="Encrypt",command=give,bg="#FFC857",border=2,cursor='hand2',font=("Arial", 15),highlightthickness=5,height=1,width=10).grid(row=5, column=1, pady=10)
            tk.Label(window, text="Encrypted Message:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=6, column=0)
            global encrypted_message_entry
            encrypted_message_entry = tk.Entry(window, width=50)
            encrypted_message_entry.grid(row=6, column=1)
            root.resizable(0, 0)
        else:
            if get_field.get()=="2":
                window = tk.Toplevel(root)
                window.title("RSA Decryption")
                window.geometry("550x400")
                window.config(bg="#1F2041")
                tk.Label(window, text="RSA Encryption/Decryption Tool", font=("Arial", 16),fg="white",bg="#1F2041",pady=40).grid(row=0, columnspan=2,)
                tk.Label(window, text="Encryption Key:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=1, column=0)
                new_entry = tk.Entry(window, width=50)
                new_entry.grid(row=1, column=1)
                tk.Label(window, text="N",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=2, column=0)
                private_key_entry = tk.Entry(window, width=50)
                private_key_entry.grid(row=2, column=1)
                tk.Label(window, text="Decryption Key:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=3, column=0)
                global decrep_key_entry
                decrep_key_entry = tk.Entry(window, width=50)
                decrep_key_entry.grid(row=3, column=1)
                tk.Label(window, text="Message:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=4, column=0)
                message_entry = tk.Entry(window, width=50)
                message_entry.grid(row=4, column=1)
                tk.Button(window, text="Decrypt",command=give,bg="#FFC857",border=2,cursor='hand2',font=("Arial", 15),highlightthickness=5,height=1,width=10).grid(row=5, column=1, pady=10)
                tk.Label(window, text="Decrypted Message:",fg="white",bg="#1F2041",font=("Arial", 15)).grid(row=6, column=0)
                global Decrypted_message_entry
                Decrypted_message_entry = tk.Entry(window, width=50)
                Decrypted_message_entry.grid(row=6, column=1)
                root.resizable(0, 0)

    def give():
        
        def encrypt(e, N, msg):
            e = int(e)
            N= int(N)
            # if isinstance(e, str):
            #     e = int(e)
            # if isinstance(N, str):
            #    e = int(e)
        
        # Initialize the ciphertext
            cipher = ""
        
        # Encrypt each character in the message
            for c in msg:
                m = ord(c)
                cipher += str(pow(m, e, N)) + " "
        
            return cipher.strip()


        def decrypt(d, N, cipher):
            a = ""
            parts = cipher.split()
            for part in parts:
                if part:
                    c = int(part)
                    a += chr(pow(c, d, N))
            return a






        def main_1():
            t = get_field.get()
            print(f"User input: {t}")
            print(new_entry)
            e=new_entry.get()
            print(f"Value of e: {e}")
            N=private_key_entry.get()
            print(f"Value of n: {N}")
            print("Hello, RSA!")
            msg= message_entry.get()
            print(f"Your msg: {msg}")
            if t == "1":
                enc = encrypt(e, N, msg)
                
                encrypted_message_entry.insert(0, enc)
            elif t == "2":
                d = decrep_key_entry.get()
                N = int(N)
                dec = decrypt(int(d), N, msg)
                Decrypted_message_entry.insert(0, dec)

            else:
                print("not valid")
        main_1()   




    root = tk.Tk()
    root.geometry("450x250")
    # height=450
    # width=530
    # x=(root.winfo_screenwidth()//2)-(width//2)
    # y=(root.winfo_screenheight()//2)-(height//2)
    # root.geometry('{}x{}+{}+{}'.format(width,height,x,y))

    root.title("Input Form")

    root.config(bg="#1F2041")


    # Creating a label widget
    input_label = tk.Label(root, text="enter the choice\n 1 for encryption 2 for decryption\n",font=("Arial", 15),fg="white",bg="#1F2041")

    # Creating an entry widget
    get_field = tk.Entry(root)

    # Creating a give button
    give_button = tk.Button(root, text="give", command=open_new_window,bg="#FFC857",border=2,cursor='hand2',font=("Arial", 15),highlightthickness=5,height=1,width=10)

    # Placing the widgets in the window
    input_label.pack(pady=30)
    get_field.pack()
    give_button.pack(pady=20)
    root.resizable(0, 0)


    root.mainloop()

me()

