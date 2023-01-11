# flet_test
本家は以下  
https://flet.dev/

## Fletとは？
Flutterをベースにしているフレムワーク。PythonだけでWeb・デスクトップアプリを作成することができる。
イメージとしては、TkinterなどのGUI作成とflaskが同じライブラリで実装できるような感じ。


思想としては、使い慣れている言語だけで、クロスプラットフォームなアプリ開発できるようなものを提供してきたいというもの。
そのため、今後はPython以外の言語でも拡張していく模様。

FlutterはGoogleが開発しているオープンソースでモバイルアプリ開発フレームワーク。iOSやAndroidだけでなく、その他のプラットフォームにも対応している。

## 特徴
https://qiita.com/NasuPanda/items/48849d7f925784d6b6a0

- rom idea to app in minutes 
  - 「素早くGUIアプリを作成出来る」ことが、Fletの主なセールスポイント。
- Simple Architecture 
  - JSフロントエンドやRestAPIを書くこと無く、PythonだけでSPAを作る事ができる。 
- Batteries included 
  - Batteries Included は、Pythonの設計思想。電池が付属している、つまりそのままでもすぐに動かせることを指す。 
- Powered by Flutter 
  - Flet の UI は Flutter で構成されているので、綺麗なUIを提供でき、マルチプラットフォームに対応している。 
- Speaks your language 
  - Flet は言語に依存しないことを目指す。現在サポートされているのはPythonだが、今後 Go や TypeScript、 C# にも対応していく予定。 
- Deliver to any device 
  - 複数のプラットフォーム(iOS、Android、Web、Windows、Mac、Linux)に対応してる。


## なんでflet？（作ったの？）
開発者はコンソールアプリがある程度需要があることが分かった時点で、非開発者向けに社内ツール（GUIやWebAPP）を作成することがある。
この時に、electronやflutterのような大規模なフレームワークを使用したり、.NET MAUIのようなフレームワークを使用すると、実装までに時間がかかってしまう。
なので、精通しているプログラミング言語で、短い時間で実装できるようなものが必要になっていく。


## Fletの基本
内部的にはWebアプリで、ウィンドウが開いたとしても、ビルトインのWebサーバーがバックグラウンドで起動している。
FletのサーバーはFletdと呼ばれていて、デフォルトでランダムなTCPポートでリッスンしている。

- ポートをリッスン？
リッスンとは、「聞く」という意味を持つ英単語で、通信機能を持つソフトウェアが、外部からのアクセスに備えて待機することをこのように呼ぶ。


FletはControlという単位で機能をわけている。階層としては以下のようになっており、ページの追加や機能の追加をすることができる。
```
Page
 ├─ TextField
 ├─ Dropdown
 │   ├─ Option
 │   └─ Option
 └─ Row
     ├─ ElevatedButton
     └─ ElevatedButton
```


- 命令形UI

flutterなどのフレームワークは宣言形のフレームワークになっている。 
しかし、Flet は手動でプロパティを更新することで UI をコントロールする命令形のモデルを実装している。
理由としてはフロントエンドの開発経験がないプログラマーの開発ハードルを下げる狙いがある。


## 使ってみての感想
使用してみての感想は、Tkinterとかよりもスタイリッシュで様々な機能を簡易的に実装することができるし、同じ容量でWebAppも実装できる点が良い点。
逆にまだまだリリースし始めて1年もたっていないので、bugなどが他のライブラリよりも多い可能性とかはあるので、使用してみていくのが良いかなと思っている。

その他、内蔵しているアイコンなどを自由に設定することもできるし、matplotlibも綺麗に表示できるなど凝ったことが色々できる点がいいかも知れない。