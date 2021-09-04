from .agenda import Agenda
from .contato import Contato
from .tarefa import Tarefa

class Main:
    def __init__(self):
        self.em_execucao = True
        self.agenda = Agenda()
        self.agenda.set_proprietario('Edu')
        self.agenda.set_ano(2077)

    def mostrar_menu(self):
        print('')
        print("e" * 32)
        print("e" * 16 + " A G E N D A " + "e" * 13)
        print("e" * 32)
        print("Digite um dos número como escolha: ")
        print('1. Cadastrar Contato')
        print('2. Listar   Contatos')
        print('3. Excuir    Contato')
        print('4. Cadastrar  Tarefa')
        print('5. Listar    Tarefas')
        print('6. Excluir    Tarefa')
        print('7. Concluir  Tarefas')
        print('8. Definir Tarefas como "Pendentes"')
        print('0. Sair do Programa')

    def ler_opcao_menu(self):
        opcao = input(" x ")

        if(opcao == "0"):
            print("Até logo, desligando agenda. . .")
            self.em_execucao = False
            return
        elif(opcao == "1"):
            self.cadastrar_contato()
        elif(opcao == "2"):
            self.listar_contatos()
        elif(opcao == "3"):
            self.excluir_contato()
        elif (opcao == "4"):
            self.cadastrar_tarefa()
        elif (opcao == "5"):
            self.listar_tarefas()
        elif (opcao == "6"):
            self.excluir_tarefa()
        elif (opcao == "7"):
            self.concluir_tarefas()
        elif (opcao == "8"):
            self.definir_tarefas_pendentes()
    def cadastrar_contato(self):
        print("Novo Contato")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email:")
        cpf = input("CPF: ")

        contato = Contato()
        contato.set_nome(nome)
        contato.set_telefone(telefone)
        contato.set_email(email)
        contato.set_cpf(cpf)

        self.agenda.add_contato(contato)
        print("Contato Adicionado. . . !")

    def listar_contatos(self):
        print('Lista de contatos: ')
        contatos_da_agenda = self.agenda.get_contatos()
        for indice, contato in enumerate(contatos_da_agenda):
            print("Numero: " +str(indice) + " - Contato: " +contato.get_nome() + "/Tel:" + contato.get_telefone())


    def excluir_contato(self):
        self.listar_contatos()
        indice_para_excluir = input("Digite o número do contato a ser excluído: ")

        try:
            contato_selecionado = self.agenda.get_contato(int(indice_para_excluir))
        except:
            print("Contato Inválido . . .")
            return

        self.agenda.remover_contato(contato_selecionado)
        print("Contato Excluído. . .")

    def cadastrar_tarefa(self):
        print("Nova Tarefa")
        descricao = input("Descrição: ")
        status = input(" Concluida? 1. Sim / 0. Não" )

        tarefa = Tarefa()
        tarefa.set_descricao(descricao)
        if (status == 1):
            tarefa.set_status_concluida()
        elif (status == 0):
            tarefa.set_status_pendente()
        else:
            print("Status Incorreto. . .")
            return


        self.agenda.add_tarefa()
        print("Tarefa adicionada. . .")
    def listar_tarefas(self):
        self.listar_tarefas()
        tarefas_da_agenda = self.agenda.get_tarefas()
        for indice, tarefa in enumerate(tarefas_da_agenda):
            print("Número: "+str(indice)+ " - " + tarefa.get_descricao() + "/ status: " + tarefa.get_status())


    def excluir_contato(self):
        self.listar_contatos()
        indice_para_excluir = input('Digite o número do contato ')

        try:
            contato_selecionado = self.agenda.get_contato(int(indice_para_excluir))
        except:
            print('Contato inválido')
            return

        self.agenda.remover_contato(contato_selecionado)
        print('Contato excluído com sucesso')

    def cadastrar_tarefa(self):
        print('Nova tarefa')
        descricao = input('Descricao: ')
        status = input('Concluída? 1 - sim / 0 - não ')

        tarefa = Tarefa()
        tarefa.set_descricao(descricao)
        if (status == '1'):
            tarefa.set_status_concluida()
        elif(status == '0'):
            tarefa.set_status_pendente()
        else:
            print('Status inválido')
            return


        self.agenda.add_tarefa(tarefa)
        print('Tarefa adicionada com sucesso.')

    def listar_tarefas(self):
        print('Lista de tarefas:')
        tarefas_da_agenda = self.agenda.get_tarefas()
        for indice, tarefa in enumerate(tarefas_da_agenda):
            print('Numero: ' + str(indice) + ' - ' + tarefa.get_descricao() + ' / status: ' + tarefa.get_status())

    def excluir_tarefa(self):
        self.listar_tarefas()
        indice_para_excluir = input('Digite o número da tarefa ')

        try:
            tarefa_selecionada = self.agenda.get_tarefa(int(indice_para_excluir))
        except:
            print('Tarefa inválida')
            return

        self.agenda.remover_tarefa(tarefa_selecionada)
        print('Tarefa excluída com sucesso')

    def concluir_tarefas(self):
        self.listar_tarefas()
        indices_para_excluir = input('Digite o número das tarefas, separados por virgula ')
        vetor_indices_para_excluir = indices_para_excluir.split(',')

        for indice_concluir in vetor_indices_para_excluir:
            indice_concluir = indice_concluir.strip()

            try:
                tarefa_selecionada = self.agenda.get_tarefa(int(indice_concluir))
            except:
                print('Contato inválido')
                return

            tarefa_selecionada.set_status_concluida()

        print('Tarefas concluidas com sucesso')

    def definir_tarefas_pendentes(self):
        self.listar_tarefas()
        indices_definir = input('Digite o número das tarefas, separados por virgula ')
        vetor_indices_para_excluir = indices_definir.split(',')

        for indice_definir in vetor_indices_para_excluir:
            indice_definir = indice_definir.strip()

            try:
                tarefa_selecionada = self.agenda.get_tarefa(int(indice_definir))
            except:
                print('Contato inválido')
                return

            tarefa_selecionada.set_status_pendente()

        print('Tarefas marcadas como pendentes com sucesso')