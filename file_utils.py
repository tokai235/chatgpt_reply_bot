# chatGPTの人格注入のためのプロンプトをテキストファイルから読み込む
def read_prompt(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text