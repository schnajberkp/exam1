def check_character(text, char):
    count = 0

    # Iterate through each character in the text
    for c in text:
        # Check if the character matches the specified character
        if c == char:
            count += 1
    
    return count 



print(check_character("Butcher of Blaviken, Olgierd Von Everec, Vernon Roche, Gaunter O'Dimm", "i"))

