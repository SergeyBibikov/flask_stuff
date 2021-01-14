from argon2 import PasswordHasher


def hash_pass(password):
    hasher = PasswordHasher(time_cost=4,hash_len=32,salt_len=32)
    hash = hasher.hash(password)
    return hash

def is_passw_correct(hash, password):
    hasher = PasswordHasher(time_cost=4,hash_len=32,salt_len=32)
    try:
        result = hasher.verify(hash,password)
    except:
        result = False
    return result