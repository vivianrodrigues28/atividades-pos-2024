import json
from xml.dom.minidom import parse

def xml_para_dict(doc):
    
    def parse_imovel(imovel):
        return {
            "descricao": imovel.getElementsByTagName("descricao")[0].firstChild.data,
            "proprietario": {
                "nome": imovel.getElementsByTagName("nome")[0].firstChild.data if imovel.getElementsByTagName("nome") else None,
                "email": imovel.getElementsByTagName("email")[0].firstChild.data if imovel.getElementsByTagName("email") else None,
                "telefone": imovel.getElementsByTagName("telefone")[0].firstChild.data if imovel.getElementsByTagName("telefone") else None,
            },
            "endereco": {
                "rua": imovel.getElementsByTagName("rua")[0].firstChild.data,
                "bairro": imovel.getElementsByTagName("bairro")[0].firstChild.data,
                "cidade": imovel.getElementsByTagName("cidade")[0].firstChild.data,
                "numero": imovel.getElementsByTagName("numero")[0].firstChild.data if imovel.getElementsByTagName("numero") else None,
            },
            "caracteristicas": {
                "tamanho": imovel.getElementsByTagName("tamanho")[0].firstChild.data,
                "numQuartos": imovel.getElementsByTagName("numQuartos")[0].firstChild.data,
                "numBanheiros": imovel.getElementsByTagName("numBanheiros")[0].firstChild.data,
            },
            "valor": imovel.getElementsByTagName("valor")[0].firstChild.data,
        }
    
    imobiliaria = doc.getElementsByTagName('imobiliaria')[0]
    imoveis = imobiliaria.getElementsByTagName('imovel')
    return [parse_imovel(imovel) for imovel in imoveis]

def salvar_json(dados, caminho_arquivo):
    
    with open(caminho_arquivo, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def main():
    caminho_arquivo_xml = 'xml\imobiliaria.xml'  
    caminho_arquivo_json = 'imobiliaria.json'
    
    
    try:
        doc = parse(caminho_arquivo_xml)
    except Exception as e:
        print(f"Erro ao carregar o arquivo XML: {e}")
        return
    
   
    dados = xml_para_dict(doc)
    
    
    salvar_json(dados, caminho_arquivo_json)
    print(f"Dados convertidos e salvos em {caminho_arquivo_json}")

if __name__ == "__main__":
    main()
