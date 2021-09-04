class Somar:  # esta é a classe somar
    @staticmethod  # este "@staticmethod" configura as próximas funções para
    def adiciona(vet_recebe):  # a função "adiciona" pega os valores dentro de "vet_recebe"(o vetor)
        resultado = 0  # variável de tipo "int" para continuar a operação.

        for algo in vet_recebe:  # condiciona o andamento da operação, chamando "algo" para alterar no "resultado"
            resultado = resultado + algo

        return resultado
