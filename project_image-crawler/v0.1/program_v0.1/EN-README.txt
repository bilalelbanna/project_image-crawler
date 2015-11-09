#####################Start of EN-README############################
README file for v0.1

Author: Bilal El Banna
Date: 09 Nov 2015

To properly use the package Python 2.7 or higher is required.
For further details run help().

###################################################################

Further development:
	-Support for other types of plaintext files, not only .txt.
	-Support for other types of databases, not only sqlite.
	-Support for image type detection and processing.

###################################################################

File and folder description:

/start.py

	Starting program v0.1.


/configuration/config.py

	Configuration file for start.py

/database
	
	Database save folder.

/storage

	Image save folder.

/data

	Folder for plaintext files.
	

/abstract_factory/plaintext_abs_factory.py

	Abstract factory to detect and process plaintext files, applying specified 
	routines on each data type after detection, using python's standard libraries.


/abstract_factory/database_abs_factory.py

	Abstract factory to create and apply specialized routines on databases, 
	after type input and database path, by using python's standard libraries.


/libs/db_handling.py

	Module with class methods to create an SQLite database and to populate a database, using
	python's standard libraries.


/libs/txt_handler.py

	Module with class methods to process input .txt-Files, 
	using python's standard libraries.

/libs/pic_handler.py

	Module with class methods to process input URLs of images, 
	using python's standard libraries.


/test/unittest_txt_handler.py

	Applying unit-tests on module txt_handler.py, using
	python's standard libraries.


/test/unittest_plaintext_abs_factory.py
	
	Applying unit-tests on module plaintext_abs_factory.py, using
	python's standard libraries.


/test/unittest_pic_handler.py

	Applying unit-tests on module pic_handler.py, using
	python's standard libraries.


/test/unittest_db_handling.py

	Applying unit-tests on module db_handling.py, using
	python's standard libraries.


/test/unittest_database_abs_factory.py

	Applying unit-tests on module database_abs_factory, using
	python's standard libraries.


/test/test_files

	Folder for unit-tests with example data and database (reading/writing) 

#####################End of EN-README##########################
	
