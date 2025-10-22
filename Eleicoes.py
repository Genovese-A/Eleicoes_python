# Contador de votos:
joao = 0
jose = 0
paulo = 0
maria = 0
branco = 0
nulo = 0

while True:
    print("-----------------------------------------")
    print("|           Candidatos                  |")
    print("|                                       |")
    print("| 1 - Joao                              |")
    print("| 2 - Jose                              |")
    print("| 3 - Paulo                             |")
    print("| 4 - Maria                             |")
    print("| 5 - Voto em Branco                    |")
    print("| 6 - Voto Nulo                         |")
    print("-----------------------------------------")

    try:
        candidatos = int(input("Qual o número do seu candidato: "))
    except ValueError:
        print("Digite apenas numero de 1 a 6")
        continue
    
    if candidatos == 1:
        joao += 1
    elif candidatos == 2:
        jose += 1
    elif candidatos == 3:
        paulo += 1
    elif candidatos == 4:
        maria += 1
    elif candidatos == 5:
        branco += 1
    elif candidatos == 6:
        nulo += 1
    else:
        print("Número invalido, por favor digite um número VALIDO.")
        continue

    encerrar = input("Deseja encerrar a votação? [s]im / [n]ão: ").strip().lower()
    
    if encerrar in ["s", "sim"]:
        print("Votação Encerrada!")
        break
    elif encerrar in ["n", "nao", "não"]:
        print("Votação continua...\n")
    else:
        print("Opção inválida. Votação continua...\n")
total_de_votos = jose + joao + paulo + maria + nulo + branco

if total_de_votos == 0:
    print("Não houve votos")
else:
    percentagem_nulo = (nulo / total_de_votos) * 100
    percentagem_branco = (branco / total_de_votos) * 100

    total_votos_canditados ={"Jose": jose, "Joao": joao, "Paulo": paulo, "Maria": maria}
    
    vencedor = max(total_votos_canditados, key=total_votos_canditados.get)


print("============== RESULTADO DA VOTAÇÃO =====================")
print(f"|Joao.............: {joao} votos                        |")
print(f"|Jose.............: {jose} votos                        |")
print(f"|Paulo............: {paulo} votos                       |")
print(f"|Maria............: {maria} votos                       |")
print(f"|Votos em Branco..: {branco} votos                      |")
print(f"|Votos Nulos......: {nulo} votos                        |")
print("|--------------------------------------------------------|")
print(f"| Porcentagem de votos nulos: {percentagem_nulo:.2f}%   |")
print(f"| Porcentagem de votos nulos: {percentagem_branco:.2f}% |")
print("|--------------------------------------------------------|")
print(f"Total de votos: {total_de_votos}                        |")
print(f"VENCEDOR: {vencedor}                                    |")
print("==========================================================")