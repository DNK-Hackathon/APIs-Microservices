import pandas as pd


columns = [
    'Quantity', 'Units', 'HSCODE', 'Product Description', 'Invoice Number',
    'Invoice Date (Date Calendar)', 'Gross Weight (Gms)', 'Net Weight (Gms)', 'FOB',
    'Currency', 'Value in Currency', 'Exchange Rate', 'Export Duty Rate', 'Export Duty Amount',
    'Cess Rate', 'Cess Amount', 'CTH', 'Invoice No', 'Invoice Date',
    'SI No of item invoice', 'Value', 'LUT/Bond Details', 'IGST Rate', 'IGST Amount',
    'Compensation Rate', 'Compensation Amount', 'Ecommerce', 'URL', 'Payment txn ID', 'SKU No'
]


try:
    existing_data = pd.read_csv('invoice_data.csv')
except FileNotFoundError:
    existing_data = pd.DataFrame(columns=columns)


new_data = pd.DataFrame(columns=columns)


for column in columns:
    if column == 'LUT/Bond Details':
        lut_bond_details = input(f"Enter {column} (YES/NO): ").upper()
        new_data[column] = [lut_bond_details]
    elif column in ['IGST Rate', 'IGST Amount', 'Compensation Rate', 'Compensation Amount']:
        if lut_bond_details == 'YES':
            
            new_data[column] = ['0']
        else:
            new_data[column] = [input(f"Enter {column}: ")]
    else:
        new_data[column] = [input(f"Enter {column}: ")]


combined_data = pd.concat([existing_data, new_data], ignore_index=True)


combined_data.to_csv('invoice_data.csv', index=False)

print("Data has been saved to invoice_data.csv")
