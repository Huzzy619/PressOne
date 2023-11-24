
# PressOne Africa API

Backend Support Engineer Code Test



## Issues Found

- line 11, Exception handling was not done when trying to get an item.
- line 17, serializer was not validated before attempting to call the save method in post function.
- line 18, No response data was returned. returning just status of 201 is not enough and does not follow the API design convention.

- line 19, the code will never execute to reach the response on line 19, as there's already a return statement that on same indentation space. if the serializer validation had been done properly, the response for errors would have been better placed.  

- Defining a detail get view and a post method in same APIView class will give issues when trying to create a url path. 
a detail view has to be something like this `"/item/:id"`, and post view `"/item"`.


## Optimizations and Bug Fix
- Separated the views and renamed them to ItemView and ItemDetailView to match the naming pattern as provided by DRF and separate concerns. That way we can properly write the url patterns. later when we decide to add more actions, we can add the list functionality to ItemView using a ``GET`` method. and we can add ``PATCH`` , ``PUT`` and ``DELETE`` functionalities to ItemDetailView

- Handled `DoesNotExist`  exception that would have been raised in the get function if the item_id provided is not found in the Database. 

- Called the `is_valid` method before calling save.

- Handled the situation where there's an issue with validating the data sent, and returned a proper response indicating the fields with problems. 

- Returned a proper response data after item has been created successfully using `POST` method.

## Extras
- Added the remaining Project files such as serializer and model to make a complete and testable application.

- Added type hint to allow for better editor suggestions and clarity of the datatype of the arguments.

- Used Absolute imports because they are more explicit about the module or package being imported, In some cases, using absolute imports can help avoid circular import issues, where two modules depend on each other.

- Added a documentation page that can be accessed using http://localhost/api/docs

- Added ```  serializer_class = ItemSerializer``` in the Views to enable the docs automatically generate a schema using OpenAPI schema
 

## Run Locally

Clone the project

```bash
  git clone https://github.com/Huzzy619/PressOne.git
```

Go to the project directory

```bash
  cd PressOne
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```



## Running Tests

The test has been written using Arrange-Act-Assert(AAA) Methodology using DRF and Django's built in Test Framework. 

To run tests, run the following command


```bash
  python manage.py test
```
