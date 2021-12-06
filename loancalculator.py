import math
import argparse
import sys

lst = sys.argv[2:]
parser = argparse.ArgumentParser(description='This is a loan calculator')
# You don't have to specify a type or action, it's not necessary.
# I feel it's more comfortable to convert it along the line since am using OOP
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--periods')
parser.add_argument('--payment')
args = parser.parse_args()


class Calculator:

    def loan_interest(self):  # Converts the loan interest from percentages to decimal
        global i
        try:  # use exception to accommodate for both integers and floats
            interest = int(args.interest)
        except ValueError:
            interest = float(args.interest)
        i = interest / (12 * 100)

    def check_4_negative(self):  # checks the list sys.argv from second input for negative value
        global run
        run = True
        for x in lst:
            try:  # using exceptions to accommodate for both integers and floats
                v = int(x[(x.find('=') + 1):])
            except ValueError:
                v = float(x[(x.find('=') + 1):])
            if v * -1 > 0:
                run = False

    def no_of_months(self):  # computes the number of months(period)
        principal = int(args.principal)
        monthly_payment = int(args.payment)
        self.loan_interest()  # gets i
        calc = monthly_payment / (monthly_payment - i * principal)
        n = math.log(calc, i + 1)
        if n < 12:
            print(f'It will take {round(n)} months to repay this loan!')
        elif n > 12 and round(n) % 12 != 0:
            print(f'It will take {n // 12} years and {math.ceil(n % 12)} months to repay this loan!')
        else:
            if n == 12:
                print('It will take 1 year to repay this loan!')
            else:
                print(f'It will take {round(n) // 12} years to repay this loan!')
        print(f'Overpayment= {(monthly_payment * round(n)) - principal}')

    def annuity(self):  # calculates the annuity payments
        principal = int(args.principal)
        n = int(args.periods)
        self.loan_interest()  # gets i
        calc = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        annuity_payment = math.ceil(principal * calc)
        print(f'Your monthly payment = {annuity_payment}!')
        over_payment = round((annuity_payment * n) - principal)
        print(f'Overpayment = {over_payment}')

    def loan_principal(self):  # computes the loan principal
        payment = int(args.payment)
        n = int(args.periods)
        self.loan_interest()  # gets i
        calc = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        principal = math.floor(payment / calc)
        print(f'Your loan principal = {principal}!')
        print(f'Overpayment= {math.floor((payment * n) - principal)}')

    def differentiated_payment(self):  # computes the differentiated payment
        self.loan_interest()  # gets i
        principal = int(args.principal)
        n = int(args.periods)
        m = 1
        total = 0
        while m <= n:
            diff = math.ceil((principal / n) + i * (principal - (principal * (m - 1)) / n))
            print(f'Month {m}: payment is {round(diff)}')
            total += diff
            m += 1
        print(f'Overpayment = {round(total - principal)}')

    def main(self):  # Pieces code together
        self.check_4_negative()
        if args.interest is None:
            print('Incorrect parameters')
            quit()
        if len(sys.argv) == 5 and run:  # Checks that minimum of 5 command entered from terminal
            if args.type == 'annuity':
                if args.periods is None:
                    self.no_of_months()
                elif args.payment is None:
                    self.annuity()
                elif args.principal is None:
                    self.loan_principal()
            elif args.type == 'diff':
                if args.payment is None:
                    self.differentiated_payment()
                else:
                    print('Incorrect parameters')
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')


calculator = Calculator()
calculator.main()
