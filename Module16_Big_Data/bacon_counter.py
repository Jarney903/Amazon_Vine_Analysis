from mrjob.job import MRJob

#Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class
class Bacon_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1
    def reducer(self, key, values):
        yield key, sum(values) 

if __name__ == "__main__":
   Bacon_count.run()

# You might have noticed that nowhere in the code is a file imported or opened. The mrjob library works by reading in a file passed to it in the terminal.
# Let's use a file full of random words, input.txt (Links to an external site.) we just created.
# Run the following code in the terminal:
# $ python bacon_counter.py input.txt
