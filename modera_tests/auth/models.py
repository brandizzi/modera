import unittest2 as unittest
import hashlib

import modera.db
import modera.util
from modera.auth.db.models import User

class ModelsTestCase(unittest.TestCase):

    def test_hash_password(self):
        u = User('Juliana Vilela', 'juju', password='1234')
        self.assertEquals(u.password,  
                hashlib.sha224('1234'+modera.util.salt()).hexdigest())
        u = User('Juliana Vilela', 'juju', password='1234', hash_password=False)
        self.assertEquals(u.password, '1234')
    
    
    def setUp(self):
        self.engine = modera.db.get_db_engine('sqlite:///:memory:')
        self.session = modera.db.create_session(self.engine)
        modera.db.create_tables_for_entities(User, self.engine)
        
