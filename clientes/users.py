import requests

api_url = "https://jsonplaceholder.typicode.com/users"

while True:
    print("Digite 1 para listar todos os usuários")
    print("Digite 2 para listar as tarefas de um usuário específico")
    print("Digite 3 para Criar/Ler/Atualizar/Deletar usuários")
    

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        response = requests.get(api_url).json()
        for user in response:
            print(f"{user['id']} - {user['name']}")

    elif opcao == "2":
        user_id = int(input("Digite o ID do usuário: "))
        response = requests.get(f"{api_url}/{user_id}/todos").json()
        for todo in response:
            print(todo["title"])

    elif opcao == "3":
        print("Digite 1 para criar um novo usuário")
        print("Digite 2 para ler um usuário")
        print("Digite 3 para atualizar os dados de um usuário")
        print("Digite 4 para deletar um usuário")
        opcao2 = input()

        if opcao2 == "1":
            user_data = {}
            user_data["name"] = input("Digite o nome do usuário: ")
            user_data["username"] = input("Digite o username do usuário: ")
            user_data["email"] = input("Digite o email do usuário: ")
            user_address = {}
            user_address["street"] = input("Digite o endereço de usuário: ")
            user_address["city"] = input("Digite a cidade de usuário: ")

            user_data["address"] = user_address
            response = requests.post(api_url, json=user_data).status_code
            if response == 201:
                print("Usuário criado com sucesso.")
            else:
                print("Falha ao criar o usuário.")

        elif opcao2 == "2":
            user_id2 = input("Digite o ID do usuário: ")
            response = requests.get(api_url+"/"+user_id2).json()
            print(response)

        elif opcao2 == "3":
            user_id = input("Digite o ID do usuário: ")
            old_user = requests.get(api_url+"/"+user_id).json()
            print(f"Você está modificando o usuário {old_user['name']}")
            old_user["name"] = input("Digite o novo nome do usuário: ")
            old_user["username"] = input("Digite o novo username do usuário: ")
            old_user["email"] = input("Digite o novo email do usuário: ")
            response = requests.patch(api_url+"/"+user_id, json=old_user).status_code

            if response == 200:
                print("Usuário atualizado com sucesso.")
            else:
                print("Falha ao atualizar o usuário.")

        elif opcao2 == "4":
            user_id2 = input("Digite o ID do usuário: ")
            response = requests.delete(api_url+"/"+user_id2).status_code
            if response == 200:
                print("Usuário deletado com sucesso.")
            else:
                print("Falha ao deletar o usuário.")

        else:
            print("Opção inválida.")

    

    else:
        print("Opção inválida, tente novamente.")
        