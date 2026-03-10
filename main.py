def main(): #tate
    #accepts no arguments
    #it runs the ceasar cipher
    #and calls programs acordingly
    pass

def get_shift(): #henry
    #accepts no arguments
    #it ask the user for how much to shift
    #and returns that
    
    #loop and variables
    valid = 'n'
    while valid == 'n':
    
        try:
                
            shift = int(input('Enter a number form 1-25 for your encoding shift value: '))
            print()
                
            #validation
            if shift < 25 :
                valid = 'y'
                return shift
            
        except ValueError:
            print('Error try')
            valid = 'n'

def choose_option():#tate
    #accepts no arguments
    #it ask the user for 1 or 2
    #1 to encode
    #2 to decode
    #it then returns it
    pass

def get_message():#henry
    #accepts no arguemtns
    #it ask the user for a message
    #and retruns it
    
    #input
    message = str(input('Enter a message to encode or decode: '))
    print()
    
    #return
    return message

def create_key(shift): #tate
    #accepts shift for the argument
    #and creates a object according to the shift
    pass

def encode(message, key):#henry
    #it accepts message and key
    #according to the message and the key
    #and encodes it
    
    #variable
    string = ''
    
    #start loop
    for letter in key:
        key.get(letter)
        string += 'blah'
        
    print(string)
        
        
    
    

def decode(message, key):#tate
    #it accepts message and key
    #according to the message and the key
    #and decodes it
    pass
