# importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools
import DataBaser
import time


# Criando as Funções

def registro():
    
    jan2 = Tk()

    LeftFrame2 = Frame(jan2, width=500, height=400, bg="SteelBlue3", relief="raise")
    LeftFrame2.pack(side=LEFT)

    RightFrame2 = Frame(jan2, width=295, height=400, bg="MIDNIGHTBLUE", relief="raise")
    RightFrame2.pack(side=RIGHT)


    # Configuração da janela principal
    jan2.title('Registro de Usuarios')
    jan2.configure(background='#D3D3D3')
    jan2.geometry('800x400')
    jan2.resizable(width=False, height=False)
    jan2.iconbitmap(default="logos/LogoIcon.ico")
    
    # Inserindo Widgets de Cadastro
    NomeLabel = Label(LeftFrame2, text="Nome: ", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
    NomeLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(LeftFrame2, width=30)
    NameEntry.place(x=100, y=18)

    EmailLabel = Label(LeftFrame2, text="Email: ", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(LeftFrame2, width=32)
    EmailEntry.place(x=90, y=63)

    UserLabel = Label(LeftFrame2, text="Username:", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
    UserLabel.place(x=5, y=95)

    UserEntry = ttk.Entry(LeftFrame2, width=30)
    UserEntry.place(x=150, y=108)

    PassLabel = Label(LeftFrame2, text="Password:", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
    PassLabel.place(x=5, y=140)

    PassEntry = ttk.Entry(LeftFrame2, width=30, show="●")
    PassEntry.place(x=150, y=153)

    PassLabel_confirmar = Label(LeftFrame2, text="Confirm password:", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
    PassLabel_confirmar.place(x=5, y=185)

    PassEntry_confirmar = ttk.Entry(LeftFrame2, width=30, show="●")
    PassEntry_confirmar.place(x=260, y=198)

    def ComfRegister():
        # logica para senhas
        Pass1 = PassEntry.get()
        Pass2 = PassEntry_confirmar.get()

        if Pass1 == Pass2:
            Pass_True = Pass1
            verdade = True
        else:
            verdade = False

        time.sleep(5)

        if verdade == False:
            lambda: close_window(jan2)
        elif verdade == True:
            pass
        # logica para senhas
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if Name == "" or Email == "" or User == "" or Pass == "":
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")

        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))

            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Register Sucessfull")

            print(Name)
            print(Email)
            print(User)
            print(Pass)

        # funtion para confirmar Registro

    registro = ComfRegister

    ComfRegisterButton = ttk.Button(RightFrame2, text="Registrar", width=40, command= registro)# confirmar Registro
    ComfRegisterButton.place(x=5, y=5)

    VoltarButton = ttk.Button(RightFrame2, text="Voltar", width=40, command= lambda: close_window(jan2))
    VoltarButton.place(x=5, y=50)

    def close_window (jan2): 
        jan2.destroy()
        # funtion para sair da janela de registro / lambda

def Login():
    UserLogin = UserEntry.get()
    PassLogin = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE User = ? AND Password = ?
    """, (UserLogin, PassLogin))
    VerifyLogin = DataBaser.cursor.fetchone()

    try:
        if UserLogin in VerifyLogin and PassEntry in VerifyLogin:
            messagebox.showinfo(title="Aviso de Login", message="Acesso confirmado, Hello World !")
            Sistema_jan()
        
        else:
            pass
    except:
        messagebox.showinfo(title="Aviso de Login", message="Acesso Negado !")

    print("Hello, World")


def Sistema_jan():
    jan2 = Tk()

    LeftFrame3 = Frame(jan3, width=500, height=400, bg="SteelBlue3", relief="raise")
    LeftFrame3.pack(side=LEFT)

    RightFrame3 = Frame(jan3, width=295, height=400, bg="MIDNIGHTBLUE", relief="raise")
    RightFrame3.pack(side=RIGHT)


     # Configuração da janela pricipal de usuarios
    jan2.title('DP Systems')
    jan2.configure(background='#D3D3D3')
    jan2.geometry('800x400')
    jan2.resizable(width=False, height=False)
    jan2.iconbitmap(default="logos/LogoIcon.ico")



# https://www.vivaolinux.com.br/topico/Python/Desenvolvendo-varias-telas-Pycharm-Tkinter
# https://pt.stackoverflow.com/questions/319195/transi%C3%A7%C3%A3o-de-telas-tkinter