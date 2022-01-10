import MeCab
import collections

wakati = MeCab.Tagger("-Owakati")
sentence_wakati = wakati.parse("私はQAエンジニアをしておりソフトウェアテストなど品質保証の支援を行なっています。").split()

print(sentence_wakati)