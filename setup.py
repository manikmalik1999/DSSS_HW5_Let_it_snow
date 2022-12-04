from setuptools import setup

setup(
    name='DSSS_HW5_Let_it_snow',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/manikmalik1999/DSSS_HW5_Let_it_snow/',
    author='Manik Malik',
    author_email='manik.malik@fau.de',
    license='BSD 2-clause',
    packages=['DSSS_HW5_Let_it_snow'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)