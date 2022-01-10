from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

text = "彼女と国立新美術館へ行った。"

token_filters = [POSKeepFilter(['名詞', '動詞', '記号'])]
a = Analyzer(token_filters=token_filters)

for token in a.analyze(text):
    print(token)
