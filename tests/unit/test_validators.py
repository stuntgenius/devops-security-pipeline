from src.utils.validators import validate_email

def test_email_validation():
    assert validate_email('test@example.com') == True
    assert validate_email('invalid-email') == False
