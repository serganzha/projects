# Thanks Darren Noortman for the following suggestion https://csiplearninghub.com/python-if-else-conditional-statement-practice/ in one of the reviews of my tasks, the practice exersices helped out

user_num = int(input("Please enter a number, or -1 to quit: "))
num_count = 0
sum_of_numbers = 0

while user_num != -1:
    num_count += 1
    sum_of_numbers += user_num
    user_num = int(input("Please enter a number, or -1 to quit: "))
    avarage_num = sum_of_numbers / num_count
    print("The avarage of numbers entered is ", avarage_num)
    if user_num == -1:
        print("Thank you for your participation!")
