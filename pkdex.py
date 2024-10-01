# nump = ["nome", hp, att, def, spa, spd, spe, lvl, shiny]

p1 = ["Bulbasaur", 45, 49, 49, 65, 65, 45, 100, False]
p2 = ["Ivysaur", 60, 62, 63, 80, 80, 60, 1, False]
p3 = ["Venusaur", 80, 82, 83, 100, 100, 80, 1, False]


def stats(pkmn):
    print(f"""
Nome: {pkmn[0]}
HP: {pkmn[1] + pkmn[7]}
Attack: {pkmn[2] + pkmn[7]}
Defense: {pkmn[3] + pkmn[7]}
Sp Atk: {pkmn[4] + pkmn[7]}
Sp Def: {pkmn[5] + pkmn[7]}
Speed: {pkmn[6] + pkmn[7]}
Total: {sum(pkmn[1:7])}

Level: {pkmn[7]}
Nota: {sum(pkmn[1:7]) // len(pkmn[1:7])}
Shiny: {pkmn[8]}
""")


stats(p1)
