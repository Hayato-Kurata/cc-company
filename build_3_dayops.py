# -*- coding: utf-8 -*-
"""③ 当日運用マニュアル（集合〜撤収・接客・会計・緊急時）"""
from deck_lib import *

FOOT = "指づくりWS ③ 当日運用マニュアル"
prs, BLANK = new_prs()


def b(no, title, caption=None, danger=False):
    return base(prs, BLANK, no, title, FOOT, caption, danger)


TOTAL = 9

cover(prs, BLANK, "当日運用マニュアル", None,
      "集合〜撤収・接客・会計・緊急時",
      ["当日スタッフ向け。前日までに一読",
       "迷ったら「進行統括」に聞けばOK",
       "WS（指キーホルダー）の作り方は別冊②へ"],
      "困ったら・迷ったら、すべて進行統括へ")

# 01 当日の流れ
s, top = b("01", "当日の1日の流れ（集合〜撤収）", caption="10:00開場の場合の目安。実際の時刻は朝礼で共有します")
phases = [("開場前", ["集合・点呼（証類を忘れずに）", "搬入 → ブース設営", "釣り銭・WS道具の準備", "朝礼（最終ブリーフィング）"]),
          ("開場中", ["接客・WS進行", "物販・呼び込み", "予約客を優先", "昼休憩は交代で（同時はNG）"]),
          ("閉場後", ["撤収・ブース掃除", "売上集計（2人で）", "搬出（レンタカー）", "振り返り・解散"])]
xs, cw = cols(3, gap=0.4); ch = 4.3
for x, (ph, items) in zip(xs, phases):
    rrect(s, x, top + 0.1, cw, ch, PANEL, line=LINEC)
    rrect(s, x, top + 0.1, cw, 0.6, BLOOD, radius=0.12)
    t = tb(s, x, top + 0.13, cw, 0.55, MSO_ANCHOR.MIDDLE); one(t, ph, 17, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.3, top + 0.95, cw - 0.55, ch - 1.0)
    for i, it in enumerate(items):
        line(t, [("▌ ", 14, BLOOD_HI, True), (it, 14, INK, False)], first=(i == 0), sa=10)
pageno(s, 1, TOTAL)

# 02 開場前
s, top = b("02", "開場前にやること", caption="開場までの準備の要点")
items = [("1", "なるべくまとまって入場", "バラバラだと時間がかかる", False), ("2", "設営は進行統括の指示で", "勝手に動かない", False),
         ("3", "釣り銭3〜4万円を2人で確認", "1人では数えない", True), ("4", "PayPay用QRコードを設置", "現金＋PayPayのみ", False),
         ("5", "初参加スタッフは1回練習", "通しで制作してみる", False), ("6", "朝礼で最終確認", "役割・動線・休憩・緊急時・SNS", False)]
xs, cw = cols(2, gap=0.5); rh = 1.4; gy = 0.25
for i, (num, ttl, sub, em) in enumerate(items):
    x = xs[i % 2]; y = top + 0.1 + (i // 2) * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y, 1.1, rh, MSO_ANCHOR.MIDDLE); one(t, num, 34, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 1.3, y + 0.22, cw - 1.5, rh - 0.4, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 16, BLOOD_HI if em else INK, bold=True, sa=4); one(t, sub, 12, MUTE, first=False)
pageno(s, 2, TOTAL)

# 03 接客トーク
s, top = b("03", "接客・呼び込みトーク例", caption="そのまま使える声かけのことば")
talks = [("呼び込み", ["「ちょいグロな“自分の指のキーホルダー”作れまーす！」", "「20分でできます！」　※通路を妨げない位置で"]),
         ("制作中の会話", ["作家（@I_LOVE_Clown）の紹介、人気作の話", "お客さんの指輪・ネイル・推し趣味から広げる"]),
         ("会計時", ["「お支払いは現金かPayPayです（カード不可）」", "「領収書いりますか？」"])]
yy = top + 0.15; chh = 1.45
for ttl, lns in talks:
    rrect(s, 0.95, yy, W - 1.9, chh, PANEL, line=LINEC)
    rrect(s, 1.2, yy + 0.25, 2.6, 0.55, BLOOD, radius=0.18)
    t = tb(s, 1.2, yy + 0.28, 2.6, 0.5, MSO_ANCHOR.MIDDLE); one(t, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, 4.1, yy + 0.2, W - 4.1 - 1.2, chh - 0.4, MSO_ANCHOR.MIDDLE)
    for j, ln in enumerate(lns):
        one(t, ln, 14, INK, first=(j == 0), sa=6)
    yy += chh + 0.25
pageno(s, 3, TOTAL)

# 04 受付・会計
s, top = b("04", "受付・会計のルール", caption="お金まわりは特に慎重に")
rrect(s, 0.95, top + 0.1, W - 1.9, 1.7, PANEL2, line=BLOOD_HI, lw=2.0)
t = tb(s, 1.3, top + 0.1, 1.2, 1.7, MSO_ANCHOR.MIDDLE); one(t, "🔒", 34, INK, align=PP_ALIGN.CENTER)
t = tb(s, 2.5, top + 0.3, W - 2.5 - 1.2, 1.3, MSO_ANCHOR.MIDDLE)
one(t, "現金は最初と最後に Steenzスタッフ2人で確認", 19, BLOOD_HI, bold=True, sa=4)
one(t, "1人では絶対に数えない → 確認額は収益シートに記録", 15, INK, first=False)
chips = ["受付は基本1名（残りはWS）", "お釣り3〜4万円（5,000円札も）", "予約客を優先・当日枠は整理券",
         "売上は現金／電子別に即メモ", "値引き・サービスは個人判断しない", "PayPay不調は現金切替を最優先"]
xs, cw = cols(2, gap=0.5); ry = top + 2.05
for i, c in enumerate(chips):
    x = xs[i % 2]; y = ry + (i // 2) * 0.78
    rrect(s, x, y, cw, 0.62, PANEL, line=LINEC)
    t = tb(s, x + 0.25, y, cw - 0.4, 0.62, MSO_ANCHOR.MIDDLE)
    line(t, [("▌ ", 13, BLOOD_HI, True), (c, 13.5, INK, False)], first=True)
pageno(s, 4, TOTAL)

# 05 SNS・アンケート
s, top = b("05", "SNS・アンケートの案内", caption="お見送り時にお願いすること")
xs, cw = cols(2, gap=0.5)
x = xs[0]
rrect(s, x, top + 0.15, cw, 4.0, PANEL, line=LINEC)
rrect(s, x, top + 0.15, cw, 0.7, BLOOD, radius=0.12)
t = tb(s, x, top + 0.18, cw, 0.62, MSO_ANCHOR.MIDDLE); one(t, "SNS", 18, INK, bold=True, align=PP_ALIGN.CENTER)
t = tb(s, x + 0.35, top + 1.1, cw - 0.7, 1.0)
one(t, "「Xに投稿いただけると", 15, INK, sa=2); one(t, "　作家が見にいきます」と案内", 15, INK, first=False)
rrect(s, x + 0.35, top + 2.05, cw - 0.7, 0.6, PANEL2, line=BLOOD)
tt = tb(s, x + 0.35, top + 2.05, cw - 0.7, 0.6, MSO_ANCHOR.MIDDLE); one(tt, "#指キーホルダー", 15, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
rrect(s, x + 0.35, top + 2.8, cw - 0.7, 0.6, PANEL2, line=BLOOD)
tt = tb(s, x + 0.35, top + 2.8, cw - 0.7, 0.6, MSO_ANCHOR.MIDDLE); one(tt, "@I_LOVE_Clown", 15, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
x = xs[1]
rrect(s, x, top + 0.15, cw, 4.0, PANEL, line=LINEC)
rrect(s, x, top + 0.15, cw, 0.7, BLOOD, radius=0.12)
t = tb(s, x, top + 0.18, cw, 0.62, MSO_ANCHOR.MIDDLE); one(t, "アンケート", 18, INK, bold=True, align=PP_ALIGN.CENTER)
t = tb(s, x + 0.35, top + 1.1, cw - 0.7, 3.0)
for j, ln in enumerate(["全イベント共通の1本（毎回作らない）", "印刷QRコードを見せて案内", "「1分で終わります！」とひと言", "強制はしない。答えてくれたらお礼"]):
    line(t, [("▸ ", 14, BLOOD_HI, True), (ln, 14, INK, False)], first=(j == 0), sa=12)
pageno(s, 5, TOTAL)

# 06 基本ルール
s, top = b("06", "スタッフの基本ルール", caption="参加前に必ず一読")
tiles = [("服装", ["黒基調・汚れてもいい服", "スカート一律禁止", "スニーカー（終日立ち仕事）"]),
         ("持ち物", ["スマホ・モバイルバッテリー", "飲み物・軽食・着替え", "常備薬・絆創膏"]),
         ("連絡", ["遅刻欠席は気づいた時点でLINE", "朝が早い日は起きたら一言", "調整は進行統括が対応"]),
         ("休憩", ["1人あたり合計1時間", "全員同時はNG", "30分ずつずらして交代"])]
xs, cw = cols(2, gap=0.5); rh = 2.0; gy = 0.25
for i, (ttl, lns) in enumerate(tiles):
    x = xs[i % 2]; y = top + 0.1 + (i // 2) * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL, line=LINEC)
    rrect(s, x + 0.3, y + 0.28, 1.5, 0.55, BLOOD, radius=0.18)
    tt = tb(s, x + 0.3, y + 0.31, 1.5, 0.5, MSO_ANCHOR.MIDDLE); one(tt, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.35, y + 1.0, cw - 0.7, rh - 1.0)
    for j, ln in enumerate(lns):
        line(t, [("・ ", 13, BLOOD_HI, True), (ln, 13.5, INK, False)], first=(j == 0), sa=5)
pageno(s, 6, TOTAL)

# 07 お金
s, top = b("07", "お金のこと（報酬・交通費）", caption="スタッフへの支払いについて")
rrect(s, 0.95, top + 0.2, 4.4, 3.6, PANEL2, line=BLOOD, lw=2.0)
t = tb(s, 0.95, top + 0.7, 4.4, 1.4, MSO_ANCHOR.MIDDLE)
one(t, "日給", 16, MUTE, align=PP_ALIGN.CENTER, sa=2); one(t, "14,000円", 40, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER, first=False)
t = tb(s, 0.95, top + 2.5, 4.4, 0.8, MSO_ANCHOR.MIDDLE); one(t, "＋ 交通費", 20, INK, bold=True, align=PP_ALIGN.CENTER)
rx = 5.8; rw = W - 0.95 - rx
flow = [("受け取り方", "イベント終了後に銀行振込（振込先は終了後に個別確認）"),
        ("交通費の精算", "「外部協力者用 経費精算シート」に記入 → PDF化 → 渡邊さんへDM"),
        ("領収書", "電車・バスは領収書不要")]
yy = top + 0.2
for h, bdy in flow:
    rrect(s, rx, yy, rw, 1.05, PANEL, line=LINEC)
    t = tb(s, rx + 0.3, yy + 0.15, rw - 0.6, 0.8, MSO_ANCHOR.MIDDLE)
    one(t, h, 14, BLOOD_HI, bold=True, sa=3); one(t, bdy, 13, INK, first=False)
    yy += 1.2
pageno(s, 7, TOTAL)

# 08 緊急時
s, top = b("08", "緊急時対応", caption="迷わず進行統括へエスカレーション", danger=True)
rows = [("体調不良（軽度）", "WS中断・休憩・水分。回復しなければ救護室へ", False),
        ("体調不良（重度・出血）", "救護室に即連絡、119の判断は早めに", True),
        ("アレルギー反応", "WS即中断・材料除去・救護室・LINE共有", True),
        ("PayPay不調", "現金切替を最優先（復旧は後回し）", False),
        ("釣り銭切れ", "近隣ATM・両替所へ", False),
        ("クレーム", "その場で謝罪 → 進行統括へ", False)]
tx = 0.95; tw = W - 1.9; c1 = 3.6; rh = 0.62; y = top + 0.15
rrect(s, tx, y, tw, rh, BLOOD, radius=0.06)
t = tb(s, tx + 0.25, y, c1, rh, MSO_ANCHOR.MIDDLE); one(t, "状況", 15, INK, bold=True)
t = tb(s, tx + c1 + 0.25, y, tw - c1 - 0.4, rh, MSO_ANCHOR.MIDDLE); one(t, "対応", 15, INK, bold=True)
y += rh + 0.08
for stt, resp, em in rows:
    rrect(s, tx, y, tw, rh, PANEL2 if em else PANEL, line=BLOOD_HI if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, tx + 0.25, y, c1, rh, MSO_ANCHOR.MIDDLE); one(t, stt, 13.5, BLOOD_HI if em else INK, bold=True)
    t = tb(s, tx + c1 + 0.25, y, tw - c1 - 0.4, rh, MSO_ANCHOR.MIDDLE); one(t, resp, 13.5, INK)
    y += rh + 0.08
pageno(s, 8, TOTAL)

# 09 持ち物＋まとめ
s, top = b("09", "持ち物チェックリスト ＆ まとめ", caption="搬入前の最終チェック")
checks = [("WS用", ["材料一式", "道具一式", "見本サンプル", "アレルギー確認用紙", "タイマー"]),
          ("ブース", ["出展者証・什器", "看板・POP", "整理券・QR", "台車", "ゴミ袋"]),
          ("会計", ["レジ箱・釣り銭", "PayPay QR", "予約表・受付表", "領収書", "売上メモ"]),
          ("個人", ["スマホ・充電器", "着替え", "飲み物・軽食", "常備薬・絆創膏", ""])]
xs, cw = cols(4, gap=0.3); chh = 3.3
for x, (ttl, items) in zip(xs, checks):
    rrect(s, x, top + 0.1, cw, chh, PANEL, line=LINEC)
    rrect(s, x, top + 0.1, cw, 0.55, BLOOD, radius=0.14)
    t = tb(s, x, top + 0.13, cw, 0.5, MSO_ANCHOR.MIDDLE); one(t, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.25, top + 0.85, cw - 0.4, chh - 0.9)
    fr = True
    for it in items:
        if not it: continue
        line(t, [("□ ", 13, BLOOD_HI, True), (it, 13, INK, False)], first=fr, sa=7); fr = False
rrect(s, 0.95, top + 3.65, W - 1.9, 0.8, BLOOD, radius=0.1)
t = tb(s, 0.95, top + 3.65, W - 1.9, 0.8, MSO_ANCHOR.MIDDLE)
one(t, "困ったら・迷ったら、すべて進行統括へ。今日もよろしくお願いします！", 17, INK, bold=True, align=PP_ALIGN.CENTER)
pageno(s, 9, TOTAL)

out = "指づくりWS_③当日運用マニュアル_ダーク.pptx"
prs.save(out); print("saved:", out, "/ slides:", len(prs.slides._sldIdLst))
