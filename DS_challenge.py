import pandas as pd
sneaker_sales = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv')

# 1.a
#    The calculated AOV of $3145.13 does not consider the validity or trends of the dataset. 
#    Since the AOV seems too high, let's look at the highest few transactions. 


print(sneaker_sales.sort_values(['total_items'], ascending=[False])[0:25])

#    Sorting by Number of Items Per Order (total_items), there is an evident jump in values for the top 17 transactions 
#    (all other orders have an order_amount of 8 or less)
        # - They are purchased by the same user_id 607
        # - Each order is exactly 2000 sneakers from shop_id 42 for a total of $704000


user_id607 = sneaker_sales[sneaker_sales["user_id"] == 607]
print(user_id607.sort_values(["created_at"]))

        # - Ordering by date shows each purchase is made precicely at 4am, up to 3 times a day
        # - Same-day same-time transactions are likely duplicate entries 
            # Since order_ids are different and all use credit cards, user_id 607 might be running a script to place fast repeated orders
        # - user_is 607 is most likely bulk purchasing and reselling sneakers at a higher price 
            # Must evaluate whether or not we want to include resellers' bulk purchases as valid 


unit_price = sneaker_sales[sneaker_sales["total_items"] == 1]
print(unit_price.sort_values(['order_amount'], ascending = [False])[0:25])

    # Sorting by Price Per Item (order_amount with total_items = 1), 19 top transactions stand out from the rest 
    # (next most expensive item is priced at $352 from shop_id 42)
        # - They are all from shop_id 78 
        # - Each item is listed as $25725 – unlikely for sneakers
        # - Probably an error in entering the value 

# 1.b 
#    We can use the MEDIAN as a metric for this data set as it is a more robust measure of center 
#    that is not going to be easily affected by outliers/extreme values

# 1.c 
print(sneaker_sales["order_amount"].median())
    # Median order amount is $284.0


# 2.a 
#   How many orders were shipped by Speedy Express in total?
#       Answer: 54
#   SELECT COUNT (*)
#   FROM ORDERS o, SHIPPERS s
#   WHERE o.ShipperID = s.ShipperID AND ShipperName = 'Speedy Express';


# 2.b 
#   What is the last name of the employee with the most orders?
#       Answer: Peacock 
#   SELECT LastName
#   FROM EMPLOYEES e, ORDERS o
#   WHERE e.EmployeeID = o.EmployeeID 
#   GROUP BY e.EmployeeID
#   ORDER BY COUNT(*) DESC
#   LIMIT 1 


# 2.c
#   What product was ordered the most by customers in Germany?
#       Answer: Boston Crab Meat 
#   SELECT ProductName
#   FROM Products p, OrderDetails od, Orders o, Customers c
#   WHERE p.ProductID = od.ProductID 
#     AND od.OrderID = o.OrderID 
#     AND o.CustomerID = c.CustomerID
#     AND c.Country = "Germany"
#   GROUP BY p.ProductID
#   ORDER BY SUM(Quantity) DESC
#   LIMIT 1
