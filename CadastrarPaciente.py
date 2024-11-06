from customtkinter import *
from PIL import Image

class CadastrarPaciente():
    def __init__ (self):
        self.janelaPrincipal = CTk()
        self.janelaPrincipal.title('Cadastro de Pacientes')
        self.janelaPrincipal.geometry("800x450")
        self.janelaPrincipal.configure(fg_color='#FFFFFF')
        self.janelaPrincipal.iconbitmap('images/icon_logo.ico') # ícone da barra de título
        self.janelaPrincipal._set_appearance_mode('light') # passando a janela para o modo claro
        self.janelaPrincipal.wm_state('zoomed') # maximiza a janela
        self.janelaPrincipal.update() # Atualiza tudo para garantir que o 'zoomed' irá funcionar



        # Inicializando a imagem da logo, que será usada mais para frente
        self.logo = Image.open("images/logo.png")
        self.logo_ctk = None
        self.seta1 = Image.open("images/seta-direita.png")
        self.seta1_ctk = None
        self.seta2 = Image.open("images/seta-direita.png")
        self.seta2_ctk = None



        # Frame que contêm nossa barra de navegação
        self.frmLateral = CTkFrame(self.janelaPrincipal, fg_color="#C5E7FF", corner_radius=0)
        self.frmLateral.place(relx=0, rely=0, relwidth=0.18, relheight=1)



        # Frame que contêm as informações superiores, como logo, título e subtítulo
        self.frmLogo = CTkFrame(self.frmLateral, fg_color="#C5E7FF")
        self.frmLogo.place(relx=0.50, rely=0.07, relwidth=0.75, relheight=0.075, anchor="center")

        # Label que armazena nossa logo
        self.imgLogo = CTkLabel(self.frmLogo, image=self.logo_ctk, text="")
        self.imgLogo.place(relx=0.18, rely=0.5, relwidth=0.35, relheight=1, anchor="center")



        # Frame que contêm as escritas referente ao nome da empresa alinhadas verticalmente
        self.frmEscrita = CTkFrame(self.frmLogo, fg_color="#C5E7FF")
        self.frmEscrita.place(relx=0.35, relwidth=0.65, relheight=1)
        

        # Primeira parte do nome que ficará mais acima
        self.lblAdolfo = CTkLabel(self.frmEscrita, text="ADOLFO", font=("Roboto", 15, "bold"), text_color="#042F48")
        self.lblAdolfo.grid(row=0, column=0, sticky="nw")

        # Segunda parte do nome, esse label ficará no meio
        self.lblLutz = CTkLabel(self.frmEscrita, text="LUTZ", font=("Roboto", 15, "bold"), text_color="#042F48")
        self.lblLutz.grid(row=1, column=0, sticky="w")

        # Terceira parte do nome, esse label ficará em baixo
        self.lblClinica = CTkLabel(self.frmEscrita, text="Clínica de Fisioterapia", font=("Roboto", 9), text_color="#042F48")
        self.lblClinica.grid(row=2, column=0, sticky="sw")

        # Ajusta as linhas do grid no frame "frmEscrita", frame que contêm o nome da empresa
        for i in range(3):
            self.frmEscrita.grid_rowconfigure(i,weight=1)

        #Tópico "Procedimento" da barra lateral
        self.btnProcedimento = CTkButton(self.frmLateral, text="Procedimento", text_color="#042F48", fg_color="#C5E7FF",
                                         font=("Roboto", 13, "bold"), corner_radius=25, hover_color="skyblue")
        self.btnProcedimento.place(relx=0.5, rely=0.225, relwidth=0.7, anchor="center")

        #Tópico "Pacientes" da barra lateral
        self.btnPacientes = CTkButton(self.frmLateral, text="Pacientes", text_color="#042F48", fg_color="skyblue",
                                         font=("Roboto", 13, "bold"), corner_radius=25, hover_color="#C5E7FF")
        self.btnPacientes.place(relx=0.5, rely=0.3, relwidth=0.7, anchor="center")

        #Botão "Sair" da barra lateral
        self.btnSair = CTkButton(self.frmLateral, text="Sair", text_color="#042F48", fg_color="#C5E7FF",
                                 font=("Roboto", 13, "bold"), corner_radius=25, hover_color="skyblue", command= lambda: self.DestruirTela())
        self.btnSair.place(relx=0.1, rely=0.975, relwidth=0.3, anchor="sw")


        
        # Frame que agrupapa toda a tela fora da barra lateral
        self.frmCadastrar = CTkFrame(self.janelaPrincipal, fg_color="#FFFFFF", corner_radius=0)
        self.frmCadastrar.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)


        # Label com título da página "CADASTRAR PACIENTE"
        self.lblCadastrar = CTkLabel(self.frmCadastrar, text="CADASTRAR PACIENTE", font=("Roboto", 25,"bold"), text_color="#2A618D")
        self.lblCadastrar.place(relx=0.5, rely=0.08, anchor="center")

        # Label que formará a linha cinza embaixo do título
        self.lblLinha = CTkLabel(self.frmCadastrar, text="", fg_color="#DDDDDD")
        self.lblLinha.place(relx=0.5, rely=0.16, relwidth=0.90, relheight=0.002, anchor="center")


        # Label para o campo "CPF do paciente"
        self.lblCPF = CTkLabel(self.frmCadastrar, text="CPF do paciente", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblCPF.place(relx=0.1, rely=0.2)
        # Caixa de Entrada/Entry para "CPF do paciente"
        self.cxaCPF = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaCPF.place(relx=0.1, rely=0.245, relwidth=0.335, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaCPF.bind("<KeyRelease>", lambda event: self.AplicarMascaraCPF(event))

        # Label para o campo "RG do paciente"
        self.lblRG = CTkLabel(self.frmCadastrar, text="RG do paciente", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblRG.place(relx=0.1, rely=0.335)
        # Caixa de Entrada/Entry para "RG do paciente"
        self.cxaRG = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaRG.place(relx=0.1, rely=0.38, relwidth=0.335, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaRG.bind("<KeyRelease>", lambda event: self.AplicarMascaraRG(event))

        # Label para o campo "CEP"
        self.lblCEP = CTkLabel(self.frmCadastrar, text="CEP", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblCEP.place(relx=0.1, rely=0.47)
        # Caixa de Entrada/Entry para "CEP"
        self.cxaCEP = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaCEP.place(relx=0.1, rely=0.515, relwidth=0.335, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaCEP.bind("<KeyRelease>", lambda event: self.AplicarMascaraCEP(event))

        # Label para o campo "Nome"
        self.lblNome = CTkLabel(self.frmCadastrar, text="Nome", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblNome.place(relx=0.45, rely=0.2)
        # Caixa de Entrada/Entry para "Nome"
        self.cxaNome = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaNome.place(relx=0.45, rely=0.245, relwidth=0.465, relheight=0.07)

        # Label para o campo "Data de Nascimento"
        self.lblData = CTkLabel(self.frmCadastrar, text="Data de Nascimento", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblData.place(relx=0.45, rely=0.335)
        # Caixa de Entrada/Entry para "Data de Nascimento"
        self.cxaData = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaData.place(relx=0.45, rely=0.38, relwidth=0.29, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaData.bind("<KeyRelease>", lambda event: self.AplicarMascaraData(event))

        # Label para o campo "Sexo"
        self.lblSexo = CTkLabel(self.frmCadastrar, text="Sexo", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblSexo.place(relx=0.755, rely=0.335)
        #Cria uma variável vazia para iniciar a caixa de seleção
        self.varSexo = StringVar(value="")
        # Caixa de Seleção/Option Menu para "Sexo"
        self.cxaSexo = CTkOptionMenu(self.frmCadastrar, variable=self.varSexo, values=["Feminino", "Masculino", "Outros"],
                                     font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                                     corner_radius=15, button_color="#C5E7FF", button_hover_color="#C5E7FF",
                                     dropdown_fg_color="#C5E7FF", dropdown_hover_color="skyblue", dropdown_text_color="#042F48",)
        self.cxaSexo.place(relx=0.755, rely=0.38, relwidth=0.16, relheight=0.07)

        # Label para o campo "Endereço"
        self.lblEndereco = CTkLabel(self.frmCadastrar, text="Endereço", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblEndereco.place(relx=0.45, rely=0.47)
        # Caixa de Entrada/Entry para "Endereço"
        self.cxaEndereco = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaEndereco.place(relx=0.45, rely=0.515, relwidth=0.465, relheight=0.07)

        # Label para o campo "Bairro"
        self.lblBairro = CTkLabel(self.frmCadastrar, text="Bairro", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblBairro.place(relx=0.1, rely=0.605)
        # Caixa de Entrada/Entry para "Data de Nascimento"
        self.cxaBairro = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaBairro.place(relx=0.1, rely=0.65, relwidth=0.29, relheight=0.07)

        # Label para o campo "Cidade"
        self.lblCidade = CTkLabel(self.frmCadastrar, text="Cidade", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblCidade.place(relx=0.405, rely=0.605)
        # Caixa de Entrada/Entry para "Cidade"
        self.cxaCidade = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaCidade.place(relx=0.405, rely=0.65, relwidth=0.335, relheight=0.07)

        # Label para o campo "UF"
        self.lblUF = CTkLabel(self.frmCadastrar, text="UF", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblUF.place(relx=0.755, rely=0.605)
        #Valores possíveis de UF
        self.listaUF = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", 
                        "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", 
                        "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        # Caixa de Entrada/Entry para "UF"
        self.cxaUF = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaUF.place(relx=0.755, rely=0.65, relwidth=0.16, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaUF.bind("<KeyRelease>", lambda event: self.AplicarMascaraUF(event))

        # Label para o campo "Celular"
        self.lblCelular = CTkLabel(self.frmCadastrar, text="Celular", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblCelular.place(relx=0.1, rely=0.74)
        # Caixa de Entrada/Entry para "Celular"
        self.cxaCelular = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaCelular.place(relx=0.1, rely=0.785, relwidth=0.29, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaCelular.bind("<KeyRelease>", lambda event: self.AplicarMascaraCelular(event))

        # Label para o campo "Telefone Fixo"
        self.lblFixo = CTkLabel(self.frmCadastrar, text="Telefone Fixo", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblFixo.place(relx=0.405, rely=0.74)
        # Caixa de Entrada/Entry para "Telefone Fixo"
        self.cxaFixo = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaFixo.place(relx=0.405, rely=0.785, relwidth=0.29, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaFixo.bind("<KeyRelease>", lambda event: self.AplicarMascaraFixo(event))


        self.btnConcluido = CTkButton(self.frmCadastrar, text="Concluído", text_color="#FFFFFF", fg_color="#659BDB", 
                                      font=("Roboto", 22, "bold"), corner_radius=15, anchor="w", hover_color="#4379B9")
        self.btnConcluido.place(relx=0.75, rely=0.875, relwidth=0.175, relheight=0.075)
        self.btnConcluido.bind("<Enter>", self.on_enterBtn) 
        self.btnConcluido.bind("<Leave>", self.on_leaveBtn)

        self.imgSeta1 = CTkLabel(self.btnConcluido, image=self.seta1_ctk, text="")
        self.imgSeta1.place(relx=0.8, rely=0.5, anchor="e")
        self.imgSeta1.bind("<Enter>", self.on_enterBtn) 
        self.imgSeta1.bind("<Leave>", self.on_leaveBtn)

        self.imgSeta2 = CTkLabel(self.btnConcluido, image=self.seta2_ctk, text="")
        self.imgSeta2.place(relx=0.875, rely=0.5, anchor="e")
        self.imgSeta2.bind("<Enter>", self.on_enterBtn) 
        self.imgSeta2.bind("<Leave>", self.on_leaveBtn)


        
        





        # Toda vez que a janela for redimensionada chama as funções "AjustarFonte" e "AjustarImagem"
        self.janelaPrincipal.bind("<Configure>", lambda event: (self.AjustarFonte(event), self.AjustarImagem(event)))

        self.janelaPrincipal.mainloop()

    # Deixa a imagem de logo responsiva
    def AjustarImagem(self, event):
        self.logo_ctk = CTkImage(self.logo, size=(int(self.janelaPrincipal.winfo_width()*0.044), int(self.janelaPrincipal.winfo_width()*0.044)))
        self.imgLogo.configure(image=self.logo_ctk)
        self.imgLogo.image = self.logo_ctk

        self.seta1_ctk = CTkImage(self.seta1, size=(int(self.janelaPrincipal.winfo_width()*0.012), int(self.janelaPrincipal.winfo_width()*0.012)))
        self.imgSeta1.configure(image=self.seta1_ctk)
        self.imgSeta1.image = self.seta1_ctk
        
        self.seta2_ctk = CTkImage(self.seta2, size=(int(self.janelaPrincipal.winfo_width()*0.012), int(self.janelaPrincipal.winfo_width()*0.012)))
        self.imgSeta2.configure(image=self.seta2_ctk)
        self.imgSeta2.image = self.seta2_ctk

    # Deixa todas as escritas responsivas
    def AjustarFonte(self, event):
        escala = self.janelaPrincipal.winfo_width() / 1366
        self.lblAdolfo.configure(font=("Roboto", escala*15, "bold"))
        self.lblLutz.configure(font=("Roboto", escala*15, "bold"))
        self.lblClinica.configure(font=("Roboto", escala*9))

        self.btnProcedimento.configure(font=("Roboto", escala*13, "bold"))
        self.btnPacientes.configure(font=("Roboto", escala*13, "bold"))
        self.btnSair.configure(font=("Roboto", escala*13, "bold"))

        self.lblCadastrar.configure(font=("Roboto", escala*25, "bold"))

        self.lblCPF.configure(font=("Roboto", escala*20, "bold"))
        self.cxaCPF.configure(font=("Roboto", escala*15, "bold"))
        self.lblNome.configure(font=("Roboto", escala*20, "bold"))
        self.cxaNome.configure(font=("Roboto", escala*15, "bold"))
        self.lblRG.configure(font=("Roboto", escala*20, "bold"))
        self.cxaRG.configure(font=("Roboto", escala*15, "bold"))
        self.lblData.configure(font=("Roboto", escala*20, "bold"))
        self.cxaData.configure(font=("Roboto", escala*15, "bold"))
        self.lblSexo.configure(font=("Roboto", escala*20, "bold"))
        self.cxaSexo.configure(font=("Roboto", escala*15, "bold"))
        self.lblCEP.configure(font=("Roboto", escala*20, "bold"))
        self.cxaCEP.configure(font=("Roboto", escala*15, "bold"))
        self.lblEndereco.configure(font=("Roboto", escala*20, "bold"))
        self.cxaEndereco.configure(font=("Roboto", escala*15, "bold"))
        self.lblBairro.configure(font=("Roboto", escala*20, "bold"))
        self.cxaBairro.configure(font=("Roboto", escala*15, "bold"))
        self.lblCidade.configure(font=("Roboto", escala*20, "bold"))
        self.cxaCidade.configure(font=("Roboto", escala*15, "bold"))
        self.lblUF.configure(font=("Roboto", escala*20, "bold"))
        self.cxaUF.configure(font=("Roboto", escala*15, "bold"))
        self.lblCelular.configure(font=("Roboto", escala*20, "bold"))
        self.cxaCelular.configure(font=("Roboto", escala*15, "bold"))
        self.lblFixo.configure(font=("Roboto", escala*20, "bold"))
        self.cxaFixo.configure(font=("Roboto", escala*15, "bold"))

        self.btnConcluido.configure(font=("Roboto", escala*22, "bold"))



    # Modifica o campo e adiciona a máscara CPF
    def AplicarMascaraCPF(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaCPF.get()))
        
        if len(digitos) <= 3:
            cpf = digitos
        elif len(digitos) <= 6:
            cpf = f"{digitos[:3]}.{digitos[3:]}"
        elif len(digitos) <= 9:
            cpf = f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:]}"
        else:
            cpf = f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:11]}"
        
        self.cxaCPF.delete(0, "end")
        self.cxaCPF.insert(0, cpf)
        
    # Modifica o campo e adiciona a máscara RG
    def AplicarMascaraRG(self, event):
        digitos = ''.join(filter(str.isalnum, self.cxaRG.get()))

        if len(digitos) <= 2:
            rg = digitos
        elif len(digitos) <= 5:
            rg = f"{digitos[:2]}.{digitos[2:]}"
        elif len(digitos) <= 8:
            rg = f"{digitos[:2]}.{digitos[2:5]}.{digitos[5:]}"
        else:
            rg = f"{digitos[:2]}.{digitos[2:5]}.{digitos[5:8]}-{digitos[8:9]}"
        
        self.cxaRG.delete(0, "end")
        self.cxaRG.insert(0, rg)
    
    # Modifica o campo e adiciona a máscara CEP
    def AplicarMascaraCEP(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaCEP.get()))
        
        if len(digitos) <= 5:
            cep = digitos
        else:
            cep = f"{digitos[:5]}-{digitos[5:8]}"
        
        self.cxaCEP.delete(0, "end")
        self.cxaCEP.insert(0, cep)

    # Modifica o campo e adiciona a máscara Data
    def AplicarMascaraData(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaData.get()))
        
        if len(digitos) <= 2:
            data = digitos
        elif len(digitos) <= 4:
            data = f"{digitos[:2]}/{digitos[2:4]}"
        else:
            data = f"{digitos[:2]}/{digitos[2:4]}/{digitos[4:8]}"
        
        self.cxaData.delete(0, "end")
        self.cxaData.insert(0, data)

    # Modifica o campo e adiciona a máscara UF
    def AplicarMascaraUF(self, event):
        digitos = ''.join(filter(str.isalpha, self.cxaUF.get())).upper()
        
        if len(digitos) <= 1:
            uf = digitos
        elif len(digitos) <=2:
            if digitos in self.listaUF:
                uf = digitos
            else:
                uf = ""
        else:
            uf = digitos[:2]

        self.cxaUF.delete(0, "end")
        self.cxaUF.insert(0, uf)

    # Modifica o campo e adiciona a máscara Celular
    def AplicarMascaraCelular(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaCelular.get()))
        
        if len(digitos) <= 2:
            celular = f"({digitos})"
        elif len(digitos) <= 7:
            celular = f"({digitos[:2]}) {digitos[2:]}"
        else:
            celular = f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:11]}"
        
        self.cxaCelular.delete(0, "end")
        self.cxaCelular.insert(0, celular)

    # Modifica o campo e adiciona a máscara Telefone
    def AplicarMascaraFixo(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaFixo.get()))
        
        if len(digitos) <= 2:
            fixo = f"({digitos})"
        elif len(digitos) <= 6:
            fixo = f"({digitos[:2]}) {digitos[2:]}"
        else:
            fixo = f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:10]}"
        
        self.cxaFixo.delete(0, "end")
        self.cxaFixo.insert(0, fixo)

    
    #Toda vez que o mouse para por cima do "Concluído" faz mudar de cor
    def on_enterBtn(self, event):
        self.btnConcluido.bind("<Enter>", self.btnConcluido.configure(fg_color="#4379B9"))
        self.imgSeta1.bind("<Enter>", self.imgSeta1.configure(fg_color="#4379B9"))
        self.imgSeta2.bind("<Enter>", self.imgSeta2.configure(fg_color="#4379B9"))
    
    #Quando o mouse sai de cima do "Concluído" faz voltar a cor inicial
    def on_leaveBtn(self, event):
        self.btnConcluido.bind("<Leave>", self.btnConcluido.configure(fg_color="#659BDB"))
        self.imgSeta1.bind("<Leave>", self.imgSeta1.configure(fg_color="#659BDB"))
        self.imgSeta2.bind("<Leave>", self.imgSeta2.configure(fg_color="#659BDB"))

    def DestruirTela(self):
        self.janelaPrincipal.destroy()
        

CadastrarPaciente()