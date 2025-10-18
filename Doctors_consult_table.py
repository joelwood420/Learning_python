from tabulate import tabulate

data = [
    ['Consultation Type', 'Price', 'CSC Holder Price'],
    ['GP Visit', 80.50, 55.00],
    ['Acc Visit', 50.00, 20.00],
    ['Repeat Script', 20.00, 'free'],
    ['Wound Redressing', 20.00, 10.00]
]

print(tabulate(data, headers='firstrow' ))
