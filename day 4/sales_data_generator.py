import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sales_data(num_records=int(input("Enter the number of sales records you want to create: "))):
    # 1. Setup Master Lists for realistic random selection
    regions = {"Asia": ["India", "Japan", "China"], "Europe": ["UK", "Germany", "France"], "Americas": ["USA", "Canada", "Brazil"]}
    states_india = [random.choice(["Madhya Pradesh", "Maharashtra", "Delhi", "Gujarat"]) for _ in range(num_records)]
    cities_mp = ["Bhopal", "Indore", "Gwalior", "Jabalpur"]
    categories = {
        "Electronics": [("Laptop", "Inspiron 15", "Dell"), ("Phone", "iPhone 15", "Apple")],
        "Furniture": [("Chair", "ErgoChair", "IKEA"), ("Desk", "OfficeDesk", "Featherlite")]
    }
    payment_modes = ["UPI", "Credit Card", "Cash", "Net Banking"]

    data = []

    # 2. Loop to create each row
    for i in range(num_records):
        # Generate IDs and Dates
        order_id = 1001 + i
        date = (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 30))).strftime("%m/%d/%Y")
        
        region = "Asia"
        country = "India"
        state = states_india[i]
        city = random.choice(cities_mp if state == "Madhya Pradesh" else ["Mumbai", "Pune", "Nagpur"] if state == "Maharashtra" else ["New Delhi", "Noida", "Ghaziabad"] if state == "Delhi" else ["Ahmedabad", "Surat", "Vadodara"])
        
        # Product Logic 
        cat = random.choice(list(categories.keys()))
        prod_type, prod_name, brand = random.choice(categories[cat])
        
        # Financial Logic
        quantity = random.randint(1, 5)
        unit_price = random.choice([55000, 45000, 12000, 8000])
        discount = random.choice([5, 10, 20])
        sales = (unit_price * quantity) * (1 - discount/100)
        profit = sales * 0.12 # Assuming 12% profit margin

        # 3. Append as a dictionary
        data.append({
            "OrderID": order_id, "OrderDate": date, "Region": region,
            "Country": country, "State": state, "City": city,
            "CustomerID": f"C{str(i+1).zfill(3)}", "CustomerName": f"Customer_{i+1}",
            "ProductCategory": cat, "ProductName": prod_name, "Brand": brand,
            "Quantity": quantity, "UnitPrice": unit_price, "Discount": f"{discount}%",
            "Sales": sales, "Profit": profit, "PaymentMode": random.choice(payment_modes)
        })

    return pd.DataFrame(data)

# Create and save
df_sales = generate_sales_data()
print(df_sales.head())
df_sales.to_csv("sales_data.csv", index=False)