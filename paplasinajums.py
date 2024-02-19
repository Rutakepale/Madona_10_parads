def lasit_izdrukat(nosaukums, formāts):
    try:
        pilns_fails = f"{nosaukums}.{formāts}"


        with open(pilns_fails, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"Faila '{pilns_fails}' saturs:")
            print(saturs)


    except FileNotFoundError:
        print(f"Fails '{pilns_fails}' nav atrasts.")



    except Exception as e:
        print(f"radas kluda: {e}")



if __name__ == "__fails__":
    nosaukums = input(" faila nosaukums : ")
    formāts = input("fails ar paplašinājumu:")
    lasit_izdrukat(nosaukums, formāts)
