# -*- coding: utf-8 -*-
"""指づくりワークショップ スタッフマニュアル(はじめてのスタッフ向け)
ダーク・ホラー調 / 図解・レイアウト重視の PowerPoint 生成スクリプト
"""
from pptx import Presentation
from pptx.util import Inches as In, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---- パレット ----
BG       = RGBColor(0x0B, 0x0B, 0x0D)
PANEL    = RGBColor(0x16, 0x16, 0x1A)
PANEL2   = RGBColor(0x1E, 0x1E, 0x23)
BLOOD    = RGBColor(0xB7, 0x12, 0x1C)
BLOOD_HI = RGBColor(0xE6, 0x1A, 0x1A)
BLOOD_DK = RGBColor(0x4A, 0x0A, 0x0E)
INK      = RGBColor(0xEC, 0xEC, 0xEC)
MUTE     = RGBColor(0x9A, 0x9A, 0x9E)
LINEC    = RGBColor(0x40, 0x15, 0x18)

JP = "Yu Gothic UI"
W, H = 13.333, 7.5


def ea(run, name=JP):
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {}); rPr.append(el)
        el.set("typeface", name)


def bg(slide, color=BG):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, In(W), In(H))
    s.fill.solid(); s.fill.fore_color.rgb = color; s.line.fill.background()
    s.shadow.inherit = False
    sp = s._element; sp.getparent().remove(sp); slide.shapes._spTree.insert(2, sp)


def rrect(slide, x, y, w, h, fill, line=None, radius=0.09, lw=1.0):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, In(x), In(y), In(w), In(h))
    try: s.adjustments[0] = radius
    except Exception: pass
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(lw)
    s.shadow.inherit = False
    return s


def rect(slide, x, y, w, h, fill):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, In(x), In(y), In(w), In(h))
    s.fill.solid(); s.fill.fore_color.rgb = fill; s.line.fill.background()
    s.shadow.inherit = False
    return s


def tb(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    t = slide.shapes.add_textbox(In(x), In(y), In(w), In(h)).text_frame
    t.word_wrap = True; t.vertical_anchor = anchor
    t.margin_left = 0; t.margin_right = 0; t.margin_top = 0; t.margin_bottom = 0
    return t


def line(tf, runs, first=False, align=PP_ALIGN.LEFT, sa=3, ls=1.05):
    """runs: list of (text, size, color, bold)"""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align; p.space_after = Pt(sa); p.space_before = Pt(0); p.line_spacing = ls
    for txt, sz, col, bold in runs:
        r = p.add_run(); r.text = txt
        r.font.size = Pt(sz); r.font.bold = bold; r.font.color.rgb = col; ea(r)
    return p


def one(tf, text, size, color, bold=False, align=PP_ALIGN.LEFT, first=True, sa=3, ls=1.05):
    return line(tf, [(text, size, color, bold)], first=first, align=align, sa=sa, ls=ls)


prs = Presentation(); prs.slide_width = In(W); prs.slide_height = In(H)
BLANK = prs.slide_layouts[6]
PAGES = 14  # cover + 13


def base(no, title, danger=False, caption=None):
    s = prs.slides.add_slide(BLANK); bg(s)
    rect(s, 0, 0, W, 1.4, PANEL); rect(s, 0, 1.4, W, 0.045, BLOOD)
    t = tb(s, 0.55, 0.15, 1.5, 1.1, MSO_ANCHOR.MIDDLE)
    one(t, no, 38, BLOOD, bold=True)
    t = tb(s, 1.95, 0.15, 10.8, 1.1, MSO_ANCHOR.MIDDLE)
    one(t, ("⚠ " if danger else "") + title, 27, INK, bold=True)
    top = 1.72
    if caption:
        c = tb(s, 0.95, 1.55, 11.6, 0.4)
        one(c, caption, 13, MUTE)
        top = 2.05
    # footer
    f = tb(s, 0.95, 7.05, 9.0, 0.35, MSO_ANCHOR.MIDDLE)
    one(f, "指づくりWS 当日マニュアル", 9, MUTE)
    return s, top


def footer_pageno(s, idx):
    p = tb(s, 11.4, 7.05, 1.4, 0.35, MSO_ANCHOR.MIDDLE)
    one(p, f"{idx}/{PAGES-1}", 9, MUTE, align=PP_ALIGN.RIGHT)


def cols(n, gap=0.3, left=0.95, right=0.95):
    total = W - left - right
    cw = (total - gap * (n - 1)) / n
    return [left + i * (cw + gap) for i in range(n)], cw


def card_header(s, x, y, w, label, fill=BLOOD):
    """カード上部の見出し帯（角丸カードの上に小見出し）"""
    h = tb(s, x + 0.25, y + 0.18, w - 0.5, 0.5)
    one(h, label, 16, fill if fill != BLOOD else BLOOD_HI, bold=True)


# ============================================================
# 表紙
# ============================================================
s = prs.slides.add_slide(BLANK); bg(s)
rect(s, 0, 0, 0.35, H, BLOOD)
rect(s, 0.95, 1.75, 7.5, 0.07, BLOOD)
t = tb(s, 1.0, 2.0, 11.4, 2.4)
one(t, "指づくりワークショップ", 44, INK, bold=True, sa=2)
one(t, "当日マニュアル", 44, INK, bold=True, first=False)
t = tb(s, 1.0, 4.35, 11.4, 0.6)
one(t, "はじめてのスタッフ向け 完全ガイド", 21, BLOOD_HI, bold=True)
t = tb(s, 1.0, 5.1, 11.4, 1.6)
for ln in ["ピエロ大好き人間（@I_LOVE_Clown）× Steenz",
           "自分の指の複製キーホルダーづくり ワークショップ",
           "このスライドを読めば、はじめてでも当日動けます"]:
    one(t, "▸  " + ln, 15, MUTE, first=(ln.startswith("ピエロ")), sa=5)
rect(s, 0, 6.95, W, 0.55, PANEL)
t = tb(s, 1.0, 6.95, 11.4, 0.55, MSO_ANCHOR.MIDDLE)
line(t, [("⚠  ", 14, BLOOD_HI, True), ("迷ったら「進行統括」に聞けばOK", 14, INK, True)], first=True)

# ============================================================
# 01 概要 — スタッツタイル + メイン業務バンド
# ============================================================
s, top = base("01", "このイベントって何をするの？", caption="指キーホルダーづくりの体験WS ＋ イラスト・作品の物販を行う")
xs, cw = cols(4)
stats = [("3,000円", "WS 1回の料金"), ("約20分", "所要時間の目安"), ("最大6席", "場所により変動・6席で十分"), ("現金・PayPay", "カード不可")]
for x, (big, lab) in zip(xs, stats):
    rrect(s, x, top + 0.15, cw, 1.9, PANEL, line=LINEC)
    t = tb(s, x, top + 0.5, cw, 0.85, MSO_ANCHOR.MIDDLE)
    one(t, big, 27, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x, top + 1.42, cw, 0.5, MSO_ANCHOR.MIDDLE)
    one(t, lab, 12, MUTE, align=PP_ALIGN.CENTER)
by = top + 2.35
rrect(s, 0.95, by, W - 1.9, 1.95, PANEL, line=LINEC)
card_header(s, 0.95, by, W - 1.9, "スタッフのメイン業務")
t = tb(s, 1.3, by + 0.7, W - 2.6, 1.2)
line(t, [("① ", 16, BLOOD_HI, True), ("ワークショップの運営", 16, INK, True), ("（進行・受付）", 14, MUTE, False)], first=True, sa=6)
line(t, [("② ", 16, BLOOD_HI, True), ("物販対応", 16, INK, True), ("（イラスト・作品の販売）", 14, MUTE, False)], sa=6)
line(t, [("③ ", 16, BLOOD_HI, True), ("お客さんへの声かけ・集客", 16, INK, True), ("（手が空いたら大きな声で）", 14, MUTE, False)])
footer_pageno(s, 1)

# ============================================================
# 02 当日の流れ — 3フェーズ・タイムライン
# ============================================================
s, top = base("02", "当日の1日の流れ（集合〜撤収）", caption="10:00開場の場合の目安。実際の時刻は朝礼で共有します")
phases = [
    ("開場前", ["集合・点呼（証類を忘れずに）", "搬入 → ブース設営", "釣り銭・WS道具の準備", "朝礼（最終ブリーフィング）"]),
    ("開場中", ["接客・WS進行", "物販・呼び込み", "予約客を優先", "昼休憩は交代で（同時はNG）"]),
    ("閉場後", ["撤収・ブース掃除", "売上集計（2人で）", "搬出（レンタカー）", "振り返り・解散"]),
]
xs, cw = cols(3, gap=0.4)
ch = 4.3
for x, (ph, items) in zip(xs, phases):
    rrect(s, x, top + 0.1, cw, ch, PANEL, line=LINEC)
    rrect(s, x, top + 0.1, cw, 0.6, BLOOD, radius=0.12)
    t = tb(s, x, top + 0.13, cw, 0.55, MSO_ANCHOR.MIDDLE)
    one(t, ph, 17, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.3, top + 0.95, cw - 0.55, ch - 1.0)
    for i, it in enumerate(items):
        line(t, [("▌ ", 14, BLOOD_HI, True), (it, 14, INK, False)], first=(i == 0), sa=10, ls=1.05)
footer_pageno(s, 2)

# ============================================================
# 03 開場前にやること — 番号タイル 2×3
# ============================================================
s, top = base("03", "開場前にやること", caption="開場までの準備の要点")
items = [
    ("1", "なるべくまとまって入場", "バラバラだと時間がかかる", False),
    ("2", "設営は進行統括の指示で", "勝手に動かない", False),
    ("3", "釣り銭3〜4万円を2人で確認", "1人では数えない", True),
    ("4", "PayPay用QRコードを設置", "現金＋PayPayのみ", False),
    ("5", "初参加スタッフは1回練習", "通しで制作してみる", False),
    ("6", "朝礼で最終確認", "役割・動線・休憩・緊急時・SNS", False),
]
xs, cw = cols(2, gap=0.5)
rh = 1.4; gy = 0.25
for i, (num, ttl, sub, em) in enumerate(items):
    col = i % 2; row = i // 2
    x = xs[col]; y = top + 0.1 + row * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y, 1.1, rh, MSO_ANCHOR.MIDDLE)
    one(t, num, 34, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 1.3, y + 0.22, cw - 1.5, rh - 0.4, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 16, BLOOD_HI if em else INK, bold=True, sa=4)
    one(t, sub, 12, MUTE, first=False)
footer_pageno(s, 3)

# ============================================================
# 04 材料・道具・席
# ============================================================
s, top = base("04", "ワークショップの作り方①（材料・道具・席）", caption="1人あたりに使う材料と道具")
# 左：材料カード
lw_ = 5.7
rrect(s, 0.95, top + 0.1, lw_, 4.3, PANEL, line=LINEC)
card_header(s, 0.95, top + 0.1, lw_, "1人分の材料")
mats = [("かたと〜る", "型取り用（真空脱泡して使う）", False), ("エコフレックス35", "A剤＋B剤を必ず同量", True), ("クリップ＋チェーンボール", "1セット（型に設置）", False)]
yy = top + 0.85
for name, qty, em in mats:
    rrect(s, 1.25, yy, lw_ - 0.6, 1.0, PANEL2, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, 1.5, yy, lw_ - 1.0, 1.0, MSO_ANCHOR.MIDDLE)
    one(t, name, 16, INK, bold=True, sa=3)
    one(t, qty, 14, BLOOD_HI if em else MUTE, bold=em, first=False)
    yy += 1.12
# 右上：道具
rx = 0.95 + lw_ + 0.4; rw = W - 0.95 - rx
rrect(s, rx, top + 0.1, rw, 2.5, PANEL, line=LINEC)
card_header(s, rx, top + 0.1, rw, "道具")
t = tb(s, rx + 0.3, top + 0.8, rw - 0.6, 1.7)
for ln in ["計量カップ／紙コップ（小）", "混ぜ棒（ハンドミキサー）", "真空脱泡機（かたと〜る用）", "爪楊枝／接着剤／タイマー"]:
    one(t, "・ " + ln, 14, INK, first=(ln.startswith("計量")), sa=6)
# 右下：席
rrect(s, rx, top + 2.8, rw, 1.6, PANEL, line=LINEC)
card_header(s, rx, top + 2.8, rw, "席の運用")
t = tb(s, rx + 0.3, top + 3.4, rw - 0.6, 1.0)
line(t, [("最大6席", 16, BLOOD_HI, True), ("（場所・イベントで変動。6席以上は不要）", 13, MUTE, False)], first=True, sa=5)
one(t, "整理券でタイムスロット運用（並ばせず時間に戻ってもらう）", 13, INK, first=False)
footer_pageno(s, 4)

# ============================================================
# 05 20分台本 — 5ステップ・タイムライン
# ============================================================
s, top = base("05", "ワークショップの進め方（受付〜完成）", caption="受付から完成まで6ステップ。アイスブレイクは挟まず進める")
steps = [
    ("①", "受付と誘導", "普通に受付をして席へ誘導する", False),
    ("②", "準備と検討", "スタッフがかたと〜る（型取り材）を準備／その間にお客さんはどの指で作るか考える", False),
    ("③", "型取り", "かたと〜るを真空脱泡機で気泡抜き → 容器に指を入れて型取り。どの指でもOK／同時2本は不可・1本ずつ", True),
    ("④", "成形（流し込み）", "型が固まったら指を抜く → エコフレックスをA＋B同量で混ぜて型に流し込む（エコフレックスは脱泡しない）", False),
    ("⑤", "仕上げ", "クリップ＋チェーンボールを型に設置 → 硬化を待つ", False),
    ("⑥", "完了", "指（成形物）を取り出して完成。着色は行わない", True),
]
xs, cw = cols(3, gap=0.3)
rh = 1.85; gy = 0.18
for i, (num, ttl, note, em) in enumerate(steps):
    x = xs[i % 3]; y = top + 0.05 + (i // 3) * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y + 0.2, cw - 0.5, 0.5)
    line(t, [(num + "  ", 22, BLOOD_HI, True), (ttl, 16, INK, True)], first=True)
    t = tb(s, x + 0.25, y + 0.82, cw - 0.5, rh - 0.9)
    one(t, note, 12.5, BLOOD_HI if em else INK, ls=1.12)
band = top + 0.05 + 2 * (rh + gy)
rrect(s, 0.95, band, W - 1.9, 0.6, BLOOD, radius=0.12)
t = tb(s, 0.95, band, W - 1.9, 0.6, MSO_ANCHOR.MIDDLE)
one(t, "最後にアンケートの案内をして終了。着色なし／同時に2本は不可 に注意", 14, INK, bold=True, align=PP_ALIGN.CENTER)
footer_pageno(s, 5)

# ============================================================
# 06 安全・NG — 警告カード 2×3
# ============================================================
s, top = base("06", "安全・NG事項（必ず守る）", danger=True, caption="ここだけは絶対に守ること")
ng = [
    ("アレルギー申告者はお断り", "ラテックス・シリコン", True),
    ("A剤・B剤は必ず同量", "比率ミスは未硬化の原因", True),
    ("材料を皮膚に放置しない", "長時間つけたままNG", False),
    ("手順を勝手にアレンジしない", "台本どおりに", False),
    ("動画撮影は許可を取ってから", "参加者の同意必須", False),
    ("苦手・不調の素振りは即中断", "無理させない", False),
]
xs, cw = cols(2, gap=0.5)
rh = 1.4; gy = 0.22
for i, (ttl, sub, em) in enumerate(ng):
    col = i % 2; row = i // 2
    x = xs[col]; y = top + 0.1 + row * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL2 if em else PANEL, line=BLOOD_HI if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, x + 0.25, y, 0.9, rh, MSO_ANCHOR.MIDDLE)
    one(t, "⚠", 26, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 1.1, y + 0.22, cw - 1.3, rh - 0.4, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 16, BLOOD_HI if em else INK, bold=True, sa=4)
    one(t, sub, 12, MUTE, first=False)
footer_pageno(s, 6)

# ============================================================
# 07 接客トーク — 3つの吹き出しカード
# ============================================================
s, top = base("07", "接客・呼び込みトーク例", caption="そのまま使える声かけのことば")
talks = [
    ("呼び込み", ["「ちょいグロな“自分の指のキーホルダー”作れまーす！」", "「20分でできます！」　※通路を妨げない位置で"]),
    ("硬化待ちの会話", ["作家（@I_LOVE_Clown）の紹介、人気作の話", "お客さんの指輪・ネイル・推し趣味から広げる"]),
    ("会計時", ["「お支払いは現金かPayPayです（カード不可）」", "「領収書いりますか？」"]),
]
yy = top + 0.15; chh = 1.45
for ttl, lns in talks:
    rrect(s, 0.95, yy, W - 1.9, chh, PANEL, line=LINEC)
    rrect(s, 1.2, yy + 0.25, 2.6, 0.55, BLOOD, radius=0.18)
    t = tb(s, 1.2, yy + 0.28, 2.6, 0.5, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, 4.1, yy + 0.2, W - 4.1 - 1.2, chh - 0.4, MSO_ANCHOR.MIDDLE)
    for j, ln in enumerate(lns):
        one(t, ln, 14, INK, first=(j == 0), sa=6)
    yy += chh + 0.25
footer_pageno(s, 7)

# ============================================================
# 08 受付・会計 — 重要ルール強調 + チップ
# ============================================================
s, top = base("08", "受付・会計のルール", caption="お金まわりは特に慎重に")
rrect(s, 0.95, top + 0.1, W - 1.9, 1.7, PANEL2, line=BLOOD_HI, lw=2.0)
t = tb(s, 1.3, top + 0.1, 1.2, 1.7, MSO_ANCHOR.MIDDLE)
one(t, "🔒", 34, INK, align=PP_ALIGN.CENTER)
t = tb(s, 2.5, top + 0.3, W - 2.5 - 1.2, 1.3, MSO_ANCHOR.MIDDLE)
one(t, "現金は最初と最後に Steenzスタッフ2人で確認", 19, BLOOD_HI, bold=True, sa=4)
one(t, "1人では絶対に数えない → 確認額は収益シートに記録", 15, INK, first=False)
chips = ["受付は基本1名（残りはWS）", "お釣り3〜4万円（5,000円札も）", "予約客を優先・当日枠は整理券",
         "売上は現金／電子別に即メモ", "値引き・サービスは個人判断しない", "PayPay不調は現金切替を最優先"]
xs, cw = cols(2, gap=0.5)
ry = top + 2.05
for i, c in enumerate(chips):
    col = i % 2; row = i // 2
    x = xs[col]; y = ry + row * 0.78
    rrect(s, x, y, cw, 0.62, PANEL, line=LINEC)
    t = tb(s, x + 0.25, y, cw - 0.4, 0.62, MSO_ANCHOR.MIDDLE)
    line(t, [("▌ ", 13, BLOOD_HI, True), (c, 13.5, INK, False)], first=True)
footer_pageno(s, 8)

# ============================================================
# 09 SNS・アンケート — 2大カード
# ============================================================
s, top = base("09", "SNS・アンケートの案内", caption="お見送り時にお願いすること")
xs, cw = cols(2, gap=0.5)
# SNS
x = xs[0]
rrect(s, x, top + 0.15, cw, 4.0, PANEL, line=LINEC)
rrect(s, x, top + 0.15, cw, 0.7, BLOOD, radius=0.12)
t = tb(s, x, top + 0.18, cw, 0.62, MSO_ANCHOR.MIDDLE)
one(t, "SNS", 18, INK, bold=True, align=PP_ALIGN.CENTER)
t = tb(s, x + 0.35, top + 1.1, cw - 0.7, 3.0)
one(t, "「Xに投稿いただけると", 15, INK, sa=2)
one(t, "　作家が見にいきます」と案内", 15, INK, first=False, sa=12)
rrect(s, x + 0.35, top + 2.05, cw - 0.7, 0.6, PANEL2, line=BLOOD)
tt = tb(s, x + 0.35, top + 2.05, cw - 0.7, 0.6, MSO_ANCHOR.MIDDLE)
one(tt, "#指キーホルダー", 15, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
rrect(s, x + 0.35, top + 2.8, cw - 0.7, 0.6, PANEL2, line=BLOOD)
tt = tb(s, x + 0.35, top + 2.8, cw - 0.7, 0.6, MSO_ANCHOR.MIDDLE)
one(tt, "@I_LOVE_Clown", 15, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER)
# アンケート
x = xs[1]
rrect(s, x, top + 0.15, cw, 4.0, PANEL, line=LINEC)
rrect(s, x, top + 0.15, cw, 0.7, BLOOD, radius=0.12)
t = tb(s, x, top + 0.18, cw, 0.62, MSO_ANCHOR.MIDDLE)
one(t, "アンケート", 18, INK, bold=True, align=PP_ALIGN.CENTER)
t = tb(s, x + 0.35, top + 1.1, cw - 0.7, 3.0)
for j, ln in enumerate(["全イベント共通の1本（毎回作らない）",
                         "印刷QRコードを見せて案内",
                         "「1分で終わります！」とひと言",
                         "強制はしない。答えてくれたらお礼"]):
    line(t, [("▸ ", 14, BLOOD_HI, True), (ln, 14, INK, False)], first=(j == 0), sa=12)
footer_pageno(s, 9)

# ============================================================
# 10 基本ルール — 2×2 タイル
# ============================================================
s, top = base("10", "スタッフの基本ルール", caption="参加前に必ず一読")
tiles = [
    ("服装", ["黒基調・汚れてもいい服", "スカート一律禁止", "スニーカー（終日立ち仕事）"]),
    ("持ち物", ["スマホ・モバイルバッテリー", "飲み物・軽食・着替え", "常備薬・絆創膏"]),
    ("連絡", ["遅刻欠席は気づいた時点でLINE", "朝が早い日は起きたら一言", "調整は進行統括が対応"]),
    ("休憩", ["1人あたり合計1時間", "全員同時はNG", "30分ずつずらして交代"]),
]
xs, cw = cols(2, gap=0.5)
rh = 2.0; gy = 0.25
for i, (ttl, lns) in enumerate(tiles):
    col = i % 2; row = i // 2
    x = xs[col]; y = top + 0.1 + row * (rh + gy)
    rrect(s, x, y, cw, rh, PANEL, line=LINEC)
    rrect(s, x + 0.3, y + 0.28, 1.5, 0.55, BLOOD, radius=0.18)
    tt = tb(s, x + 0.3, y + 0.31, 1.5, 0.5, MSO_ANCHOR.MIDDLE)
    one(tt, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.35, y + 1.0, cw - 0.7, rh - 1.0)
    for j, ln in enumerate(lns):
        line(t, [("・ ", 13, BLOOD_HI, True), (ln, 13.5, INK, False)], first=(j == 0), sa=5)
footer_pageno(s, 10)

# ============================================================
# 11 お金 — 大きな数字 + フロー
# ============================================================
s, top = base("11", "お金のこと（報酬・交通費）", caption="スタッフへの支払いについて")
rrect(s, 0.95, top + 0.2, 4.4, 3.6, PANEL2, line=BLOOD, lw=2.0)
t = tb(s, 0.95, top + 0.7, 4.4, 1.4, MSO_ANCHOR.MIDDLE)
one(t, "日給", 16, MUTE, align=PP_ALIGN.CENTER, sa=2)
one(t, "14,000円", 40, BLOOD_HI, bold=True, align=PP_ALIGN.CENTER, first=False)
t = tb(s, 0.95, top + 2.5, 4.4, 0.8, MSO_ANCHOR.MIDDLE)
one(t, "＋ 交通費", 20, INK, bold=True, align=PP_ALIGN.CENTER)
rx = 5.8; rw = W - 0.95 - rx
flow = [("受け取り方", "イベント終了後に銀行振込（振込先は終了後に個別確認）"),
        ("交通費の精算", "「外部協力者用 経費精算シート」に記入 → PDF化 → 渡邊さんへDM"),
        ("領収書", "電車・バスは領収書不要")]
yy = top + 0.2
for i, (h, b) in enumerate(flow):
    rrect(s, rx, yy, rw, 1.05, PANEL, line=LINEC)
    t = tb(s, rx + 0.3, yy + 0.15, rw - 0.6, 0.8, MSO_ANCHOR.MIDDLE)
    one(t, h, 14, BLOOD_HI, bold=True, sa=3)
    one(t, b, 13, INK, first=False, ls=1.05)
    yy += 1.2
footer_pageno(s, 11)

# ============================================================
# 12 緊急時 — 状況→対応 テーブル
# ============================================================
s, top = base("12", "緊急時対応", danger=True, caption="迷わず進行統括へエスカレーション")
rows = [
    ("体調不良（軽度）", "WS中断・休憩・水分。回復しなければ救護室へ", False),
    ("体調不良（重度・出血）", "救護室に即連絡、119の判断は早めに", True),
    ("アレルギー反応", "WS即中断・材料除去・救護室・LINE共有", True),
    ("PayPay不調", "現金切替を最優先（復旧は後回し）", False),
    ("釣り銭切れ", "近隣ATM・両替所へ", False),
    ("クレーム", "その場で謝罪 → 進行統括へ", False),
]
tx = 0.95; tw = W - 1.9; c1 = 3.6; rh = 0.62; y = top + 0.15
rrect(s, tx, y, tw, rh, BLOOD, radius=0.06)
t = tb(s, tx + 0.25, y, c1, rh, MSO_ANCHOR.MIDDLE); one(t, "状況", 15, INK, bold=True)
t = tb(s, tx + c1 + 0.25, y, tw - c1 - 0.4, rh, MSO_ANCHOR.MIDDLE); one(t, "対応", 15, INK, bold=True)
y += rh + 0.08
for stt, resp, em in rows:
    rrect(s, tx, y, tw, rh, PANEL2 if em else PANEL, line=BLOOD_HI if em else LINEC, lw=1.5 if em else 1.0)
    t = tb(s, tx + 0.25, y, c1, rh, MSO_ANCHOR.MIDDLE)
    one(t, stt, 13.5, BLOOD_HI if em else INK, bold=True)
    t = tb(s, tx + c1 + 0.25, y, tw - c1 - 0.4, rh, MSO_ANCHOR.MIDDLE)
    one(t, resp, 13.5, INK)
    y += rh + 0.08
footer_pageno(s, 12)

# ============================================================
# 13 持ち物 + まとめ — 4列チェックリスト + 締めバンド
# ============================================================
s, top = base("13", "持ち物チェックリスト ＆ まとめ", caption="搬入前の最終チェック")
checks = [
    ("WS用", ["材料一式", "道具一式", "見本サンプル", "アレルギー確認用紙", "タイマー"]),
    ("ブース", ["出展者証・什器", "看板・POP", "整理券・QR", "台車", "ゴミ袋"]),
    ("会計", ["レジ箱・釣り銭", "PayPay QR", "予約表・受付表", "領収書", "売上メモ"]),
    ("個人", ["スマホ・充電器", "着替え", "飲み物・軽食", "常備薬・絆創膏", ""]),
]
xs, cw = cols(4, gap=0.3)
chh = 3.3
for x, (ttl, items) in zip(xs, checks):
    rrect(s, x, top + 0.1, cw, chh, PANEL, line=LINEC)
    rrect(s, x, top + 0.1, cw, 0.55, BLOOD, radius=0.14)
    t = tb(s, x, top + 0.13, cw, 0.5, MSO_ANCHOR.MIDDLE)
    one(t, ttl, 15, INK, bold=True, align=PP_ALIGN.CENTER)
    t = tb(s, x + 0.25, top + 0.85, cw - 0.4, chh - 0.9)
    fr = True
    for it in items:
        if not it: continue
        line(t, [("□ ", 13, BLOOD_HI, True), (it, 13, INK, False)], first=fr, sa=7); fr = False
rrect(s, 0.95, top + 3.65, W - 1.9, 0.8, BLOOD, radius=0.1)
t = tb(s, 0.95, top + 3.65, W - 1.9, 0.8, MSO_ANCHOR.MIDDLE)
one(t, "困ったら・迷ったら、すべて進行統括へ。今日もよろしくお願いします！", 17, INK, bold=True, align=PP_ALIGN.CENTER)
footer_pageno(s, 13)

out = "指づくりWS_当日マニュアル_ダーク.pptx"
prs.save(out)
print("saved:", out, "/ slides:", len(prs.slides._sldIdLst))
