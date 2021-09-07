open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     line = line.rstrip('\n').split(",")
#     print (line)
#     print(line[2])
#     quantity = float(line[3])
#     price = float(line[4])
#     print(quantity * price)
       
sum = 0


for line in open_file:
    line = line.rstrip('\n').split(",")
    print (line)
    print(line[2])
    quantity = float(line[3])
    price = float(line[4])
    sum += (quantity * price)

# done = sum(total_sales)
print(f'Sales totals for today = {sum}')

# cupcake_flav = []
# for line in open_file:
#     line = line.rstrip('\n').split(",")
#     quantity = float(line[3])
#     price = float(line[4])
#     cupcake_flav.append(quantity * price)



# cupcake_flav.append(line[3] * line[4])

# print(cupcake_flav)


# my_list = [1,2,3,4,5,6,7]
# sol = []

# sol.append(my_list[0] * my_list[1])

# print(sol)




