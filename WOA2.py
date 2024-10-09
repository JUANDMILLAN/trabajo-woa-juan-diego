import random, os

class Clan:
    cantidadMiembros = 0
    def __init__(self, nombre, fundador):
        self.miembros = []
        self.nombre = nombre
        self.fundador = fundador.nombre
        self.miembros.append(fundador)
        self.cantidadMiembros += 1
        
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
        self.cantidadMiembros += 1
        
    def listar_miembros(self):
        print()
        print("*** *** *** *** ***")
        print(f"The clan {self.nombre} has {self.cantidadMiembros} members")
        for miembro in self.miembros:
            print(miembro)

#***********************************************************************

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        #self.slot_pocion = slot_pocion = []
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        f"{self.nombre} has realized an attack!"
        damage = ((self.fuerza + self.ataque) / ((self.vida_original-self.puntos_vida) + self.vida_original)) / 10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        f"{self.nombre} has taking damage!"
        factor_damage = (self.defensa * damage) / 100
        self.fuerza = round(self.fuerza / (factor_damage + 1))
        self.puntos_vida = round(self.puntos_vida / (factor_damage + 1))
        self.defensa = round(self.defensa / (factor_damage + 1))
        self.ataque = round(self.ataque / (factor_damage + 1))

        if self.puntos_vida > 0:
            print(f"{self.nombre} has received an attack hit points = {self.puntos_vida}")
        else:
            print(f"El {self.titulo} {self.nombre} has died")

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Strength: {self.fuerza},live points: {self.puntos_vida}, "
                f"Defense: {self.defensa}, Stroke: {self.ataque}, "
                f"Clan: {self.clan}")
        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre, titulo = "Warrior"):
        super().__init__(nombre, titulo)
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Wizard"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida

#***********************************************************************

class Arquero(Personaje):
    def __init__(self, nombre, titulo = "Archer"):
        super().__init__(nombre, titulo)
        self.fuerza = 95
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 120
        self.vida_original = self.puntos_vida

#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Founder")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        print(f"{self.nombre} Has founded a clan.")
        
#***********************************************************************


#--INICIO FUNCIONES--

def crearGuerrero(titulo):
    nombre = input(f"Name of {titulo}: ").upper()
    guerrero = Guerrero(nombre)
    guerreros.append(guerrero)
    return guerrero

def crearMago(titulo):
    nombre = input(f"Name of {titulo}: ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearArquero(titulo):
    nombre = input(f"Name of {titulo}: ").upper()
    arquero = Arquero(nombre)
    arqueros.append(arquero)
    return arquero

def crearFundador(mago):
    print("Your destiny is to be a founder in these wastelands of Pythonias...")
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("clan's name: ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)

def seleccionarClan(personaje):
    asignado = False
    while not asignado:
        for index, clan in enumerate(clanes):
            print(f"{index+1} : {clan.nombre}")
        print()
        nombreClan = input("Enter the name of the clan -> ").upper()
        for clan in clanes:
            if clan.nombre == nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                input(f"{personaje.nombre} Has been added to the clan {clan.nombre} <ENTER TO CONTINUE>")
                asignado = True
        if asignado == False:
            print(f"El clan {nombreClan} no existe...")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros):
    print("-- Selection mode --")
    print("-- Select your target --")
    print("1. By clan.")
    print("2. List all characters.")
    print("3. Attack by title.")
    opcion = int(input("Choose an option: "))
    
    if opcion == 1:
        print("clan list")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Select clan number: ")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            print(f"clan members {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("Enter the name of your target: ").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("Invalid clan")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros + arqueros
        print("list of all characters")
        for miembro in listaPersonajes:
            print(miembro)
            print()
        nombreObjetivo = input("Enter the name of your target: ").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        print("Title to list")
        print("1. Founders")
        print("2. Wizards")
        print("3. Warriors")
        print("4. Archers")
        tipo = int(input("Enter your option: "))
        if tipo == 1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        elif tipo == 4:
            listaObjetivos = arqueros
        print("Characters:")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("Enter the name of your target: ").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    print("Invalid option")
    return None


def organizarTurno(lst_pjs):
    input("The characters' turn will be selected at random\n<ENTER TO CONTINUE> ")
    limpiar_consola()
    turnos_ordenados = lst_pjs[:]
    random.shuffle(turnos_ordenados)
    
    print("This will be the order of turns per player: ")
    for index, pj in enumerate(turnos_ordenados):
        print(f"{index+1} | Title: {pj.titulo} | Name: {pj.nombre}")
    return turnos_ordenados

#--FIN FUNCIONES--

#--INICIO PROCEDIMIENTOS--

def listarTodoElStaff():
    global lista_personajes
    #Agregar a lista_personajes todos las clases según se vayan creando
    lista_personajes = fundadores + magos + guerreros + arqueros
    print("List of all the characters present in the game: ")
    print("--***---***--***---***--***---***")
    for pj in lista_personajes:
        print(pj.nombre)
    print("--***---***--***---***--***---***")
    print()

def limpiar_consola():
    os.system("cls") if os.name == "nt" else os.system("clear")

#--FIN PROCEDIMIENTOS--

#--INICIO ARREGLOS--

guerreros = []
magos = []
arqueros = []
fundadores = []
clanes = []

lista_personajes = fundadores + magos + guerreros + arqueros

#--FIN ARREGLOS

#INICIO CÓDIGO PRINCIPAL

cantidadJugadores = int(input("Number of players: "))
limpiar_consola()
for i in range(cantidadJugadores):
    if i == 0:
        mago = crearMago("Founder")
        fundador = crearFundador(mago)
        crearClan(fundador)
        limpiar_consola()
    else:
        print()
        print(f"Choosing the player class {i+1}/{cantidadJugadores}: ")
        
        opcionPersonaje = int(input("1.Warrior\n2.Mage\n3.Archer\nOption: "))
        if opcionPersonaje == 1:
            guerrero = crearGuerrero("Warrior")
            seleccionarClan(guerrero)
            limpiar_consola()
        elif opcionPersonaje == 2:
            mago = crearMago("wizard")
            opcionCrearClan = int(input("Do you want to create your own clan?\n1. YES\n2. NO\nOption: "))
            if opcionCrearClan == 1:
                fundador = crearFundador(mago)
                crearClan(fundador)
                limpiar_consola()
            else:
                seleccionarClan(mago)
        elif opcionPersonaje == 3:
            arquero = crearArquero("Archer")
            seleccionarClan(arquero)
            limpiar_consola()


listarTodoElStaff()

turnos_ordenados = organizarTurno(lista_personajes)

limpiar_consola()

cont_turnos = 0

for pj in turnos_ordenados:
    cont_turnos += 1
    print(f"*** turn: {cont_turnos} ***")
    print(f"It's the turn of {pj.titulo} | {pj.nombre}")
    objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros, arqueros)
    print("--Choose an option --")
    if pj.titulo == "Founder":
        print("1. Attack.")
        print("2. Create potions. (NOT IMPLEMENTED)")
        print("3. Deliver potions. (NOT IMPLEMENTED)")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Warrior":
        print("1. Attack.")
        print("2. Defend. (NOT IMPLEMENTED)")
        print("3. Sword dance. (NOT IMPLEMENTED)")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Wizard":
        print("1. Attack.")
        print("2. Heal. (NOT IMPLEMENTED)")
        print("3. Meteorite storm ☄")
        opc = int(input("Option: "))
        if opc == 1:
            pj.realizar_ataque(objetivo)
    elif pj.titulo == "Archer":
        print("1. Attack.")
        print("2. Accurate crush. (NOT IMPLEMENTED)")
        print("3. arrow storm. (NOT IMPLEMENTED)")
        if opc == 1:
            pj.realizar_ataque(objetivo)
        opc = int(input("Option: "))
    print(objetivo)