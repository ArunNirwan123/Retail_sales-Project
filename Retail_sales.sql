SELECT * FROM project2.retail_sales;
-- 1. Total Revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM project2.retail_sales;

-- 2. Total Quantity
SELECT SUM(Quantity) AS Total_Quantity
FROM project2.retail_sales;

-- 3. Total Orders
SELECT COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM project2.retail_sales;

-- 4. Unique Customers
SELECT COUNT(DISTINCT CustomerID) AS Unique_Customers
FROM project2.retail_sales;

-- 5. Unique Products
SELECT COUNT(DISTINCT ProductName) AS Unique_Products
FROM project2.retail_sales;

-- 6. Country Count
SELECT COUNT(DISTINCT Country) AS Country_Count
FROM project2.retail_sales;

-- --GROUPBY

-- 7. Country-wise Revenue
SELECT Country,SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY Country ORDER BY Revenue DESC;

-- 8. Product-wise Revenue
SELECT ProductName,SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY ProductName ORDER BY Revenue DESC;

-- 9. Customer-wise Revenue
SELECT CustomerID, SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY CustomerID ORDER BY Revenue DESC;

-- 10. Monthly Revenue
SELECT Year, Month,SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY Year, Month 
ORDER BY Year, Month;

-- 11. Day-wise Revenue
SELECT DATE(InvoiceDate) AS Sale_Date, SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY DATE(InvoiceDate) ORDER BY Sale_Date;

-- 12. SalesChannel-wise Revenue
SELECT SalesChannel, SUM(Revenue) AS Revenue
FROM project2.retail_sales
GROUP BY SalesChannel ORDER BY Revenue DESC;

