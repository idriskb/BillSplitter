from billsplit import BillSplitter

bills = {
    'gas': (100, '2024-08-01', '2024-08-31'),
    'water': (50, '2024-08-01', '2024-08-31'),
    'electricity': (120, '2024-08-01', '2024-08-31')
}

flatmates = {
    'Alice': [('2024-08-05', '2024-08-10'), ('2024-08-20', '2024-08-25')],
    'Bob': [('2024-08-15', '2024-08-20')],
    'Charlie': [('2024-08-01', '2024-08-03'), ('2024-08-28', '2024-08-31')]
}

splitter = BillSplitter(bills)
splitter.calculate_payments(flatmates)
splitter.nice_printing()
# To check if the split sums to the bills sum
splitter.checking_output()
