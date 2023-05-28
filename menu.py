import sys
import os
import toml


while True:

    if os.path.exists("output.xml"):
        os.remove("output.xml")
    if os.path.exists("output.json"):
        os.remove("output.json")
    if os.path.exists("output.yaml"):
        os.remove("output.yaml")

    path = input("Digite o path do ficheiro a testar: ")

    if os.path.exists(path):

        # Leitura do arquivo TOML
        with open(path) as file:
            data = file.read()

        try:
            # Parsing do arquivo TOML
            parsed_data = toml.loads(data)
            print("O arquivo TOML está formatado corretamente.")
        except toml.TomlDecodeError as e:
            print("Erro ao decodificar o arquivo TOML:")
            print(e)

        while True:

            linguagem = input("Escolha a linguagem para a qual quer converter: ")
    
            if linguagem in ["yaml", "json", "xml"]:
                break
            else:
                print("Linguagem não suportada. Tente novamente.")

        break
    else:
        print("O ficheiro não existe. Tente novamente.")
