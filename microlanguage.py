alias = {"q": "quit", "h": "help", "l": "list"}

def execml(string:str) :
    if string in alias :
        string = alias[string]
    match string :
        case "quit": exit()
        case "help": return "quit: Quitte le programme\nhelp: Affiche l'aide\nlist: Liste les alias"
        case "list": return "\n".join([f"{key}: {value}" for key, value in alias.items()])