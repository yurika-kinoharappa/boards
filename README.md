poetry run python manage.py runserver

mysql.server start
mysql -u root

use boards

select * from event_study;
select * from event_diary;
select * from event_dd;
select * from event_smoke;
select * from event_diet;
select * from event_eat;


truncate table event_study;
truncate table event_diary;
truncate table event_dd;
truncate table event_smoke;
truncate table event_diet;
truncate table event_eat;


poetry shell

python manage.py makemigrations event

python manage.py migrate



ダイエット
chatgptをつなげて食事を登録して何が足りていないか
体脂肪率等を計算してくれる
chatgptがカロリー計算

夢日記
絵を描けるように

勉強
グラフ
selectに追加できる

タバコ
登録するごとに背景を黒く
selectに追加できる
「前回の登録から何時間経ってます、えらい！」みたいなの出す

Noneを記録なしに
消去・編集機能の追加