f = open('forex10.txt', 'r')
txt = f.read()
x = ' '.join(bin(letter)[2:].zfill(7) for letter in txt.encode('UTF-8'))
x = list(x)
lista = list(x[:])
k = 2
y = len(lista)

#Calculate number of spaces
plithos = 0
for keno in lista:
    if keno == " ":
        plithos += 1

#Keep first two and last two bits from every element
sinolo = (y - plithos)//7
for i in range(sinolo):
    for j in range(3):
        lista.pop(k)
    k += 5

#Removing spaces in list
for stoixeio in lista:
    if stoixeio == " ":
        lista.remove(stoixeio)

#New string for the following
string = ""
for element in lista:
    string += element
print("The following is: " + str(string))
nealista = []
arithmos = ""
orio = 1
#Separate by 16bit
for element in string:
    if orio <=16:
        arithmos += element
        orio +=1
    else:
        nealista.append(arithmos)
        arithmos = ""
        orio = 1
print("Hexademical numbers: " +str(nealista))
mikosneaslistas = len(nealista)
#Stats
plithos_zigwn = 0
plithos_akribwsmetotria = 0
plithos_akribwsmetopente = 0
plithos_akribwsmetoefta = 0
for elem in nealista:
    dec = int(elem,16)
    if dec % 2 == 0:
        plithos_zigwn += 1
    if dec % 3 == 0:
        plithos_akribwsmetotria += 1
    if dec % 5 == 0:
        plithos_akribwsmetopente += 1
    if dec % 7 == 0:
        plithos_akribwsmetoefta += 1

#Output
posostozigwn = round(((plithos_zigwn/mikosneaslistas) * 100),2)
posostometotria = round(((plithos_akribwsmetotria/mikosneaslistas) * 100),2)
posostometopente = round(((plithos_akribwsmetopente/mikosneaslistas) * 100),2)
posostometoefta = round(((plithos_akribwsmetoefta/mikosneaslistas) * 100),2)
print("Percentage of even numbers: " + str(posostozigwn) + " %")
print("Percentage of numbers that are devided by 3: " + str(posostometotria) + " %")
print("Percentage of numbers that are devided by 5: " + str(posostometopente) + " %")
print("Percentage of numbers that are devided by 7: " + str(posostometoefta) + " %")
f.close()




