# Jogo da Forca
Desenha no terminal o jogo da forca.

---
## O Jogo

#### Palavra secreta
Primeiramente é pedido ao usuário informar a palavra secreta.

<img width="500px" style="float: right;" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-input.png"></img>

#### Início do jogo
Desenha as traves da forca, a corda na ponta, os campos reservados aos caracteres e informa o número de lances.

<img width="170px" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-begin.png"></img>

#### Durante
Depois de ter errado quatro vezes, sua cabeça e seus braços estão roxos por quase não haver mais circulação sanguínea. Só não vemos as pernas roxas também porque o enforcado está usando calça jeans.

<img width="160px" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-2chance.png"></img>

Estando já na última chance o enforcado está furioso. As cruzes ('+') no aviso são o prenúncio de que o fim está próximo.

<img width="220px" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-lastchance.png"></img>

#### Desfecho
Com final feliz

<img width="200px" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-winner.png"></img>

Trágico - sem vida nos olhos, o enforcado sucumbe reclinando sua cabeça para o lado.

<img  width="180px" src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-dead.png"></img>


---

## Dependencia
Precisa do Python 3 instalado. Se usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão.
Verifique com o comando:
```sh
python --version
```
_Output: Python 3.10.6_

Caso não esteja instalado, instale com os comandos abaixo:
```sh
sudo apt update
```
```sh
sudo apt install python3
```

---

## Executar

### Com o comando python3
Baixe o arquivo forca.py e no mesmo diretório executeo comando:

```sh
python3 forca.py
```
### Como shell script
Baixe o arquivo forca.py e forneça permissão de execução ao arquivo:

```sh
chmod +x forca.py
```
E execute com:
```sh
./forca.py
```

Se encontrar algum erro na linha 1 devido a `#!/usr/bin/env python3` dê o comando 
```sh
whereis python
```
E corrija o path do python pela saída do whereis, ficaria algo assim: #!/usr/bin/python


### Colab
Se tiver uma conta google pode abrir diretamente no Colab. No aquivo [jogo_forca.ipynb](https://github.com/earmarques/jogo-forca/blob/main/jogo_forca.ipynb) clique na imagem <a href="https://github.com/earmarques/jogo-forca/blob/main/jogo_forca.ipynb"><img src="https://github.com/earmarques/jogo-forca/blob/main/images/forca-colab.png"></a> para criar uma cópia e poder rodar.



