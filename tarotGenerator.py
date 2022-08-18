
import random
import urllib
from urllib.request import urlopen


def checkNum(num):
    
    #print("looping", num)
    sum = 0
    for n in num:
        b = n.isdigit()
        if b == False:
            num = input("Invalid entry. Choose numbers only.\nPick a number: ")
            return num
        sum+=int(n)

    #print("returning", sum)   
    return str(sum) 


print("\nWelcome to the Oracle.")
question = input("What is your question?: ")
num = input("Pick a number: ")

while len(num)!=1:
    num = checkNum(num)

#print("s ",num)
if num == "0":
    num = 1

for i in range(int(num)):
    card= random.randint(0,77)
#print("Debug: Number", card)

def majorArcana(number): 
    if number==0    :
        print("Your card is: The Fool")
        link="the-fool"
    if number==1	:
        print("Your card is: The Magician")
        link="the-magician"
    if number==2	:    
        print("Your card is: The High Priestess")
        link="the-high-priestess"
    if number==3	:
        print("Your card is: The Empress")
        link="the-empress"
    if number==4	:
        print("Your card is: The Emperor")
        link="the-emperor"
    if number==5	:
        print("Your card is: The Hierophant")
        link="the-hierophant"
    if number==6	:
        print("Your card is: The Lovers")
        link="the-lovers"
    if number==7	:
        print("Your card is: The Chariot")
        link="the-chariot"
    if number==8	:
        print("Your card is: Strength")
        link="strength"
    if number==9	:
        print("Your card is: The Hermit")
        link="the-hermit"
    if number==10	:
        print("Your card is: Wheel of Fortune")
        link="the-wheel-of-fortune"
    if number==11	:
        print("Your card is: Justice")
        link="justice"
    if number==12	:
        print("Your card is: The Hanged Man")
        link="the-hanged-man"
    if number==13	:
        print("Your card is: Death")
        link="death"
    if number==14	:
        print("Your card is: Temperance")
        link="temperance"
    if number==15	:
        print("Your card is: The Devil")
        link="the-devil"
    if number==16	:
        print("Your card is: The Tower")
        link="the-tower"
    if number==17	:
        print("Your card is: The Star")
        link="the-star"
    if number==18	:
        print("Your card is: The Moon")
        link="the-moon"
    if number==19	:
        print("Your card is: The Sun")
        link="the-sun"
    if number==20	:
        print("Your card is: Judgement")
        link="judgement"
    if number==21	:
        print("Your card is: The World")
        link="the-world"

    return link


def minorArcana(card):

    if 22<=card<36:
        c = card - 21
        if c == 14:
            print("Your card is King of Wands")
            link="king-of-wands"
        elif c == 13:
            print("Your card is Queen of Wands")
            link="queen-of-wands"
        elif c == 12:
            print("Your card is Knight of Wands")
            link="knight-of-wands"
        elif c == 11:
            print("Your card is Page of Wands")
            link="page-of-wands"
        else:
            if c==1:
                print("Your card is Ace of Wands")
                link="ace-of-wands"
            else: 
                print("Your card is ",c," of Wands")
                if c==2: 
                    link="two-of-wands"
                elif c==3: 
                    link="three-of-wands"
                elif c==4: 
                    link="four-of-wands"
                elif c==5: 
                    link="five-of-wands"
                elif c==6: 
                    link="six-of-wands"
                elif c==7: 
                    link="seven-of-wands"
                elif c==8: 
                    link="eight-of-wands"
                elif c==9: 
                    link="nine-of-wands"
                else:
                    link="ten-of-wands"


    elif 36<=card<50:
        c = card - 35
        if c == 14:
            print("Your card is King of Cups")
            link="king-of-cups"
        elif c == 13:
            print("Your card is Queen of Cups")
            link="queen-of-cups"
        elif c == 12:
            print("Your card is Knight of Cups")
            link="knight-of-cups"
        elif c == 11:
            print("Your card is Page of Cups")
            link="page-of-cups"
        else:
            if c==1:
                print("Your card is Ace of Cups")
                link="ace-of-cups"
            else: 
                print("Your card is ",c," of Cups")
                if c==2: 
                    link="two-of-cups"
                elif c==3: 
                    link="three-of-cups"
                elif c==4: 
                    link="four-of-cups"
                elif c==5: 
                    link="five-of-cups"
                elif c==6: 
                    link="six-of-cups"
                elif c==7: 
                    link="seven-of-cups"
                elif c==8: 
                    link="eight-of-cups"
                elif c==9: 
                    link="nine-of-cups"
                else:
                    link="ten-of-cups"

    elif 50<=card<64:
        c = card - 49
        if c == 14:
            print("Your card is King of Swords")
            link="king-of-swords"
        elif c == 13:
            print("Your card is Queen of Swords")
            link="queen-of-swords"
        elif c == 12:
            print("Your card is Knight of Swords")
            link="knight-of-swords"
        elif c == 11:
            print("Your card is Page of Swords")
            link="page-of-swords"
        else:
            if c==1:
                print("Your card is Ace of Swords")
                link="ace-of-swords"
            else: 
                print("Your card is ",c," of Swords")
                if c==2: 
                    link="two-of-swords"
                elif c==3: 
                    link="three-of-swords"
                elif c==4: 
                    link="four-of-swords"
                elif c==5: 
                    link="five-of-swords"
                elif c==6: 
                    link="six-of-swords"
                elif c==7: 
                    link="seven-of-swords"
                elif c==8: 
                    link="eight-of-swords"
                elif c==9: 
                    link="nine-of-swords"
                else:
                    link="ten-of-swords"
                
    else: # cards 64 - 77, including 77.
        c = card - 63
        if c == 14:
            print("Your card is King of Pentacles")
            link="king-of-pentacles"
        elif c == 13:
            print("Your card is Queen of Pentacles")
            link="queen-of-pentacles"
        elif c == 12:
            print("Your card is Knight of Pentacles")
            link="knight-of-pentacles"
        elif c == 11:
            print("Your card is Page of Pentacles")
            link="page-of-pentacles"
        else:
            if c==1:
                print("Your card is Ace of Pentacles")
                link="ace-of-pentacles"
            else: 
                print("Your card is ",c," of Pentacles")
                if c==2: 
                    link="two-of-pentacles"
                elif c==3: 
                    link="three-of-pentacles"
                elif c==4: 
                    link="four-of-pentacles"
                elif c==5: 
                    link="five-of-pentacles"
                elif c==6: 
                    link="six-of-pentacles"
                elif c==7: 
                    link="seven-of-pentacles"
                elif c==8: 
                    link="eight-of-pentacles"
                elif c==9: 
                    link="nine-of-pentacles"
                else:
                    link="ten-of-pentacles"

    return link


if 0<=card<22:
    link = majorArcana(card)
    url = "https://labyrinthos.co/blogs/tarot-card-meanings-list/"+link+"-meaning-major-arcana-tarot-card-meanings"
else:
    link = minorArcana(card)
    url = "https://labyrinthos.co/blogs/tarot-card-meanings-list/"+link+"-meaning-tarot-card-meanings"


import webbrowser
webbrowser.open(url)
