import os
import random
from colorama import Fore, Style, init
init(autoreset=True)

num1 = 0
num2 = 0
operacao = ""
validacao_numeros = False
validacao_op = False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
import random
from colorama import Fore, Style, init
init(autoreset=True)

def jogo_de_adivinhacao():
  opcao_dificuldade = -1

  while opcao_dificuldade != 0: 
    try:
      opcao_dificuldade = int(input(Fore.CYAN + """
      Bem vindo ao jogo de adivinhação!!
      Qual será a dificuldade??
      (1) Fácil 1 a 10
      (2) Médio 1 a 15
      (3) Difícil 1 a 20
      (4) Muito difícil 1 a 30
      (0) Sair """ + Fore.RESET))

      if opcao_dificuldade == 1:
          tentativas = 5
          numero_secreto = random.randint(1,10)

          while tentativas > 0:
            try:
              chute = int(input(Fore.YELLOW + f"Tente acertar o número secreto de 1 a 10. Você tem {tentativas} tentativa(s): " + Fore.RESET))
            except ValueError:
              print(Fore.RED + "Escolha um número válido")
              continue

            if chute == numero_secreto:
              print(Fore.GREEN + f"Parabéns! Você acertou o número secreto: {numero_secreto}")
              input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)
              break
            elif chute > numero_secreto:
              print(Fore.RED + "O seu chute é maior que o número secreto!!")
            elif chute < numero_secreto:
              print(Fore.RED + "O seu chute é menor que o número secreto!!")

            tentativas -= 1

          if tentativas == 0:
            print(Fore.RED + f"Você não conseguiu adivinhar! O número secreto era {numero_secreto}.")
            input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)

      if opcao_dificuldade == 2:
          tentativas = 5
          numero_secreto = random.randint(1,15)

          while tentativas > 0:
            try:
              chute = int(input(Fore.YELLOW + f"Tente acertar o número secreto de 1 a 15. Você tem {tentativas} tentativa(s): " + Fore.RESET))
            except ValueError:
              print(Fore.RED + "Escolha um número válido")
              continue

            if chute == numero_secreto:
              print(Fore.GREEN + f"Parabéns! Você acertou o número secreto: {numero_secreto}")
              input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)
              break
            elif chute > numero_secreto:
              print(Fore.RED + "O seu chute é maior que o número secreto!!")
            elif chute < numero_secreto:
              print(Fore.RED + "O seu chute é menor que o número secreto!!")

            tentativas -= 1

          if tentativas == 0:
            print(Fore.RED + f"Você não conseguiu adivinhar! O número secreto era {numero_secreto}.")
            input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)

      if opcao_dificuldade == 3:
          tentativas = 5
          numero_secreto = random.randint(1,20)

          while tentativas > 0:
            try:
              chute = int(input(Fore.YELLOW + f"Tente acertar o número secreto de 1 a 20. Você tem {tentativas} tentativa(s): " + Fore.RESET))
            except ValueError:
              print(Fore.RED + "Escolha um número válido")
              continue

            if chute == numero_secreto:
              print(Fore.GREEN + f"Parabéns! Você acertou o número secreto: {numero_secreto}")
              input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)
              break
            elif chute > numero_secreto:
              print(Fore.RED + "O seu chute é maior que o número secreto!!")
            elif chute < numero_secreto:
              print(Fore.RED + "O seu chute é menor que o número secreto!!")

            tentativas -= 1

          if tentativas == 0:
            print(Fore.RED + f"Você não conseguiu adivinhar! O número secreto era {numero_secreto}.")
            input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)

      if opcao_dificuldade == 4:
          tentativas = 4
          numero_secreto = random.randint(1,30)

          while tentativas > 0:
            try:
              chute = int(input(Fore.YELLOW + f"Tente acertar o número secreto de 1 a 30. Você tem {tentativas} tentativa(s): " + Fore.RESET))
            except ValueError:
              print(Fore.RED + "Escolha um número válido")
              continue

            if chute == numero_secreto:
              print(Fore.GREEN + f"Parabéns! Você acertou o número secreto: {numero_secreto}")
              input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)
              break
            elif chute > numero_secreto:
              print(Fore.RED + "O seu chute é maior que o número secreto!!")
            elif chute < numero_secreto:
              print(Fore.RED + "O seu chute é menor que o número secreto!!")

            tentativas -= 1

          if tentativas == 0:
            print(Fore.RED + f"Você não conseguiu adivinhar! O número secreto era {numero_secreto}.")
            input(Fore.MAGENTA + "Pressione ENTER para voltar ao menu." + Fore.RESET)

      elif opcao_dificuldade == 0:
          print(Fore.CYAN + "Obrigado por usar o jogo de adivinhação. Saindo..." + Fore.RESET)
      else:
          print(Fore.RED + "Escolha uma opção válida")

    except ValueError:
      print(Fore.RED + "Escolha um número válido")

def calculadora_simples():
    global num1, num2, operacao, validacao_numeros, validacao_op

    limpar_tela()
    validacao_numeros = False
    validacao_op = False

    while not validacao_numeros:
        try:
            num1 = float(input(Fore.CYAN + "Escolha o primeiro número para calcular: "))
            num2 = float(input(Fore.CYAN + "Escolha o segundo número para calcular: "))
            validacao_numeros = True
        except:
            print(Fore.RED + "Digite um número válido")

    while not validacao_op:
        operacao = input(Fore.CYAN + "Qual operação você deseja realizar (+) (-) (*) (/): ")
        if operacao not in ["+", "-", "*", "/"]:
            print(Fore.RED + "Escolha uma operação válida")
        else:
            validacao_op = True

    if operacao == "+":
        resultado = num1 + num2
        print(Fore.GREEN + "O resultado é de", num1, "+", num2, "=", resultado)

    elif operacao == "-":
        resultado = num1 - num2
        print(Fore.GREEN + "O resultado é de", num1, "-", num2, "=", resultado)

    elif operacao == "*":
        resultado = num1 * num2
        print(Fore.GREEN + "O resultado é de", num1, "*", num2, "=", resultado)

    else:
        try:
            resultado = num1 / num2
            print(Fore.GREEN + "O resultado é de", num1, "/", num2, "=", resultado)
        except:
            print(Fore.RED + "Não é possível dividir um número por 0")

    input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu.")

def rolador_de_dados():
    opcao_dos_dados = -1
    while opcao_dos_dados != 0:
        limpar_tela()
        try:
            print(Fore.CYAN + """
Escolha uma opção para realizar!!
(1) Dado de seis lados
(2) Dado de dez lados
(3) Dado de vinte lados
(4) Dado de cem lados
(0) Sair""")

            opcao_dos_dados = int(input("Escolha: "))

            if opcao_dos_dados in [1, 2, 3, 4]:
                try:
                    rolar_dados = int(input("Quantas vezes você quer rolar o dado? "))
                except ValueError:
                    print(Fore.RED + "Escolha um número válido!!")
                    continue

                lados = {1: 6, 2: 10, 3: 20, 4: 100}[opcao_dos_dados]
                for i in range(rolar_dados):
                    valor_tirado = random.randint(1, lados)
                    print(Fore.GREEN + "Valor tirado:", valor_tirado)
                input(Fore.YELLOW + "\nPressione ENTER para voltar ao menu.")

            elif opcao_dos_dados == 0:
                print(Fore.YELLOW + "Obrigado por usar o rolador de dados!!")

            else:
                print(Fore.RED + "Escolha uma opção válida")

        except ValueError:
            print(Fore.RED + "Escolha um valor válido")
            input("Pressione ENTER para continuar.")

opcao = -1
while opcao != 0:
    limpar_tela()
    try:
        print(Fore.CYAN + """
Bem-vindo ao App Variado!!
(1) Calculadora
(2) Jogo de adivinhação
(3) Rolador de dados
(0) Sair""")

        opcao = int(input("Escolha a opção que você deseja fazer: "))

        if opcao == 1:
            calculadora_simples()
        elif opcao == 2:
            jogo_de_adivinhacao()
            input("Pressione ENTER para voltar ao menu.")
        elif opcao == 3:
            rolador_de_dados()
        elif opcao == 0:
            print(Fore.YELLOW + "Obrigado por usar o App Variado! Saindo...")
        else:
            print(Fore.RED + "Escolha uma opção válida!")
            input("Pressione ENTER para continuar.")

    except ValueError:
        print(Fore.RED + "Por favor, digite um número válido.")
        input("Pressione ENTER para continuar.")