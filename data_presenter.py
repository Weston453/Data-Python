open_file = open("CupcakeInvoices.csv")
       
sum = 0

for line in open_file:
    line = line.rstrip('\n').split(",")
    print (line)
    print(line[2])
    quantity = float(line[3])
    price = float(line[4])
    sum += (quantity * price)

print(f'Sales totals for today = {sum}')

open_file.close()