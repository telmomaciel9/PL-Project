import sys
import json
import toml
import yaml
import xml.etree.ElementTree as ET
from yacc import parsed_dict, linguagem
import ply.yacc as yacc

if linguagem == "yaml":
    # Converter para YAML
    yaml_data = yaml.dump(parsed_dict)

    # Exibir o YAML
    #print(yaml_data)

    # Guardar no ficheiro output.yaml
    with open("output.yaml", "w") as f:
        yaml.dump(parsed_dict, f, default_style='')

elif linguagem == "json":
    # Função para transformar o dicionário TOML em uma string JSON
    def to_json(toml_dict):
        return json.dumps(toml_dict, indent=2)
    
    json_string = to_json(parsed_dict)

    # Exibir o JSON
    #print(json_string)

    # Guardar no ficheiro output.json
    with open("output.json", "w") as f:
        json.dump(parsed_dict, f, ensure_ascii=False)

else:
    # Função recursiva para criar os elementos XML
    def create_xml_element(parsed_dict, parent):
        for key, value in parsed_dict.items():
            if isinstance(value, dict):
                # Elemento aninhado
                element = ET.SubElement(parent, key)
                create_xml_element(value, element)
            else:
                # Elemento simples
                element = ET.SubElement(parent, key)
                element.text = str(value)

    # Criar o elemento raiz do XML
    root = ET.Element('root')

    # Converter o dicionário para XML
    create_xml_element(parsed_dict, root)

    # Criar a árvore XML
    tree = ET.ElementTree(root)

    # Gravar o XML em um arquivo
    tree.write('output.xml', encoding='utf-8', xml_declaration=True)













