import random                                 # the.randint() function generates
nums= random.randint(1000,9999)               # random integer number within the specified range generated
num1 = nums % 10                              # modulus of the number gives the once place digit
num2 = (nums // 10) % 10                      #// provides the integer value only gets the tens place digit
num3 = (nums // 100) % 10
num4 = (nums // 1000) % 10
print(nums)                                    # Print the random number
nguesses=10                                     # no of times the loop execute
marks=20
while nguesses<=10:                              # loop repeats as long as the guess is correct or the turn over
    guess = int(input("GUESS A FOUR DIGIT NUMBER"))
    if nums==guess:                                # comparision of the number
        print("HURRAY U GUESSED IT CORRECTLY")
        marks=marks+5
        break                                       # guess correct then comes out of the loop
        nums = random.randint(1000, 9999)
        num1 = nums % 10
        num2 = (nums // 10) % 10
        num3 = (nums // 100) % 10
        num4 = (nums // 1000) % 10
        print(nums)
    elif nums!=guess:                                  # when the guess no is not correct
        marks=marks-2
        print("TURNS REMAINIG",nguesses-1)
        if num1==guess%10:
            print("THE DIGIT IN CORRECT PLACE IS",guess%10)
            if num2 == (guess // 10) % 10:
                print("THE DIGIT IN CORRECT PLACE IS",(guess //10) % 10)
                if num3 == (guess //100) % 10:
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 100) % 10)
                    if num4==(guess//1000)%10:
                        print("THE DIGIT IN CORRECT PLACE IS",(guess//1000)%10)
                elif (num4 == (guess // 1000) %10):
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 1000) % 10)
            elif (num3 == (guess // 100) % 10):
                print("THE DIGIT IN CORRECT PLACE IS", (guess // 100) % 10)
                if num4 == (guess // 1000)%10:
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 1000)%10)
            elif num4==(guess//1000)%10:
                print("THE DIGIT IN CORRECT PLACE IS",(guess//1000)%10)
        elif num2== (guess // 10) % 10:
                print("THE DIGIT IN CORRECT PLACE IS",(guess //10) % 10)
                if num3 == (guess //100) % 10:
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 100) % 10)
                    if num4==(guess//1000)%10:
                        print("THE DIGIT IN CORRECT PLACE IS",(guess//1000)%10)
                elif (num4 == (guess // 1000) %10):
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 1000) % 10)
        elif num3==(guess //100) % 10:
                    print("THE DIGIT IN CORRECT PLACE IS", (guess // 100) % 10)
                    if num4==(guess//1000)%10:
                        print("THE DIGIT IN CORRECT PLACE IS",(guess//1000)%10)
        elif (num4 == (guess // 1000) % 10):
                    print("THE DIGIT IN CORRECT PLACE IS", (guess //1000) % 10)
        else:
            print("NONE OF THE DIGITS IS CORRECT")
            marks=marks-2
            print("marks=",marks)
    nguesses-=1                                                             # decrement of the no of guessing time
print("GAME OVER\nSTART A NEW GAME\nYOUR SCORE IS=",marks)


