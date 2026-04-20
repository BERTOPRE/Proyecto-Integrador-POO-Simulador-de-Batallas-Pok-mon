class Menu:

    @classmethod
    def mostrar_menu(cls):
        print("==========================================")
        print("SIMULADOR DE BATALLAS POKÉMON (POO)")
        print("==========================================")
        
        while True:
            print("Seleccione el modo de juego")
            print("1. Jugador vs Jugador")
            print("2. Jugador vs Computadora")
            print("3. Salir")
            
            try:
                opcion = int(input("Ingresa una opción: "))
                
                match opcion:
                    case 1:
                        print("Seleccionó la opción 1")
                        break
                    case 2: 
                        print("Seleccionó la opción 2")
                        break
                    case 3: 
                        print("Gracias por jugar")
                        break
                    case _:
                        print("Opción inválida\n")
                        
            except ValueError:
                print("Opción inválida, debe ser un número\n")