---------------------------------------------------------------------------------------------------------------------------------------------------------------------
README1 - Running the source code
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
There are two ways to run the the codebase: Github or through the files below. The first contains the latest version of the code and it's proven to work. 


Recommended Way to Execute Source Files:

	1)	Clone the Github repository located at https://github.com/Vatsal09/Garage-Automation 

	2)	Install virtualenv via pip and start a virtual environment within the cloned repository: 
		a.	Execute: pip install virtualenv
		b.	cd into the folder with cloned repository
		c.	Execute: virtualenv env
		d.	To begin using the virtual environment, it needs to be activated:
			i.	Linux/OSX: source env/bin/activate
			ii.	Windows: cd into env folder and execute: ./Scripts/activate
		e.	Install dependencies:
			i.	cd into the parent folder (where the requirements.txt and windows_requirements.txt are located)
			ii.	Linux – Execute: pip install –r requirements.txt
			iii. Windows/OSX – Execute: pip install –r windows_requirements.txt
			iv. Locate and cd into “License Plate Reader” folder from the base/parent directory
			v.	cd into “cloudapi/python” folder
			vi.	Run the program: python setup.py install 

	3)	Running the Django project:
		a.	cd into mysite folder 
		b.	For all platforms (Linux/Windows/OSX) – Execute: python manage.py runserver
		c.	From your browser, go to:
			i.	http://127.0.0.1:8000/garageAutomation/login - To view User Interface (follow the more specific directions provided below in the User Interface Section)
			ii.	http://127.0.0.1:8000/parking - To view Parking Monitoring/System (follow the more specific directions provided below in the Parking Section)  

Not Recommended Way to Execute Source Files:

	1)	Install virtualenv via pip and start a virtual environment within this folder: 
		a.	Execute: pip install virtualenv
		b.	cd into “1_code” folder 
		c.	Execute: virtualenv env
		d.	To begin using the virtual environment, it needs to be activated:
			i.	Linux/OSX: source env/bin/activate
			ii.	Windows: cd into env folder and execute: ./Scripts/activate
		e.	Install dependencies:
			i.	cd into “1_code” folder (where the requirements.txt and windows_requirements.txt are located)
			ii.	Linux – Execute: pip install –r requirements.txt
			iii.Windows/OSX – Execute: pip install –r windows_requirements.txt
			iv. Locate and cd into “License Plate Reader” folder from the base/parent directory
			v.	cd into “cloudapi/python” folder
			vi.	Run the program: python setup.py install 

	2)	Running the Django project:
		a.	cd into “1_code/mysite” folder 
		b.	For all platforms (Linux/Windows/OSX) – Execute: python manage.py runserver
		c.	From your browser, go to:
			i.	http://127.0.0.1:8000/garageAutomation/login - To view User Interface (follow the more specific directions provided below in the User Interface Section)
			ii.	http://127.0.0.1:8000/parking - To view Parking Monitoring/System (follow the more specific directions provided below in the Parking Section)
			
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
User Interface Specific Instructions
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run the run the code, you must start the website: in the terminal go to mysite and then run python manage.py runserver
Then go to http://127.0.0.1:8000/garageAutomation/login: Username="Guy" password="group10password"  #NOTE! the capital G in the username, don’t include quotes

This account has some payment methods and parking sessions already set in the database

Register a new account in http://127.0.0.1:8000/garageAutomation/register if necessary 

Using the Map
	It will be displayed after logging in. You can view different levels by pressing the button on the bottom

Viewing Account Info
	Pressing the hamburger button on the top left will display the Payment, History, and Settings buttons that will each display the pages if they are pressed.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Parking Specific Instructions
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run the run the code, you must start the website: in the terminal go to mysite and then run python manage.py runserver
Then go to http://127.0.0.1:8000/parking and double click login: Username="Vatsal" password="group10password"  #NOTE! the capital V in the username, dont include quotes

Register a new account in http://127.0.0.1:8000/parking, if necessary 

This account has been initialized to show how a manager will first start system initialization. When the management team is starting this system, we need a way for parking spots to be associated with sensor ids. Here the manager first creates a parking lot (one manager can have multiple lots) and then they need to add the spot-sensor associalting through "Add a spot".This way when we poll the sensors, we can get an updated view of the real time occupancy. The managers can also enable/disable spots if they need to perform maintainence. Additionally, all the spots can be deleted. 


Base page: http://127.0.0.1:8000/parking

	Login or register a new manager account

Add Lot/ Delete Lot

	You will see button in the nav bar to "Add Parking Lot" to add a lot. Click "All Lots" -> click delete icon to delete a lot (don't delete lot with address 220 Marvin Lane because we will use it to show other functionality)

View all lots
	
	Shows all of owner's lots

View lot details

	Click the lot to view details about spots, add spots, delete spots, enable, and disable spots (best seen with the initialized lot with address 220 Marvin Lane)

Map of the occupancy

	Shows occupancy of parking lot. Navigate to parking lot with address 220 Marvin Lane and click the "Check Map" button. Scroll to bottom and click "Next Level" to see other levels


