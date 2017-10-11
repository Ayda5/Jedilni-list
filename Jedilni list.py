# -*- encoding: utf-8 -*-

print "Program za vnos dnevnega menija."

jedilni_list = "meni.txt"
dnevni_meni = {}

while True:

    ime_jedi = raw_input("Vnesite ime jedi: ")
    cena_jedi = raw_input("Vnesite ceno jedi: ")
    dnevni_meni[ime_jedi] = cena_jedi
    print("Danes na meniju: " + ime_jedi + " " + str(cena_jedi)+"€")

    nadaljuj = raw_input("Želite vnesti še kakšno jed? Da/Ne ")
    print
    if nadaljuj.lower() == "ne":
        break

with open("meni.txt", "w+") as meni_file:
    for jed in dnevni_meni:
        meni_file.write("- " + ime_jedi + " : " + str(cena_jedi) + "€" + "\n")
