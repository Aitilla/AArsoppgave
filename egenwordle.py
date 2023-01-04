import random #Importerer library random som gir meg muligheten til å velge et tilfeldig objekt fra en array
from words import wordlist #Importerer wordlist arrayen i words.py filen
from termcolor import colored #Importerer library Termcolor som gir meg muligheten til å farge ord
import mysql.connector

mydb = mysql.connector.connect(
    host="10.2.2.13",
    user="wordleDB",
    password="raring123",
    database="wordle"
)

chosenword = random.choice(wordlist) #Velger tilfelig ord fra ordlisten


#Startmeny hvor du skal bestemme om du skal spille, sjekke leaderboard, lage eller logge inn på en bruker eller avslutte programmet
#OBS det er ikke mulig å lage brukere eller logge inn enda

def printMeny():
    print("-------------------ORDLEK-------------------")
    print("| 1. Play                                  |")
    print("| 2. Leaderboard                           |")
    print("| 3. Logg inn                              |")
    print("| 4. Create account                        |")
    print("| 5. Exit                                  |")
    print("--------------------------------------------")
    menyvalg = input("Skrin inn tall for å velge fra menyen:")
    utfoerMenyvalg(menyvalg)

#Her bestemmes hvor du skal sendes 
def utfoerMenyvalg(valgtall):
    if(valgtall < "1" or valgtall > "5"):
        print("Skriv et tall mellom 1 og 5")
        printMeny()
    else:
        if(valgtall == "1"):
            play()
        elif(valgtall == "2"):
            leaderboard()
        elif(valgtall == "3"):
            print("rar")
        elif(valgtall == "4"):
            print("rar")
        elif(valgtall == "5"):
            print("Du har nå avsluttet programmet")
            exit()

#Hvis ordet du gjetter er riktig, stopper programmet og printer at du gjettet korrekt
def check_brukerord(brukerord):
    if brukerord == chosenword:
        print("Du har gjettet riktig ord. Ordet var", colored(chosenword, 'green'))
        exit()

def play():
    #Introduksjon til spillet
    print("************ORDLEK************") #Det er 12 stjerner på hver side
    print("Ordet skal inneholde maksimalt 4 bokstaver og du har 6 forsøk på å gjette ordet")
    print("Hvis en bokstav lyser", colored("gult,", 'yellow'), "vil det si at bokstaven er i ordet, men er feil plassert")
    print("Hvis bokstaven lyser", colored("grønt,", 'green'), "vil det si at bokstaven er i ordet og riktig plassert")
    print("Hvis ordet lyser", colored("rødt,", 'red'), "vil det si at hele ordet er feil")
    
    allowed_guesses = 6 #Mengde forsøk du starter med

    #En løkke som sier så lenge du har mer en 0 forsøk skal koden kjøre
    while allowed_guesses > 0:
        brukerord = input("Sriv et ord på 4 bokstaver").upper()
        check_brukerord(brukerord)
        if len(brukerord) > 4 or len(brukerord) < 4: #Hvis ordet du skriver inn er mer eller mindre enn 4 bokstaver skal den ikke kjøre koden under
            print("Ordet må være 4 bokstaver")
        else:
            for x in range(0, len(brukerord)):  
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
                    print(brukerord[0] + brukerord[1] + brukerord[2] + colored(brukerord[3], 'yellow'))  
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

                    break #Stopper loopen sånn at den bare går en gang

#Hvis du skriver "2" printes highscores
#OBS den er ikke fult optimal, men det funker
def leaderboard():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT id, points, user FROM attemps")

    highscores = mycursor.fetchall()
    print(highscores)


printMeny()