# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:27:18 2024

@author: ADMIN
"""

distance=float(input("nhap do dai den truongm"))
if distance>1200:
    print("thoi nho ban cho")
elif distance<300:
    print("di bo tot")
elif distance>=300 and distance<=1200:
    print("thoi nho ban cho")
else:
    print("khong biet nua")
    