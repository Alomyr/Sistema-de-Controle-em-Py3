"""
Módulo de Gerenciamento de Estados de Tarefas.

Este módulo provê a lógica de máquina de estados para garantir que as tarefas
sempre possuam um status válido dentro do sistema.
"""


def render_status() -> str:
    """
    Exibe as opções de status disponíveis e captura a entrada do usuário.

    Returns:
        str: A letra correspondente à opção escolhida, formatada em maiúscula.
    """
    print("\nStatus disponíveis:")
    print("C - Concluído")
    print("I - In Progress")
    print("N - Não Iniciada")
    return input("Opção: ").strip().capitalize()


def state_machine_status() -> str:
    """
    Controla o fluxo de seleção de status, garantindo uma escolha válida.

    A função executa um loop contínuo até que o usuário forneça uma das
    entradas aceitas ('C', 'I' ou 'N').

    Returns:
        str: O nome descritivo do status selecionado (ex: "Concluido").

    Note:
        Se uma opção inválida for digitada, o usuário será alertado e o
        menu de status será exibido novamente.
    """
    while True:
        opt = render_status()
        match opt:
            case "C":
                return "Concluido"
            case "I":
                return "In Progress"
            case "N":
                return "Não Iniciada"
            case _:
                print("\n[Erro] Opção inválida! Escolha C, I ou N.")
