# -*- coding: utf-8 -*-
"""Fibonacci number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J0AAtc08QqMgultDLNoN8moD-cZwzS6L
"""

nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1