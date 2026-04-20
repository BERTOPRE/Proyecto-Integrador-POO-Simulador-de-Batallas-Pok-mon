class Menu:
    def mostrar_menu(self):
        while True:
            print("==========================================")
            print("SIMULADOR DE BATALLAS POKÉMON (POO)")
            print("==========================================")
            print("1. Seleccione el modo de juego")
            print("2. Jugador vs Jugador")
            print("3. Jugador vs Computadora")
            print("4. Salir")
            
            try:
                opcion = int(input("Ingresa una opción: "))
                return opcion
            except ValueError:
                print("Opción inválida, intenta de nuevo\n")