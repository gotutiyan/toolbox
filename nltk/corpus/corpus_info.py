from nltk.corpus import reuters, brown, webtext

def show_corpus_info(corpus):
    print('ファイル数:', len(corpus.fileids()))
    try:
        print('カテゴリ数:', len(corpus.categories()))
    except AttributeError:
        pass
    words = corpus.words()
    print('単語数:', len(words))
    print('単語種類数:', len(set(words)))
    print('文数:', len(corpus.sents()))

    return
    


def main():
    print('----reuters----')
    show_corpus_info(reuters)

    print('----brown----')
    show_corpus_info(brown)

    print('----webtext----')
    show_corpus_info(webtext)



if __name__ == '__main__':
    main()

