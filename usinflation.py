from __future__ import division
import csv

def load_inflation_data(filename='usinf.csv'):
    with open(filename, 'rb') as inflation:
        reader = csv.reader(inflation)
        reader.next() #ignore first line
        data = {int(row[0]): float(row[1]) for row in reader}

    return data

def calculate_inflation(principle, start_year, end_year, inflation_data_file='usinf.csv'):
    data = load_inflation_data(inflation_data_file)
    if start_year >= end_year:
        raise ValueError('Start year must be before end year')

    if start_year < min(data.keys()):
        raise ValueError('Start year must be greater than or equal to %s'%min(data.keys()))

    if end_year > max(data.keys()):
        raise ValueError('End year must be greater than or equal to %s'%max(data.keys()))
    
    amount = principle
    for year in xrange(start_year, end_year+1):
        amount += data[year]/100 * amount

    return amount

def get_user_input():
    start_year = int(raw_input('Enter a start year: '))
    end_year = int(raw_input('Enter a end year: '))
    principle = float(raw_input('Enter a starting amount: '))

    print principle, 'USD in', start_year, 'is equal to', calculate_inflation(principle, start_year, end_year), 'in', end_year

if __name__ == '__main__':
    get_user_input()       
