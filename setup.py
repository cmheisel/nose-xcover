from setuptools import setup, find_packages

try:
    desc = open('README.rst').read()
except:
    desc = 'see README.rst'

setup(
    name='nosexcover',
    version='1.0.10',
    description='Extends nose.plugins.cover to add Cobertura-style XML reports',
    long_description=desc,
    author='Chris Heisel',
    author_email='chris@heisel.org',
    url='http://github.com/cmheisel/nose-xcover/',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['nose', 'coverage>=3.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'nose.plugins': ['xcover = nosexcover.nosexcover:XCoverage']
    },
)
