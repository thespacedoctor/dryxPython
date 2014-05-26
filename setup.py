from setuptools import setup


def readme():
    with open('README.md') as f:
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
                'dryxPython.htmlframework', 'dryxPython.mmd', 'dryxPython.kws', 'dryxPython.tagging'],
      package_data={'dryxPython.mmd': ['assets/*']},
      install_requires=[
          'pyyaml',
          'docopt',
          'numpy',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': [
              'py_get_help_for_python_module=dryxPython.command_line:get_help_for_python_module',
              'dft_print_fits_header=dryxPython.command_line:dft_print_fits_header',
              'dpc-createpythonpackage=dryxPython.packagecreator.createpythonpackage:main',
              'dms_execute_mysql_script=dryxPython.mysql.execute_mysql_script:main',
              'dcu_update_git_repos=dryxPython.commonutils.update_git_repos:main',
              'dat_check_for_sdss_coverage=dryxPython.astrotools.check_for_sdss_coverage:main',
              'dat_ra_sexegesimal_to_decimal=dryxPython.astrotools.ra_sexegesimal_to_decimal:main',
              'dat_declination_sexegesimal_to_decimal=dryxPython.astrotools.declination_sexegesimal_to_decimal:main',
              'dt_add_mavericks_tags_to_dayone=dryxPython.tagging.add_mavericks_tags_to_dayone:main',
              'dt_add_mavericks_tags_to_voodoopad=dryxPython.tagging.add_mavericks_tags_to_voodoopad:main',
              'dcu_get_outliers_from_list=dryxPython.commonutils.get_outliers_from_list:main',
              'dc_xy_scatter=dryxPython.plotting.xy_scatter:main',
              'dms_convert_collate_and_charset_of_mysql_database=dryxPython.mysql.convert_collate_and_charset_of_mysql_database:main',
              'dms_convert_mysql_database_to_myisam=dryxPython.mysql.convert_mysql_database_to_myisam:main',
              'dp_xy_scatter=dryxPython.plotting.xy_scatter:main',
              'astromCorrector=dryxPython.astrotools.astrometry_corrector:main'
          ],
      },
      zip_safe=False)
