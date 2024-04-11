import customtkinter as ctk
from tkinter import *

def criartelaclientes(frame):
    frame.pack(side=RIGHT)

def Removertelaclientes(frame): 
    frame.pack_forget()

def parametrosinicias(frame):
    filter_frame = ctk.CTkFrame(master=frame, width=900, height=100, fg_color=("#801090"))
    filter_frame.pack(side=TOP)
    list_frame = ctk.CTkFrame(master=frame, width=900, height=480, fg_color=("#809090"))
    list_frame.pack(side=TOP)
