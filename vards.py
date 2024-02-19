def ievadit_ierakstit(vards):

    try:
        with open("pp.txt", 'w', encoding='utf-8') as fails:
            fails.write(vards)
        print("vards veiksmigi ierakstits faila 'pp.txt'.")


    except IOError as e:
        print(f"kluda rakstot failu: {e}")


    except Exception as e:
        print(f"radas kluda: {e}")


if __name__ == "__main__":
    lietotaja_vards = input("Ievadiet savu vārdu: ")
    ievadit_ierakstit(lietotaja_vards)
