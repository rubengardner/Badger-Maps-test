
## Dear reader

I'm Ruben Gardner and I'm applying for the software internship at Badger Maps. I will briefly explain the procedure I took for producing this code.

### Coding style

I wanted to replicate the style I use when coding in production which has the following concepts:
* Separate each functionality into functions that are clear for fellow coders to interpret
* Create scalable code
* Extensive use of comments
* Small and meaningful git commits

### How I solved the problem

* Pandas: I used Pandas python library for this test. I find Pandas very useful, especially if we would be dealing with a very big dataset. This code is scalable to a bigger CSV file.

* Exception handling: I interpreted from the instructions that rows with empty fields, indifferently if whether it's a required field or not, should be dropped from the analysis. I am not 100% confident that is what you were asking.
I also print the number of blank rows and their indexes. O do the same for a row with at least 1 NaN value.

### Requirements
Requirements can be found in the requirements.txt file
