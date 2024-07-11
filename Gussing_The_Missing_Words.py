class Secound_Project:
    def __init__(self):
        # PRINTING THE GAME RULES
        print("Some of the Rules : -")
        print("    ")
        print("There Will Be One Word Given By Us ")
        print("You Have To Enter the Missing Words")
        print("If You Enter the Right Word You Will Win OR ELSE You Will Lose The Game")
      
    def Gamming_Function(self, required):
        # PRINTING THE REQUIRED LIST
        print(required)
        for i in range(len(required)):
            if required[i] == '_':
                # PROMPT USER FOR MISSING CHARACTER
                value = input()
                required[i] = value
            else:
                # PRINT NON-MISSING CHARACTERS
                print(required[i])
                
    def Convert_List(self, required, answer):
        # CONCATENATE ELEMENTS OF 'REQUIRED' INTO 'ANSWER'
        for i in range(len(required)):
            answer += required[i]
        return answer
           
    def Check_Result(self, Set_Word, answer):
        # CHECK IF USER'S ANSWER MATCHES THE SET WORD
        if answer == Set_Word:
            print("You Won. You Have Guessed The Right Word")
        else:
            print("Better Try Next Time")

# CREATING THE OBJECTS
Set_Word = "hello"  # THE WORD TO GUESS
required = ['h', '_', '_', 'l', '_']  # THE WORD WITH MISSING CHARACTERS
answer = ''  # INITIAL EMPTY ANSWER STRING

# CREATING AN INSTANCE OF Secound_Project CLASS
Object_For_Secound_Project = Secound_Project()

# RUNNING THE GAMING FUNCTION TO ALLOW USER TO GUESS MISSING CHARACTERS
Object_For_Secound_Project.Gamming_Function(required)

# UPDATING 'ANSWER' STRING WITH THE FILLED 'REQUIRED' LIST
answer = Object_For_Secound_Project.Convert_List(required, answer)

# CHECKING IF THE USER'S ANSWER MATCHES THE SET WORD
Object_For_Secound_Project.Check_Result(Set_Word, answer)