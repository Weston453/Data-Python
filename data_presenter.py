open_file = open("CupcakeInvoices.csv")
       
# import matplotlib.pyplot as plt 
    
# # x axis values 
# x = ["Chocolate", "Vanilla", "Strawberry"] 
# # corresponding y axis values 
y = [] 
    
# # plotting the points  
# plt.plot(x, y) 
    
# # naming the x axis 
# plt.xlabel('Cupcake Flavor') 
# # naming the y axis 
# plt.ylabel('Amount Purchased') 
    
# # giving a title to my graph 
# plt.title('My Cupcake Sales') 
    
# # function to show the plot 
# plt.show() 


sum = 0

for line in open_file:
    line = line.rstrip('\n').split(",")
    print(line)
    print(line[2])
    quantity = float(line[3])
    price = float(line[4])
    sum += (quantity * price)

print(f'Sales totals for today = {sum}')

open_file = open("CupcakeInvoices.csv")

choc_arr = []
van_arr = []
straw_arr = []

tot_choc = 0
tot_van = 0
tot_straw = 0

for line in open_file:
  line = line.rstrip('\n').split(",")
  for i in line:
    if i == 'Chocolate':
      choc_quantity = choc_arr.append(int(line[3]))
      sum = sum(choc_arr)
    elif i == 'Vanilla':
      van_quantity = van_arr.append(int(line[3]))
    elif i == 'Strawberry':
      straw_quantity = straw_arr.append(int(line[3]))

    
# y.append(sum(choc_arr))
# y.append(tot_van)
# y.append(tot_straw)

# print(y)
print(choc_arr)
print(van_arr)
print(straw_arr)



open_file.close()