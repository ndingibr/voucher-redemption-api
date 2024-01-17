import pytest
import os

def run_tests():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = current_dir + '/tests/test_voucher_routes.py'
    print(test_file)
    pytest.main([test_file])
    
    test_file = current_dir + '/tests/test_redeem_routes.py'
    print(test_file)
    pytest.main([test_file])
    
if __name__ == "__main__":
    # Run tests if the script is executed directly
    run_tests()


