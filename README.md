# Voucher Management API Documentation

This API allows you to manage vouchers, including retrieving all vouchers, getting details of a specific voucher, and creating new vouchers.

**How to get started**
**create a virtual enviroment**
```
----
git clone https://github.com/ndingibr/voucher-redemption-api.git
cd app
python -m venv venv
source venv/bin/activate
----
# On Windows, use
`venv\Scripts\activate`
pip install -r requirements.txt
python app.py
```
NB: don't use docker-compose, it has a bug in connecting to the database that I didn't have enough time to troubleshoot

**Endpoints**: 
- **GET /vouchers**
  - Retrieve all vouchers.
- **GET /vouchers/<string:voucher_code>**
  - Retrieve details of a specific voucher by its code.
- **POST /vouchers**
  - Get all redeems.
- **GET /redeems**
  - Redeem a single voucher.
- **GET /redeem**
  - Redeem Multiple Vouchers.
- **POST /redeem-multiple**
  - Redeem multiple vouchers.
