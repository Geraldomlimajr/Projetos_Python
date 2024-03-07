import customtkinter #importação da bilioteca Ctk
from tkinter import *
from PIL import Image, ImageTk

#Configuração do tema

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#configuração da janela
janela= customtkinter.CTk()
janela.geometry("700x350")
janela.title("Biblioteca python")
janela.iconbitmap("icone_python.ico")
janela.resizable(False,False)



#construção dos frames cadastro e logo para a inserção da image e os campos de cadastro.
frame_logo=customtkinter.CTkFrame(master=janela,width=200,height=350)
frame_logo.pack(side=LEFT)

frame_cadastro=customtkinter.CTkFrame(master=janela,width=500,height=350)
frame_cadastro.pack(side=RIGHT)

imagem_fundo = customtkinter.CTkImage(light_image=Image.open(r"logo_python.png"),size=(200,350))

texto_apresentacao="""Bem vindos \na biblioteca de \nlivros python



"""

label_imagem=customtkinter.CTkLabel(master=frame_logo,image=imagem_fundo,text=texto_apresentacao,font=("Roboto",18,"bold"),text_color="white",compound=("center")).place(x=0,y=0)

label_cadastro=customtkinter.CTkLabel(master=frame_cadastro,text="Cadastre um titulo que queira ver em \nnossa biblioteca.",font=("Roboto",20,"roman","bold")).place(x=55,y=5)

label_titulo=customtkinter.CTkLabel(master=frame_cadastro,text="Titulo:",font=("Roboto",16,"roman","bold")).place(x=55,y=90)

entrada_titulo=customtkinter.CTkEntry(master=frame_cadastro,placeholder_text="", width=350, font=("Roboto",16)).place(x=55,y=115)


label_autor=customtkinter.CTkLabel(master=frame_cadastro,text="Autor:",font=("Roboto",16,"roman","bold")).place(x=55,y=150)

entrada_autor=customtkinter.CTkEntry(master=frame_cadastro,placeholder_text="", width=350, font=("Roboto",16)).place(x=55,y=175)

btn_cadastrar=customtkinter.CTkButton(master=frame_cadastro,width=150,height=40,text="Cadastrar",font=("Roboto",18,"bold")).place(x=150,y=270)

btn_acervo=customtkinter.CTkButton(master=frame_logo, text="Acesse o \nnosso acervo",fg_color="black",font=("Roboto",18,"bold"),border_width=6,corner_radius=6).place(x=25,y=210)



janela.mainloop()






