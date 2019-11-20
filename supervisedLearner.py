# -*- coding: utf-8 -*-
hindi_dic_file = './datasets/hi_hdtb-ud-dev.conllu'
hindi_out_file = './outputs/train_data.txt'

def _lemmaIn(lemmas, lemma):
    for l in lemmas:
        if l["root"] != lemma["root"]: continue
        if l["tag1"] != lemma["tag1"]: continue
        if l["tag2"] != lemma["tag2"]: continue
        return True
    return False

def _serializeLemma(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["tag2"])

def read_training_data(input_training_file, dest_file = None):
    dataset = {}
    with open(input_training_file, 'r') as hindiFile:
        for ln in hindiFile.readlines():
            if len(ln) < 5 or ln[0] == '#': continue
            word, root, tag1, tag2 = ln.split("\t")[1:1+4]
            if not word in dataset: dataset[word] = []
            lemma = {
                "root": root, "tag1": tag1, "tag2": tag2,
            }
            if _lemmaIn(dataset[word], lemma): continue # Lemma already exists
            dataset[word].append(lemma)
    if not dest_file is None:
        with open(dest_file, 'w') as out:
            lines = []
            for word, lemmas in dataset.items():
                lines.append(
                    '{}:{}\n'.format(word, ', '.join([_serializeLemma(lemma) for lemma in lemmas]))
                )
            out.writelines(lines)

    return dataset

def supervised_learn():
    training = read_training_data(hindi_dic_file, hindi_out_file)
    for word, lemmas in training.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
        # TODO: DO TRAINING


# Run main things here
supervised_learn()
