import csv, sys, re, os

def clean(string):
    """
    Limpa as frases, removendo espacos em excesso no final
    da frase e então adiciona ';' ao final para para 
    delimitar uma frase da outra
    """
    string = re.sub(r'[ ]*$', '', string)
    return re.sub(r'[;]*$',';', string)

def adapt(file, output):
    """
    adapta as frases para serem usadas pelo Anki, otimizando-as
    para que sejam convertidas razoavelmente bem para .csv
    """
    f = open(str(file), encoding="utf8")

    stripped = [line.strip(";") for line in f]
    split_l = [line.split('-') for line in stripped]
    nl = split_l

    # remove linhas extras e pontos-e-vírgulas das frases
    for index in range(len(nl)):
        for phrase_index in range(len(nl[index])):
            nl[index][phrase_index] = nl[index][phrase_index].replace("\n", "")
            nl[index][phrase_index] = nl[index][phrase_index].replace(";", '')

    # adiciona as frases a um arquivo .csv
    with open(output, mode="w+", encoding="utf8") as out:
        writer = csv.writer(out)
        writer.writerows(nl)

def convert(FILE_T):
    """
    Escolhe um arquivo, e flexibiliza seu título para criar arquivos temporários,
    aplicar as duas funcões acima, criando um arquivo .csv, e então deletando
    o arquivo temporário.
    """
    FILE = re.sub(r'[.txt]*$','', FILE_T) # verifica se o arquivo é .txt. Se for, remove a extensão
    target = open(FILE+".tmpfile",mode="w+", encoding="utf8") # cria arquivo temporário

    # tenta encontrar arquivo  com o nome escolhido. Retorna um erro caso não encontre.
    try:
        f = open(FILE, encoding="utf8")
    except FileNotFoundError:
        f = open(FILE+".txt", encoding="utf8")
    except:
        return -1

    # lê cada linha do arquivo e as altera conforme necessário, e então
    # às escreve no arquivo temporário
    fl = f.readlines()
    for x in fl:
        x = clean(x)
        target.write(x)

    # fecha os arquivos anteriormente abertos
    target.close()
    f.close()

    adapt(FILE+".tmpfile", FILE+".csv") 
    os.remove(FILE+".tmpfile") # deleta o arquivo temporário
