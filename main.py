import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import sqlite3


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window_config()
        self.janela_inicial()

    def coletar_dados_formulario(self):

        self.codigo = self.codigo_value.get()
        self.nome = self.name_value.get()
        self.contato = self.contato_value.get()
        self.cidade = self.cidade_value.get()

        return self.codigo, self.nome, self.contato, self.cidade
    def window_config(self):
        self.title('Cadastro de Clientes')
        self.geometry('700x500')
        self.resizable(False, False)

    def salvando_dados(self):
        with sqlite3.connect('clientes.db') as conexao:
            self.coletar_dados_formulario()

            self.db = conexao.cursor()
            self.db.execute('create table if not exists clientes(codigo integer, nome text, contato text, cidade text)')

            self.valor_para_verificar = self.codigo
            self.sql = 'SELECT 1 FROM clientes WHERE codigo = ? LIMIT 1'
            self.db.execute(self.sql, (self.valor_para_verificar,))
            self.resultado = self.db.fetchone()

            if self.resultado:
                messagebox.showinfo('Codigo já existe', f'O Código {self.valor_para_verificar}, já existe!')
            else:
                self.db.execute('insert into clientes values(?,?,?,?)',
                                [self.codigo, self.nome, self.contato, self.cidade])
                conexao.commit()
                messagebox.showinfo('Sucesso', 'Cliente adicionado com sucesso')
                self.limpar_campos()

    def ler_banco_de_dados(self):
        with sqlite3.connect('clientes.db') as conexao:
            self.db = conexao.cursor()
            # clientes = self.db.execute('select * from clientes')
            # for cliente in clientes:
            #     print(cliente)

            self.valor_pesquisa = f'{self.codigo_entry.get()}'
            self.sql = 'SELECT * FROM clientes WHERE codigo = ?'

            self.db.execute(self.sql, (self.valor_pesquisa,))
            self.resultados = self.db.fetchall()

            if self.resultados:
                for linha in self.resultados:
                    self.codigo, self.nome, self.contato, self.cidade = linha
                    print(f'Codigo: {self.codigo}, Nome: {self.nome}, Contato = {self.contato}, Cidade: {self.cidade}')
                    self.codigo_value.set(self.codigo)
                    self.name_value.set(self.nome)
                    self.contato_value.set(self.contato)
                    self.cidade_value.set(self.cidade)
            else:
                messagebox.showinfo('Erro ao buscar', f'{self.valor_pesquisa}, não foi encontrado')

    def recuperar_dados(self):
        with sqlite3.connect('clientes.db') as conexao:
            self.db = conexao.cursor()
            self.db.execute('SELECT * FROM clientes')

            self.dados = self.db.fetchall()
            self.db.close()

            return self.dados

    def preencher_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.dados = self.recuperar_dados()

        for item in self.dados:
            self.tree.insert("", "end", values=item)

    def atualizar_tabela(self):
        self.preencher_tabela()
        self.after(1000, self.atualizar_tabela)

    def atualizar_dados(self):
        self.coletar_dados_formulario()

        self.conexao = sqlite3.connect('clientes.db')
        self.db = self.conexao.cursor()


        self.sql = 'UPDATE clientes SET nome = ?, contato = ?, cidade = ? WHERE codigo = ?'

        self.db.execute(self.sql, (self.nome, self.contato, self.cidade, self.codigo))
        messagebox.showinfo('Alteração', 'Os dados foram alterados com sucesso!')
        self.conexao.commit()

    def excluir_linha(self):
        with sqlite3.connect('clientes.db') as conexao:
            db = conexao.cursor()
            id_para_excluir = self.codigo_entry.get()

            sql = 'DELETE FROM clientes WHERE codigo = ?'

            db.execute(sql, (id_para_excluir,))

            conexao.commit()
            print("Cliente excluido com sucesso!")

    def limpar_campos(self):
        self.codigo_value.set('')
        self.name_value.set('')
        self.contato_value.set('')
        self.cidade_value.set('')
        print('Todos os campos foram limpos!')

    def janela_inicial(self):

        self.codigo_value = StringVar()
        self.name_value = StringVar()
        self.contato_value = StringVar()
        self.cidade_value = StringVar()

        self.formulario_frame = ctk.CTkFrame(self, height=220, width=670, fg_color='grey')
        self.dados_frame = ctk.CTkFrame(self, height=220, width=670, fg_color='grey')

        self.formulario_frame.place(x=15, y=20)
        self.dados_frame.place(x=15, y=260)

        self.codigo_label = ctk.CTkLabel(self.formulario_frame, text='Código:', font=('arial bold', 18))
        self.nome_label = ctk.CTkLabel(self.formulario_frame, text='Nome:', font=('arial bold', 18))
        self.contato_label = ctk.CTkLabel(self.formulario_frame, text='Contato:', font=('arial bold', 18))
        self.cidade_label = ctk.CTkLabel(self.formulario_frame, text='Cidade:', font=('arial bold', 18))

        self.codigo_entry = ctk.CTkEntry(self.formulario_frame, width=100, height=30, font=('arial', 16),
                                         fg_color='white', text_color='black', textvariable=self.codigo_value)
        self.nome_entry = ctk.CTkEntry(self.formulario_frame, width=500, height=30, font=('arial', 16),
                                       fg_color='white', text_color='black', textvariable=self.name_value)
        self.contato_entry = ctk.CTkEntry(self.formulario_frame, width=200, height=30, font=('arial', 16),
                                          fg_color='white', text_color='black', textvariable=self.contato_value)
        self.cidade_entry = ctk.CTkEntry(self.formulario_frame, width=200, height=30, font=('arial', 16),
                                         fg_color='white', text_color='black', textvariable=self.cidade_value)

        self.botao_limpar = ctk.CTkButton(self.formulario_frame, text='Limpar', width=60, height=30,
                                          font=('arial bold', 18), command=self.limpar_campos)
        self.botao_buscar = ctk.CTkButton(self.formulario_frame, text='Buscar', width=60, height=30,
                                          font=('arial bold', 18), command=self.ler_banco_de_dados)
        self.botao_adicionar = ctk.CTkButton(self.formulario_frame, text='Novo', width=60, height=30,
                                             font=('arial bold', 18), command=self.salvando_dados)
        self.botao_alterar = ctk.CTkButton(self.formulario_frame, text='Alterar', width=60, height=30,
                                           font=('arial bold', 18), command= self.atualizar_dados)
        self.botao_excluir = ctk.CTkButton(self.formulario_frame, text='Excluir', width=60, height=30,
                                           font=('arial bold', 18), command=self.excluir_linha)

        self.botao_limpar.place(x=200, y=20)
        self.botao_buscar.place(x=275, y=20)
        self.botao_adicionar.place(x=400, y=20)
        self.botao_alterar.place(x=470, y=20)
        self.botao_excluir.place(x=545, y=20)

        self.codigo_label.place(x=20, y=20)
        self.nome_label.place(x=20, y=70)
        self.contato_label.place(x=20, y=120)
        self.cidade_label.place(x=320, y=120)

        self.codigo_entry.place(x=90, y=20)
        self.nome_entry.place(x=90, y=70)
        self.contato_entry.place(x=90, y=120)
        self.cidade_entry.place(x=390, y=120)

        self.dados_frame.place(x=15, y=260)

        # Definir colunas da tabela
        self.colunas = ("Codigo", "Nome", "Contato", "Cidade")

        # Criar tabela usando ttk.treeview
        self.tree = ttk.Treeview(self.dados_frame, columns=self.colunas, show="headings")

        self.tree.heading('Codigo', text='Codigo')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Contato', text='Contato')
        self.tree.heading('Cidade', text='Cidade')

        self.tree.column('Codigo', width=166, anchor='center')
        self.tree.column('Nome', width=166)
        self.tree.column('Contato', width=166, anchor='center')
        self.tree.column('Cidade', width=166, anchor='center')

        # Adicionar a tabela ao frame
        self.tree.pack(fill='both', expand=True)

        # Configurar o estilo da tabela para combinar com o CustomTkinter
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")  # Usar o tema "Clam" que é mais moderno
        self.estilo.configure('Treeview.Heading', background='#2E2E2E', foreground='white')
        self.estilo.configure('Treeview', background='#1E1E1E', foreground='white', fieldbackground='#1E1E1E')

        self.preencher_tabela()
        self.atualizar_tabela()


if __name__ == '__main__':
    app = App()
    app.mainloop()
