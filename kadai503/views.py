# from config.settings import TEMPLATES
from django.shortcuts import render

from django.http import HttpResponse
from datetime import date


# Create your views here.
def helloworldfunction(request):
    today = date.today()
    todaystr = today.strftime('%Y/%m/%d %A')
    context = {'date': todaystr}
    return render(request, 'hello.html', context)

def get_list(request):
    fruitlist = [
        ['メロン', '高い'],
        ['リンゴ', 'おいしいよ'],
        ['マスカット', 'つぶつぶです'],
        ['アケビ', 'おいしいよ'],
        ['アセロラ', 'ビタミンたくさん'],
        ['アボカド', '栄養あるよ'],
        ['アンズ(杏)', 'おいしいよ'],
        ['イチゴ', 'ビタミンたくさん'],
        ['イチジク', '栄養あるよ'],
        ['ウメ(梅)', 'おいしいよ'],
        ['温州ミカン(みかん)', 'ビタミンたくさん'],
        ['オレンジ', '栄養あるよ'],
        ['カキ(柿)', 'おいしいよ'],
        ['カリン', 'ビタミンたくさん'],
        ['カンキツ類', '栄養あるよ'],
        ['キウイフルーツ', 'おいしいよ'],
        ['キワノ', 'ビタミンたくさん'],
        ['クリ(栗)', '栄養あるよ'],
        ['グアバ', 'おいしいよ'],
        ['グレープフルーツ', 'ビタミンたくさん'],
        ['香酸柑橘', '栄養あるよ'],
        ['サクランボ(桜桃)', 'おいしいよ'],
        ['ザクロ', 'ビタミンたくさん'],
        ['スイカ(西瓜)', '栄養あるよ'],
        ['スターフルーツ', 'おいしいよ'],
        ['スモモ(プラム)', 'ビタミンたくさん'],
        ['西洋ナシ(西洋梨)', '栄養あるよ'],
        ['チェリモヤ', 'おいしいよ'],
        ['中国ナシ(中国梨)', 'ビタミンたくさん'],
        ['ドラゴンフルーツ', '栄養あるよ'],
        ['ドリアン', 'おいしいよ'],
        ['ナシ(日本梨)', 'ビタミンたくさん'],
        ['ネクタリン', '栄養あるよ'],
        ['バナナ', 'おいしいよ'],
        ['パイナップル', 'ビタミンたくさん'],
        ['パッションフルーツ', '栄養あるよ'],
        ['パパイア', 'おいしいよ'],
        ['ビワ(枇杷)', 'ビタミンたくさん'],
        ['ブドウ(葡萄)', '栄養あるよ'],
        ['ブルーベリー', 'おいしいよ'],
        ['プルーン', 'ビタミンたくさん'],
        ['ベリー類', '栄養あるよ'],
        ['マルメロ', 'おいしいよ'],
        ['マンゴスチン', 'ビタミンたくさん'],
        ['マンゴー', '栄養あるよ'],
        ['メロン', 'おいしいよ'],
        ['モモ(桃)', 'ビタミンたくさん'],
        ['ライチ（レイシ）', '栄養あるよ'],
        ['リンゴ', 'おいしいよ'],
        ['レモン', 'ビタミンたくさん'],
    ]
    listnum = get_listnum(fruitlist)
    context = {
        'fruit' : fruitlist,
        'listnum' : listnum,
    }
    return render(request, 'list.html', context)

def get_listnum(list):
    listnum = len(list)
    return listnum 