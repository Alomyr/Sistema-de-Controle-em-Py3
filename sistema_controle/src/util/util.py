def render_status():
    print("C- concluido\nI-in progress\nN- nao iniciada\n")
    return input("Opt: ").capitalize()


# REFACTOR: LIMPAR E ADD CASE DEFAULT
def state_machine_status():
    while True:
        opt = render_status()
        match opt:
            case "C":
                return "Concluido"
            case "I":
                return "in progress"
            case "N":
                return "nao iniciada"
