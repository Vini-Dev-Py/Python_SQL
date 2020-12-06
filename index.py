# importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools
from function import registro, Sistema_jan
import DataBaser

# Criar Nossa janela

jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="#D3D3D3")
jan.resizable(width=False, height=False)
# jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="logos/LogoIcon.ico")

# Carregando imagens
logo = PhotoImage(file="Logos/logo.png")

# Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="SteelBlue3", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
UserLabel.place(x=5, y=10)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=25)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="SteelBlue3", fg="Black")
PassLabel.place(x=5, y=75)

PassEntry = ttk.Entry(RightFrame, width=30, show="●")
PassEntry.place(x=150, y=88)

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

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width= 30, command=Login)
LoginButton.place(x=150, y=250)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=registro)
RegisterButton.place(x=5, y=250)

jan.mainloop()
