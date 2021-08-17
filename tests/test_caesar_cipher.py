from caesar_cipher import __version__

from caesar_cipher.caesar_cipher import encrypt , decrypt ,crack
def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_a_string_with_a_given_shift():
    excepted = 'do rvn wvy yvt'
    actual =  encrypt('it was bad day',177)
    assert actual == excepted
    
def test_decrypt_a_previously_encrypted_string_with_the_same_shift():
    excepted = 'it was bad day'
    actual =  decrypt('do rvn wvy yvt',177)
    assert actual == excepted    
    
def test_encryption_should_handle_upper_and_lower_case_letters():
    excepted = 'do rVn wvY yvt'
    actual =  encrypt('it wAs baD day',177)
    assert actual == excepted
    
def test_encryption_should_allow_non_alpha_characters_but_ignore_them_including_white_space():
    excepted = 'do rvn wvy yvt'
    actual =  encrypt('it was bad day*&^%$##@!',177)
    assert actual == excepted      

def test_decrypt_a_previously_encrypted_string_with_the_same_shift():
    excepted = 'It was the best of times it was the worst of times'
    actual =  crack('Bm ptl max uxlm hy mbfxl bm ptl max phklm hy mbfxl')
    assert actual == excepted       