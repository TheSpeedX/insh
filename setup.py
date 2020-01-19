from distutils.core import setup


with open("README.md", "r") as fh:
	long_description = fh.read()
setup(
	name = 'insulter',
    version = '1.0',
    description = 'Insults You When You Get An Error',
    long_description=long_description,  
    long_description_content_type='text/markdown', 

    author='TheSpeedX',
    author_email='ggspeedx29@gmail.com',
	url = 'https://github.com/TheSpeedX/insh',
	download_url ="https://github.com/TheSpeedX/insh/archive/master.zip",
	keywords = ['shell','funny','insult','python'],
	data_files=[('', ['LICENSE'])],
	include_package_data=True,
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Operating System :: OS Independent',
	'Environment :: Console',
	],
    license = 'MIT',
    entry_points="""
    [console_scripts]
        ish=insulter:execute
        """,
)