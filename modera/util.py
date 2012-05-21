import hashlib

from modera_config import MODERA_CONFIG

def salt():
    return MODERA_CONFIG['SALT'] \
            if 'SALT' in MODERA_CONFIG \
            else 'aI(*ojT0Ht-BAlJe' # A placeholder value

def get_hashed_password(password):
    return hashlib.sha224(password + salt()).hexdigest()
