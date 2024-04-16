import customtkinter as ctk
from tkinter import *

def criartelauser(frame):
    frame.pack(side=RIGHT, fill = BOTH,expand=True)

def Removertelauser(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    frame_top_user = ctk.CTkFrame(master=frame, width=900, height=100, fg_color=("#8E44AD"))
    frame_top_user.pack(side=TOP, fill = X)
    list_users = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#F7F9F9"))
    list_users.pack(side=TOP, fill = X)