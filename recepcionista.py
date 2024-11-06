from customtkinter import *
from PIL import Image, ImageTk

class Recepcionista():
    def __init__ (self):
        self.janelaPrincipal = CTk()
        self.janelaPrincipal.title('Recepção')
        self.janelaPrincipal.geometry("800x450")
        self.janelaPrincipal.configure(fg_color='white')
        self.janelaPrincipal.iconbitmap('images/icon_logo.ico') #ícone da barra de título
        self.janelaPrincipal._set_appearance_mode('light') #passando a janela para o modo claro
        self.janelaPrincipal.wm_state('zoomed') #maximiza a janela
        self.janelaPrincipal.update()

        self.icon1 = ImageTk.PhotoImage(Image.open("images/icon1.png"))
        self.icon2 = ImageTk.PhotoImage(Image.open("images/icon2.png"))
        self.icon3 = ImageTk.PhotoImage(Image.open("images/icon3.png"))

        #barra de navegação
        self.frmNav = CTkFrame(self.janelaPrincipal, fg_color="#BFE9F4")
        self.frmNav.place(relwidth=0.17, relheight=1)

        #botão "Procedimentos" barra de navegação
        self.btnProcedimentos = CTkButton(self.frmNav, text="Procedimentos",
                                   fg_color="#9ECFDB", font=("Arial", 12, "bold"), text_color="#012C47", corner_radius=20)
        self.btnProcedimentos.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.04)

        #botão "Paciente Particular" barra de navegação
        self.btnPaciente = CTkButton(self.frmNav, text="Paciente Particular", fg_color="#BFE9F4",
                                     font=("Arial", 12, "bold"), text_color="#012C47")
        self.btnPaciente.place(relx=0.2, rely=0.204, relwidth=0.6, relheight=0.04)

        #botão "Outros" barra de navegação
        self.btnPaciente = CTkButton(self.frmNav, text="Outros", fg_color="#BFE9F4",
                                     font=("Arial", 12, "bold"), text_color="#012C47")
        self.btnPaciente.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.04)

        #hora
        self.lblHora = CTkLabel(self.janelaPrincipal, text="14:34", font=("Arial", 17), text_color="#666666")
        self.lblHora.place(relx=0.22, rely=0.05)

        #data
        self.lblData = CTkLabel(self.janelaPrincipal, text="Quarta-Feita, 22 de agosto de 2024", font=("Arial", 17),
                                text_color="#666666")
        self.lblData.place(relx=0.22, rely=0.08)

        #linha
        self.lblLinha = CTkLabel(self.janelaPrincipal, text="", fg_color="#999999")
        self.lblLinha.place(relx=0.22, rely=0.12, relwidth=0.7, relheight=0.0025)

        #Marcar Consultas e Procedimentos
        self.btnMarcar = CTkButton(self.janelaPrincipal, text="Marcar Consultas e Procedimentos", anchor="nw",
                                   fg_color="#4B98F1", font=("Roboto", 27, "bold"), text_color="#FFFFFF", corner_radius=20)
        self.btnMarcar.place(relx=0.22, rely= 0.15, relwidth=0.2266, relheight=0.30)
        self.lblBtn1 = CTkLabel(self.btnMarcar, text="Marcar Consultas e Procedimentos", font=("Roboto", 27, "bold"), text_color="#FFFFFF")
        self.lblBtn1.grid(row=0, column=0, sticky="nw")
        self.imgBtn1 = CTkLabel(self.btnMarcar, image=self.icon1)
        self.imgBtn1.grid(row=1, column=1, sticky="se")


        #Marcar Consultas e Procedimentos
        self.btnMarcarHoje = CTkButton(self.janelaPrincipal, text="Marcar consultas para hoje", anchor="nw",
                                   fg_color="#F14B4B", font=("Roboto", 27, "bold"), text_color="#FFFFFF", corner_radius=20)
        self.btnMarcarHoje.place(relx=0.4566, rely= 0.15, relwidth=0.2266, relheight=0.30)

        #Marcar Consultas e Procedimentos
        self.btnVer = CTkButton(self.janelaPrincipal, text="Ver Procedimentos Marcados", anchor="nw",
                                   fg_color="#F1914B", font=("Roboto", 27, "bold"), text_color="#FFFFFF", corner_radius=20)
        self.btnVer.place(relx=0.6932, rely= 0.15, relwidth=0.2266, relheight=0.30)

        #Label "Senhas"
        self.lblSenhas = CTkLabel(self.janelaPrincipal, text="Senhas", font=("Arial", 20, "bold"), text_color="#2A618D")
        self.lblSenhas.place(relx=0.22, rely=0.55)

        #Senhas
        self.btnSenha1 = CTkButton(self.janelaPrincipal, text="FM0001", fg_color="#FAFAFA",
                                   font=("Roboto", 30, "bold"), text_color="#2A618D", anchor="w")
        self.btnSenha1.place(relx=0.22, rely=0.60, relwidth=0.2266, relheight=0.15)

        self.btnSenha2 = CTkButton(self.janelaPrincipal, text="FM0001", fg_color="#FAFAFA",
                                   font=("Roboto", 30, "bold"), text_color="#2A618D", anchor="w")
        self.btnSenha2.place(relx=0.4566, rely=0.60, relwidth=0.2266, relheight=0.15)

        self.btnSenha3 = CTkButton(self.janelaPrincipal, text="FM0001", fg_color="#FAFAFA",
                                   font=("Roboto", 30, "bold"), text_color="#2A618D", anchor="w")
        self.btnSenha3.place(relx=0.22, rely=0.765, relwidth=0.2266, relheight=0.15)

        self.btnSenha4 = CTkButton(self.janelaPrincipal, text="FM0001", fg_color="#FAFAFA",
                                   font=("Roboto", 30, "bold"), text_color="#2A618D", anchor="w")
        self.btnSenha4.place(relx=0.4566, rely=0.765, relwidth=0.2266, relheight=0.15)

        #Botão "Consultas Atrasadas"
        self.btnAtrasadas = CTkButton(self.janelaPrincipal, text="Consultas Atrasadas", text_color="#FFFFFF",
                                      font=("Roboto", 27, "bold"), fg_color="#DB3500", corner_radius=20)
        self.btnAtrasadas.place(relx=0.6932, rely=0.6, relwidth=0.2266, relheight=0.31)
        




        self.janelaPrincipal.mainloop()





Recepcionista()


