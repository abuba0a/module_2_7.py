print()

number = input('Введите любое многозначное число : ')

print()
print(number)


def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[0])
    if len(str_number) > 1:
        return(first * get_multiplied_digits(int(str_number[1:])))
    if first == 0:
        return 1
    else:
        return(int(first))


result = get_multiplied_digits(number)


print('Произведение цифр этого числа (без учёта нулей) = ', result)

