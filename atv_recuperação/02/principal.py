from operante import Somar   # o escrito "from" serve para selecionar o "arquivo.py" e
# pastas se digitalmente dispostas antes do "."
# enquanto o "import" serve para selecionar a classe dentro do "arquivo.py".

vet_recebe = [1, 2]  # vetor que recepciona valores dentro de si,
# (este mesmo é indicado pelos colchetes), no caso, a função dele é guardar os valores, para assim o
# "operante.py" exercer a função de soma(preparativo).

resultado = Somar.adiciona(vet_recebe)  # este "resultado" é a string que chama a classe, e, depois do ponto,
# chama a função, acionando a operação(feitio).
print("soma do único valor no vetor é: " + str(resultado))  # enfim imprime os valores já prontos após a operação feita
