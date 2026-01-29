"""
Módulo Controlador Principal (Main Loop).

Este módulo gerencia o fluxo principal de execução do aplicativo, conectando
as interações da View com as regras de negócio e persistência.
"""

from sistema_controle.db.task_repository import export_tasks
from sistema_controle.src.view.task_view import (
    cadastro,
    edit_status_view,
    edit_task_view,
    render_menu,
    status_filter_view,
    task_delet_all_view,
    task_list_view,
    task_delet_view,
)


def state_machine():
    """
    Executa o loop principal (Máquina de Estados) do sistema de tarefas.

    A função mantém o programa em execução, processa a escolha do usuário
    obtida via menu e coordena qual componente da View deve ser acionado.

    O loop continua até que a opção de saída (0) seja selecionada,
    alterando o estado para 'stopped'.
    """
    estado_sistema = "running"

    while estado_sistema == "running":
        try:
            # Captura a opção do usuário através do menu renderizado
            opcao = render_menu()

            match opcao:
                case 1:
                    cadastro()
                case 2:
                    task_list_view()
                case 3:
                    task_delet_view()
                case 4:
                    edit_task_view()
                case 5:
                    edit_status_view()
                case 6:
                    task_delet_all_view()
                case 7:
                    status_filter_view()
                case 8:
                    export_tasks()
                case 0:
                    print("\nEncerrando sistema... Até logo!")
                    estado_sistema = "stopped"
                case _:
                    print("\n[Erro] Opção inválida! Tente um número de 0 a 8.")

        except ValueError:
            print("\n[Erro] Entrada inválida! Por favor, digite apenas números.")
        except Exception as e:
            print(f"\n[Erro Crítico] Ocorreu um problema inesperado: {e}")
