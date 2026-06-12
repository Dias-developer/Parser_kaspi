import csv
import os
def save():
    os.makedirs('results', exist_ok=True)

    file = open('results/results.csv', 'w', newline='', encoding='utf-8-sig')
    writer = csv.DictWriter(file, fieldnames=['title', 'price', 'url'], delimiter=';')
    writer.writeheader()

    return file, writer
