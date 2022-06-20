import math, sys

def returnIntArray(string = "") -> list:
    return map(lambda char: ord(char) if ord(char) < 256 else 32, string)

def calcOperators(char_num = 0) -> tuple: # Needs re-factor a posteriori
    pow_numbers = [x**2 for x in range(1,17)]
    integer_to_pow = 0
    the_rest = 0
    anterior_index = 0
    distance_between_number_and_char_num = 0
    distanace_between_anterior_number_and_char_num = 0
    for numbers in pow_numbers:
        if(numbers != 256):
            anterior_index = (pow_numbers.index(numbers) + 1)
            if(char_num == numbers):
                integer_to_pow = math.sqrt(numbers)
                the_rest = 0
                break
            elif(char_num > numbers and char_num < pow_numbers[anterior_index]):
                distance_between_number_and_char_num = char_num - numbers
                distanace_between_anterior_number_and_char_num = pow_numbers[anterior_index] - char_num
                if(distance_between_number_and_char_num < distanace_between_anterior_number_and_char_num):
                    integer_to_pow = math.sqrt(numbers)
                    the_rest = char_num - numbers
                else:
                    integer_to_pow = math.sqrt(pow_numbers[anterior_index])
                    the_rest = char_num - pow_numbers[anterior_index]  
                break
        else:
            integer_to_pow = 16
            the_rest = -1
    return (int(integer_to_pow), int(the_rest))

def returnPiceInstruction(char_num : int = 0) -> str:
    operators = calcOperators(char_num)
    pow_string = '+' * operators[0]
    remove_or_add_to_string = "+" * operators[1] if operators[1] >= 0 else "-" * (operators[1] * -1)
    instruction = f"{pow_string}[>{pow_string}<-]>{remove_or_add_to_string}.[-]<"
    return instruction
    

def returnFullInstruction(num_array = []) -> str:
    instruction = ""
    actual_cell_number = 1
    for ascii_numbers in num_array:
        instruction += returnPiceInstruction(ascii_numbers)
    return instruction

def main(argv = ()) -> None:
    string = " ".join(argv[1::])
    int_array = returnIntArray(string)
    print(returnFullInstruction(int_array))

if __name__ == "__main__":
    main(sys.argv)
