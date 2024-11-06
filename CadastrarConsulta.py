from customtkinter import *
from PIL import Image

#iniciar class
class CadastrarConsulta():
    def __init__ (self):
        self.janelaPrincipal = CTk()
        self.janelaPrincipal.title('Cadastro de Consultas')
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
        self.btnProcedimento = CTkButton(self.frmLateral, text="Procedimento", text_color="#042F48", fg_color="skyblue",
                                         font=("Roboto", 13, "bold"), corner_radius=25, hover_color="#C5E7FF")
        self.btnProcedimento.place(relx=0.5, rely=0.225, relwidth=0.7, anchor="center")

        #Tópico "Pacientes" da barra lateral
        self.btnPacientes = CTkButton(self.frmLateral, text="Pacientes", text_color="#042F48", fg_color="#C5E7FF",
                                         font=("Roboto", 13, "bold"), corner_radius=25, hover_color="skyblue")
        self.btnPacientes.place(relx=0.5, rely=0.3, relwidth=0.7, anchor="center")

        #Botão "Sair" da barra lateral
        self.btnSair = CTkButton(self.frmLateral, text="Sair", text_color="#042F48", fg_color="#C5E7FF",
                                 font=("Roboto", 13, "bold"), corner_radius=25, hover_color="skyblue", command= lambda: self.DestruirTela())
        self.btnSair.place(relx=0.1, rely=0.975, relwidth=0.3, anchor="sw")


        
        # Frame que agrupapa toda a tela fora da barra lateral
        self.frmCadastrar = CTkFrame(self.janelaPrincipal, fg_color="#FFFFFF", corner_radius=0)
        self.frmCadastrar.place(relx=0.18, rely=0, relwidth=0.82, relheight=1)


        # Label com título da página "CADASTRAR PACIENTE"
        self.lblCadastrar = CTkLabel(self.frmCadastrar, text="MARCAR PROCEDIMENTO", font=("Roboto", 25,"bold"), text_color="#2A618D")
        self.lblCadastrar.place(relx=0.5, rely=0.08, anchor="center")

        # Label que formará a linha cinza embaixo do título
        self.lblLinha = CTkLabel(self.frmCadastrar, text="", fg_color="#DDDDDD")
        self.lblLinha.place(relx=0.5, rely=0.16, relwidth=0.90, relheight=0.002, anchor="center")


        # Label para o campo "Paciente"
        self.lblPaciente = CTkLabel(self.frmCadastrar, text="Paciente", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblPaciente.place(relx=0.1, rely=0.2)
        # Caixa de Entrada/Entry para "Paciente"
        self.cxaPaciente = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaPaciente.place(relx=0.1, rely=0.245, relwidth=0.3925, relheight=0.07)

        # Label para o campo "Procedimento"
        self.lblProcedimento = CTkLabel(self.frmCadastrar, text="Procedimento", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblProcedimento.place(relx=0.5075, rely=0.2)
        #Cria uma variável vazia para iniciar a caixa de seleção
        self.varProcedimento = StringVar(value="")
        # Caixa de Seleção/Option Menu para "Procedimento"
        self.cxaProcedimento = CTkOptionMenu(self.frmCadastrar, variable=self.varProcedimento,font=("Roboto", 15, "bold"),
                                             values=["Sessão de Avaliação Inicial", "Sessão de Fisioterapia", "Terapia Manual",
                                             "Ultrassom Terapêutico", "Eletroterapia", "Terapia com Laser", "Pacote de Sesões",
                                             "Reabilitação Pós-Cirúrgica", "Aulas de Pilates ou Exercícios em Grupo"],
                                             text_color="#042F48", fg_color="#C5E7FF", corner_radius=15, button_color="#C5E7FF",
                                             button_hover_color="#C5E7FF", dropdown_fg_color="#C5E7FF",
                                             dropdown_hover_color="skyblue", dropdown_text_color="#042F48",)
        self.cxaProcedimento.place(relx=0.5075, rely=0.245, relwidth=0.3925, relheight=0.07)

        # Label para o campo "Fisioterapeuta"
        self.lblFisioterapeuta = CTkLabel(self.frmCadastrar, text="Fisioterapeuta", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblFisioterapeuta.place(relx=0.1, rely=0.335)
        # Caixa de Entrada/Entry para "Fisioterapeuta"
        self.cxaFisioterapeuta = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaFisioterapeuta.place(relx=0.1, rely=0.38, relwidth=0.3925, relheight=0.07)
    
        # Label para o campo "Data"
        self.lblData = CTkLabel(self.frmCadastrar, text="Data", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblData.place(relx=0.5075, rely=0.335)
        # Caixa de Entrada/Entry para "Data"
        self.cxaData = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaData.place(relx=0.5075, rely=0.38, relwidth=0.3925, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaData.bind("<KeyRelease>", lambda event: self.AplicarMascaraData(event))

        # Label para o campo "Horário"
        self.lblHorario = CTkLabel(self.frmCadastrar, text="Horário", font=("Roboto", 20,"bold"), text_color="#2A618D")
        self.lblHorario.place(relx=0.1, rely=0.47)
        # Caixa de Entrada/Entry para "Horario"
        self.cxaHorario = CTkEntry(self.frmCadastrar, font=("Roboto", 15, "bold"), text_color="#042F48", fg_color="#C5E7FF",
                               corner_radius=15, border_width=0)
        self.cxaHorario.place(relx=0.1, rely=0.515, relwidth=0.27, relheight=0.07)
        # Chama a função para adicionar máscara
        self.cxaHorario.bind("<KeyRelease>", lambda event: self.AplicarMascaraHorario(event))



        #Botão "Concluído" para marcar o procedimento
        self.btnConcluido = CTkButton(self.frmCadastrar, text="Concluído", text_color="#FFFFFF", fg_color="#659BDB", 
                                      font=("Roboto", 22, "bold"), corner_radius=15, anchor="w", hover_color="#4379B9",
                                      command= lambda: self.TelaMarcado())
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


    #Criar frame para exibir finalização do agendamento
    def TelaMarcado(self):
        pass

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

    def AjustarFonte(self, event):
        escala = self.janelaPrincipal.winfo_width() / 1366
        self.lblAdolfo.configure(font=("Roboto", escala*15, "bold"))
        self.lblLutz.configure(font=("Roboto", escala*15, "bold"))
        self.lblClinica.configure(font=("Roboto", escala*9))

        self.btnProcedimento.configure(font=("Roboto", escala*13, "bold"))
        self.btnPacientes.configure(font=("Roboto", escala*13, "bold"))
        self.btnSair.configure(font=("Roboto", escala*13, "bold"))

        self.lblCadastrar.configure(font=("Roboto", escala*25, "bold"))

        self.lblPaciente.configure(font=("Roboto", escala*20, "bold"))
        self.cxaPaciente.configure(font=("Roboto", escala*15, "bold"))
        self.lblProcedimento.configure(font=("Roboto", escala*20, "bold"))
        self.cxaProcedimento.configure(font=("Roboto", escala*15, "bold"))
        self.lblFisioterapeuta.configure(font=("Roboto", escala*20, "bold"))
        self.cxaFisioterapeuta.configure(font=("Roboto", escala*15, "bold"))
        self.lblData.configure(font=("Roboto", escala*20, "bold"))
        self.cxaData.configure(font=("Roboto", escala*15, "bold"))
        self.lblHorario.configure(font=("Roboto", escala*20, "bold"))
        self.cxaHorario.configure(font=("Roboto", escala*15, "bold"))

        self.btnConcluido.configure(font=("Roboto", escala*22, "bold"))

    

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

    # Modifica o campo e adiciona a máscara Data
    def AplicarMascaraHorario(self, event):
        digitos = ''.join(filter(str.isdigit, self.cxaHorario.get()))
        
        if len(digitos) <= 2:
            if int(digitos) <= 24:
                horario = digitos
            else:
                horario = ""
        else:
            if int(digitos[2:4]) <= 60:
                horario = f"{digitos[:2]}:{digitos[2:4]}"
            else:
                horario = f"{digitos[:2]}:"
            
        
        self.cxaHorario.delete(0, "end")
        self.cxaHorario.insert(0, horario)



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
    
CadastrarConsulta()