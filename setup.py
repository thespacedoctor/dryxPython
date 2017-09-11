from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()


setup(name='dryxPython',
      version='1.1.0',
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
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'pyyaml',
          'docopt',
          'pdfkit',
          'gdata',
          'mysql-python',
          'eventlet'
      ],
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
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
              'dms_convert_mysql_database_to_innodb=dryxPython.mysql.convert_mysql_database_to_innodb:main',
              'dp_xy_scatter=dryxPython.plotting.xy_scatter:main',
              'astromCorrector=dryxPython.astrotools.astrometry_corrector:main',
              'git_update_request_watcher=dryxPython.git.update_request_watcher:main',
              'dwc_convert_list_of_urls_to_pdfs=dryxPython.webcrawlers.urlToPdf.convert_list_of_urls_to_pdfs:main',
              'dat_crossmatch_ned=dryxPython.astrotools.catalogue_queries.ned:main',
              'dat_get_angular_separation=dryxPython.astrotools.get_angular_separation:main',
              'dat_shift_coordinates=dryxPython.astrotools.shift_coordinates:main',
              'dat_date_to_mjd=dryxPython.astrotools.date_to_mjd:main',
              'dft_convert_excel_workbook_to_binary_fits_table=dryxPython.fitstools.convert_excel_workbook_to_binary_fits_table:main',
              'dat_mjd_to_date=dryxPython.astrotools.mjd_to_date:main',
              'dat_minor_planet_checker=dryxPython.astrotools.minor_planet_checker:main',
              'dms_add_htmids_to_mysql_table=dryxPython.mysql.add_HTMIds_to_mysql_tables:main',
              'dft_convert_spectrum_fits_to_ascii=dryxPython.fitstools.convert_spectrum_fits_to_ascii:main'
          ],
      },
      zip_safe=False)
