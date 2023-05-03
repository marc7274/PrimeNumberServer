num_min = int(input("primo numero da calcolare: "))
num_max = int(input("ultimo numero da calcolare: "))
last_number_given = num_min - 1

while last_number_given<num_max:  
    if num_max-last_number_given>=1024:
       print(last_number_given+1,last_number_given+1024)
       last_number_given+=1024
    else:
        print(last_number_given+1, last_number_given+(num_max-last_number_given))
        last_number_given+=num_max-last_number_given
