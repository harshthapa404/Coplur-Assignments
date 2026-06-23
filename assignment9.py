#Assignment 9

#In this we have to find the kaprekar Constant : 6174
#First we have to arrange the number into descending order meaning biggest to smallest
#Second we have to arrange the number into ascending order meaning smallest to biggest
#Use the same number when you are Descending or Ascending the number.
#Then you have to subtract the descending number from ascending number
#Then you have to repeat this until the 4 digit number is equal to the 6174.

#This will work only in 4 digits number.


def number(num):

    while num != 6174:  #This will run until the num == 6174.

        descending=int("".join(sorted(str(num),reverse=True)))  #Arranging the number into descending order.

        ascending=int("".join(sorted(str(num))))                #Arranging the number into ascending order.

        num=descending-ascending                                #Subtract descending number from ascending number

        print(f"\n{descending} - {ascending} = {num}")            #printing the result of descending and ascending number.
                                                                
                                                                #And if the number become 6174 than exit the loop otherwise repeat the same.

    print("\nKaprekar Constant Reached : 6174")
        


num=9876
number(num)