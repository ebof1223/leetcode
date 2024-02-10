select
  product_name, year, price
from product
right join sales
on sales.product_id = product.product_id