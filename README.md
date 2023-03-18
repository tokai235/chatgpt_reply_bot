# chatGPT でリプライを返してくれる Twitter Bot
## サーバの立ち上げ
1. python のインストール
```
$ sudo amazon-linux-extras install -y python3.8
```
1. git のインストール
1. git pull
1. .env ファイルの配置
1. バックグラウンドで起動
```
$ nohup python main.py  >/dev/null 2>&1 &
```