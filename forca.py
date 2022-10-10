#!/usr/bin/env python3

#*************************************************
#   Author: Éder A. R. Marques                   *
#   Email:  earmarques@gmail.com                 *
#   Local:  Gastão Vidigal/SP Brazil             *
#   Date:   22/05/2020                           *
#************************************************/

# COLAB: descomentar essa linha se for rodar no Colab
#from google.colab import output


# ATARI Computação Gráfica LTDA-íssima -----------------------------------------

# Paleta de Cores
DEFAULT_NEGRITO =  "\033[1;0m"
BRANCO =           "\033[1;37m"
VERMELHO =         "\033[1;31m"
VERMELHO_ITALICO = "\033[3;31m"
AMARELO =          "\033[1;33m"
VERDE =            "\033[1;32m"
AZUL =             "\033[1;34m"
ROXO =             "\033[1;35m"
RESET_DEFAULT =    "\033[0;0m"

# Componentes
trave_superior = " _________"
poste =          "\n |"
corda =          "\t |"
forca =          "       §"
cabeca =         "       @"
cabeca_brava =   "     (`~´)"
cabeca_morta =   "     (x.x)"
corpo =          "      [E]"   # super E'der
braco_direito =        "/"
braco_esquerdo =       "\\"
pernas =         "      / \\"


# Montando a Estrutura ---------------------------------------------------------

linhas = list()
linhas.append("\033c")                          # linha 0:  limpa o terminal
linhas.append(list(trave_superior))             # linha 1
linhas.append(list(poste + corda))              # linha 2
linhas.append(list(poste + corda))              # linha 3
linhas.append(list(poste + forca))              # linha 4:  cabecas
linhas.append([])                               # linha 5:  corpo&bracos
linhas.append([])                               # linha 6:  pernas
linhas.append(list(poste))                      # linha 7
linhas.append(list(poste))                      # linha 8
linhas.append([])                               # linha 9:  letras descobertas
linhas.append([])                               # linha 10: base tracejada


# Cabeçário --------------------------------------------------------------------

# Limpa a tela depois de digitar palavra secreta
print("\033c", end="")
cabecalho = DEFAULT_NEGRITO + "  Jogo da Forca  "
print(cabecalho.center(80,"_"))
print()


# Entrada de Dados  ------------------------------------------------------------

palavra = input(" Entre com a palavra secreta:\n>> ")
palavra = list(palavra.upper())

# Limpa a tela depois de digitar palavra secreta
print("\033c", end="")
#output.clear()      # COLAB: descomentar essa linha se for rodar no Colab

# Dimensionando lista de chutes e inicializando com espaços
letras_descobertas = []
for c in palavra:
  letras_descobertas.append(' ')


# Variáveis de Controles  ------------------------------------------------------
morreu = False
ganhou = False
erro = 0

while not morreu:

  # linha 4 - cabecas
  if erro == 6:   # morreu
    linhas[4] = list(poste + cabeca_morta)
  elif erro == 5: # tá quase
    linhas[4] = list(poste + cabeca_brava)
  elif erro > 0:
    linhas[4] = list(poste + cabeca)
  else:
    linhas[4] = list(poste + forca)

  # linha 5 - corpo&bracos
  if erro > 1:
    linhas[5] = list(poste + corpo)
    if erro > 2:
      linhas[5][8] = braco_direito
      linhas[5].append(braco_esquerdo)
      # linha 6 - pernas
      if erro > 3:
        linhas[6] = list(poste + pernas)
      else:
        # sem pernas
        linhas[6] = list(poste)
  else:
    # sem corpo&bracos e sem pernas
    linhas[5] = list(poste)
    linhas[6] = list(poste)

  # Letras Descobertas
  linhas[9] = list(poste)
  for letra in letras_descobertas:
    linhas[9].append("  " + letra.upper() + " ")

  # Base Trasejada
  traco = "___"
  linhas[10] = list(poste)
  for c in palavra:
    linhas[10].extend(list(" " + traco))


  # Colorindo o Desenho --------------------------------------------------------

  linhas[1].insert(1, DEFAULT_NEGRITO)
  linhas[2].insert(1, DEFAULT_NEGRITO)
  linhas[3].insert(1, DEFAULT_NEGRITO)

  # Cabeças
  linhas[4].insert(1, DEFAULT_NEGRITO)
  if erro > 0 and erro < 5:
    linhas[4].insert(4, ROXO)
  elif erro == 5:
    linhas[4].insert(4, VERMELHO)
  elif erro == 6:
    linhas[4].insert(4, VERMELHO_ITALICO)
    linhas[4].append(RESET_DEFAULT)

  # Braços na mesma cor da cabeça
  linhas[5].insert(0, DEFAULT_NEGRITO)
  if erro > 2 and erro < 5:
    linhas[5].insert(8, ROXO)       # braco
    linhas[5].insert(11, VERDE)     # corpo
    linhas[5].insert(15, ROXO)      # braco
  elif erro >= 5:
    linhas[5].insert(8, VERMELHO)   # braco
    linhas[5].insert(11, VERDE)     # corpo
    linhas[5].insert(15, VERMELHO)  # braco
  else:
    # pinta só o corpinho
    linhas[5].insert(4, VERDE)

  linhas[6].insert(1, DEFAULT_NEGRITO)
  linhas[6].insert(4, AZUL)              # pernas
  linhas[7].insert(1, DEFAULT_NEGRITO)
  linhas[8].insert(1, DEFAULT_NEGRITO)
  linhas[9].insert(1, DEFAULT_NEGRITO)
  linhas[9].insert(4, VERDE)             # letras descobertas
  linhas[10].insert(1, DEFAULT_NEGRITO)


# Renderização  ----------------------------------------------------------------

  pincel = []
  for linha in linhas:
    pincel.append("".join(linha))

#  output.clear()    # COLAB: descomentar essa linha se for rodar no Colab
  print("".join(pincel))


# Interação com o Jogador    ---------------------------------------------------

  # Controle
  if ganhou:
    break   # saia do loop

  # Vidas do Jogador
  msg = "\n"
  if erro == 6: # game-over
    morreu = True
  elif erro == 5:
    msg += VERMELHO + "  Última chance!!!  ".center(30,"+") + RESET_DEFAULT
  else:
    msg += " Você tem {} chances.".format(6 - erro)
  print(msg)

  # Coleta do Chute/Palpite
  if not morreu:
    chute = input("\n Arrisque uma letra:\n>> ")
    chute = chute.upper()
    # Validação do chute
    acertou = False
    for indice, letra in enumerate(palavra):
      if chute == letra:
        acertou = True
        letras_descobertas[indice] = letra
    if not acertou:
      erro += 1

  # Checando Vencedor
  palavra_secreta = "".join(palavra)
  palavra_descoberta = "".join(letras_descobertas)

  if (palavra_secreta == palavra_descoberta):
    ganhou = True


# Resultado do Jogo ------------------------------------------------------------

if morreu:
  print(VERMELHO + "..... Perdeu Playboy!!!")
elif ganhou:
  print("\n\n" + VERDE + "  Congratulations!!!  ".center(32, "*"))

print(RESET_DEFAULT + "\n\n\n\n")
