import random #Importerer library random som gir meg muligheten til å velge et tilfeldig objekt fra en array
from words import wordlist #Importerer wordlist arrayen i words.py filen
from termcolor import colored #Importerer library Termcolor som gir meg muligheten til å farge ord

chosenword = random.choice(wordlist) #Velger tilfelig ord fra ordlisten

allowed_guesses = 6 #Mengde forsøk du starter med

#Introduksjon til spillet
print("************ORDLEK************") #Det er 12 stjerner på hver side
print("Ordet skal inneholde maksimalt 4 bokstaver")
print("Hvis en bokstav lyser", colored("gult,", 'yellow'), "vil det si at bokstaven er i ordet, men er feil plassert")
print("Hvis bokstaven lyser", colored("grønt,", 'green'), "vil det si at bokstaven er i ordet og riktig plassert")
print("Hvis ordet lyser", colored("rødt,", 'red'), "vil det si at hele ordet er feil")

#Sjekker om ordet er riktig og hvis det er riktig stop programmet
def check_brukerord(brukerord):
    if brukerord == chosenword:
        print("Du har gjettet riktig ord. Ordet var", colored(chosenword, 'green'))
        exit()

#En løkke som sier så lenge du har mer en 0 forsøk skal koden kjøre

while allowed_guesses > 0:
    brukerord = input("Sriv et ord på 4 bokstaver").upper()
    check_brukerord(brukerord)
    if len(brukerord) > 4 or len(brukerord) < 4: #Hvis ordet du skriver inn er mer eller mindre enn 4 bokstaver skal den ikke kjøre koden under
        print("Ordet må være 4 bokstaver")
    else:
        for bokstav in range(0, len(brukerord)):  
            if brukerord[0] == chosenword[0]: #Bokstav 1 i ordet som er riktig plassert
                print(colored(brukerord[0], 'green') + brukerord[1] + brukerord[2] + brukerord[3])
            if brukerord[1] == chosenword[1]: #Bokstav 2 i ordet som er riktig plassert
                print(brukerord[0] + colored(brukerord[1], 'green') + brukerord[2] + brukerord[3])  
            if brukerord[2] == chosenword[2]: #Bokstav 3 i ordet som er riktig plassert
                print(brukerord[0] + brukerord[1] + colored(brukerord[2], 'green') + brukerord[3]) 
            if brukerord[3] == chosenword[3]: #Bokstav 4 i ordet som er riktig plassert
                print(brukerord[0] + brukerord[1] + brukerord[2] + colored(brukerord[3], 'green'))
                
            #Bokstav 1 i ordet som er feil plassert
            if brukerord[1] == chosenword[0]:
                print(brukerord[0] + colored(brukerord[1], 'yellow') + brukerord[2] + brukerord[3])  
            if brukerord[2] == chosenword[0]:
                print(brukerord[0] + brukerord[1] + colored(brukerord[2], 'yellow') + brukerord[3])  
            if brukerord[3] == chosenword[0]:
                print(brukerord[0] + brukerord[1] + brukerord[2] + colored(brukerord[3], 'yellow'))   

            #Bokstav 2 i ordet som er feil plassert
            if brukerord[0] == chosenword[1]:
                print(colored(brukerord[0] + 'yellow'), brukerord[1] + brukerord[2] + brukerord[3])  
            if brukerord[2] == chosenword[1]:
                print(brukerord[0] + brukerord[1] + colored(brukerord[2], 'yellow') + brukerord[3])  
            if brukerord[3] == chosenword[1]:
                print(brukerord[0] + brukerord[1] + brukerord[2] + colored(brukerord[3], 'yellow'))   
                
            #Bokstav 3 i ordet som er feil plassert
            if brukerord[1] == chosenword[2]:
                print(brukerord[0] + colored(brukerord[1], 'yellow') + brukerord[2] + brukerord[3])  
            if brukerord[3] == chosenword[2]:
                print(brukerord[0], brukerord[1] + brukerord[2] + colored(brukerord[3], 'yellow'))  
            if brukerord[0] == chosenword[2]:
                print(colored(brukerord[0], 'yellow') + brukerord[1] + brukerord[2] + brukerord[3])   
                
            #Bokstav 4 i ordet som er feil plassert
            if brukerord[0] == chosenword[3]:
                print(colored(brukerord[0], 'yellow') + brukerord[1] + brukerord[2] + brukerord[3])  
            if brukerord[1] == chosenword[3]:
                print(brukerord[0] + colored(brukerord[1], 'yellow') + brukerord[2] + brukerord[3])  
            if brukerord[2] == chosenword[3]:
                print(brukerord[0] + brukerord[1] + colored(brukerord[2], 'yellow') + brukerord[3])   

            if brukerord != chosenword: #Trekker fra forsøk etter hver gang du gjetter feil
                print(colored(brukerord, 'red'))
                allowed_guesses = allowed_guesses -1
                print("Du har", allowed_guesses, "forsøk igjen")
                if allowed_guesses <= 0: #Hvis du har brukt opp forsøkene dine skal programmet si hva dagens ord var og skrive det ur i grønt
                    print("Ordet var", colored(chosenword, 'green'))

                break