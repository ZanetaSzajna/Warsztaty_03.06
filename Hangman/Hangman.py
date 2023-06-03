import random
import colorsys
from colorsys import r
from list_words import word_list

def get_word():

    keyword=random.choice(word_list)
    return keyword

def user():
    user_letter = (input("Enter yor letter --> ")).upper()
    return user_letter

def play_game(keyword):
    gues_word = list(keyword)
    user_letters=[]

    for i in range(len(keyword)):
        gues_word[i] = "_"
    tries=10
    print("********************************")
    print("Let's play !!!!")
    print("********************************")
    print(display_hangman(tries))
    print(" ".join(gues_word))
    print("\n")
    print("")

    while tries > 0:
        print(f"You use letter {user_letters}")
        user_letter = user()
        if user_letter.isalpha()==True and len(user_letter)==1:
            if user_letter.upper() in keyword and user_letter.upper() and user_letter.upper() not in user_letters:
                for letter in range(len(keyword)):
                    if keyword[letter] == user_letter.upper():
                        print("congratulations you have successfully guessed the letter ")
                        gues_word[letter] = user_letter.upper()
                        user_letters.append(user_letter.upper())
                if "".join(map(str, gues_word)) == keyword:
                    print("You win !!!!!!!!!!!!!!!!")
                    break;
            elif user_letter.upper() not in keyword and user_letter.upper() and user_letter.upper() not in user_letters:
                tries-= 1
                print(f"Sorry, {user_letter} is not in the keyword. Try Again ")
                user_letters.append(user_letter.upper())
            else:
                print("you used this letter earlier ")
        else:
            print("Please enter a letter")

        #  wyświetenie zaszyfrowaneh=go hasłą

        print(display_hangman(tries))
        print(" ".join(gues_word))
        print("\n")



def display_hangman(tries):
    hangman = [ '''
    
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼-
                       |       ┌┴┐
                       |                SORRY YOU'RE DEAD
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼-
                       |       ┌┴
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼-
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        O
                       |       -┼
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        O
                       |        ┼
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        O
                       |        
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------┐
                       |        |
                       |        
                       |        
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌--------
                       |        
                       |        
                       |        
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       ┌
                       |        
                       |        
                       |        
                       |       
                       |    
                    ___|___             
                '''
                ,
                '''
                
                       
                       
                              
                             
                             
                         
                    ______             
                '''
                ,
                """
                
                
                
                
                
                
                
                
                """
                ]
    return  hangman[tries]

def main():
    keyword=str(get_word()).upper()
    print(keyword)
    play_game(keyword)

if __name__== "__main__":
    main()