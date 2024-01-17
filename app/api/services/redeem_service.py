from api.services.voucher_service import VoucherServicefrom api.models.redeem import RedeemModelfrom api.models.redeem import redeem_schemafrom datetime import datetimefrom api import dbclass RedeemService:    @staticmethod    def validate_redemption(voucher, user_id, amount, products_redeemed):        """        Validate redemption based on voucher attributes.            Args:            voucher (VoucherModel): Voucher object to be redeemed.            user_id (str): ID of the user attempting redemption.            products_redeemed (str): List of products redeemed.            Returns:            dict: Dictionary indicating the result of the validation.                - If successful: {'success': 'Redemption validation passed'}                - If unsuccessful: {'error': 'Reason for validation failure'}        """        # Check if the voucher is expired based on expiration_date        if voucher.expiration_date < datetime.now().date():            return {'error': f'Validation failed: Voucher {voucher.code} has expired'}            # Validate for redemption limit        redeem_count = RedeemModel.query.filter_by(voucher_code=voucher.code).count()            if redeem_count >= voucher.redemption_limit:            return {'error': f'Validation failed: Redemption limit exceeded for voucher {voucher.code}'}            # Validate for the amount        redeem_sum = RedeemModel.query.filter_by(voucher_code=voucher.code).with_entities(db.func.sum(RedeemModel.amount)).scalar() or 0            if redeem_sum + amount > voucher.value:            return {'error': f'Validation failed: Amount exceeded for voucher {voucher.code}'}            # Validate user ID against user_restrictions if not None        if voucher.user_restrictions is not None:            if user_id in voucher.user_restrictions.split(','):                return {'error': f'Validation failed: {user_id} is not allowed to redeem voucher {voucher.code}'}            # Validate products_redeemed against voucher.products if not None        if voucher.products is not None:            for product_redeemed in products_redeemed.split(','):                if product_redeemed not in voucher.products.split(','):                    return {'error': f'Validation failed: {product_redeemed} is not associated with the voucher.'}            return {'success': 'Redemption validation passed'}    @classmethod    def get_all_redeems(cls):        """        Get all redemption records.        Returns:            list: List of redemption records.        """        try:            # Query all redeems from the database            redeems = RedeemModel.query.all()            # Serialize the redeems using the redeem_schema            result = redeem_schema.dump(redeems, many=True)            return result        except Exception as e:            # Raise a ValueError with the error message            raise ValueError(str(e))    @classmethod    def redeem_voucher(cls, voucher_code, user_id=None, transaction_id=None, staff_id=None, created_date=None, products_redeemed=None, amount=None, discount=None):        """        Redeem a voucher.        Args:            voucher_code (str): Code of the voucher to be redeemed.            user_id (str, optional): ID of the user attempting redemption. Defaults to None.            transaction_id (str, optional): Transaction ID. Defaults to None.            staff_id (str, optional): ID of the staff member processing the redemption. Defaults to None.            products_redeemed (str, optional): List of products redeemed. Defaults to None.        Returns:            dict: Dictionary indicating the result of the redemption.                - If successful: {'success': 'Voucher redeemed successfully', 'redeem': created_redeem}                - If unsuccessful: {'error': 'Reason for failure'}        """        try:            # Retrieve the voucher using VoucherService            voucher = VoucherService.get_voucher_by_code(voucher_code)            # Check if the voucher exists            if voucher is None:                raise ValueError(f'Voucher with code {voucher_code} not found')            # Validate the redemption using the validate_redemption method            validation_result = cls.validate_redemption(voucher, user_id, amount, products_redeemed)                        if 'error' in validation_result:                raise ValueError(validation_result['error'])            # Create a new RedeemModel instance            redeem = RedeemModel(                created_date=datetime.now(),                voucher_code=voucher.code,                user_id=user_id,                transaction_id=transaction_id,                staff_id=staff_id,                products_redeemed=products_redeemed,                amount=amount,                discount=discount,                net_amount=voucher.value - voucher.discount            )            # Add the redemption record to the database and commit changes            db.session.add(redeem)            db.session.commit()            # Serialize the created redeem object using redeem_schema            created_redeem = redeem_schema.dump(redeem)            return {'success': 'Voucher redeemed successfully', 'redeem': created_redeem}        except Exception as e:            # Raise a ValueError with the error message            raise ValueError(str(e))