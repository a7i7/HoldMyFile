'''Unit tests for legofy'''
# They can be run individually, for example:
# nosetests tests.test_legofy:Create.test_legofy_image
import os
import unittest
import holdmyfile
import random

TEST_DIR = os.path.realpath(os.path.dirname(__file__))
TEST_FILE = os.path.join(TEST_DIR, 'test_data', 'test_file.txt')
TEMP_FILE = os.path.join(TEST_DIR, 'test_data', 'new_file.txt')

class HelperFunctions(unittest.TestCase):

    def test_convert_to_two_bytes(self):
    	"""Can we convert any ascii character to two bytes?"""
    	self.assertEqual(holdmyfile.helper.convert_to_two_bytes(chr(210)),'nc')
    	self.assertEqual(holdmyfile.helper.convert_to_two_bytes(chr(0)),'aa')
    	self.assertEqual(holdmyfile.helper.convert_to_two_bytes(chr(255)),'pp')

    def test_convert_back_from_two_bytes(self):
    	"""Can we convert back from the two bytes to ascii"""
    	self.assertEqual(39,holdmyfile.helper.convert_back_from_two_bytes('bx'))
    	self.assertEqual(255,holdmyfile.helper.convert_back_from_two_bytes('pp'))

    def test_inverse_property(self):
    	"""Are the functions inverses of each other"""
    	ascii_value = 139
    	two_bytes = holdmyfile.helper.convert_to_two_bytes(chr(ascii_value))
    	ascii_value_back = holdmyfile.helper.convert_back_from_two_bytes(two_bytes)
    	self.assertEqual(ascii_value,ascii_value_back)    	

    def test_data_upload_download(self):
    	"""Can data be uploaded and downloaded"""
    	content = "This is a sample test string"
    	resp = holdmyfile.helper.netcat('termbin.com',9999,content)
    	self.assertNotEqual(len(resp),0)
    	data_uploaded = holdmyfile.helper.retrieve_from_url(resp)
    	self.assertEqual(data_uploaded,content)

class FileDataTest(unittest.TestCase):

	def test_file_backup_and_restore(self):
		"""Can we backup data and restore it"""
		#upload it
		test_file = holdmyfile.FileData(TEST_FILE)
		retrieved_id = test_file.backup_file()
		#download it
		restore_test_file = holdmyfile.FileData(retrieved_id)
		restore_test_file.restore_file(TEMP_FILE)

		#get_content
		test_file_data=''
		temp_file_data=''

		for data in open(TEST_FILE,'r'):
			test_file_data+=data

		for data in open(TEMP_FILE,'r'):
			temp_file_data+=data
		
		#remove temp file
		os.remove(TEMP_FILE)

		#compare
		self.assertEqual(test_file_data,temp_file_data)

if __name__ == '__main__':
    unittest.main()
