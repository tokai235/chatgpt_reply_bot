# chatGPT でリプライを返してくれる Twitter Bot
## サーバの立ち上げ
1. python のインストール
```
$ sudo yum install python3 -y
```
1. pip のインストール([参考](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html))
```
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ python3 get-pip.py --user
```
1. パッケージをインストール
```
$ pip3 install openai tweepy python-dotenv retrying
```
1. git のインストール
```
$ sido yum install git -y
```
1. git のユーザー設定
```
$ git config --global user.name "【アカウント名】"
$ git config --global user.email "【メールアドレス】"
```
1. git clone & pull
```
$ git clone https://github.com/ibis7895123/chatgpt_reply_bot.git
```
1. `.env`の配置
1. `chatgpt_prompt.txt`の配置
1. バックグラウンドで起動
```
# 自前でログを出すので nohup のログを出力しない
$ nohup python3 main.py >/dev/null 2>&1 &
```

## 別アカウントにリプライをさせる
- そのアカウントの access_token / secret を取得する必要がある
- 以下コマンドで取得する
```
$ pip3 install twitter
$ python3 auth.py
```

## プロセス動いてるか確認したい
```
$ ps ux
```

## リカバリ用にchatGPTの回答だけ取得したい
- `chatgpt_utils.py` の`text`に質問を入れてコマンド
```
$ python3 chatgpt_utils.py
```

## うまくいかないメモ
- 鍵アカウントは `/2/tweets/search/stream`では取得できないっぽい
- やろうと思ったら v1.1 の検索api を使って自分で polling しないといけないかも