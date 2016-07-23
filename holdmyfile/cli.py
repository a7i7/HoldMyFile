import click
import holdmyfile
@click.command()
@click.argument('mode',type=str,required=True)
@click.argument('file_details',type=str,required=True)

def main(mode,file_details):
	"""This program is used to temporarily just backup your files on the web. 
	The absolute file address is also stored. So you can just restore the files backs with a single command.
	This program is specially useful when you are experimenting with changes to a file that may later turn out to be hazardous for your system.
	
	To back up a file:
	holdmyfile give /home/dave/file.txt
	File Backed up successfully. Id is qvje
	
	To restore it again:
	holdmyfile take qvje
	File Restored successfully. File address is /home/dave/file.txt
	"""
	if mode=="give":
		holdmyfile.backup(file_details)
	elif mode=="take":
		holdmyfile.restore(file_details)
	else:
		click.echo("Invalid Mode. Can take one of the following values: give,take")


