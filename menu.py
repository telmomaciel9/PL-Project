import sys
import os


while True:

    if os.path.exists("output.xml"):
        os.remove("output.xml")
    if os.path.exists("output.json"):
        os.remove("output.json")
    if os.path.exists("output.yaml"):
        os.remove("output.yaml")

    path = input("Digite o path do ficheiro a testar: ")

    if os.path.exists(path):

        while True:

            linguagem = input("Escolha a linguagem para a qual quer converter: ")
    
            if linguagem in ["yaml", "json", "xml"]:
                break
            else:
                print("Linguagem não suportada. Tente novamente.")

        break
    else:
        print("O ficheiro não existe. Tente novamente.")
