import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window_config()
        self.janela_inicial()


    def window_config(self):
        self.title('Cadastro de Clientes')
        self.geometry('700x500')
        self.resizable(False, False)

    def janela_inicial(self):
        self.formulario_frame = ctk.CTkFrame(self, height=220, width=670, fg_color='grey')
        self.dados_frame = ctk.CTkFrame(self, height=220, width=670, fg_color='grey')


        self.formulario_frame.place(x = 15, y = 20)
        self.dados_frame.place(x = 15, y = 260)

        self.codigo_label = ctk.CTkLabel(self.formulario_frame, text='Código:', font=('arial bold', 18))
        self.nome_label = ctk.CTkLabel(self.formulario_frame, text='Nome:', font=('arial bold', 18))
        self.contato_label = ctk.CTkLabel(self.formulario_frame, text='Contato:', font=('arial bold', 18))
        self.cidade_label = ctk.CTkLabel(self.formulario_frame, text='Cidade:', font=('arial bold', 18))

        self.codigo_entry = ctk.CTkEntry(self.formulario_frame, width=100, height=30, font=('arial', 16), fg_color='white', text_color='black')
        self.nome_entry = ctk.CTkEntry(self.formulario_frame, width=500, height=30, font=('arial', 16), fg_color='white', text_color='black')
        self.contato_entry = ctk.CTkEntry(self.formulario_frame, width=200, height=30, font=('arial', 16), fg_color='white', text_color='black')
        self.cidade_entry = ctk.CTkEntry(self.formulario_frame, width=200, height=30, font=('arial', 16), fg_color='white', text_color='black')

        self.botao_limpar = ctk.CTkButton(self.formulario_frame, text='Limpar', width=60, height=30, font=('arial bold', 18))
        self.botao_buscar = ctk.CTkButton(self.formulario_frame, text='Buscar', width=60, height=30,font=('arial bold', 18))
        self.botao_adicionar = ctk.CTkButton(self.formulario_frame, text='Novo', width=60, height=30,font=('arial bold', 18))
        self.botao_alterar = ctk.CTkButton(self.formulario_frame, text='Alterar', width=60, height=30, font=('arial bold', 18))
        self.botao_excluir = ctk.CTkButton(self.formulario_frame, text='Excluir', width=60, height=30, font=('arial bold', 18))

        self.botao_limpar.place(x = 200, y = 20)
        self.botao_buscar.place(x = 275, y = 20)
        self.botao_adicionar.place(x = 400, y = 20)
        self.botao_alterar.place(x = 470, y = 20)
        self.botao_excluir.place(x = 545, y = 20)

        self.codigo_label.place(x = 20, y = 20)
        self.nome_label.place(x = 20, y = 70)
        self.contato_label.place(x = 20, y = 120)
        self.cidade_label.place(x = 320, y = 120)

        self.codigo_entry.place(x = 90, y = 20)
        self.nome_entry.place(x = 90, y = 70)
        self.contato_entry.place(x = 90, y = 120)
        self.cidade_entry.place(x = 390, y = 120)


if __name__ == '__main__':
    app = App()
    app.mainloop()