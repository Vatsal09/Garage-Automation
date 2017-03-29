------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
README3 - Integration Testing the source code
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Integration tests involve the testing of modules to see if the modules work with each other. For a Django project, by unit testing each view in Django, you are inherently testing integration for that project as well. This is because Django receives an HTTP request and parses the structure of the URL to find a match in the mysite/urls.py file. Then, it relays that information to a specific Django view where the logic is processed and passed onto the template engine to render some client-side response. So, if each view, in each Django app works, then integration test for Django project is successful. 

Some of the other integration tests involve integration with database and with browsers. The database integration was tested with the creation, population, and successful migrations within the database. 


For User Interface browser integration testing:
	Thanks to the use of Bootstrap, the page dynamically resized itself. This means it works the same on desktop and mobile.
	Testing the appearance on mobile can be done through chrome:
		Settings --> More Tools --> Developer Tools
		On the top left, press the phone/tablet icon

For Parking bowser integration testing:
	Similar to the User Interface, we employed the use of Bootstrap frontend framework to render HTML/CSS. This ensures browser compatibility with different browsers and different versions of browsers. 
	Test by changing the size of the window. We made it so that a manager can view the site from a tablet.
