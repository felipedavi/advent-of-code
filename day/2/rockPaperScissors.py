score = int(0)
def game(x,y):
    global score
    # Rock
    if x == 'A' and y == 'X':
        print("Rock x  Rock")
        score+=3
        score+=1
    elif x == 'A' and y == 'Y':
        print("Rock x  Paper")
        score+=6
        score+=2
    elif x == 'A' and y == 'Z':
        print("Rock x Scissors")
        score+=0
        score+=3
    #Paper
    if x == 'B' and y == 'X':
        print("Paper x Rock")
        score+=1
    elif x == 'B' and y == 'Y':
        print("Paper x Paper")
        score+=(3+2)
    elif x == 'B' and y == 'Z':
        print("Paper x Scissors")
        score+=(6+3)
    #Scissors
    if x == 'C' and y == 'X':
        print("Scissors x Rock")
        score+=(6+1)
    if x == 'C' and y == 'Y':
        print("Scissors x Paper")
        score+=2
    elif x == 'C' and y == 'Z':
        print("Scissors x Scissors")
        score+=(3+3)
#-----------------------------------------------------
def main():
    f = open("dataday.txt", "r")
    for x in f:
        if x in ['\n', '\r\n']:
            pass
        else:
            tmp = x.split(' ')
            game(tmp[0],tmp[1].replace('\n', ''))
    print("Score: " + str(score))
#-----------------------------------------------------
if __name__ == '__main__':
    main()
    
