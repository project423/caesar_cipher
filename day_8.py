from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if shift_amount > len(alphabet):
      shift_amount = shift_amount % len(alphabet)
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
        end_text+=char
        continue
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



def start_program():    
    should_continue = True
    while should_continue:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))


        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        rerun_input = input('Do you want to run the program again y/n \n')
        if rerun_input.lower() == 'y':
            caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        else:
            should_continue = False
            print('Goodbye')

start_program()