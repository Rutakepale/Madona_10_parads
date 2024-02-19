def lasit_failu(ceļš):


    try:
        with open(ceļš, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(saturs)



    except FileNotFoundError:
        print(f"Fails '{ceļš}' nav atrasts.")



    except Exception as e:
        print(f"Radās kļūda: {e}")



if __name__ == "__main__":
    faila_ceļš = input("lai Tev skaista diena šodien: ")
    lasit_failu(faila_ceļš)

    import csv

def lasit_csv_failu(ceļš):
    try:
        with open(ceļš, 'r', newline='', encoding='utf-8') as csv_fails:
            csv  = csv.reader(csv_fails)
            
           
            for rindina in csv:
                if len(rindina) >= 4:
                    ceturta_kolonna = rindina[3]
                    print(ceturta_kolonna)


                else:
                    print("lai Tev skaista siena šodien.")
    except FileNotFoundError:
        print(f"Fails '{ceļš}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")


if __name__ == "__main__":
    csv_faila_ceļš = input("lai Tev skaista diena šodien: ")
    lasit_csv_failu(csv_faila_ceļš)



def lasit_rindas(ceļš):
    try:
        with open(ceļš, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            
           
            if len(rindas) >= 4:
                tresa_rinda = rindas[2].strip()  
                ceturta_rinda = rindas[3].strip()
                
                print("tresa rinda:", tresa_rinda)
                print("ceturta rinda:", ceturta_rinda)
            else:
                print(" nav pietiekami daudz rindu faila.")
    except FileNotFoundError:
        print(f"fails '{ceļš}' nav atrasts.")


    except Exception as e:
        print(f"Radās kļūda: {e}")


if __name__ == "__main__":
    faila_ceļš = input("lai Tev skaista diena šodien: ")
    lasit_rindas(faila_ceļš)
