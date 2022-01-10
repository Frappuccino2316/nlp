import MeCab
import collections

wakati = MeCab.Tagger("-Owakati")

# テキストを読み込み
f = open("ma/melos.txt")
text = f.read()
f.close()

# 改行を削除
text_removed_new_line = text.replace('\n', '')

# テキストを形態素解析する
text_wakati = wakati.parse(text_removed_new_line)

# 頻出順に並べる
c = collections.Counter(text_wakati)

# 上位20件を表示
print(c.most_common(20))
