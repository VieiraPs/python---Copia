from customtkinter import *
from PIL import Image

class Login():
    def __init__ (self):
        self.janelaPrincipal = CTk()
        self.janelaPrincipal.title('Login')
        self.janelaPrincipal.geometry("800x450")
        self.janelaPrincipal.configure(fg_color='#C5E7FF')
        self.janelaPrincipal.iconbitmap('images/icon_logo.ico') #ícone da barra de título
        self.janelaPrincipal._set_appearance_mode('light') #passando a janela para o modo claro
        self.janelaPrincipal.wm_state('zoomed') #maximiza a janela
        self.janelaPrincipal.update() #Atualiza tudo para garantir que o 'zoomed' irá funcionar



        #Criação de uma fonte especial que seja sublinhada (não é possível sublinhar no customtkinter)
        self.underline_font = CTkFont(family="Roboto", size=12, underline=True)



        #Inicializando a imagem da logo, que será usada mais para frente
        self.logo = Image.open("images/logo.png")
        self.image_ctk = None



        #Frame que contêm tudo dentro do "quadrado branco de login"
        self.frmLogin = CTkFrame(self.janelaPrincipal, fg_color="#FFFFFF", corner_radius=20)
        self.frmLogin.place(relx=0.50, rely=0.50, relwidth=0.30, relheight=0.70, anchor="center")



        #Frame que contêm as informações superiores, como logo, título e subtítulo
        self.frmTop = CTkFrame(self.frmLogin, fg_color="#FFFFFF")
        self.frmTop.place(relx=0.50, rely=0.15, relwidth=0.65, relheight=0.20, anchor="center")

        #Label que armazena nossa logo
        self.imgLogo = CTkLabel(self.frmTop, image=self.image_ctk, text="")
        self.imgLogo.place(relx=0.18, rely=0.5, relwidth=0.40, relheight=1, anchor="center")

        #Frame que contêm as escritas referente ao nome da empresa alinhadas verticalmente
        self.frmEscrita = CTkFrame(self.frmTop, fg_color="#FFFFFF")
        self.frmEscrita.place(relx=0.40, relwidth=0.60, relheight=1)
        
        #Primeira parte do nome que ficará mais acima
        self.lblAdolfo = CTkLabel(self.frmEscrita, text="ADOLFO", font=("Roboto", 32, "bold"), text_color="#042F48")
        self.lblAdolfo.grid(row=0, column=0, sticky="nw")

        #Segunda parte do nome, esse label ficará no meio
        self.lblLutz = CTkLabel(self.frmEscrita, text="LUTZ", font=("Roboto", 32, "bold"), text_color="#042F48")
        self.lblLutz.grid(row=1, column=0, sticky="w")

        #Terceira parte do nome, esse label ficará em baixo
        self.lblClinica = CTkLabel(self.frmEscrita, text="Clínica de Fisioterapia", font=("Roboto", 15), text_color="#042F48")
        self.lblClinica.grid(row=2, column=0, sticky="sw")

        #Ajusta as linhas do grid no frame "frmEscrita", frame que contêm o nome da empresa
        for i in range(3):
            self.frmEscrita.grid_rowconfigure(i,weight=1)

        

        #Frame que contêm nossos campos e botôes para login
        self.frmEntry = CTkFrame(self.frmLogin, fg_color="#FFFFFF")
        self.frmEntry.place(relx=0.5, rely=0.60, relwidth=0.65, relheight=0.6, anchor="center")

        #Label "Usuário"
        self.lblUsuarioLogin = CTkLabel(self.frmEntry, text="Usuário", text_color="#042F48", font=("Roboto", 15, "bold"))
        self.lblUsuarioLogin.place(relx=0, rely=0.05, anchor="w")
        #Caixa de Entrada/Entry "Usuário"
        self.cxaUsuarioLogin = CTkEntry(self.frmEntry, fg_color="#C5E7FF", text_color="#042F48", font=("Roboto", 17), border_width=0)
        self.cxaUsuarioLogin.place(rely=0.1, relwidth=1, relheight=0.15)

        #Label "Senha"
        self.lblSenhaLogin = CTkLabel(self.frmEntry, text="Senha", text_color="#042F48", font=("Roboto", 15, "bold"))
        self.lblSenhaLogin.place(relx=0, rely=0.4, anchor="w")
        #Caixa de Entrada/Entry "Senha"
        self.cxaSenhaLogin = CTkEntry(self.frmEntry, fg_color="#C5E7FF", text_color="#042F48", font=("Roboto", 17, "bold"), border_width=0, show="*")
        self.cxaSenhaLogin.place(relx=0, rely=0.45, relwidth=1, relheight=0.15)


        #Button que levá para a próxima tela, onde ajusta a nova senh (TELA INDISPONÍVEL)
        self.btnEsqueceuSenha = CTkButton(self.frmEntry, text="Esqueceu a senha?", text_color="#666666", fg_color="#FFFFFF",
                                          hover_color="#FFFFFF", font=self.underline_font, command=lambda:self.EsqueceuSenha())
        self.btnEsqueceuSenha.bind("<Enter>", self.on_enter) 
        self.btnEsqueceuSenha.bind("<Leave>", self.on_leave)
        self.btnEsqueceuSenha.place(relx=1, rely=0.65, relwidth=0.50, relheight=0.1, anchor="e")

        #Button "Entrar"
        self.btnEntrar = CTkButton(self.frmEntry, text="Entrar", text_color="#B3D1E7", fg_color="#1672A7",
                                   font=("Arial", 15, "bold"))
        self.btnEntrar.place(relx=0.5, rely=1, relwidth=0.35, relheight=0.12, anchor="s")
        
        #Toda vez que a janela for redimensionada chama as funções "AjustarFonte" e "AjustarImagem"
        self.janelaPrincipal.bind("<Configure>", lambda event: (self.AjustarFonte(event), self.AjustarImagem(event)))
        
        self.janelaPrincipal.mainloop()


    #Clicando em "Esqueceu a senha?" leva para outra tela
    def EsqueceuSenha(self):
        self.frmLogin.place_forget()
        self.frmEsqueceu = CTkFrame(self.janelaPrincipal, fg_color="#FFFFFF", corner_radius=20)
        self.frmEsqueceu.place(relx=0.50, rely=0.50, relwidth=0.30, relheight=0.70, anchor="center")

        self.btnVoltar = CTkButton(self.frmEsqueceu, text="Voltar", command= lambda:self.Login())
        self.btnVoltar.place(relx=0.5, rely=0.5, anchor="center")

    def Login(self):
        self.frmEsqueceu.place_forget()
        self.frmLogin.place(relx=0.50, rely=0.50, relwidth=0.30, relheight=0.70, anchor="center")


    #Deixa a imagem de logo responsiva
    def AjustarImagem(self, event):
        self.image_ctk = CTkImage(self.logo, size=(int(self.janelaPrincipal.winfo_width()*0.080), int(self.janelaPrincipal.winfo_width()*0.080)))
        self.imgLogo.configure(image=self.image_ctk)
        self.imgLogo.image = self.image_ctk


    #Deixa todas as escritas responsivas
    def AjustarFonte(self, event):
        escala = self.janelaPrincipal.winfo_width() / 1366
        self.lblAdolfo.configure(font=("Roboto", escala*32, "bold"))
        self.lblLutz.configure(font=("Roboto", escala*32, "bold"))
        self.lblClinica.configure(font=("Roboto", escala*15))
        self.lblUsuarioLogin.configure(font=("Roboto", escala*15, "bold"))
        self.cxaUsuarioLogin.configure(font=("Roboto", escala*17))
        self.lblSenhaLogin.configure(font=("Roboto", escala*15, "bold"))
        self.cxaSenhaLogin.configure(font=("Roboto", escala*17, "bold"))
        self.underline_font.configure(size=int(escala*12))
        self.btnEsqueceuSenha.configure(font=self.underline_font)
        self.btnEntrar.configure(font=("Arial", escala*15, "bold"))


    #Toda vez que o mouse para por cima do "Esqueceu a senha?" faz mudar de cor
    def on_enter(self, event):
        self.btnEsqueceuSenha.bind("<Enter>", self.btnEsqueceuSenha.configure(text_color="#042F48"))
    #Quando o mouse sai de cima do "Esqueceu a senha?" faz voltar a cor inicial
    def on_leave(self, event):
        self.btnEsqueceuSenha.bind("<Leave>", self.btnEsqueceuSenha.configure(text_color="#666666"))


Login()
