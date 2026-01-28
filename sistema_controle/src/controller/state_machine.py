from sistema_controle.src.view.task_view import (
    cadastro,
    render_menu,
    task_list_view,
    task_delet_view,
)

from sistema_controle.src.view.task_view import (
    cadastro,
    render_menu,
    task_list_view,
    task_delet_view,
)


def state_machine():
    status = "running"

    while status == "running":
        opt = render_menu()

        match opt:
            case 1:
                cadastro()
            case 2:
                task_list_view()
            case 3:
                task_delet_view()
            case 0:
                print("Encerrando sistema...")
                status = "stopped"
            case _:
                print("Opção inválida!")
