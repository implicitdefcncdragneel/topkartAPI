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
