import os

# nump = ["nome", hp, att, def, spa, spd, spe, lvl, shiny]

pks = {1: ["Bulbasaur", ["Grass"], 45, 49, 49, 65, 65, 45, 100, False, [None, None, None, None]],
       2: ["Ivysaur", ["Grass"], 60, 62, 63, 80, 80, 60, 1, False, [None, None, None, None]],
       3: ["Venusaur", ["Grass", "Poison"], 80, 82, 83, 100, 100, 80, 1, False, [None, None, None, None]]}


def stats(pkmn):
    print(f"""
Nome: {pkmn[0]}
Tipo: {pkmn[1][0:]}

HP: {pkmn[2] + pkmn[8]}
Attack: {pkmn[3] + pkmn[8]}
Defense: {pkmn[4] + pkmn[8]}
Sp Atk: {pkmn[5] + pkmn[8]}
Sp Def: {pkmn[6] + pkmn[8]}
Speed: {pkmn[7] + pkmn[8]}
Total: {sum(pkmn[2:8])}

Move 1:{pkmn[10][0]}
Move 2:{pkmn[10][1]}
Move 3:{pkmn[10][2]}
Move 4:{pkmn[10][3]}

Level: {pkmn[8]}
Nota: {sum(pkmn[2:8]) // len(pkmn[2:8])}
Shiny: {pkmn[9]}
""")


def pokedex():
    while True:
        print("\nBem vindo a Pokédex!")
        print("""
[1] Todos os Pokémons
[2] Pesquisar por Pokémon
[3] Sair
""")
        opcao = input("Digite a opção: ")
        os.system('cls')

        match opcao:
            case "1":
                for x, y in pks.items():
                    print(f"{x}: {y[0]}")

            case "2":
                search = input(
                    "Digite o nome do Pokémon que quer pesquisar: ").title().strip()

                for x in pks.items():
                    if search == x[0]:
                        stats(pks[x])

            case "3":
                break

            case _:
                os.system('cls')


pokedex()
