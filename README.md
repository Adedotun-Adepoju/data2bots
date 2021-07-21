# data2bots
A program to find expired goods from a warehouse inventory dataset

The program in this repo is used to record if a product is expired or not from a arehouse inventory dataset. This is recorded in a new column called obsolete.
It contains a python package called check_items and this package has a module containing two functions(check_expiry and convert_to_json)
The test_obsolete.py file is used to run unit tests on the check_expiry function. It was created to assert two rows from the data set
The run.py file is used to load the data set as a dataframe and then pass it into the check_expiry function so that the operation to determine if a good has expired or not is performed
The run.py file also runs the convert_to_json function to pass in the updated dataframe to the function and dump it in the json format. This json file was named 'obsolete'
