from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='nrfcalendar',
      version='0.1',
      description='This is a python package to',
      long_description=readme(),
      classifiers=[
        'Development Status :: Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5+',
        'Topic :: Retail ',
      ],
      keywords='retail nrf merchandising calendar',
      url='https://github.com/thelostscientist/nrfcalendar',
      author='Zeyad Deeb',
      author_email='zeyad@extetra.com',
      license='MIT',
      packages=['nrfcalendar'],
      install_requires=[
          'pandas',
          'numpy'
      ]
      include_package_data=True,
      zip_safe=False)