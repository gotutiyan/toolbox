class Statistics():
    def __init__(self):
        self.num_of_sents = 0
        self.num_of_words = 0

    def show_stat(self):
        print('num_of_sents\t{}'.format(self.num_of_sents))
        print('num_of_words\t{}'.format(self.num_of_words))