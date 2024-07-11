Class Initialization
Secound_Project Class:
The __init__ method initializes the class and prints the game rules. These rules explain that a word will be given with missing letters, and the player has to fill in the blanks correctly to win.
Game Functions
Gamming_Function Method:

This method takes a list, required, which contains the characters of the word with some missing (_).
It iterates through the list, prompting the user to input the missing characters.
If a character in required is not missing, it is printed as is.
Convert_List Method:

This method takes the required list and concatenates its elements into a single string answer.
It returns the answer string, which now contains the user's inputs along with the original characters.
Check_Result Method:

This method compares the user's answer to the Set_Word.
If they match, it prints a winning message. Otherwise, it prints a message encouraging the user to try again.
Game Flow
Set_Word:

A string representing the word the user needs to guess ("hello").
required List:

A list representing the word with missing characters (['h', '_', '_', 'l', '_']).
answer String:

An initially empty string that will hold the user's final guessed word.
Game Execution
An instance of Secound_Project is created.
The Gamming_Function method is called, allowing the user to input the missing characters.
The Convert_List method is called to form the complete word from the required list and store it in answer.
