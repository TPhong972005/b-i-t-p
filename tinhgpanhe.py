# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:13:49 2024

@author: ADMIN
"""

GPA=float(input("nhap diem hoc luc cua ban(thandiem10):"))
if GPA<3.5:
    print("hoc luc kem")
elif GPA>=3.5 and GPA<5.0:
    print("hoc luc yeu")
elif GPA>=5.0 and GPA<7.0:
    print("hoc luc trung binh")
elif GPA>=7.0 and GPA<8.0:
    print("hoc luc kha")
elif GPA>=8.0 and GPA<9.0:
    print("hoc luc gioi")
elif GPA>=9.0 and GPA<=10:
    print("hoc luc xuat xac")
else:
    print("sai cu phap")
    
    