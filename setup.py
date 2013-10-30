from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dryxPython',
      version='1.098',
      description='A collection of useful commonly used python modules',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='utilities dryx',
      url='https://github.com/thespacedoctor/dryxPython',
      author='thespacedoctor',
      author_email='nothingbutdave@gmail.com',
      license='MIT',
      packages=['dryxPython', 'dryxPython.tests',
          'dryxPython.htmlframework', 'dryxPython.mmd', 'dryxPython.kws'],
      package_data={'dryxPython.mmd': ['assets/*']},
      install_requires=[
          'pyyaml',
          'docopt',
          'numpy',
          'matplotlib'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': [
    'py_get_help_for_python_module=dryxPython.command_line:get_help_for_python_module',
            'dft_print_fits_header=dryxPython.command_line:dft_print_fits_header',
            'dpc-createpythonpackage=dryxPython.packagecreator.createpythonpackage:main',
            'dms_execute_mysql_script=dryxPython.mysql.execute_mysql_script:main'
          ],
      },
      zip_safe=False)
