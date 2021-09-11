from aprendizado_fora_do_curso.oi import Oi

interacao = Oi.get_mensagem()

for comunicar in Oi:
    print(comunicar)

for reagir in Oi:
    print(reagir)

comunicar = input("")