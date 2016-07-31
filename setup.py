from setuptools import setup

setup(
	name='holdmyfile',
	version='1.0',
	author='Afif Ahmed',
	author_email='getafif22@gmail.com',
	url='https://github.com/a7i7',
	packages=['holdmyfile'],
	description='Backup files online or restore them back with just one easy command',
	install_requires=['click'],
	entry_points={
		'console_scripts': [
			'holdmyfile = holdmyfile.cli:main'
		]
	},
	test_suite="tests"
)
