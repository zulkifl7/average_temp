'''
A group of medical students were monitoring the body temperature of a patient daily basis.
Students captured 10 temperature readings in Celsius on a particular day.
1. Write an Algorithm to input these ten values and get the average temperature for that
day. if the average temperature value is in between 970 Fahrenheit and 990 Fahrenheit
then display the message “Your body temperature is normal…”. If it is more than 100.40
Fahrenheit then display the message “You have a fever caused by an infection or
illness…”.
2. Convert the above algorithm (written in part (1)) to a Python program to output the
desired results.
'''

temp = []
for n in range(0, 10):
    temp.append(float(input("Enter the temperature %d (In f): " % (n+1))))


avg = 0

for n in temp:
    avg += n / len(temp)


if (97 <= avg <= 99):
    print("Your body temperature is normal.")
elif (avg > 100.4):
    print("You have a fever caused by an infection or illness!")
