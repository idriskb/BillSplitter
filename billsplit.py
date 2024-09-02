from datetime import datetime

class BillSplitter:
    def __init__(self, bills):
        """
        Initialize with a dictionary of bills.
        Each key is 'gas', 'water', 'electricity' etc..
        Each value is a tuple of (amount, start_date, end_date) in the format ('YYYY-MM-DD', 'YYYY-MM-DD').
        """
        self.bills = bills

    def _date_range_intersection(self, bill_start, bill_end, away_start, away_end):
        """Helper function to find the intersection between two date ranges."""
        latest_start = max(bill_start, away_start)
        earliest_end = min(bill_end, away_end)
        delta = (earliest_end - latest_start).days + 1
        return max(0, delta)
    
    def calculate_payments(self, flatmates):
        """
        Calculate how much each flatmate should pay.
        flatmates: a dictionary where keys are flatmate names and values are lists of (start_date, end_date) tuples indicating when they were away.
        Returns a dictionary with flatmate names as keys and the amount they should pay as values.
        """
        total_days = {}
        payments = {}

        # Calculate the total number of days each flatmate was present for each bill
        for utility, (amount, start_date, end_date) in self.bills.items():
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            bill_days = (end_date - start_date).days + 1

            for flatmate, away_periods in flatmates.items():
                days_present = bill_days
                
                for away_start, away_end in away_periods:
                    away_start = datetime.strptime(away_start, '%Y-%m-%d')
                    away_end = datetime.strptime(away_end, '%Y-%m-%d')
                    overlap_days = self._date_range_intersection(start_date, end_date, away_start, away_end)
                    days_present -= overlap_days

                if flatmate not in total_days:
                    total_days[flatmate] = 0
                
                total_days[flatmate] += days_present

        # Calculate the payment for each flatmate
        total_present_days = sum(total_days.values())

        for flatmate, days in total_days.items():
            payments[flatmate] = 0
            for utility, (amount, start_date, end_date) in self.bills.items():
                share = (days / total_present_days) * amount
                payments[flatmate] += share
        self.payments = payments
        return self.payments
    
    def nice_printing(self):
        for flatemate, share in self.payments.items():
            print(f"{flatemate} pays {share}")

    def total_split(self):
        total_sum = 0
        for flatmates, amount in self.payments.items():
            total_sum += amount
        return total_sum
    
    def total_bill(self):
        total_amount = 0
        for _, (amount, _,_) in self.bills.items():
            total_amount += amount
        return total_amount
    
    def checking_output(self):
        if self.total_split() != self.total_bill():
            print('Difference in splitted bill and original bill, be careful')
            print('Splitted bill total is ', self.total_split(),'and original bill total: ', self.total_bill())
        else:
            print('Splitted correctly')
            print('Splitted bill total is ', self.total_split(),'and original bill total: ', self.total_bill())
