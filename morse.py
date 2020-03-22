try:
	from colorama import Fore,Style, init as color_ama
	color_ama(autoreset=True)
	hijau = Style.BRIGHT+Fore.GREEN
	merah = Style.BRIGHT+Fore.RED
	kuning = Style.BRIGHT+Fore.YELLOW
	magenta = Style.BRIGHT+Fore.MAGENTA
	putih = Style.BRIGHT+Fore.WHITE
	biru = Style.BRIGHT+Fore.BLUE
	reset = Fore.RESET
	
except:
	print('colorama belum terinstall\npkg install colorama\ngunakan perintah diatas untuk menginstall colorama')
print(f"{magenta}▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇<=====================X=================>{reset}")
print(f"{magenta}▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇        HELLO WELCOME TO MY PROGRAM{reset}")
print(f"{magenta}▇▇▇▏{hijau}▃▆▅▎▅▆▃{magenta}▕▇▇▇ {reset}")
print(f"{magenta}▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇             MORSE CONVERTER{reset}")
print(f"{magenta}▇▇▇◣◣{hijau}▃▅▎▅▃{magenta}◢◢▇▇▇ {reset}")
print(f"{magenta}▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇ [+]CODE BY:Mr.D4NG3R404 (ADIPEBRIAN){reset}")
print(f"{magenta}▇▇▇▇▇◣╲{hijau}▇{magenta}╱◢▇▇▇▇▇ [+] CHAT ADMIN :082219324022 {reset}")
print(f"{magenta}▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇<=====================X=================> {reset}")




ime = input(f"{biru} MASUKAN TEXT YANG AKAN DI TERJEMAHKAN PADA SANDI MORSE: \n")

lngth = len(ime)

l = ""



print("ANDA MENULIS: " + ime)
for x in range(0, lngth):

    c = ime[x]

    c = c.upper()

    if (c == "A"):

        print(f"{hijau} .- | a\n")

    elif (c == "B"):

        print(f"{hijau} -... | b\n")

    elif (c == "C"):

        print(f"{hijau} -.-. | c\n")

    elif (c == "D"):

        print(f"{hijau} -.. | d\n")

    elif (c == "E"):

        print(f"{hijau} . | e\n")

    elif (c == "F"):

        print(f"{hijau} ..-. | f\n")

    elif (c == "G"):

        print(f"{hijau} --. | g\n")

    elif (c == "H"):

        print(f"{hijau} .... | h\n")

    elif (c == "I"):

        print(f"{hijau} .. | i\n")

    elif (c == "J"):

        print(f"{hijau} .--- | j\n")

    elif (c == "K"):

        print(f"{hijau} -.- | k\n")

    elif (c == "L"):

        print(f"{hijau} .-.. | l\n")

    elif (c == "M"):

        print(f"{hijau} -- | m\n")

    elif (c == "N"):

        print(f"{hijau} -. | n\n")

    elif (c == "O"):

        print(f"{hijau} --- | o\n")

    elif (c == "P"):

        print(f"{hijau} .--. | p\n")

    elif (c == "Q"):

        print(f"{hijau} --.- | q\n")

    elif (c == "R"):

        print(f"{hijau} .-. | r\n")

    elif (c == "S"):

        print(f"{hijau} ... | s\n")

    elif (c == "T"):

        print(f"{hijau} - | t\n")

    elif (c == "U"):

        print(f"{hijau} ..- | u\n")

    elif (c == "V"):

        print(f"{hijau} ...- | v\n")

    elif (c == "W"):

        print(f"{hijau} .-- | w\n")

    elif (c == "X"):

        print(f"{hijau} -..- | x\n")

    elif (c == "Y"):

        print(f"{hijau} -.-- | y\n")

    elif (c == "Z"):

        print(f"{hijau} --.. | z\n")

    elif (c == " "):

        print(f"{hijau} \n\n")

    elif (c == "!"):
        print(f"{merah} Not existing/translatable in morse code. | !\n")
    elif (c == "?"):
        print(f"{merah} ..--.. | ?\n")
    elif (c == "@"):
        print(f"{merah} .--.-. | @\n")
    elif (c == "/"):
        print(f"{merah} -..-. | /\n")
    elif (c == "."):
        print(f"{merah} .-.-.- | .\n")
    elif (c == ","):
        print(f"{merah} --..-- | ,\n")
    elif (c == "1"):
        print(f"{merah} .---- | 1\n")
    elif (c == "2"):
        print(f"{merah} ..--- | 2\n")
    elif (c == "3"):
        print(f"{merah} ...-- | 3\n")
    elif (c == "4"):
        print(f"{merah} ....- | 4\n")
    elif (c == "5"):
        print(f"{merah} ..... | 5\n")
    elif (c == "6"):
        print(f"{merah} -.... | 6\n")
    elif (c == "7"):
        print(f"{merah} --... | 7\n")
    elif (c == "8"):
        print(f"{merah} ---.. | 8\n")
    elif (c == "9"):
        print(f"{merah} ----. | 9\n")
    elif (c == "0"):
        print(f"{merah} ----- | 0\n")
        
        
print(f"{magenta}\n[✓]TERIMAKASIH SUDAH MENGGUNAKAN PROGRAM INI[✓]\n")

