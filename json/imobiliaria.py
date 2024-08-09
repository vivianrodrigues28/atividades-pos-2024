import json

def carregar_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return json.load(f)

def exibir_menu(imoveis):
    print("Menu de Imóveis:")
    for idx, imovel in enumerate(imoveis):
        descricao = imovel.get("descricao", "Descrição não disponível")
        print(f"{idx}: {descricao}")

def exibir_detalhes(imovel):
    print("\nDetalhes do Imóvel:")
    print(f"Descrição: {imovel.get('descricao', 'N/A')}")
    print("Proprietário:")
    print(f"  Nome: {imovel.get('proprietario', {}).get('nome', 'N/A')}")
    print(f"  Email: {imovel.get('proprietario', {}).get('email', 'N/A')}")
    print(f"  Telefone: {imovel.get('proprietario', {}).get('telefone', 'N/A')}")
    print("Endereço:")
    print(f"  Rua: {imovel.get('endereco', {}).get('rua', 'N/A')}")
    print(f"  Bairro: {imovel.get('endereco', {}).get('bairro', 'N/A')}")
    print(f"  Cidade: {imovel.get('endereco', {}).get('cidade', 'N/A')}")
    print(f"  Número: {imovel.get('endereco', {}).get('numero', 'N/A')}")
    print("Características:")
    print(f"  Tamanho: {imovel.get('caracteristicas', {}).get('tamanho', 'N/A')}")
    print(f"  Número de Quartos: {imovel.get('caracteristicas', {}).get('numQuartos', 'N/A')}")
    print(f"  Número de Banheiros: {imovel.get('caracteristicas', {}).get('numBanheiros', 'N/A')}")
    print(f"Valor: {imovel.get('valor', 'N/A')}")

def main():
    caminho_arquivo_json = 'imobiliaria.json'
    
    
    try:
        imoveis = carregar_json(caminho_arquivo_json)
    except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")
        return

    while True:
       
        exibir_menu(imoveis)
        
        try:
           
            escolha = int(input("\nDigite o número do imóvel que deseja visualizar: "))
            if escolha == -1:
                print("Saindo...")
                break
            elif 0 <= escolha < len(imoveis):
                exibir_detalhes(imoveis[escolha])
            else:
                print("Número de imóvel inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
