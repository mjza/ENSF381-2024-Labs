"""
=========================================================
Name        : lab9_exe_C.py
Assignment  : Lab 9, Exercise C
Author(s)   : Mahdi Ansari, William Arthur Philip Louis
Submission  : May 21, 2030
Description : Fetch data by Python.
=========================================================
"""

import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()['products']  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_all_products(products):
    for product in products:
        print(product['title'])

def search_product(products, name):
    for product in products:
        if product['title'].lower() == name.lower():
            print(json.dumps(product, indent=4)) 
            return
    print("Product not found.")

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n> ")
            if choice == '1':
                list_all_products(products)
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
    main()
