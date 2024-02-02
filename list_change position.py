


first = input("first number: ")
second= input("second number: ")
print("before swapping:",first,second)
first,second= second,first
print("after swapping:",first,second)

#change the position in the list    
top_cities= ['NY','NJ','Chicago','Seoul']
top_cities[0],top_cities[3]=top_cities[3],top_cities[0]
print("after swapping:",top_cities)

#sort
top_cities= ['NY','NJ','Chicago','Seoul']
top_cities.sort()
print(top_cities)

#random number
random_number=[2,6,7,-1,4]
random_number.sort()
print(random_number)

random_number=[2,6,7,-1,4]
random_number.sort(reverse=True)
print(random_number)

#original

#sorted(random_number) :keeps the original unchanged

