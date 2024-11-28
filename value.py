import subprocess
import sys

import tkinter as tk
import threading
from tkinter import messagebox
# from code import *


def submit():
    a = input_field.get()
    print(f"User input: {a}")
    
    while True:

        
        if a=="1":
            import random


            def rabinMiller(n, m):
                a = random.randint(2, (n - 2) - 2)
                x = pow(a, int(m), n)  # a^m (modn)
                if x == 1 or x == n - 1:
                    return True

                # square x
                while m != n - 1:
                    
                    x = pow(x, 2, n)
                    m *= 2

                    if x == 1:
                        return False
                    elif x == n - 1:
                        return True

                # is not prime
                return False


            def isPrime(n):
                """
                    return True if n prime
                    fall back to rabinMiller if uncertain
                """

                # 0, 1, -ve numbers not prime
                if n < 2:
                    return False

                # low prime numbers to save time
                lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                             101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                             199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                             317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                             443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                             577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                             701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                             839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
                             983, 991, 997]

                # if in lowPrimes
                if n in lowPrimes:
                    return True

                # if low primes divide into n
                for prime in lowPrimes:
                    if n % prime == 0:
                        return False

                # find number m such that m * 2 ^ k = n - 1
                m = n - 1  # m even bc n not divisible by 2
                while m % 2 == 0:
                    m /= 2  # make m odd

                # prove not prime 128 times
                for i in range(128):
                    if not rabinMiller(n, m):
                        return False

                return True


            def generateKeys(keysize=1024):
                e = d = N = 0

                # get prime nums, p & q
                p = generateLargePrime(keysize)
                q = generateLargePrime(keysize)
                p_q='p: {}\nq:{}\n'.format(p,q)
                with open("output.txt", "w") as f:
                    f.write(p_q)
                

                N = p * q  # RSA Modulus
                phiN = (p - 1) * (q - 1)  # totient

                # choose e
                # e is coprime with phiN & 1 < e <= phiN
                while True:
                    e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
                    if (isCoPrime(e, phiN)):
                        break

                # choose d
                # d is mod inv of e with respect to phiN, e^d (mod phiN) = 1
                d = modularInv(e, phiN)

                return e, d, N


            def generateLargePrime(keysize):
                """
                    return random large prime number of keysize bits in size
                """

                while True:
                    num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
                    if (isPrime(num)):
                        return num


            def isCoPrime(p, q):
                """
                    return True if gcd(p, q) is 1
                    relatively prime/ co prime
                """

                return gcd(p, q) == 1


            def gcd(p, q):
                """
                    euclidean algorithm to find gcd of p and q
                """

                while q:
                    p, q = q, p % q
                return p


            def egcd(a, b):  # (extended Euclidean algorithm) # e^d mod phinN =1  (e,phiN)
                s = 0
                old_s = 1
                t = 1
                old_t = 0
                r = b
                old_r = a

                while r != 0:
                    quotient = old_r // r
                    old_r, r = r, old_r - quotient * r
                    old_s, s = s, old_s - quotient * s
                    old_t, t = t, old_t - quotient * t

                # return gcd, x, y
                return old_r, old_s, old_t


            def modularInv(a, b):   # e^d mod phinN =1  (e,phiN)
                gcd, x, y = egcd(a, b)

                if x < 0:
                    x += b

                return x


            def main():
                messagebox.showinfo("Result" , "Key is generated")
                keysize = 32
                e, d, N = generateKeys(keysize)
                output='e: {}\nd:{}\nN:{}'.format(e,d,N)
                with open("output.txt", "w") as f:
                    f.write(output)


            main()
            break
        if a=="2":
            root.destroy()
            subprocess.run(["python", "logic.py"])
            break
        if a == "3":
            root.destroy()
            sys.exit(0)
            break
         
           




root = tk.Tk()
root.geometry("450x250")

root.title("Input Form")

root.config(bg="#1F2041")


# Creating a label widget
input_label = tk.Label(root, text="1 for generate key \n 2 for encryption and decryption \n 3 for exit",font=("Arial", 15),fg="white",bg="#1F2041")

# Creating an entry widget
input_field = tk.Entry(root)

# Creating a submit button
submit_button = tk.Button(root, text="Submit", command=submit,bg="#FFC857",border=2,cursor='hand2',font=("Arial", 15),highlightthickness=5,height=1,width=10)

# Placing the widgets in the window
input_label.pack(pady=30)
input_field.pack()
submit_button.pack(pady=20)
root.resizable(0, 0)


root.mainloop()
