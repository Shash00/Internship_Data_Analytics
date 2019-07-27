'''Simple interest'''
Principle = float(input('Enter principle value'))
Rate_of_interest = float(input('Enter the rate of interest'))
Time = float(input('Enter the duration'))

simple_interest = (Principle * Rate_of_interest * Time) / 100
print(f"Simple Interest Is: {simple_interest}")
