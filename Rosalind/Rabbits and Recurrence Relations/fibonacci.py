

def rabbitPairs(num_months,num_offspring):
   #Massive Help
   #https://medium.com/algorithms-for-life/rosalind-walkthrough-rabbits-and-recurrence-relations-4812c0c2ddb3
   if num_months == 1:
      return 1
   elif num_months == 2:
      return num_offspring
   
   gen_one = rabbitPairs(num_months - 1,num_offspring)
   gen_two = rabbitPairs(num_months - 2,num_offspring)
   if num_months <= 4:
      return gen_one + gen_two 
   return gen_one + (gen_two * num_offspring)


with open("rosalind_fib.txt",'r') as f:
   data = f.read().split(' ')
   months = int(data[0])
   offspring = int(data[1])
   print(rabbitPairs(months,offspring))

