Initally, given the scope of the application / assessment, I decided that writing the challenge in Python was a good option for me as it would provide the platform to show my understanding of an object orientated piece of software. 

Learning and using Python ( I come from a c# and javascript background) I believe shows my capabilities of quickly and efficiently learning a new framework and being able to use the agnostic principles of software development.

After reading the specification I decided to separate the application in various components: 

- Obtaining Data (string format), 
- Formatting Data (present number as string)
- Conversion from string representation of a number to text. 

Separating the application into components or modules allows for the code to be more segregated/loosely coupled allowing sub components to more closely fit the Single Responsibility Principle. 

I decided to create the main module 'number_to_words.py' in such a way that it had knowledge of all dependecies, repsonsible for the initialisation of each service or utility. This is what I would describe as a compositional approach to development. 

Assumptions: 
- English input
- English output
- No ordinal cases
- Lowercase
- Numbers do not exceed 100 trillion
- No spaces between numbers e.g. 23 000
- No punctuation around numbers e.g. #34
- All numbers are integers
- All numbers are positive
- Numbers like 1900 are displayed as one thousand nine hundred and not nineteen hundred

When creating the dictionary for the language, I decided to create a type of abstract base class that could be inherited by a child class specific to a language making it easily extendable and maintainable. Inside the dictionary itself, should a developer want to increase the range, they should solely add to the large dictionary. 

When filtering text we use a number of regex commands to specify what to look for. An 'integer' surrounded by white space, after the removal of fullstops, is considered correct. An integer with an order magnitude separated by white space creates an array of 2 integers 23 500 -> [23, 500] which is not allowed. 

The getdata function doesn't expose data collection logic and as such conforms to the encapsulation and abstract aspect of software development. This means that should we require a different way of getting data, we can encapsulate that into the class. Separation of adminstration logic and business logic.

Unit tests were written against main business logic. When external administration packages or connections are used, we rely on those packages being tested by the source. 
Explain: 

Todo: 

- Add more fluent english support





