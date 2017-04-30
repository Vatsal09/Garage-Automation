The attached db.sqlite3 file contains all the information gathered up to this point, including the users, accounts, payment methods, vehicles, parking lots, parking spots, parking sessions, and etc. For every class set up within the models.py files for each app, a table exists in the database. Additionally, Django utility data like migration logs, for example, is also located in this database.

For example, for User Interface Django app: 
	Database is updated when a User registers the account, adds a payment method, update their information, and etc.
	For a specific case, let's take a look at how vehicles are added.   
	    Vehicles:
	        As described in the arrive use case I wrote, when the sensor read the license plate, a customer will swipe their credit/debit card to get entry to the lot. If that card is registered to an existing account, the vehicle will be added to the account, updating the database.

Viewing the database:
	1. Download SQLITE database browser from http://sqlitebrowser.org/
	2. Run the application and set it up
	3. Click "Open Database"
	4. Navigate to 4_data_collection and double click the db.sqlite3 file
	5. Browse the data

You can also view the database by running the server and accessing the admin pannel (sample screenshots provided):
	1. python manage.py runserver 
	2. Navigate to http://127.0.0.1:8000/admin
	3. Username: admin Password: group10password
	4. Browse the data captured by clicking the models

For you convenience, some pictures of the data is captured in the "4_data_collection" folder.