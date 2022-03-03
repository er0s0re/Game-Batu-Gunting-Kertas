import random
tebakan = 0
print("\nGAME BATU/GUNTING/KERTAS")
pemain = input("pilih salah satu diantara G (Gunting) /B (Batu) /K (kertas) or T untuk berhenti : ").upper()
while pemain != "T":
    tebakan += 1
    komputer = random.choice(["G","B","K"])
    if (pemain=="B" and komputer=="G") or (pemain=="G" and komputer=="K") or (pemain=="K" and komputer=="B"):
        print("\nkamu : ",pemain)
        print("komputer : ",komputer)
        print("Kamu menang")
    elif (pemain=="B" and komputer=="B") or (pemain=="G" and komputer=="G") or (pemain=="K" and komputer=="K"):
        print("\nkamu : ",pemain)
        print("komputer : ",komputer)
        print("kamu seri")
    elif (pemain=="B" and komputer=="K") or (pemain=="G" and komputer=="B") or (pemain=="K" and komputer=="G"):
        print("\nkamu : ",pemain)
        print("komputer : ",komputer)
        print("Kamu kalah")
    else:
        print("\nMaaf input yang anda masukkan salah")
    pemain = input("\npilih salah satu diantara ini G/B/K or T untuk berhenti : ").upper()
print("\nTotal tebakan : ",tebakan)
print("\nProgram finished")
