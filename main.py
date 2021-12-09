import openpyxl

inv_file = openpyxl.load_workbook("Inventory.xlsx")
product_list = inv_file["Sheet1"]

# calculate how products per supplier
products_per_supplier = {}

for product_row in range(2,
                         product_list.max_row + 1):  # range(2, max_row + 1)  is [2,3, 4, ..., last row] (row 1 is columns title and don't have to be treated and max_row is total row -1)
    supplier_name = product_list.cell(product_row, 4).value  # each cell for the column 4 Suppliers

    if supplier_name in products_per_supplier:
        current_num_products = products_per_supplier.get(supplier_name)
        products_per_supplier[supplier_name] = current_num_products + 1
    else:
        print("adding a new supplier")
        products_per_supplier[supplier_name] = 1

print(products_per_supplier)
