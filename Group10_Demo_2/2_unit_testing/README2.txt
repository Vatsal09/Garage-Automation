-------------------------------------------------------------------------------------------------------------------------------------------------------
README2 - Unit Testing the source code
-------------------------------------------------------------------------------------------------------------------------------------------------------

DJANGO TESTING FRAMEWORK BACKGROUND

Django provides automated testing suite that can prove to be extremely useful for the modern Web developer. As per the documentation, one should use the testing tools when:
    - You’re writing new code, you can use tests to validate your code works as expected.
    - You’re refactoring or modifying old code, you can use tests to ensure your changes haven’t affected your application’s behavior unexpectedly.

Testing a Web application is a complex task, because a Web application is made of several layers of logic – from HTTP-level request handling, to form validation and processing, to template rendering. With Django’s test-execution framework and assorted utilities, you can simulate requests, insert test data, inspect your application’s output and generally verify your code is doing what it should be doing. Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach. Subclasses from django.test.TestCase, which is a subclass of unittest.TestCase , runs each test inside a transaction to provide isolation. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

RUNNING ALL UNIT TESTS

    - Navigate to the “1_code” folder 
    - Use the README1 and follow Step 1 in the “Not Recommended Way to Execute Source Files”
    - cd into “1_code/mysite” folder 
    - For all platforms (Linux/Windows/OSX) – Execute: python manage.py test
    - The previous commands runs all of the 65 unit tests and displays “OK” if they all run successfully  
