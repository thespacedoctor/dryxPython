from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dryxPython',
      version='1.0',
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
      packages=['dryxPython'],
      install_requires=[
          'pyyaml',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      # entry_points={
      #     'console_scripts': ['funniest-joke=funniest.cmd:main'],
      # },
      zip_safe=False)
