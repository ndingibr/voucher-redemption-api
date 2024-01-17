# Voucher Management API Documentation

This API allows you to manage vouchers, including retrieving all vouchers, getting details of a specific voucher, and creating new vouchers.

## 1. Get All Vouchers

**Endpoint**: `GET /vouchers`

**Description**: Retrieve all vouchers.

**Response**: JSON response containing a list of voucher objects.

## 2. Get Voucher by Code

**Endpoint**: `GET /vouchers/<string:voucher_code>`

**Description**: Retrieve details of a specific voucher by its code.

**Parameters**:
- `voucher_code` (string, required): The unique code of the voucher.

**Response**: JSON response containing voucher details or an error message.

## 3. Create Voucher

**Endpoint**: `POST /vouchers`

**Description**: Create a new voucher.

**Request Body**:
```json
{
  "code": "V0001",
  "type": "gift voucher",
  "value": 100.0,
  "discount": 0,
  "expiration_date": "2024-10-30",
  "redemption_limit": 50,
  "user_restrictions": "user_1,user_2",
  "products": "product_a,product_b"
}
