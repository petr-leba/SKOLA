import sys
import random
print("Šibenice")
guessing_words=["být","který","mít","jeho","ale","svůj","jako","moci","rok","pro","tak","po","tento","když","všechen","jak","aby","od","nebo","říci","jeden","jen","můj","jenž","člověk","ty","stát","u","muset","velký","chtít","také","až","než","ještě","při","jít","pak","před","dva","však","ani","vědět","nový","hodně","podle","další","celý","jiný","první","mezi","dát","tady","den","tam","kde","doba","každý","druhý","místo","dobrý","takový","strana","protože","nic","začít","něco","život","vidět","říkat","země","dítě","malý","ne","sám","bez","ruka","či","svět","dostat","práce","nějaký","proto","pod","tři","kdy","město","přijít","dobře","žena","muž","teď","kdo","již","nad","asi","starý","například","případ","vysoký","žádný","společnost","několik","některý","tedy","cesta","pokud","dělat","hlava","čas","poslední","oko","právě","tvůj","Praha","věc","voda","český","proti","velmi","jaký","přes","dům","dnes","pan","část","třeba","kdyby","brzy","lze","firma","oba","slovo","tenhle","vlastní","nikdy","koruna","možný","chvíle","udělat","pouze","proč","systém","konec","kolem","málo","myslit","stejně","-li","Český","moc","problém","milión","nikdo","stále","totiž","někdo","tisíc","vůbec","zákon","nechat","najít","což","cena","rád","škola","hlavní","skupina","mladý","způsob","často","řada","jediný","mluvit","vrátit","různý","hrát","snad","zůstat","vzít","dlouhý","čekat","patřit","oblast","vláda","dokonce","známý","dokázat","peníze","mnoho","otázka","vést","právo","spíše","pozdě","žít","zase","především","ovšem","takže","století","přece","možnost","ostatní","číslo","jenom","dále","uvést","znovu","možná","služba","jestli","situace","stejný","hodiny","měsíc","získat","čtyři","jméno","dveře","daleko","otec","znát","změna","evropský","většina","nakonec","nyní","noc","snažit","se","síla","zde","dojít","potom","znamenat","vypadat","pět","informace","americký","trochu","týden","důležitý","příliš","vztah","trh","tělo","válka","hned","slyšet","téměř","dlouho","rodina","zatím","rozhodnout","výsledek","ano","pracovat","státní","pohled","zájem","zeptat","se","ulice","potřebovat","tvář","zdát","se","kniha","důvod","hlas","film","pravda","někdy","objevit","dost","základní","zcela","přitom","paní","smrt","matka","sice","rychle","cítit","minuta","pár","procento","program","určitý","večer","během","existovat","kvůli","hodnota","bílý","noha","jistý","jednou","podívat","se","včera","plný","člen","vlastně","lidský","sedět","podmínka","vždy","navíc","osoba","hra","počet","tehdy","republika","přímo","stav","banka","politický","hodina","obraz","zejména","ať","činnost","podnik","jinak","druh","soud","opět","národní","úřad","podobný","deset","kromě","nejen","auto","ukázat","černý","zda","platit","špatný","otevřít","vždycky","dávat","cíl","psát","chodit","jednotlivý","sociální","považovat","současný","Evropa","neboť","Jan","zpráva","typ","policie","stačit","opravdu","skutečnost","věřit","pocit","dílo","silný","sto","spolu","německý","vedle","tvrdit","základ","pořád","bůh","prostředí","samozřejmě","jet","zřejmě","zjistit","světlo","smysl","směr","růst","ředitel","ráno","zatímco","myslet","láska","divadlo"]
guessed_letters=[]
hidden_guess=random.choice(guessing_words)
listed_guess=list(hidden_guess)
hangman_progress=0
guess_progress=[]
guess_prog_str=""
čísla={}
correct_guess=0

for ffe in range(len(listed_guess)):
    guess_progress.append("_")

#print(hidden_guess)

while(True): 
    guess=input("Zadejte vaše zvolené písmeno nebo celé slovo: ")
    if guess in listed_guess:
        place=listed_guess.index(guess)
        guess_progress[int(place)]=guess
        correct_guess+=1
    elif guess == hidden_guess:
        print("vyhrál jsi")
        exit()
    elif len(guess)==1:
        print("špatně")
        hangman_progress+=1
        guessed_letters.append(guess)
    else:
        print("špatně")
        hangman_progress+=1        

    if hangman_progress == 10:
        print("prohrál jsi")

    if correct_guess == len(hidden_guess):
        print("vyhrál jsi")
        exit()
    guess_prog_str = ''.join(guess_progress)
    guessed_letters_str = ''.join(guessed_letters)
    print(guess_prog_str)
    print(guessed_letters_str)  
    if hangman_progress == 0:
        print("                          ")
        print("                          ")
        print("                          ")
        print("                          ")
        print("                          ")
        print("                          ")
        print("                          ")
    if hangman_progress == 1:
        print("                          ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 2:
        print("     __________           ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 3:
        print("     __________           ")
        print("     | /                  ")
        print("     |/                   ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 4:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/                   ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 5:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 6:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |        |           ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 7:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |       /|           ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 8:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |       /|\          ")
        print("     |                    ")
        print("     |                    ")
        print("     |                    ")
    elif hangman_progress == 9:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |       /|\          ")
        print("     |       /            ")
        print("     |                    ")
        print("     |                    ")
    else:
        print("     __________           ")
        print("     | /      |           ")
        print("     |/       O           ")
        print("     |       /|\          ")
        print("     |       / \          ")
        print("     |                    ")
        print("     |                    ")
        print("Slovo bylo: "+hidden_guess)
        exit()