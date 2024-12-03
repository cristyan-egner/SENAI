import tkinter as tk
from tkinter import messagebox
import sqlite3

def inicializar_banco1():
    conn = sqlite3.connect('estoque_carros1.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inicializar_banco2():
    conn = sqlite3.connect('estoque_carros2.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inicializar_banco3():
    conn = sqlite3.connect('estoque_carros3.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class Carro:
    def __init__(self, modelo, ano, preco, id=None):
        self.id = id
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

class GerenciadorEstoque1:
    def __init__(self, master):
        self.master = master
        self.master.title("Estoque de Carros")

        self.estoque = []

        self.label = tk.Label(master, text="Estoque", fg='white', bg='black', width=89, height=4, font=("Lucida Console", 35))
        self.label.pack(side="top")

        self.listbox = tk.Listbox(master, width=100, height=29)
        self.listbox.place(x=150, y=310)

        self.label_modelo = tk.Label(master, text="Modelo do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_modelo.place(x=925, y=420)
        self.entry_modelo = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_modelo.place(x=1125, y=420)

        self.label_ano = tk.Label(master, text="Ano do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_ano.place(x=925, y=460)
        self.entry_ano = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_ano.place(x=1125, y=460)

        self.label_preco = tk.Label(master, text="Preço do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_preco.place(x=925, y=500)
        self.entry_preco = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_preco.place(x=1125, y=500)

        self.btn_adicionar = tk.Button(master, text="Adicionar Carro", command=self.adicionar_carro, height=2, font=("Lucida Console", 10))
        self.btn_adicionar.place(x=915, y=580)

        self.btn_remover = tk.Button(master, text="Remover Carro", command=self.remover_carro, height=2, font=("Lucida Console", 10))
        self.btn_remover.place(x=1115, y=580)

        self.btn_atualizar = tk.Button(master, text="Atualizar Info.", command=self.atualizar_carro, height=2, font=("Lucida Console", 10))
        self.btn_atualizar.place(x=1315, y=580)

        self.btn_relatorio = tk.Button(master, text="Relatório de Estoque", command=self.gerar_relatorio, height=2, font=("Lucida Console", 10))
        self.btn_relatorio.place(x=1090, y=660)

        self.estoque = self.carregar_estoque()

        self.atualizar_lista()

        self.seta = tk.PhotoImage(file="seta.png")
        self.btn_voltar = tk.Button(master, image=self.seta, command=self.voltar, background="black", bd=0, relief="flat")
        self.btn_voltar.seta = self.seta
        self.btn_voltar.place(x=35, y=68)

    def voltar(self):
        self.master.destroy()

    def conectar_banco1(self):
        return sqlite3.connect('estoque_carros1.db')

    def carregar_estoque(self):
        conn = self.conectar_banco1()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()
        conn.close()

        estoque = []
        for carro in carros:
            estoque.append(Carro(carro[1], carro[2], carro[3], carro[0]))
        return estoque

    def adicionar_carro(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco = self.entry_preco.get()

        if modelo and ano and preco:
            try:
                ano = int(ano)
                preco = float(preco)
                carro = Carro(modelo, ano, preco)

                conn = self.conectar_banco1()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO carros (modelo, ano, preco) VALUES (?, ?, ?)", (modelo, ano, preco))
                conn.commit()
                conn.close()

                self.estoque.append(carro)
                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def remover_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            conn = self.conectar_banco1()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM carros WHERE id = ?", (carro.id,))
            conn.commit()
            conn.close()

            del self.estoque[indice]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para remover.")

    def atualizar_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            self.entry_modelo.delete(0, tk.END)
            self.entry_modelo.insert(0, carro.modelo)

            self.entry_ano.delete(0, tk.END)
            self.entry_ano.insert(0, carro.ano)

            self.entry_preco.delete(0, tk.END)
            self.entry_preco.insert(0, carro.preco)

            self.btn_atualizar.config(command=lambda: self.confirmar_atualizacao(indice))
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para atualizar.")

    def confirmar_atualizacao(self, indice):
        novo_modelo = self.entry_modelo.get()
        novo_ano = self.entry_ano.get()
        novo_preco = self.entry_preco.get()

        if novo_modelo and novo_ano and novo_preco:
            try:
                novo_ano = int(novo_ano)
                novo_preco = float(novo_preco)
                carro = self.estoque[indice]
                carro.modelo = novo_modelo
                carro.ano = novo_ano
                carro.preco = novo_preco

                conn = self.conectar_banco1()
                cursor = conn.cursor()
                cursor.execute("UPDATE carros SET modelo = ?, ano = ?, preco = ? WHERE id = ?", 
                               (novo_modelo, novo_ano, novo_preco, carro.id))
                conn.commit()
                conn.close()

                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for carro in self.estoque:
            self.listbox.insert(tk.END, f"{carro.modelo} - {carro.ano} - R${carro.preco:.2f}")

    def limpar_campos(self):
        self.entry_modelo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def gerar_relatorio(self):
        if self.estoque:
            relatorio = "\n".join([f"Modelo: {carro.modelo} | Ano: {carro.ano} | Preço: R${carro.preco:.2f}" for carro in self.estoque])
            messagebox.showinfo("Relatório de Estoque", relatorio)
        else:
            messagebox.showinfo("Relatório de Estoque", "O estoque está vazio!")

class GerenciadorEstoque2:
    def __init__(self, master):
        self.master = master
        self.master.title("Estoque de Carros")

        self.estoque = []

        self.label = tk.Label(master, text="Estoque", fg='white', bg='black', width=89, height=4, font=("Lucida Console", 35))
        self.label.pack(side="top")

        self.listbox = tk.Listbox(master, width=100, height=29)
        self.listbox.place(x=150, y=310)

        self.label_modelo = tk.Label(master, text="Modelo do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_modelo.place(x=925, y=420)
        self.entry_modelo = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_modelo.place(x=1125, y=420)

        self.label_ano = tk.Label(master, text="Ano do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_ano.place(x=925, y=460)
        self.entry_ano = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_ano.place(x=1125, y=460)

        self.label_preco = tk.Label(master, text="Preço do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_preco.place(x=925, y=500)
        self.entry_preco = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_preco.place(x=1125, y=500)

        self.btn_adicionar = tk.Button(master, text="Adicionar Carro", command=self.adicionar_carro, height=2, font=("Lucida Console", 10))
        self.btn_adicionar.place(x=915, y=580)

        self.btn_remover = tk.Button(master, text="Remover Carro", command=self.remover_carro, height=2, font=("Lucida Console", 10))
        self.btn_remover.place(x=1115, y=580)

        self.btn_atualizar = tk.Button(master, text="Atualizar Info.", command=self.atualizar_carro, height=2, font=("Lucida Console", 10))
        self.btn_atualizar.place(x=1315, y=580)

        self.btn_relatorio = tk.Button(master, text="Relatório de Estoque", command=self.gerar_relatorio, height=2, font=("Lucida Console", 10))
        self.btn_relatorio.place(x=1090, y=660)

        self.estoque = self.carregar_estoque()

        self.atualizar_lista()

        self.seta = tk.PhotoImage(file="seta.png")
        self.btn_voltar = tk.Button(master, image=self.seta, command=self.voltar, background="black", bd=0, relief="flat")
        self.btn_voltar.seta = self.seta
        self.btn_voltar.place(x=35, y=68)

    def voltar(self):
        self.master.destroy()

    def conectar_banco2(self):
        return sqlite3.connect('estoque_carros2.db')

    def carregar_estoque(self):
        conn = self.conectar_banco2()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()
        conn.close()

        estoque = []
        for carro in carros:
            estoque.append(Carro(carro[1], carro[2], carro[3], carro[0]))
        return estoque

    def adicionar_carro(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco = self.entry_preco.get()

        if modelo and ano and preco:
            try:
                ano = int(ano)
                preco = float(preco)
                carro = Carro(modelo, ano, preco)

                conn = self.conectar_banco2()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO carros (modelo, ano, preco) VALUES (?, ?, ?)", (modelo, ano, preco))
                conn.commit()
                conn.close()

                self.estoque.append(carro)
                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def remover_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            conn = self.conectar_banco2()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM carros WHERE id = ?", (carro.id,))
            conn.commit()
            conn.close()

            del self.estoque[indice]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para remover.")

    def atualizar_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            self.entry_modelo.delete(0, tk.END)
            self.entry_modelo.insert(0, carro.modelo)

            self.entry_ano.delete(0, tk.END)
            self.entry_ano.insert(0, carro.ano)

            self.entry_preco.delete(0, tk.END)
            self.entry_preco.insert(0, carro.preco)

            self.btn_atualizar.config(command=lambda: self.confirmar_atualizacao(indice))
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para atualizar.")

    def confirmar_atualizacao(self, indice):
        novo_modelo = self.entry_modelo.get()
        novo_ano = self.entry_ano.get()
        novo_preco = self.entry_preco.get()

        if novo_modelo and novo_ano and novo_preco:
            try:
                novo_ano = int(novo_ano)
                novo_preco = float(novo_preco)
                carro = self.estoque[indice]
                carro.modelo = novo_modelo
                carro.ano = novo_ano
                carro.preco = novo_preco

                conn = self.conectar_banco2()
                cursor = conn.cursor()
                cursor.execute("UPDATE carros SET modelo = ?, ano = ?, preco = ? WHERE id = ?", 
                               (novo_modelo, novo_ano, novo_preco, carro.id))
                conn.commit()
                conn.close()

                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for carro in self.estoque:
            self.listbox.insert(tk.END, f"{carro.modelo} - {carro.ano} - R${carro.preco:.2f}")

    def limpar_campos(self):
        self.entry_modelo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def gerar_relatorio(self):
        if self.estoque:
            relatorio = "\n".join([f"Modelo: {carro.modelo} | Ano: {carro.ano} | Preço: R${carro.preco:.2f}" for carro in self.estoque])
            messagebox.showinfo("Relatório de Estoque", relatorio)
        else:
            messagebox.showinfo("Relatório de Estoque", "O estoque está vazio!")

class GerenciadorEstoque3:
    def __init__(self, master):
        self.master = master
        self.master.title("Estoque de Carros")

        self.estoque = []

        self.label = tk.Label(master, text="Estoque", fg='white', bg='black', width=89, height=4, font=("Lucida Console", 35))
        self.label.pack(side="top")

        self.listbox = tk.Listbox(master, width=100, height=29)
        self.listbox.place(x=150, y=310)

        self.label_modelo = tk.Label(master, text="Modelo do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_modelo.place(x=925, y=420)
        self.entry_modelo = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_modelo.place(x=1125, y=420)

        self.label_ano = tk.Label(master, text="Ano do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_ano.place(x=925, y=460)
        self.entry_ano = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_ano.place(x=1125, y=460)

        self.label_preco = tk.Label(master, text="Preço do Carro:", fg='white', bg='#3c3c3c', font=("Lucida Console", 14))
        self.label_preco.place(x=925, y=500)
        self.entry_preco = tk.Entry(master, width=30, font=("Lucida Console", 12))
        self.entry_preco.place(x=1125, y=500)

        self.btn_adicionar = tk.Button(master, text="Adicionar Carro", command=self.adicionar_carro, height=2, font=("Lucida Console", 10))
        self.btn_adicionar.place(x=915, y=580)

        self.btn_remover = tk.Button(master, text="Remover Carro", command=self.remover_carro, height=2, font=("Lucida Console", 10))
        self.btn_remover.place(x=1115, y=580)

        self.btn_atualizar = tk.Button(master, text="Atualizar Info.", command=self.atualizar_carro, height=2, font=("Lucida Console", 10))
        self.btn_atualizar.place(x=1315, y=580)

        self.btn_relatorio = tk.Button(master, text="Relatório de Estoque", command=self.gerar_relatorio, height=2, font=("Lucida Console", 10))
        self.btn_relatorio.place(x=1090, y=660)

        self.estoque = self.carregar_estoque()

        self.atualizar_lista()

        self.seta = tk.PhotoImage(file="seta.png")
        self.btn_voltar = tk.Button(master, image=self.seta, command=self.voltar, background="black", bd=0, relief="flat")
        self.btn_voltar.seta = self.seta
        self.btn_voltar.place(x=35, y=68)

    def voltar(self):
        self.master.destroy()

    def conectar_banco3(self):
        return sqlite3.connect('estoque_carros3.db')

    def carregar_estoque(self):
        conn = self.conectar_banco3()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()
        conn.close()

        estoque = []
        for carro in carros:
            estoque.append(Carro(carro[1], carro[2], carro[3], carro[0]))
        return estoque

    def adicionar_carro(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco = self.entry_preco.get()

        if modelo and ano and preco:
            try:
                ano = int(ano)
                preco = float(preco)
                carro = Carro(modelo, ano, preco)

                conn = self.conectar_banco3()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO carros (modelo, ano, preco) VALUES (?, ?, ?)", (modelo, ano, preco))
                conn.commit()
                conn.close()

                self.estoque.append(carro)
                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def remover_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            conn = self.conectar_banco3()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM carros WHERE id = ?", (carro.id,))
            conn.commit()
            conn.close()

            del self.estoque[indice]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para remover.")

    def atualizar_carro(self):
        try:
            indice = self.listbox.curselection()[0]
            carro = self.estoque[indice]

            self.entry_modelo.delete(0, tk.END)
            self.entry_modelo.insert(0, carro.modelo)

            self.entry_ano.delete(0, tk.END)
            self.entry_ano.insert(0, carro.ano)

            self.entry_preco.delete(0, tk.END)
            self.entry_preco.insert(0, carro.preco)

            self.btn_atualizar.config(command=lambda: self.confirmar_atualizacao(indice))
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um carro para atualizar.")

    def confirmar_atualizacao(self, indice):
        novo_modelo = self.entry_modelo.get()
        novo_ano = self.entry_ano.get()
        novo_preco = self.entry_preco.get()

        if novo_modelo and novo_ano and novo_preco:
            try:
                novo_ano = int(novo_ano)
                novo_preco = float(novo_preco)
                carro = self.estoque[indice]
                carro.modelo = novo_modelo
                carro.ano = novo_ano
                carro.preco = novo_preco

                conn = self.conectar_banco3()
                cursor = conn.cursor()
                cursor.execute("UPDATE carros SET modelo = ?, ano = ?, preco = ? WHERE id = ?", 
                               (novo_modelo, novo_ano, novo_preco, carro.id))
                conn.commit()
                conn.close()

                self.atualizar_lista()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning("Erro", "Ano e Preço devem ser números válidos.")
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for carro in self.estoque:
            self.listbox.insert(tk.END, f"{carro.modelo} - {carro.ano} - R${carro.preco:.2f}")

    def limpar_campos(self):
        self.entry_modelo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def gerar_relatorio(self):
        if self.estoque:
            relatorio = "\n".join([f"Modelo: {carro.modelo} | Ano: {carro.ano} | Preço: R${carro.preco:.2f}" for carro in self.estoque])
            messagebox.showinfo("Relatório de Estoque", relatorio)
        else:
            messagebox.showinfo("Relatório de Estoque", "O estoque está vazio!")

def abrir_nova_janela1():
    nova_janela1 = tk.Toplevel(janela)
    nova_janela1.title("Estoque de Carros")
    nova_janela1.configure(background="#3C3C3C")
    nova_janela1.attributes("-fullscreen", True)
    nova_janela1.bind("<Escape>", lambda event: nova_janela1.attributes("-fullscreen", False))
    app = GerenciadorEstoque1(nova_janela1)

def abrir_nova_janela2():
    nova_janela2 = tk.Toplevel(janela)
    nova_janela2.title("Estoque de Carros")
    nova_janela2.configure(background="#3C3C3C")
    nova_janela2.attributes("-fullscreen", True)
    nova_janela2.bind("<Escape>", lambda event: nova_janela2.attributes("-fullscreen", False))
    app = GerenciadorEstoque2(nova_janela2)

def abrir_nova_janela3():
    nova_janela3 = tk.Toplevel(janela)
    nova_janela3.title("Estoque de Carros")
    nova_janela3.configure(background="#3C3C3C")
    nova_janela3.attributes("-fullscreen", True)
    nova_janela3.bind("<Escape>", lambda event: nova_janela3.attributes("-fullscreen", False))
    app = GerenciadorEstoque3(nova_janela3)

janela = tk.Tk()
janela.title("Loja de Carros")
janela.attributes("-fullscreen", True)
janela.bind("<Escape>", lambda event: janela.attributes("-fullscreen", False))
janela.configure(background="#3C3C3C")

mensagem = tk.Label(text="Estoque de Carros", fg='white', bg='black', width=89, height=4, font=("Lucida Console", 35))
mensagem.pack(side="top")

imagem = tk.PhotoImage(file="toyota.png")
imagemtext = tk.Label(text="Toyota", font=("Verdana", 23), fg='white', bg="#3C3C3C")
imagemtext.place(x=245, y=300)
w = tk.Button(janela, image=imagem, command=abrir_nova_janela1)
w.imagem = imagem
w.place(x=120, y=350)

imagem2 = tk.PhotoImage(file="nissan.png")
imagemtext2 = tk.Label(text="Nissan", font=("Verdana", 23), fg='white', bg="#3C3C3C")
imagemtext2.place(x=750, y=300)
w2 = tk.Button(janela, image=imagem2, command=abrir_nova_janela2)
w2.imagem2 = imagem2
w2.place(x=625, y=350)

imagem3 = tk.PhotoImage(file="hyundai.png")
imagemtext3 = tk.Label(text="Hyundai", font=("Verdana", 23), fg='white', bg="#3C3C3C")
imagemtext3.place(x=1237, y=300)
w3 = tk.Button(janela, image=imagem3, command=abrir_nova_janela3)
w3.imagem3 = imagem3
w3.place(x=1120, y=350)

inicializar_banco1()
inicializar_banco2()
inicializar_banco3()

janela.mainloop()