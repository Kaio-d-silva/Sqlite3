from services.clientes_services import *
from auxiliares.menu_main import menu_opcoes

# # status = listar_clientes("observacao", "cnpj")
# status = inativar_cliente(1)
# print(status)
# # cadastrar_cliente()

if __name__ == "__main__":
    resposta = menu_opcoes()
    print(resposta)
