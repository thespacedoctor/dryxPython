from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mytestpackage',
      version='0.1',
      description='',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='utilities dryx',
      # url='https://github.com/thespacedoctor/mytestpackage',
      author='thespacedoctor',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=['mytestpackage'],
      # install_requires=[
      #    'pyyaml',
      # ],
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
      # entry_points={
      #     'console_scripts': ['funniest-joke=funniest.cmd:main'],
      # },
      zip_safe=False)
