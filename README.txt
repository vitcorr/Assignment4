Victor Kolawole
101201377

HOW TO SETUP DATABASE
	-Open PgAdmin 4 and create a new Database by right clicking on Databases>Create>Database
	-Name it and save it

	-Open the create_table_script script to create the students table
	-Run it.
	-Open the insert_into_table script to populate the students table
	-Run it.
	-The database is now setup and ready for app requests.

How to run the application a4.py
	-download a4.py and open it on your pc
	-open terminal and run "py -3 -m pip install psycopg2" to install pscopg2
	-navigate to the folder where a4.py is stored and run it ("py a4.py")
	-enter the name of the database
	-enter the password you used in pgadmin4
	-enter the host. ('localhost' should work fine)
	-select one of the options provided to run the functions
		-option 1 prints the syudent record. you can run this after every function
			to confirm the actions work prfectly
		-option 2 inserts a new student record. enter the students details
		-option 3 updates an existing students email. enter the id then the new email
		-option 4 deletes a students record. enter the id you wish to delete
		-press q to exit the program

thank you!