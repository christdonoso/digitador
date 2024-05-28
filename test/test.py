import unittest
from utilities import general, data_reader

class UtilitiesFuncions(unittest.TestCase):

    def test_untuple_zip(self):
        data = data_reader.get_data('Tamizaje Los Rios 2024.xlsx')
        validate = general.untuple_zip(data['RUT'], data['RBD'])
        self.assertAlmostEqual(validate[0],isinstance(validate[0], list) )



