class word_2_vec:

    def __init__(self):
        self.word_2_ind = {}
        self.ind_2_word = {}
        self.window_size = 2

    def generate_data(vocab,corpus):

        train_data = []
        #generating word to index dictionary
        for ind,token in enumerate(vocab):
            self.word_2_ind[token] = ind
        
        #generating index to word dictionary
        for ind,token in enumerate(vocab):
            self.ind_2_word[index] = word
        
        one_hot_all = self.word_2_onehot(vocab)

        for i,word in enumerate(vocab):
            target = one_hot_all[i]
            context_word = []
            for j in range(i-window_size,i+window_size):
                if j != i and j>=0 and j<=vocab.size()-1:
                    context_word.append(one_hot_all[j])
                        
            train_data.append([target,context_word])


    def word_2_onehot(vocab):
        count = vocab.size()
        l = []
        for word in vocab:
            k = word_2_ind[word]
            enc = [0 for i in range(0, count)]
            enc[k] = 1
            l.append(enc)
        return l
