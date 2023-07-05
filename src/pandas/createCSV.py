import pandas as pd

columns = ['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address']
file = open('sales.csv','+w')
for c in columns:
    file.write(c + ',')
file.write('\n')

flag = True
while flag:
    orderID = input("Enter Order ID: ")
    product = input("Product Name: ")
    quantity = input("Quantity Ordered: ")
    price = input("Price Each: ")
    orderDate = input("Order Date: ")
    shipingAddress = input("Purchase Address: ")

    data = {
        'Order ID': [orderID],
        'Product': [product],
        'Quantity Ordered': [quantity],
        'Price Each': [price],
        'Order Date': [orderDate],
        'Purchase Address': [shipingAddress]
    }

    df = pd.DataFrame(data)
    # Append data to the CSV file
    df.to_csv(file, mode='a', header=False, index=False, lineterminator='\n')

    proceed = input("Do you want to continue? (Y/N): ")
    if proceed.upper() == 'N':
        flag = False
file.close()
