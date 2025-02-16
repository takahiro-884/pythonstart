# pythonstart


- `git checkout -b 作業ブランチ` => 作業ブランチを作成

- `git status` -> ステータスの確認
- `git add .` -> stagedにあげる
- `git commit` -> historyに形状 
- `git push` -> remote commit

リモート      (remote commit)
-------------------git push 
本命       (local commit)     
-------------------git commit          
staged               
-------------------git add
unindex  

### プロジェクトの始め方
1. `git checkout -b ブランチ名`
2. `python -m venv 環境名(なんでもいい)` ex. `myenv`
    -> ex `python -m venv myenv` => 仮想環境の作成するコマンド
3. source myenv/bin/activate => 仮想環境の立ち上げ
4. `python install ライブラリ名` => ライブラリのインストール
5. `python main.py` => 実行
6. `deactivate` => 仮想環境を抜ける