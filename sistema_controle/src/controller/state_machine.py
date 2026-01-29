from sistema_controle.db.task_repository import edit_task, export_tasks
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
                print("Encerrando sistema...")
                status = "stopped"
            case _:
                print("Opção inválida!")
