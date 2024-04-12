import customtkinter as ctk
from tkinter import *

def criartelamei(frame):
    frame.pack(side=RIGHT, fill = BOTH,expand=True)

def Removertelamei(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    filter_frame = ctk.CTkFrame(master=frame, width=900, height=100, fg_color=("#32CD32"))
    filter_frame.pack(side=TOP, fill = X)
    list_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#809090"))
    list_frame.pack(side=TOP, fill = X)