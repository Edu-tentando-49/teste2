# deve ter algo para mesa, que deve ter ocupação;
# deve ter algo para cliente;
# deve ter algo para pedido, armazenando valor na conta;
# deve ter algo para prato, com valor e nome;
# para cada conta(comanda), somente deve estar conectado um identificador;
# algo deve contar a quantidade de mesas disponíveis(vagas);
# algo deve detectar quando o pagamento está acima da conta, para que seja feito o troco;
# 15/09/2021
# MODELO CONCEITUAL PARA DIAGRAMA
# mesa: id (PK), capacidade, numero, status, comanda, cliente
# comanda: id (PK), produtos, valor_total, ativa, mesa,
# cliente: id (PK), nome
# prato: id (PK), descricao, preco
# reserva: id (PK), data_reserva, cliente
# pagamento: id (PK), comanda, reserva, cliente, operador, data_pagamento, valor_pago
# bebida: id (PK), descricao, preco
# 15/09/2021
# A CHAVE FRACA/ESTRANGEIRA é util para quando fazer relaçoes de 1 para muitos e de 1 para 1.   
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#