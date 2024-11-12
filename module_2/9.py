principle = input('Enter the principle amount: ')
rate = input('Enter the rate of interest: ')
time = input('Enter the time (in years): ')

principle = float(principle)
rate = float(rate)
time = float(time)

interest = (principle*rate*time)/ 100

print('The simple interest is: ',interest)