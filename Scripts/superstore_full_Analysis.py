import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#Stage 1: Project Setup and Dataset Understanding 
df = pd.read_excel("Superstore.xlsx")

print("\nNumber of Rows and Columns")
print(df.shape)

print("\nColumns Names")
print(df.columns)

print("\nData Types")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("Statistical Summary")
print(df.describe())


#Stage 2: Sales & Profit Overview 

#Sales Analysis 
print("\nTotal Sales")
print(df["Sales"].sum())

print("\nAverage Sales")
print(df["Sales"].mean())

print("\nHighest Sales")
print(df["Sales"].max())

print("\nLowest Sales")
print(df["Sales"].min())

#Profit Analysis 
print("\nTotal Profit")
print(df["Profit"].sum())

print("\nAverage Profit")
print(df["Profit"].mean())

print("\nHighest Profit")
print(df["Profit"].max())

print("\nLowest Profit")
print(df["Profit"].min())


#Stage 3: Products Analysis 
print("\nTop 10 Products by Sales")
top_product_sales = (
df.groupby("Product Name")["Sales"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_product_sales )

print("\nBottom 10 Products by Sales")
bottom_product_sales = (
df.groupby("Product Name")["Sales"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_product_sales)

print("\nTop 10 Products by Profit")
top_profit_products = (
df.groupby("Product Name")["Profit"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_profit_products)

print("\nBottom 10 Products by Profit")
bottom_profit_products = (
df.groupby("Product Name")["Profit"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_profit_products)

print("\nTop 10 Products by Quantity Sold")
quantity_product_sales  =(
df.groupby("Product Name")["Quantity"]. sum()
.sort_values(ascending=False)
.head(10))

print(quantity_product_sales)


#Step 4: Category and Sub-Category Analysis 
print("\nCategory by Sales")
category_sales = (
df.groupby("Category")["Sales"]. sum()
.sort_values(ascending=False))

print(category_sales)


print("\nCategory by Profit")
category_proft = (
df.groupby("Category")["Profit"]. sum()
.sort_values(ascending=False))

print(category_proft)

print("\nCategory by Quantity")
category_quantity = (
df.groupby("Category")["Quantity"].sum()
.sort_values(ascending=False))

print(category_quantity)

#Sub-Category Analysis 
print("\nTop 10 Sub-Category by Sales")
subcategory_sales = (
df.groupby("Sub-Category")["Sales"]. sum()
.sort_values(ascending=False)
.head(10))

print(subcategory_sales)

print("\nBottom 10 Sub-Category by Sales")
bottom_subcategory_sales = (
df.groupby("Sub-Category")["Sales"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_subcategory_sales )

print("\nTop 10 Sub-Category by Profit")
top_subcategory_profit = (
df.groupby("Sub-Category")["Profit"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_subcategory_profit)

print("\nBottom 10 Sub-Category Profit")
bottom_subcategory_profit = (
df.groupby("Sub-Category")["Profit"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_subcategory_profit)

print("\nTop 10 Sub-Category by Quantity Sold")
top_subcategory_quantity = (
df.groupby("Sub-Category")["Quantity"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_subcategory_quantity)

print("\nBottom 10 Sub-Category by Quantity")

bottom_subcategory_quantity = (
df.groupby("Sub-Category")["Quantity"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_subcategory_quantity)


#Stage 5: Customers Analysis 
print("\nTop 10 Customers by Sales")
top_customer_sales = (
df.groupby("Customer Name")["Sales"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_customer_sales)

print("\nBottom 10 Customers by Sales")
bottom_customer_sales = (
df.groupby("Customer Name")["Sales"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_customer_sales)

print("\nTop 10 Customers by Profit")
top_customer_profit = (
df.groupby("Customer Name")["Profit"]. sum()
.sort_values(ascending=False)
.head(10))

print (top_customer_profit)

print ("\nBottom 10 Customers by Profit")
bottom_customer_profit = (
df.groupby ("Customer Name")["Profit"].sum()
.sort_values (ascending =True)
.head(10))

print(bottom_customer_profit)

print("\nNumber of Orders Per Customers")

no_order_per_customer = (
df.groupby("Customer Name")["Order ID"]. count()
.sort_values (ascending =False)
.head(10))

print(no_order_per_customer)

print("\nAverage Sales Per Customers")
average_sales_customer = (
df.groupby("Customer Name")["Sales"]. mean()
.sort_values(ascending=False))

print(average_sales_customer)


#Stage 6:  Region & State Analysis 
#Region Analysis 
print("\nSales by Region")
region_sales = (
df.groupby("Region")["Sales"]. sum()
.sort_values(ascending=False))

print(region_sales)

print("\nProfit by Region")
region_profit = (
df.groupby("Region")["Profit"]. sum()
.sort_values(ascending=False))

print(region_profit)

#State Analysis 
print("\nTop 10 States by Sales")
top_state_sales = (
df.groupby("State")["Sales"]. sum()
.sort_values(ascending=False)
.head(10))

print(top_state_sales)

print("\nBottom 10 States by Sales")
bottom_state_sales = (
df.groupby("State")["Sales"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_state_sales)

print ("\nTop 10 States by Profit")
top_state_profit = (
df.groupby("State")["Profit"]. sum()
.sort_values(ascending=False)
.head(10))

print (top_state_profit)

print("\nBottom 10 States by Profit")
bottom_state_profit = (
df.groupby("State")["Profit"]. sum()
.sort_values(ascending=True)
.head(10))

print(bottom_state_profit)

#===================================
#STAGE 7: TIME SERIES ANALYSIS 
#===================================

#Year Analysis 
#Extracting Year from the dataframe 

print("\nTotal Sales for each Year")
df["Year"]= df["Order Date"].dt.year
year_sales = (
df.groupby("Year")["Sales"]. sum()
.sort_index())

print(year_sales)

print("\nTotal Profit for each Year")
year_profit = (
df.groupby("Year")["Profit"]. sum()
.sort_index())

print(year_profit)

#Quarter Analysis 
print("\nTotal Sales for each Quarter")
df["Quarter"] = df["Order Date"].dt.quarter
quarterly_sales = (
df.groupby("Quarter")["Sales"]. sum()
.sort_index())

print(quarterly_sales)

print("\nTotal Profit for each Quarter")
quarterly_profit = (
df.groupby("Quarter")["Profit"]. sum()
.sort_index())

print(quarterly_profit)

#Month Analysis 
df["Month"] = df["Order Date"].dt.month 

print("\nTotal Sales by each month")
monthly_sales = (
df.groupby("Month")["Sales"]. sum()
.sort_index())

print (monthly_sales)

print("\nTotal Profit for each Month")
monthly_profit = (
df.groupby("Month")["Profit"]. sum()
.sort_values())

print(monthly_profit)

#===================================
# STAGE 8 & 9:       FILTERING ANALYSIS 
#===================================

#Region Filter
print("\nWest Region") 
west_region = df[df["Region"] == "West"]

print(west_region)


print("\nEast Region")
east_region = df[df["Region"] == "East"]

print(east_region)

print("\nSouth Region")
south_region = df[df["Region"] == "South"]
print(south_region)

#Category Filter 
print("\nTECHNOLOGY PRODUCTS")
technology = df[df["Category"] == "Technology"]
print(technology)

print("\nOFFICE SUPPLIES PRODUCTS")
office_supplies = df[df["Category"] == "Office Supplies"]

print(office_supplies)

#State Filter 
print("\nOnly California")
california = df[df["State"] =="California"]
print(california)

print("\nOnly Texas")
texas = df[df["State"]  == "Texas"]
print(texas)


#Sub-Category Business Analysis 
#filter Table and Analyze it
table = df[df["Sub-Category"] == "Tables"]

print("\nTotal Sales")
print(round(table["Sales"].sum(), 2))

print("\nTotal Profit")
print(round(table["Profit"]. sum(), 2))

# after checking, Table had a total sales 

# now let print Average 
print("\nAverage Discount") 
print(table["Discount"].mean())

#let print the total order
print("\nTotal Order")
print(len(table))


# Chairs Analysis 
chair = df[df["Sub-Category"] == "Chairs"]
print("\nTotal Sales")
print(chair["Sales"].sum())

print("\nTotal Profit")
print(chair["Profit"].sum())

print("\nAverage Discount")
print(chair["Discount"].mean())

print ("\nTotal Order")
print(len(chair))

#Phone Analysis 
phone = df[df["Sub-Category"] == "Phones"]

print("\nTotal Sales")
print(phone["Sales"].sum())

print ("\nTotal Profit")
print(phone["Profit"].sum())

print("\nAverage Discount")
print(phone["Discount"].mean())

print("\nTotal Orders")
print(len(phone))

#Copier Analysis 
print ("\nCopier Analysis ")
copier = df[df["Sub-Category"] == "Copiers"]
print(copier["Discount"].mean())

print("\nCopier Sales ")
copier_sales= (copier["Sales"].sum())
print(copier_sales)

print("\nCopier Profit")
copier_profit  = (copier["Profit"].sum())

print(copier_profit)

print("\nTotal Orders")
print(len(copier))

#Category Analysis 
#Furniture Analysis 
furniture = df[df["Category"] == "Furniture"]
print("\nFurniture Analysis")
print("\nTotal Sales ")
print(furniture["Sales"].sum())

print("\nTotal Profit")
print(furniture["Profit"].sum())

print("\nAverage Discount")
print(furniture["Discount"].mean())

print("\nTotal Orders")
print(len(furniture))

#Technology Analysis 
print("\nTechnology Analysis")
technology = df[df["Category"] == "Technology"]

print("\nTotal Sales")
print(technology["Sales"].sum())

print("\nTotal Profit")
print(technology["Profit"].sum())

print("\nAverage Discount")
print(technology["Discount"].mean())

print("\nTotal Orders")
print(len(technology))

#Office Supplies Analysis 
print("\nOffice Supplier Analysis")
office_supply = df[df["Category"] == "Office Supplies"]

print("\nTotal Sales")
print(office_supply["Sales"]. sum())

print("\nTotal Profit")
print(office_supply["Profit"].sum())

print("\nAverage Discount")
print(office_supply["Discount"].mean())

print("\nTotal Orders")
print(len(office_supply))

#States Analysis 
print("\nState Analysis")
print("\nTexas Analysis")
texas = df[df["State"] == "Texas"]

#Texas Analysis 
print("\nTotal Sales")
print(texas["Sales"].sum())

print ("\nTotal Profit")
print(texas["Profit"]. sum())

print("\nAverage Discount")
print(texas["Discount"]. mean())

print("\nTotal Orders")
print(len(texas))

#New York Analysis 
print("\nNew York Analysis")

new_york = df[df["State"] == "New York"]
print("\nTotal Sales")
print(new_york["Sales"].sum())

print("\nTotal Profit")
print(new_york["Profit"].sum())

print("\nAverage Discount")
print(new_york["Discount"].mean())

print("\nTotal Orders")
print(len(new_york))

#Profit Analysis 
print("\nProfit Analysis")

gain= df[df["Profit"] >0]
print("\nProfit Greater than Zero (Gain)")

print("\nTotal Number of Orders")
print(len(gain))

print("\nTotal Profit")
print(round(gain["Profit"]. sum(), 2))

print("\nAverage Profit")
print(round(gain["Profit"].mean(), 2))

print("\nAverage Discount on Gain")
print(round(gain["Discount"].mean(), 2))

print("\nProfit Less than Zero (Loss-Making Order or Loss)")

loss = df[df["Profit"] < 0]

print("\nTotal Number of Orders")
print(len(loss))

print("\nTotal Loss")
print(round(loss["Profit"].sum(), 2))

print("\nAverage Loss")
print(round(loss["Profit"].mean(), 2))

print("\nAverage Discount on Loss")
print(round(loss["Discount"].mean(), 2))

#Discount Analysis 
print("\nDiscount Analysis")

zero_discount = df[df["Discount"] == 0]
print("\nZero Discount Analysis")

print("\nTotal Sales ")
print(round(zero_discount["Sales"].sum(), 2))

print ("\nTotal Profit")
print(round(zero_discount["Profit"].sum(), 2))

print("\nNumber of  Orders")
print(len(zero_discount))

print("\nDiscounted Order Analysis")

discounted_order = df[df["Discount"] > 0]
print("\nTotal Sales")
print(round(discounted_order["Sales"].sum(), 2))

print("\nTotal Profit")
print(round(discounted_order["Profit"].sum(), 2))

print("\nOverall Profit")
overall_profit = (zero_discount["Profit"].sum()) + (discounted_order["Profit"].sum())

print(round(overall_profit, 2))


#===================================
#STAGE 10: DASHBOARD CHARTS ANALYSIS 
#===================================
#chart 1: Total Sales by Year

df["Year"] = df["Order Date"].dt.year
yearly_sales = (
df.groupby("Year")["Sales"]. sum()
.sort_index())
print(yearly_sales)

plt.figure (figsize =(10, 5))
yearly_sales.plot(kind ="bar")

for i, value in enumerate(yearly_sales.values):
	plt.text(i, value+10000, f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Total Sales by Year")
plt.xlabel ("Year")
plt.ylabel ("Total Sales")

plt.tight_layout ()
plt.savefig("superstore_sales_by_year.png")
plt.close()


#chart 2: Total Profit by Year

df["Year"] = df["Order Date"].dt.year
yearly_profit = (
df.groupby("Year")["Profit"]. sum()
.sort_index())
print(yearly_profit)

plt.figure (figsize =(10, 5))
yearly_profit.plot(kind ="bar")

for i, value in enumerate(yearly_profit.values):
	plt.text(i, value+500, f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Total Profit by Year")
plt.xlabel ("Year")
plt.ylabel ("Total Profit")

plt.tight_layout ()
plt.savefig("superstore_profit_by_year.png")
plt.close()


#chart 3: Sales by Month 

df["Month"] = df["Order Date"].dt.month
monthly_sales = (
df.groupby("Month")["Sales"]. sum()
.sort_index())
print(monthly_sales)

plt.figure (figsize =(8, 5))
monthly_sales.plot(kind ="line", marker="o")

for i, value in enumerate(monthly_sales.values):
	plt.text(i, value+500, f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Total Monthly Sales")
plt.xlabel ("Month")
plt.ylabel ("Total Sales")

plt.tight_layout ()
plt.savefig("superstore_sales_by_month.png")
plt.close()

#chart 4: Total Profit by Month 

df["Month"] = df["Order Date"].dt.month
monthly_profit = (
df.groupby("Month")["Profit"]. sum()
.sort_index())
print(monthly_profit)

plt.figure (figsize =(8, 5))
monthly_profit.plot(kind ="line", marker="o")

for i, value in enumerate(monthly_profit.values):
	plt.text(i, value+500, f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Total Monthly Profit")
plt.xlabel ("Month")
plt.ylabel ("Total Profit")

plt.tight_layout ()
plt.savefig("superstore_Profit_by_month.png")
plt.close()


#chart 5: Total Sales by Quarter 

df["Quarter"] = df["Order Date"].dt.quarter 
quarterly_sales = (
df.groupby("Quarter")["Sales"]. sum()
.sort_index())
print(quarterly_sales)

plt.figure (figsize =(8, 5))
quarterly_sales.plot(kind ="barh")

for i, value in enumerate(quarterly_sales.values):
	plt.text(value+10000, i,  f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Total Quarterly Sales")
plt.xlabel ("Total Sales")
plt.ylabel ("Quarter")

plt.tight_layout ()
plt.savefig("superstore_sales_by_quarter.png")
plt.close()

#chart 6: Total Profit by Quarter 

df["Quarter"] = df["Order Date"].dt.quarter 
quarterly_profit = (
df.groupby("Quarter")["Profit"]. sum()
.sort_index())
print(quarterly_profit)

plt.figure (figsize =(8, 5))
quarterly_profit.plot(kind ="barh")

for i, value in enumerate(quarterly_profit.values):
	plt.text(value+500, i,  f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Total Quarterly Profit")
plt.xlabel ("Total Profit")
plt.ylabel ("Quarter")

plt.tight_layout ()
plt.savefig("superstore_profit_by_quarter.png")
plt.close()

#chart 7: Sales by Category 

category_sales = (
df.groupby("Category")["Sales"].sum()
.sort_values(ascending=False))
print(category_sales)

plt.figure (figsize =(8, 5))
category_sales.plot(kind ="bar")

for i, value in enumerate(category_sales.values):
	plt.text(i, value+10000,  f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Sales by Category")
plt.xlabel ("Categories")
plt.ylabel ("Total Sales")

plt.tight_layout ()
plt.savefig("superstore_sales_by_category.png")
plt.close()


#chart 8: Profit by Category 

category_profit = (
df.groupby("Category")["Profit"].sum()
.sort_values(ascending=False))
print(category_profit)

plt.figure (figsize =(8, 5))
category_profit.plot(kind ="bar")

for i, value in enumerate(category_profit.values):
	plt.text(i, value+1500,  f"${int(value):,}", ha="center",  fontsize=10)

plt.title ("Profit by Category")
plt.xlabel ("Categories")
plt.ylabel ("Total Profit")

plt.tight_layout ()
plt.savefig("superstore_profit_by_category.png")
plt.close()

#chart 9: Quantity Sold by Category 

category_quantity = (
df.groupby("Category")["Quantity"].sum()
.sort_values(ascending=False))
print(category_quantity)

plt.figure (figsize =(8, 5))
category_quantity.plot(kind ="bar")

for i, value in enumerate(category_quantity.values):
	plt.text(i, value+100,  f"{int(value):,}", ha="center",  fontsize=10)

plt.title ("Quantity Sold by Category")
plt.xlabel ("Categories")
plt.ylabel ("Quantity Ordered")

plt.tight_layout ()
plt.savefig("superstore_quantity_by_category.png")
plt.close()

#chart 10: Sales by Region 

region_sales = (
df.groupby("Region")["Sales"].sum()
.sort_values(ascending=False))
print(region_sales)

plt.figure (figsize =(8, 5))
region_sales.plot(kind ="barh")

for i, value in enumerate(region_sales.values):
	plt.text(value+10000, i, f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Sales by Region")
plt.xlabel ("Total Sales")
plt.ylabel ("Region")

plt.tight_layout ()
plt.savefig("superstore_sales_by_region.png")
plt.close()

#chart 11: Profit by Region 

region_profit = (
df.groupby("Region")["Profit"].sum()
.sort_values(ascending=False))
print(region_profit)

plt.figure (figsize =(8, 5))
region_profit.plot(kind ="barh")

for i, value in enumerate(region_profit.values):
	plt.text(value+1000, i,  f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Profit by Region")
plt.xlabel ("Total Profit")
plt.ylabel ("Region")

plt.tight_layout ()
plt.savefig("superstore_profit_by_region.png")
plt.close()

#chart 12: Top 10 State by Sales

top_state_sales = (
df.groupby("State")["Sales"].sum()
.sort_values(ascending=False)
.head(10))
print(top_state_sales)

plt.figure (figsize =(8, 5))
top_state_sales.plot(kind ="barh")

for i, value in enumerate(top_state_sales.values):
	plt.text(value+1000, i, f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Top 10 State by Sales")
plt.xlabel ("State")
plt.ylabel ("Total Sales")

plt.tight_layout ()
plt.savefig("superstore_sale_by_state.png")
plt.close()

#chart 13: Top 10 State by Profit

top_state_profit = (
df.groupby("State")["Profit"].sum()
.sort_values(ascending=False)
.head(10))
print(top_state_profit)

plt.figure (figsize =(8, 5))
top_state_profit.plot(kind ="barh")

for i, value in enumerate(top_state_profit.values):
	plt.text(value+1000, i, f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Top 10 State by profit")
plt.xlabel ("State")
plt.ylabel ("Total Profit")

plt.tight_layout ()
plt.savefig("superstore_profit_by_state.png")
plt.close()

#chart 14: Top 10 Product by Sales 

top_product_sales= (
df.groupby("Product Name")["Sales"].sum()
.sort_values(ascending=False)
.head(10))
print(top_product_sales)

plt.figure (figsize =(15, 5))
top_product_sales.plot(kind ="barh")

for i, value in enumerate(top_product_sales.values):
	plt.text(value+500, i, f"${int(value):,}", va="center",  fontsize=12)

plt.title ("Top 10 Products by Sales")
plt.xlabel ("Total Sales")
plt.ylabel ("Product Name")

plt.tight_layout ()
plt.savefig("superstore_product_sales.png")
plt.close()

#chart 15: Top 10 Product by Profit 

top_product_profit= (
df.groupby("Product Name")["Profit"].sum()
.sort_values(ascending=False)
.head(10))
print(top_product_profit)

plt.figure (figsize =(15, 5))
top_product_profit.plot(kind ="barh")

for i, value in enumerate(top_product_profit.values):
	plt.text(value+500, i, f"${int(value):,}", va="center",  fontsize=12)

plt.title ("Top 10 Products by Profit")
plt.xlabel ("Total Profit")
plt.ylabel ("Product Name")

plt.tight_layout ()
plt.savefig("superstore_product_profit.png")
plt.close()

#Chart 16: Top 10 Sub-Category by Sales 

subcategory_sales = (
df.groupby("Sub-Category")["Sales"].sum()
.sort_values(ascending=False)
.head(10))
print(subcategory_sales)

plt.figure (figsize =(8, 5))
subcategory_sales.plot(kind ="barh")

for i, value in enumerate(subcategory_sales.values):
	plt.text(value+5000, i, f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Sales by Sub-Category")
plt.xlabel ("Total Sales")
plt.ylabel ("Sub-Categories")

plt.tight_layout ()
plt.savefig("superstore_sales_by_sub-category.png")
plt.close()

#Chart 17: Top 10 Sub-Category by Profit 

subcategory_profit = (
df.groupby("Sub-Category")["Profit"].sum()
.sort_values(ascending=False)
.head(10))
print(subcategory_profit)

plt.figure (figsize =(8, 5))
subcategory_profit.plot(kind ="barh")

for i, value in enumerate(subcategory_profit.values):
	plt.text(value+100, i, f"${int(value):,}", va="center",  fontsize=10)

plt.title ("Profit by Sub-Category")
plt.xlabel ("Total Profit")
plt.ylabel ("Sub-Categories")

plt.tight_layout ()
plt.savefig("superstore_profit_by_sub-category.png")
plt.close()

#Discount Analysis
# Chart 18: Zero Discount VS Discounted Order Profit 
zero_discount = df[df["Discount"] == 0]
discounted_order = df[df["Discount"] > 0]

zero_discount_profit = zero_discount["Profit"].sum()
discounted_order_profit = discounted_order["Profit"].sum()

labels = ["Zero Discount", "Discounted Orders"]
profits = [zero_discount_profit, discounted_order_profit]

plt.figure(figsize=(7,5))

plt.bar(labels, profits)

for i, value in enumerate(profits):
    plt.text(i, value, f"${value:,.2f}",
             ha="center", va="bottom", fontsize=10)

plt.title("Zero Discount VS Discounted Order Profit")
plt.xlabel("Order Type")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("superstore_zero_discount_vs_discounted_order.png")
plt.close()






