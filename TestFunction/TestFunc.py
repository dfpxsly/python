import unittest

def getName(first,last):
    full_name=first+' '+last
    return full_name.title()

class NameTest(unittest.TestCase):
    def test1(self):
        f_name=getName('gao','shan')
        self.assertEqual(f_name,'Gao Shan')

unittest.main()
