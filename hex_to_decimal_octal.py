

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.
DECIMAL_ENTERED = int(input('Please, write a number: '))
decimal = DECIMAL_ENTERED
binary = ''
binary2 = ''
octal = ''
octal2 = ''
power = 1
############### Binary converter ##################
while (2 ** power <= decimal):
	power += 1

while power > 0:
	if (2 ** (power - 1)) > decimal:
		binary += '0'
	else:
		binary += '1'
		decimal = decimal - (2 ** (power - 1))

	power -= 1
print('A binary representation of {} is {}'.format(DECIMAL_ENTERED, binary))
############### Binary converter 2 ##################
decimal = DECIMAL_ENTERED

while decimal > 1:
	binary2 += str(decimal % 2)
	decimal = decimal // 2
print('A binary2 representation of {} is {}'.format(DECIMAL_ENTERED, binary))
############### Octal converter ##################
decimal = DECIMAL_ENTERED
power = 1

while (8 ** power <= decimal):
	power += 1

while power > 0:
	if (8 ** (power - 1)) > decimal:
		octal += '0'
	else:
		temp = decimal // (8 ** (power - 1))
		octal += str(temp)
		decimal = decimal - (temp * (8 ** (power - 1)))

	power -= 1
print('An octal representation of {} is {}'.format(DECIMAL_ENTERED, octal))
############### Octal 2 converter ##################
decimal = DECIMAL_ENTERED

while decimal > 1:
	octal2 += str(decimal % 8)
	decimal = decimal // 8
print('An octal2 representation of {} is {}'.format(DECIMAL_ENTERED, octal))

############## Alternative solution ##################

for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

x = int(input("Please enter a number: "))

printing = False

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power

























