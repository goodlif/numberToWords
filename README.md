Initally, given the scope of the application / assessment, I decided that writing the challenge in Python was a good option for me as it would provide the platform to show my understanding of an object orientated piece of software. 

Learning and using Python ( I come from a c# and javascript background) I believe shows my capabilities of quickly and efficiently learning a new framework and being able to use the agnostic principles of software development.

After reading the specification I decided to separate the application in various components: 

- Obtaining Data (string format), 
- Formatting Data (present number as string)
- Conversion from string representation of a number to text. 

Separating the application into components or modules allows for the code to be more segregated/loosely coupled allowing sub components to more closely fit the Sigle Responsibility Principle. 

I decided to create the main module 'number_to_words.py' in such a way that it had knowledge of all dependecies, repsonsible for the initialisation of each service or utility. This is what I would describe as a compositional approach to software development. 

Assumptions: 
English input
English output
No ordinal cases
Lowercase
numbers do not exceed 100 trillion
no spaces between numbers e.g. 23 000
no punctuation around numbers e.g. #34
all numbers are integers
all numbers are positive
numbers like 1900 are displayed as one thousand nine hundred and not nineteen hundred

Explain: 
- Extendable dictionary (language)
- Increase number range
- Add more regex filtering
- Add more text logic
- Extend data aquisition strategy
- Talk through unit testing strategy


Todo: 

Hook in logging 


