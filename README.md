


## Management Panel
- **URL:** `http://127.0.0.1:8000/`
  - **Description:** Displays the options available in the management panel.

## Order Management
- **Get Orders Sorted by Name**
  - **URL:** `http://127.0.0.1:8000/order/order/<str:name>`
  - **Description:** Retrieves orders sorted by the customer's name, specifically ordered by the highest total price.

- **Get Customer Invoices**
  - **URL:** `http://127.0.0.1:8000/order/accounts/<str:name>`
  - **Description:** Fetches all invoices associated with a specific customer identified by their name.

## Product Management
- **Get All Products**
  - **URL:** `http://127.0.0.1:8000/prodact`
  - **Description:** Retrieves a list of all available products.

- **Get Products Sorted by Name**
  - **URL:** `http://127.0.0.1:8000/prodact/<str:name>`
  - **Description:** Retrieves products sorted by name, specifically ordered by the highest rating.

- **Search Products**
  - **URL:** `http://127.0.0.1:8000/search=<str:searchs>`
  - **Description:** Searches for products based on the specified search term in the name field.

## Product Management (Admin)
- **Add Product**
  - **URL:** `http://127.0.0.1:8000/manager`
  - **Description:** Endpoint for adding new products to the inventory.

- **Edit or Delete Product**
  - **URL:** `http://127.0.0.1:8000/manager/<int:pk>`
  - **Description:** Allows editing or deleting a product based on its unique identifier (ID).


