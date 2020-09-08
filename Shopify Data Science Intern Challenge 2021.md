## Shopify Data Science Intern Challenge 2021

### Question 1 Answers (Summary)
<br>

**Question 1a**

The AOV of $3145.13 is calculated from the dataset without consideration for orders that seem erroneous. There are large transactions that are possibly duplicates, and unrealisticly high prices suggesting inaccurate data entries. Those orders are significantly inflating the AOV.

A better way to evaluate this data would be to use a different measure of center that would be less affected by the high values that are currently driving up the AOV. In this case, the *median* would be a good alternative. 

<br>

**Question 1b** 

We can use the *median* as a metric for this data set as it is a more robust measure of center that is not going to be easily affected by outliers/extreme values.

<br>

**Question 1c**

Median order amount is $284.0


### Question 1 Answers (Full)

**Question 1a**

Let's take a look at the dataset


```python
# save the data as a csv file
import pandas as pd
sneaker_sales = pd.read_csv('Intern Challenge Data Set.csv')

sneaker_sales.describe()
```

The naively calculated AOV of $3145.13 is the average of the order_amount.

Let's see a visual representation of the sales with each point as one order...


```python
sneaker_sales.plot.scatter(x='order_id', y='order_amount')
```

From the plot above, it looks like most of the sales are under $100,000 and the AOV is driven up by a few unreasonably high purchases. 

Let's look into the top transactions...


```python
sneaker_sales.sort_values(['total_items'], ascending=[False])[0:20]
```

Sorting by total_items, there is an evident jump in values for the top 17 transactions. Compared to 2000 items per order for the top 17, all other orders have an total_items of 8 or less. 
Looking at other columns, we find that: 
- they are purchased by the same user_id 607
- each order is exactly 2000 sneakers from shop_id 42 for a total of $704000
    
It seems more plausible that these values were accidentally multiplied by 1000 such that each order is actually 2 sneakers for a total of $704. Since we cannot determine whether it was a mistake or not, we will keep these entries. 

Let's sort these 17 transactions by the time they were created at...


```python
user_id607 = sneaker_sales[sneaker_sales["user_id"] == 607]
user_id607.sort_values(["created_at"])
```

Ordering by time, it is evident that each purchase is made precicely at 4am up to 3 times a day, all with credit cards. 
This suggests that the transactions are duplicate entries. However, since the order_ids are different, it seems like user_id 607 is running a script to make fast bulk purchases. 

Let's now look at the top transactions sorting by price per item...



```python
unit_price = sneaker_sales[sneaker_sales["total_items"] == 1]
unit_price.sort_values(['order_amount'], ascending = [False])[0:25]
```

Sorting by unit price, the top 19 transactions stand out from the rest. They are all from shop_id 78 selling for $25725 each, excessively expensive compared to the next priciest item at 352.

This high price point is unusual for an average pair of sneakers, and is likely due to an error in inputting or computing the values.


**Question 1c**

Compute the Median:


```python
sneaker_sales["order_amount"].median()
```


### Question 2 Answers
<br>

**Question 2a**: How many orders were shipped by Speedy Express in total?
  
  Answer: *54*
  
      SELECT COUNT (*)
      FROM ORDERS o, SHIPPERS s
      WHERE o.ShipperID = s.ShipperID 
        AND ShipperName = 'Speedy Express';

<br>

**Question 2b**: What is the last name of the employee with the most orders?

  Answer: *Peacock*
  
      SELECT LastName
      FROM EMPLOYEES e, ORDERS o
      WHERE e.EmployeeID = o.EmployeeID 
      GROUP BY e.LastName
      ORDER BY COUNT(*) DESC
      LIMIT 1 

<br>

**Question 2c**: What product was ordered* the most by customers in Germany?
  
  Answer: *Boston Crab Meat* 
          
      SELECT ProductName
      FROM Products p, OrderDetails od, Orders o, Customers c
      WHERE p.ProductID = od.ProductID 
        AND od.OrderID = o.OrderID 
        AND o.CustomerID = c.CustomerID
        AND c.Country = "Germany"
      GROUP BY p.ProductID
      ORDER BY SUM(Quantity) DESC
      LIMIT 1

***Note**: This question could also be asking about which product had the most orders (i.e. not unit sales, but separate orders), in which case* SUM(Quantity) *should be replaced by* COUNT(p.ProductID) *for an answer of Gorgonzola Telino*

