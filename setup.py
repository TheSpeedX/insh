from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()
setup(
	name = 'insulter',
    version = '1.0',
    description = 'Insults You When You Get An Error',
    long_description=long_description,
    author='TheSpeedX',
    author_email='ggspeedx29@gmail.com',
	url = 'https://github.com/TheSpeedX/insulter',
	download_url ="https://github.com/TheSpeedX/insulter/archive/master.zip",
	keywords = ['shell','funny','insult','python'],
	data_files=[('', ['LICENSE'])],
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Operating System :: OS Independent',
	'Environment :: Console',
	],
    license = 'MIT',
	entry_points={
        'console_scripts': [
            'ish = insulter:main',
        ],
		}
)