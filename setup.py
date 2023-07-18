from setuptools import setup


setup_params = dict(
    
    name =             'pysqream_blue_sqlalchemy',
    version =          '0.5',
    description =      'SQLAlchemy dialect for SQream Blue', 
    long_description = open("README.rst", "r", encoding="utf-8").read(),
    url=               "https://github.com/SQream/pysqream_blue_sqlalchemy",
    
    author =           'SQream',
    author_email =     'info@sqream.com',
    
    classifiers =      [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    keywords = 'database sqlalchemy sqream sqreamdb',

    python_requires =  '>=3.9',
    
    install_requires = ['sqlalchemy>=1.3.18',
                        'pysqream-blue>=1.0.30',
                        'setuptools>=57.4.0',
                        'pudb==2022.1.2',
                        'pandas==1.1.5',
                        'numpy==1.22.0',
                        'alembic>=1.6.3'],
    
    packages         = ['pysqream_blue_sqlalchemy'], 
    
    entry_points =     {'sqlalchemy.dialects': 
        ['sqream_blue = pysqream_blue_sqlalchemy.dialect:SqreamBlueDialect']
    },
    # sqream://sqream:sqream@localhost/master
)


if __name__ == '__main__':
    setup(**setup_params)
