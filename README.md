# Topkart Lightning Deals API

This API handles lightning deals for Topkart, a global e-commerce website. Lightning deals are time-limited discounted products available on the website. The API provides functionality for both admins and customers, allowing them to manage and participate in lightning deals.

## Lightning Deal Structure

A lightning deal consists of the following data points:

- Product Name
- Actual Price & Final Price
- Total Units & Available Units
- Expiry Time


## Requirements

The API should fulfill the following requirements:

- Users should not be able to place an order for an expired deal.
- Admins can create and update lightning deals.
- Admins can approve orders.
- Customers can access available unexpired deals.
- Customers can place orders.
- Customers can check the status of their orders.

## Installation and Setup

1. Clone the repository or download the source code.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Alternatively use `docker-compose up` for running the application.
4. The API will be accessible at the specified base URL.

# API Endpoints

## User Authentication/Authorization API

- `POST /api/account/customer/` - Create a customer user.
- `POST /api/account/tadmin/` - Create a Admin user.
- `POST /api/account/login/` - Obtain an access token by providing valid credentials.
- `POST /api/account/refresh/token/` - Refresh an expired access token.

## Product API

- `GET /api/product/lightningdeal/` - Retrieve a list of Product for Admin user.
- `POST /api/product/lightningdeal/` - Create Product by the Admin user.
- `PATCH /api/product/lightningdeal/{product_id}/` - Update the product for the given product ID.

## Order API

- `GET /api/order/lightningdeal/` - Retrieve a list of Product which are categorize as lightningdeal.
- `POST /api/order/{product_id}/` - Create Order for the Product.
- `GET /api/order/status/` - View status of all order placed by a user.
- `GET /api/order/status/{order_id}` - View status of specific order placed by a user.
- `PATCH /api/order/action/{order_id}/` - Admin can modify the status of order by "Approved" or "Rejected".


## Contact

For any questions or inquiries, please contact [chandranandan.chandrakar@gmail.com](mailto:chandranandan.chandrakar@gmail.com).

**Note:** 
Use the `topKart.postman_collection.json` attached with the repository to test the API.