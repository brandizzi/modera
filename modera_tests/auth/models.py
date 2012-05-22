import unittest2 as unittest
import hashlib

import modera.db
import modera.util
import modera_config
from modera.auth.db.models import User, authenticate

class ModelsTestCase(unittest.TestCase):

    def test_hash_password(self):
        u = User('Juliana Vilela', 'juju', password='1234')
        self.assertEquals(u.password,  
                hashlib.sha224('1234'+modera.util.salt()).hexdigest())
        u = User('Juliana Vilela', 'juju', password='1234', hash_password=False)
        self.assertEquals(u.password, '1234')

    def test_authenticate(self):
        juju = User('Juliana Vilela', 'juju', password='1234')
        self.session.add(juju)

        u = authenticate('nouser', 'nopassword')
        self.assertIsNone(u)
        
        u = authenticate('juju', 'wrongpass')
        self.assertIsNone(u)
        u = authenticate('juju', '1234')
        self.assertIsNotNone(u)
        self.assertEquals(u, juju)
    
    def setUp(self):
        modera_config.MODERA_CONFIG['DATABASE_URI'] = 'sqlite:///:memory:'
        self.session = modera.db.create_session()
        modera.db.create_tables_for_entities(User)
    
    def tearDown(self):
        self.session.close()
