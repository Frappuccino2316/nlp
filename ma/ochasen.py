import MeCab

mecab = MeCab.Tagger("-Ochasen")
# mecab = MeCab.Tagger("/mecab-ipadic-neologd")
print(mecab.parse("すもももももももものうち"))