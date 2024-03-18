file_name = "./elenco-comuni-italiani.csv"

def load (fn:str):
    with open(fn, "r") as f:
        lines = f.readlines()

    print(lines[3:10])
    return [{'city': l[5], 'acronym': l[14]} for l in
            [s.strip().split(';') for s in lines [3:]]]

cities = load (file_name)
print (cities[:10])
print("QUante città in archivio?", len(cities))

print("Tutte le città in provincia di Roma:",
    len([x for x in cities if x ['acronym'] == 'RM']))
print("Quante città il cui nome inizia per A?",
    len([x for x in cities if x['city'].startswith('A')]))
print("Tutte le città inl cui nome inizia per 'bo':",
      [c for c in cities if c ['city'].lower().startswith('bo')])
