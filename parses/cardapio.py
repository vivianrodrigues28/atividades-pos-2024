import xml.dom.minidom

def carregar_xml(caminho_arquivo):
    
    return xml.dom.minidom.parse(caminho_arquivo)

def extrair_pratos(doc):
    
    pratos = doc.getElementsByTagName('prato')
    lista_pratos = []
    for prato in pratos:
        prato_id = prato.getAttribute('id')
        nome = prato.getElementsByTagName('nome')[0].firstChild.data
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.data
        ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.data
        preco = prato.getElementsByTagName('preco')[0].firstChild.data
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.data
        tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.data

        lista_pratos.append({
            'id': prato_id,
            'nome': nome,
            'descricao': descricao,
            'ingredientes': ingredientes,
            'preco': preco,
            'calorias': calorias,
            'tempo_preparo': tempo_preparo
        })
    
    return lista_pratos

def exibir_menu(pratos):
    print("Menu de Pratos:")
    for prato in pratos:
        print(f"{prato['id']}: {prato['nome']}")

def exibir_detalhes(prato):
    print("\nDetalhes do Prato:")
    print(f"ID: {prato['id']}")
    print(f"Nome: {prato['nome']}")
    print(f"Descrição: {prato['descricao']}")
    print(f"Ingredientes: {prato['ingredientes']}")
    print(f"Preço: {prato['preco']}")
    print(f"Calorias: {prato['calorias']}")
    print(f"Tempo de Preparo: {prato['tempo_preparo']}")

def main():
    caminho_arquivo_xml = 'xsd\cardapio.xml' 
    try:
        doc = carregar_xml(caminho_arquivo_xml)
    except Exception as e:
        print(f"Erro ao carregar o arquivo XML: {e}")
        return
    
    pratos = extrair_pratos(doc)
    
    while True:
        exibir_menu(pratos)
        escolha = input("\nDigite o ID do prato que deseja visualizar: ").strip()
        
        if escolha.lower() == 'sair':
            print("Saindo...")
            break
        
        prato_encontrado = next((prato for prato in pratos if prato['id'] == escolha), None)
        
        if prato_encontrado:
            exibir_detalhes(prato_encontrado)
        else:
            print("ID do prato não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()
