def cumulative_product(list):
    prod=1
    for i in range(0,len(list)):
        prod=prod*(list[i]);
        print(prod)
list=[10,78,6,4]
print(list)
print("The cumulative products are:\n")
cumulative_product(list)