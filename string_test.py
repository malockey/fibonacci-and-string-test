import string

def test_string(letter=""):
    count = 0
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pretium, ante at rhoncus imperdiet, nunc lacus vulputate purus, at dictum mi ligula iaculis tortor. Donec ut rhoncus lacus. Etiam a felis nec elit ullamcorper gravida eu molestie mi. Nullam eu est eu eros vulputate imperdiet vel sit amet nisl. Morbi faucibus sollicitudin tortor, sed aliquam mauris semper at. Nunc nec lectus nec sapien viverra ultricies sed bibendum enim. Pellentesque interdum tellus nisl, quis tempor tellus varius eu. Curabitur ut eros vitae velit porta pulvinar id efficitur lacus. Fusce dignissim rhoncus nibh, in pharetra ipsum venenatis vel. Nam massa elit, elementum vel mauris sed, placerat pretium turpis. Morbi cursus neque id nisi vestibulum, vitae faucibus felis euismod. Maecenas nibh justo, dictum laoreet volutpat a, consectetur a tellus. Curabitur semper justo ipsum, eget accumsan elit placerat eget. Nam at ligula gravida, vehicula dolor sit amet, tristique elit. Sed porttitor at magna nec tristique. Suspendisse at feugiat nulla, pellentesque viverra dui."

    if len(letter) == 0:
        return "Empty string"

    letter = letter.lower() # case-insensitive
    
    for i in text:
        if i.lower() == letter:
            count += 1

    if count == 0:
        return "No letters in the string"

    return count

def main():
    print('Type a letter:')
    letter = input()
    print(test_string(letter))

if __name__ == "__main__":
    main()