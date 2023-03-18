# chatGPT でリプライを返してくれる Twitter Bot
## サーバの立ち上げ
1. python のインストール
```
$ sudo amazon-linux-extras install -y python3.8
```
1. パッケージをインストール
```
$ pip install openai tweepy python-dotenv
```
1. git のインストール
1. git pull
1. .env ファイルの配置
1. バックグラウンドで起動
```
# 自前でログを出すので nohup のログを出力しない
$ nohup python main.py  >/dev/null 2>&1 &
```

## 別アカウントにリプライをさせる
- そのアカウントの access_token / secret を取得する必要がある
- 以下コマンドで取得する
```
$ pip install twitter
$ python auth.py
```