# Courier Kata
## Features
Given the parcel size and weight, calculate the delivery cost. Speedy order option available with higher cost.
### Size
- Small parcel: all dimensions < 10cm. 1kg. Cost $3
- Medium parcel: all dimensions < 50cm. 3kg. Cost $8
- Large parcel: all dimensions < 100cm. 6kg. Cost $15
- XL parcel: any dimension >= 100cm. 10kg. Cost $25
- Heavy parcel: 50kg. Cost $50.
### Extra weight
Parcels which exceed weight limit are charged extra $2/kg,
except for heavy parcels, which is charged +$1/kg.
### Discount
- Small parcel mania! Every 4th small parcel in an order is free!
- Medium parcel mania! Every 3rd medium parcel in an order is free!
- Mixed parcel mania! Every 5th parcel in an order is free!
- Each parcel can only be used in a discount once
- Within each discount, the cheapest parcel is the free one
- The combination of discounts which saves the most money should be selected every
time
### Speedy Shipping
- Speedy shipping: double total cost
## Usage
Add the folder `courier_kata` to your Python project. 
```Python
from courier_kata.order import Order
from courier_kata.parcel_builder import ParcelBuilder
```
Create the `ParcelBuilder` object, which can be shared among
different orders.
```Python
parcel_builder = ParcelBuilder()
```
Order take one parameter, True for speedy order,
False for normal speed order.
```Python
order = Order(True)
```
Create a parcel object, 
the first 3 parameters are the dimensions in cm, 
last parameter is weight in kg.
Repeat this step to add more parcels.
```python
parcel = parcel_builder.build_parcel(1, 5, 9, 1)
order.add_order(parcel)
```
Get total cost of orders
```python
order.get_total_cost()
```

