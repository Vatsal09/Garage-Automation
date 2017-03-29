------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
README2 - Unit Testing the source code
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
User Interface Unit Testing
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To test my code I registered an account through the registration page and then checked in the django shell to make sure that an account object was created and had the correct attributes. Then I logged into the account through the login page and navigated to the history option to display the history of parking sessions for this account. For now I created history sessions manually and added them to the database but in the future the history sessions should come from the other part of the system that tracks the vehicle in the parking lot. 


home menu: 
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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Parking Unit Testing
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

home menu: 
    Navigate to http://127.0.0.1:8000/parking
    Double click either the Login or Register button
    Login Details - Username: Vatsal Password: group10password

All Parking Payment Page:
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




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Manager Unit Testing
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------