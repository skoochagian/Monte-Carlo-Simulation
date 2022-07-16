from setuptools import setup

setup(
 name = 'montecarlopackage',
 version = '0.1.0',
 author = 'Sara Koochagian',
 author_email = 'sk2hh@virginia.edu',
 packages = ['montecarlopackage'],
 scripts = ['bin/script1','bin/script2'],
 url = 'https://github.com/skoochagian/FINALPROJECT',
 license = 'LICENSE.txt',
 description = 'A package that simulates Monte Carlo',
 long_description = open('README.txt').read(),
 install_requires = [
 "Django >= 1.1.1",
 "pytest",
 ],
)
