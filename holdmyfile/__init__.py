import os
from FileData import FileData
from urllib2 import HTTPError

def backup(file_path):
	file_path = os.path.abspath(file_path)
	try:
		file_data = FileData(file_path)
	except IOError:
		print "Unable to backup file. File Address invalid"
		return

	file_data.backup_file()
	url = file_data.file_url
	id_start_index = url.rfind('/')+1
	print "File Backed up successfully. Note down the id: %s " %url[id_start_index:]

def restore(file_id):
	file_url = "http://termbin.com/"+file_id
	try:
		file_data = FileData(file_url)
		file_path = file_data.restore_file()
	except HTTPError:
		print "Invalid id. File does not exist online"
		return
	except ValueError:
		print "Invalid formatting of text. Could not extract text"
		return

	print "File Restored successfully. File address is %s" %file_path

