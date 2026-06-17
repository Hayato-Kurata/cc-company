# -*- coding: utf-8 -*-
"""② ワークショップマニュアル（指キーホルダーの作り方）"""
from deck_lib import *

FOOT = "指づくりWS ② ワークショップマニュアル"
prs, BLANK = new_prs()


def b(no, title, caption=None, danger=False):
    return base(prs, BLANK, no, title, FOOT, caption, danger)


TOTAL = 4

cover(prs, BLANK, "ワークショップ", "マニュアル",
      "指キーホルダーの作り方（材料・手順・安全）",
      ["WS進行・受付の担当者向け",
       "手順どおりに進めれば、はじめてでも回せる",
       "集合〜撤収などの運用は別冊③『当日運用マニュアル』へ"],
      "アレルギー申告者にはWSを実施しない")

# 01 WSの概要
s, top = b("01", "ワークショップの概要", caption="メニュー＝自分の指の複製キーホルダーづくり")
xs, cw = cols(4)
stats = [("3,000円", "1回の料金"), ("約20分", "所要時間の目安"), ("最大6席", "場所により変動・6席で十分"), ("1本ずつ", "同時に2本は不可")]
for x, (big, lab) in zip(xs, stats):
    rrect(s, x, top + 0.15, cw, 1.9, PANEL, line=LINEC)
    t = tb(s, x, top + 0.5, cw, 0.85, MSO_ANCHOR.MIDDLE); one(t, big, 27, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x, top + 1.42, cw, 0.5, MSO_ANCHOR.MIDDLE); one(t, lab, 12, MUTE, align=PP_ALIGN.CENTER)
by = top + 2.35
rrect(s, 0.95, by, W - 1.9, 1.95, PANEL, line=LINEC)
chead(s, 0.95, by, W - 1.9, "どんな体験？")
t = tb(s, 1.3, by + 0.7, W - 2.6, 1.2)
line(t, [("・ ", 15, BLOOD_HI, True), ("お客さんの指の型を取り、エコフレックスで複製キーホルダーを作る", 15, INK, False)], first=True, sa=6)
line(t, [("・ ", 15, BLOOD_HI, True), ("どの指でもOK／", 15, INK, False), ("着色は行わない", 15, BLOOD_HI, True)], sa=6)
line(t, [("・ ", 15, BLOOD_HI, True), ("WSのほか、イラスト・作品の物販も実施（物販の運用は別冊③）", 14, MUTE, False)])
pageno(s, 1, TOTAL)

# 02 材料・道具・席
s, top = b("02", "材料・道具・席", caption="1人あたりに使う材料と道具")
lw_ = 5.7
rrect(s, 0.95, top + 0.1, lw_, 4.3, PANEL, line=LINEC)
chead(s, 0.95, top + 0.1, lw_, "1人分の材料")
mats = [("かたと〜る", "型取り用（真空脱泡して使う）", False), ("エコフレックス35", "A剤＋B剤を必ず同量", True), ("クリップ＋チェーンボール", "1セット（型に設置）", False)]
yy = top + 0.85
for name, qty, em in mats:
    rrect(s, 1.25, yy, lw_ - 0.6, 1.0, PANEL2, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, 1.5, yy, lw_ - 1.0, 1.0, MSO_ANCHOR.MIDDLE)
    one(t, name, 16, INK, bold=True, sa=3); one(t, qty, 14, BLOOD_HI if em else MUTE, bold=em, first=False)
    yy += 1.12
rx = 0.95 + lw_ + 0.4; rw = W - 0.95 - rx
rrect(s, rx, top + 0.1, rw, 2.5, PANEL, line=LINEC)
chead(s, rx, top + 0.1, rw, "道具")
t = tb(s, rx + 0.3, top + 0.8, rw - 0.6, 1.7)
for ln in ["計量カップ／紙コップ（小）", "混ぜ棒（ハンドミキサー）", "真空脱泡機（かたと〜る用）", "爪楊枝／接着剤／タイマー"]:
    one(t, "・ " + ln, 14, INK, first=(ln.startswith("計量")), sa=6)
rrect(s, rx, top + 2.8, rw, 1.6, PANEL, line=LINEC)
chead(s, rx, top + 2.8, rw, "席の運用")
t = tb(s, rx + 0.3, top + 3.4, rw - 0.6, 1.0)
line(t, [("最大6席", 16, BLOOD_HI, True), ("（場所・イベントで変動。6席以上は不要）", 13, MUTE, False)], first=True, sa=5)
one(t, "整理券でタイムスロット運用（並ばせず時間に戻ってもらう）", 13, INK, first=False)
pageno(s, 2, TOTAL)

# 03 進め方6ステップ
s, top = b("03", "ワークショップの進め方（受付〜完成）", caption="受付から完成まで6ステップ。アイスブレイクは挟まず進める")
steps = [("①", "受付と誘導", "普通に受付をして席へ誘導する", False),
         ("②", "準備と検討", "スタッフがかたと〜る（型取り材）を準備／その間にお客さんはどの指で作るか考える", False),
         ("③", "型取り", "かたと〜るを真空脱泡機で気泡抜き → 容器に指を入れて型取り。どの指でもOK／同時2本は不可・1本ずつ", True),
         ("④", "成形（流し込み）", "型が固まったら指を抜く → エコフレックスをA＋B同量で混ぜて型に流し込む（エコフレックスは脱泡しない）", False),
         ("⑤", "仕上げ", "クリップ＋チェーンボールを型に設置 → 硬化を待つ", False),
         ("⑥", "完了", "指（成形物）を取り出して完成。着色は行わない", True)]
xs, cw = cols(3, gap=0.3); rh = 1.85; gy = 0.18
for i, (num, ttl, note, em) in enumerate(steps):
    x = xs[i % 3]; y = top + 0.05 + (i // 3) * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y + 0.2, cw - 0.5, 0.5)
    line(t, [(num + "  ", 22, BLOOD_HI, True), (ttl, 16, INK, True)], first=True)
    t = tb(s, x + 0.25, y + 0.82, cw - 0.5, rh - 0.9); one(t, note, 12.5, BLOOD_HI if em else INK, ls=1.12)
band = top + 0.05 + 2 * (rh + gy)
rrect(s, 0.95, band, W - 1.9, 0.6, BLOOD, radius=0.12)
t = tb(s, 0.95, band, W - 1.9, 0.6, MSO_ANCHOR.MIDDLE)
one(t, "最後にアンケートの案内をして終了。着色なし／同時に2本は不可 に注意", 14, INK, bold=True, align=PP_ALIGN.CENTER)
pageno(s, 3, TOTAL)

# 04 安全・NG
s, top = b("04", "安全・NG事項（必ず守る）", caption="ここだけは絶対に守ること", danger=True)
ng = [("アレルギー申告者はお断り", "ラテックス・シリコン", True), ("A剤・B剤は必ず同量", "比率ミスは未硬化の原因", True),
      ("材料を皮膚に放置しない", "長時間つけたままNG", False), ("手順を勝手にアレンジしない", "マニュアルどおりに", False),
      ("動画撮影は許可を取ってから", "参加者の同意必須", False), ("苦手・不調の素振りは即中断", "無理させない", False)]
xs, cw = cols(2, gap=0.5); rh = 1.4; gy = 0.22
for i, (ttl, sub, em) in enumerate(ng):
    x = xs[i % 2]; y = top + 0.1 + (i // 2) * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD_HI if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y, 0.9, rh, MSO_ANCHOR.MIDDLE); one(t, "⚠", 26, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 1.1, y + 0.22, cw - 1.3, rh - 0.4, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 16, BLOOD_HI if em else INK, bold=True, sa=4); one(t, sub, 12, MUTE, first=False)
pageno(s, 4, TOTAL)

out = "指づくりWS_②ワークショップマニュアル_ダーク.pptx"
prs.save(out); print("saved:", out, "/ slides:", len(prs.slides._sldIdLst))
