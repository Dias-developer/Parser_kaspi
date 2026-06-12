import json
import os
from save_to_csv import save
def scrape_json():
    file, writer = save()

    for filename in os.listdir('data'):
        if not filename.endswith('.json'):
            continue

        path = os.path.join('data', filename)

        with open(path, 'r') as f:
            page = json.load(f)

        for product in page.get('data', []):
            writer.writerow({
                'title': product.get('title'),
                'price': product.get('priceFormatted'),
                'url': product.get('shopLink'),
            })
        print(f"Processed {filename}")
    file.close()

if __name__ == '__main__':
    scrape_json()
