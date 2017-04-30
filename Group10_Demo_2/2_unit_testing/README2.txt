-------------------------------------------------------------------------------------------------------------------------------------------------------
README2 - Unit Testing the source code
-------------------------------------------------------------------------------------------------------------------------------------------------------

We perform unit testing by checking each app's (User Interface, Parking, and Manager) each URL-tied feature. Testing this will test the logic (views) and, in the process, check the HTML/CSS/JS through the Django template engine. 

-------------------------------------------------------------------------------------------------------------------------------------------------------
User Interface Unit Testing
-------------------------------------------------------------------------------------------------------------------------------------------------------

Home menu: 
    Press button on top left on http://127.0.0.1:8000/garageAutomation/home/
    Press anywhere on screen other than white area to close menu

Payment Page:
    Press button on top left on http://127.0.0.1:8000/garageAutomation/home/
    Press Payment
    *****IMPORTANT*****
	-Adding a card that already exists in the database or removing the only card in the account is prohibited by design!
	*****IMPORTANT*****
    1 ----Payment Details-----
        Press on listed Payment Payment method
        a ----back----
            press back arrow on top left
        b ----Remove----
            press Remove
                if have more than 1 card on account:
                    selected card will no longer be listed in Payment Page
                else
                    selected card will still be visible in Payment Page
    2 ----Add Payment Method-----
        Press Add Payment
        a ----Press Save----
            if missing any fields:
                webpage will indicate fields 
            if any fields are improperly filled:
                webpage will indicate fields and how to fill them
            else
                Payment Page will now dispaly new card with provided credentials
        b ----back----
            press back arrow on top left
    3 ----Close-----
        press x on top left
    
Settings Page:
    Set up: 
        A) Add vehicle through shell to account with username Guy: 
            1) go to mysite directory through terminal
            2) python manage.py shell
            3) from garageAutomation.models import Account, PaymentMethod, Vehicle, ParkingSession
            4) v = vehicle()
            5) v.account = Account.objects.get(pk=1)
            6) v.license_plate = "ABC123"  #NOTE: string cannot be more than 10 chars and must be UNIQUE
            7) v.make = "Honda" #NOTE: string cannot be more than 10 chars
            8) v.color = "Red" #NOTE: string cannot be more than 10 chars
            9) v.save()
        B) Log into account at http://127.0.0.1:8000/garageAutomation/login: Username="Guy" password="group10password"
    
    Press button on top left on http://127.0.0.1:8000/garageAutomation/home/
    Press Settings
    Vehicle created in Set up should be listed
    1 ----Remove Vehicle-----        
    Pressing the x button in vehicle's box will ask for a confirmation
        Pressing cancel: alert will close and nothing will happen
        Pressing ok: vehicle will no longer be listed in Settings page
    2 ----Close-----
        press x on top left

Login/Register an Account:
	To test my code I registered an account through the registration page and then checked in the django shell to make sure that an account object was created and had the correct attributes. Then I logged into the account through the login page and navigated to the history option to display the history of parking sessions for this account. For now I created history sessions manually and added them to the database but in the future the history sessions should come from the other part of the system that tracks the vehicle in the parking lot. 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Parking Unit Testing
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Login/Register Page: 
    Navigate to http://127.0.0.1:8000/parking
    Double click either the Login or Register button
   
    1 ----Login-----
        Double clicking the login page leads you to the login page
        Enter login details - Username: Vatsal Password: group10password
        	if the query to the database with given username and password matches
        		displays all of the user's parking lots
        	else
        		displays "invalid login"
    2 ----Register-----
    	Enter a Username, Email, and Password
    		if all details are inputed and email address contains 1 @ symbol
    			sucessfully added to database
    		else
    			displays error message

Main Page: 
    Displays all the user's lots. You can click "Add a Lot" to add a lot, logout by clicking "Logout", or view deatils by clicking either the picture of the parking lot or the "View Details" button. One can also delete a lot by clicking the "Delete" button.

    1 ----All Parking Lots-----
        Diplays the user's lots
        	if the user is authenticated, query User.Parking_Lot in the database 
        		displays all of the user's parking lots
        	else
        		show a "Add a Lot" button
    2 ----Add a Lot-----
    	Displays a form to add a new lot and a quick guide on how to add on the right
    		if all details are inputed and max levels > 0 and Max Spots > 0
    			Lot is sucessfully added to database and associated with user
    		else
    			displays error message
    3 ----Logout-----
        For safety puposes, logout button is added to logout the user so unautherized people don't get access.
       		if logout is clicked
       			user is logged out and exited to the Loin/Register page
    4 ----Home-----
        At any point, home is clicked it brings you to the Main Page as a means of user ease
       		if home is clicked
       			execute logic of All Parking Lots

Detail Page (of each Parking Lot)
	If the parking lot is clicked in the Main Page, query the database for the matching parking lot identification and display the spot details, lot details, and buttons for checking map, adding spot, enabling spots, and disabling spots. 

	1 ----Lot Details-----
        Diplays the lot's address, manager username, number of levels, and number of spots
        	if the user is authenticated and a query is made to obtain lot object
        		displays information to left 
        	else
        		show default
    2 ----Add a Spot-----
    	Displays a form to add a new spot 
    		if all details are inputed and level > 0 and spot number > 0
    			Spot is sucessfully added to database and associated with the lot 
    		else
    			displays error message if the conditions aren't met
    3 ----All Spots-----
        If the parking lot has spots, it displays them to the right by querying all the spots associated to the lot. 
    4 ----Enable/Disable-----
        At any point, manager might want to perform maintainence on a spot(s). This buttons let them diable/enable spot so that the occupancy map displays that the spot is unavilable. The manager can also enable the spot once the maintainence is completed. 
    5 ----Delete Spot-----
    	Deletes the spot from the database
    		if the trash icon is clicked
    			query the database to GET lotnumber and spot number; delete it
    6----Map-----
    	Displays the occupancy of the map based on the current occupancy reading
    		if the check map button is clicked
    			Get all spots in the database associated with the lot and check occupancy
    				if occupied
    					display red
    				if not occupied
    					display green
    			Display the next level if not max level

Update Occupancy
	Poll the sensors to update the database of the occupancy at each spot by first going on a specific parking lot
	Now, given that the current URL, add update_occupancy at the end of the URL and press enter (For example: http://localhost:8000/1/update_occupancy)

	This will take some time so please be patient

		For each sensor
			perform a random function generator operation to output a random boolean representing if the spot is taken or not
				update the database
	 

