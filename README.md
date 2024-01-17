# Voucher Management API Documentation

This API allows you to manage vouchers, including retrieving all vouchers, getting details of a specific voucher, and creating new vouchers.

**How to get started**
**create a virtual enviroment**
```
git clone https://github.com/your-username/your-flask-app.git
cd your-flask-app
python -m venv venv
source venv/bin/activate
# On Windows, use
`venv\Scripts\activate`
pip install -r requirements.txt
python app.py
```
**Endpoints**: 
- **GET /vouchers**
  - *Description*: Retrieve all vouchers.

- **GET /vouchers/<string:voucher_code>**
  - *Description*: Retrieve details of a specific voucher by its code.

- **POST /vouchers**
  - *Description*: Get all redeems.

- **GET /redeems**
  - *Description*: Redeem a single voucher.

- **GET /redeem**
  - *Description*: Redeem Multiple Vouchers.

- **POST /redeem-multiple**
  - *Description*: Redeem multiple vouchers.
