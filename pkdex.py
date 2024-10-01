# nump = ["nome", hp, att, def, spa, spd, spe, lvl, shiny]

p1 = ["Bulbasaur", 45, 49, 49, 65, 65, 45, 100, False]
p2 = ["Ivysaur", 60, 62, 63, 80, 80, 60, 1, False]
p3 = ["Venusaur", 80, 82, 83, 100, 100, 80, 1, False]

currentp = p1

statstot = sum(currentp[1:7])
nota = sum(currentp[1:7]) // len(currentp[1:7])

print(f"""
Nome: {currentp[0]}
HP: {currentp[1]+currentp[7]}
Attack: {currentp[2]+currentp[7]}
Defense: {currentp[3]+currentp[7]}
Spe Att: {currentp[4]+currentp[7]}
Spe Def: {currentp[5]+currentp[7]}
Speed: {currentp[6]+currentp[7]}
Total: {statstot}

Level: {currentp[7]}
Nota: {nota}
Shiny: {currentp[8]}
""")
