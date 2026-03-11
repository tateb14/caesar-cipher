def main(): #tate
    #accepts no arguments
    #it runs the ceasar cipher
    #and calls programs acordingly
    
    # run shift programs
    shift = get_shift()
    message = get_message()
    encode_bool = choose_option()
    key = create_key(shift)
    
    # If encode return is true...
    if encode_bool == True:
        encode(message, key)
    else:
        decode(message, key)

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
    
    encode_bool = False
    
    option = int(input("Choose '1' to encode or '2' to decode: "))
    
    while option != 1 and option != 2:
        option = input("INVALID INPUT: Choose '1' to encode or '2' to decode: ")
    
    if option == 1:
        encode_bool = True
    
    return encode_bool

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
    import string
    key = {}
    count = 1
    uppercase = {}
    lowercase = {}
    
    # create uppercase dictionary
    for letter in string.ascii_uppercase:
        uppercase[letter] = count
        count += 1
        
        
    #reset count
    count = 1
    for letter in string.ascii_lowercase:
        lowercase[letter] = count
        count += 1
        
    count = 1
    
    #handle upper
    for letter in uppercase:
        value = uppercase[letter]
        value = value + shift
        if value > 26:
            value = value % shift
        
        key[letter] = value
    # handle lowercase key
    for letter in lowercase:
        value = lowercase[letter]
        value = value + shift
        if value > 26:
            value = value % shift
        
        key[letter] = value
    
    return key

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

main()
