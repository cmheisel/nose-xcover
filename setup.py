from setuptools import setup, find_packages

try:
	desc = file.read(open('README.markdown'))
except StandardError:
	desc = 'see README.markdown'

setup(
    name='nosexcover',
    version='1.0.4',
    description='Extends nose.plugins.cover to add Cobertura-style XML reports',
    long_description=desc,
    author='Chris Heisel',
    author_email='chris@heisel.org',
    url='http://github.com/cmheisel/nose-xcover/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['nose', 'coverage<3.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points = {
        'nose.plugins': [ 'xcover = nosexcover:XCoverage' ]
    },
)

