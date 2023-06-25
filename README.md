# Movie Ratings Dataset Generator
Generate big test data files for ECE 454: Distributed Computing - Spring 2023 Assignment 2 (Hadoop &amp; Spark with Scala)

# How to Run
Make sure you have python/python3 installed
1. `git clone` the repository locally
2. `cd` into the cloned directory
3. Run the command below:
```
python3 generator.py <NUMBER OF MOVIES> <NUMBER OF USERS>
```
i.e.
```
python3 generator.py 3000 1000 
```
will generate `3000movies_1000users.txt` in the same directory
