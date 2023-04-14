# Add Scores
class AddScore:

    filename = None

    def __init__(self, filename):
        self.filename = filename

    def add_more(self, score):
        file = open(self.filename, 'a')
        file.write(str(score) + ',')
        print(f'write score {score}')
        file.close()

    def add_and_clear(self, score):
        file = open(self.filename, 'w')
        file.write(str(score) + ',')
        file.close()


# Read Scores Stored in score.txt
class ReadScore:

    filename = None

    def __init__(self, filename):
        self.filename = filename

    def read_max(self):
        rfile = open(self.filename, 'r')
        data_read = rfile.readlines()[0].strip('')
        data_read_split = list(map(int, data_read.split(',')[:-1]))
        rfile.close()

        return max(data_read_split)
