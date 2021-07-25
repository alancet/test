import pyttsx3
engine = pyttsx3.init()

#参照した言葉
words = ["腹筋、板チョコ！","ナイスバルク！","でかいよ！、他が見えない！",
        "土台が違うよ、土台が！","もうでかい！","切れてるよ！","バリバリ",
        "仕上がってるよ！","三角チョコパイ！","腹筋グレネード！",
        "腹筋ちぎりパン！","腹斜筋で大根をおろしたい！","脚が歩いている！",
        "グレートケツプリ！","カーフでかいよ！","胸がケツみたい！",
         "胸がはち切れる！","背中に羽が生えてる！","空も飛べるはず！",
        "背中に鬼が宿ってる！","背中にクリスマスツリー！",
         "上腕二頭筋ナイス！チョモランマ！","さんとうもいいね〜",
        "肩メロン！","肩にちっちゃいジープ乗せてんのかい！"]

rate = engine.getProperty("rate")
engine.setProperty("rate",200)

volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

#参照した言葉の出力
for word in words:
    engine.say(word)

engine.runAndWait()