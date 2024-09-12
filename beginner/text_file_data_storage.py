# Define a function to store user-inputted messages as a text file
def input_to_text():
    # Create a list to store the sentences in
    user_sentences = []
    # Create a for loop to prompt 3 sentences, which will then be stored in the list
    for i in range (1,4):
        sentence = input(f"Enter sentence {i}: ")
        user_sentences.append(sentence)

    # Save the sentences to a text file using a another for loop to iterate through the user sentences list
    #! NOTE: with is a context manager -> it simplifies file handling by automatically closing the file after the code block is executed, even if an error occurs
    with open("user_sentences.txt", "w") as file:
        #! Use the enumerate() function, which will return the INDEX and VALUE of each item of a list/word/etc
        #! **SYNTAX** enumerate(iterable, start=0), where iterable = any object that supports iteration and start = the index value from which the counter is to be started (default = 0)
        #! NOTE: in the if statement, we take both i (the index) and sentence (the value) so that we can insert dashed lines between each sentence but not after the last one
        for i, sentence in enumerate(user_sentences):
            file.write(sentence + "\n")
            if i < len(user_sentences) - 1:
                file.write("-" * 20 + "\n")

    # Print a confirmation message
    print("Sentences have been saved to user_sentences.txt.")                

# Call the function
result = input_to_text()