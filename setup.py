from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='insh',
    packages=['insh'],
    version='2.0',
    description='A Python package that insults you when you encounter an error',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='TheSpeedX',
    url='https://github.com/TheSpeedX/insh',
    download_url="https://github.com/TheSpeedX/insh/archive/master.zip",
    keywords=['shell', 'funny', 'gpt', 'python'],
    data_files=[('', ['LICENSE'])],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'insh = insh.command_line:main',
        ],
    },
    install_requires=[
        'openai>=1.13.3,<2',
    ]
)
