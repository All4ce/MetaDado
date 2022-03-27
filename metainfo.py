import os
import sys

if (len(sys.argv)) <= 2:
    print("[*] Metodo de uso incorreto!\n--------------------------------------")
    print("[*] Utilize 2 argumentos\n--------------------------------------")
    print("[*] // [1] Alvo URL | [2] Arquivo // \n---------------------------------------")
    print("[*] Arquivos Sugeridos: pdf, xls, xlss, doc, docx, ppt, pptx\n------------------------------------")
    quit()
else:
    alvo = sys.argv[1]
    doc = sys.argv[2]
    num = 0
    os.system(f"lynx --dump 'https://google.com/search?&q=site:{alvo}+ext:{doc}' | grep .{doc} | cut -d '=' -f2 | egrep -v 'site|google' | sed 's/...$//' > filtro.txt")
    
    arq = open('filtro.txt', "r")
    linhas = arq.readlines()

    for url in linhas:
        os.system(f"wget -q {url}")
        num += 1

os.system(f"exiftool *.{doc}")

print(f"[*] ------- Encontrados e lidos {num} Arquivos! ------- [*]")
os.system(f"rm *.pdf*")

