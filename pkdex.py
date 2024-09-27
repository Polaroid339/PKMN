# nump = ["nome", hp, att, def, spa, spd, spe, lvl]

p1 = ["Bulbasaur", 45, 49, 49, 65, 65, 45, 1]
p2 = ["Ivysaur", 60, 62, 63, 80, 80, 60, 1]
p3 = ["Venusaur", 80, 82, 83, 100, 100, 80, 1]

currentp = p3
statstot = sum(currentp[1:7])

print(f"""
Nome: {currentp[0]}
HP: {currentp[1]}
Attack: {currentp[2]}
Defense: {currentp[3]}
Spe Att: {currentp[4]}
Spe Def: {currentp[5]}
Speed: {currentp[6]}
Total: {statstot}

Level: {currentp[7]}
""")
