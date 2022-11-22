import view

def run():
    while True:
        view.my_menu()
        num = input("Выберите действие: ")
        match num:
            case '1': 
                model.show_child()
            case '2': 
                pass
            case '3': 
                pass
            case '4':
                exit()