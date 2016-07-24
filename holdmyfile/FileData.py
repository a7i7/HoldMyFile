from helper import *
class FileData:

	def __init__(self,file_address):
		self._content = None
		if file_address.startswith('http://termbin.com'):
			self.file_url = file_address
			self.backed_up = True
			self._encoded_file_content = retrive_from_url(file_address)
			self.file_content = None
		else:
			self.file_path = file_address
			self.backed_up = False
			self._encoded_file_content = None
			self.file_content = retrive_from_file(file_address)

	def _get_content(self):
		if self.file_content==None:
			start_index = 1
			end_index = self._encoded_file_content.index('}')

			if start_index>end_index:
				raise ValueError
			
			self.file_content = self._encoded_file_content[end_index+1:]
			self.file_path = self._encoded_file_content[start_index:end_index].split(':')[1]
		return self.file_content

	def _encode_content(self):
		if self._encoded_file_content==None:
			self._encoded_file_content = '{path:'+self.file_path+'}'+self.file_content
		return self._encoded_file_content

	def backup_file(self):
		if self.backed_up:
			return
		self._encode_content()
		self.file_url = netcat('termbin.com',9999,self._encoded_file_content)
		self.backed_up = True
		return self.file_url

	def restore_file(self):
		content = self._get_content()
		file = open(self.file_path,'wb')
		start_index = 0
		while start_index<len(content):
			current_character = content[start_index:start_index+3]
			file.write(chr(int(current_character)))
			start_index+=3
		file.close()
		return self.file_path