# -*- coding: utf-8 -*-
"""
倉田速音さんの活動紹介スライド (PowerPoint) を生成するスクリプト。
出典はネット上の公開情報（プレスリリース・メディア記事等）に基づく。
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---- カラーパレット（空のグラデーション＝ブランドの世界観に合わせて） ----
NAVY   = RGBColor(0x1B, 0x2A, 0x4A)   # 深い夜空
BLUE   = RGBColor(0x2E, 0x6F, 0xB5)   # 空色
SKY    = RGBColor(0x6FB,  0x00, 0x00) if False else RGBColor(0x7E, 0xC8, 0xE3)  # 淡い空
ORANGE = RGBColor(0xF2, 0x8C, 0x3B)   # 夕陽
YELLOW = RGBColor(0xF7, 0xC5, 0x4C)   # 太陽
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
INK    = RGBColor(0x22, 0x2A, 0x3A)   # 本文
GRAY   = RGBColor(0x5B, 0x66, 0x77)
LIGHT  = RGBColor(0xF3, 0xF6, 0xFA)   # 背景

FONT = "Yu Gothic"
FONT_B = "Yu Gothic"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(BLANK)


def bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def rect(slide, x, y, w, h, color, line=False):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sp.fill.solid()
    sp.fill.fore_color.rgb = color
    if not line:
        sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return tb, tf


def setpar(p, text, size, color, bold=False, font=FONT, align=PP_ALIGN.LEFT,
           space_after=6, line=1.15):
    p.text = text
    p.alignment = align
    p.space_after = Pt(space_after)
    p.line_spacing = line
    for r in p.runs:
        r.font.size = Pt(size)
        r.font.color.rgb = color
        r.font.bold = bold
        r.font.name = font
    return p


def gradient_bg(slide, c1, c2, angle=45):
    """簡易グラデーション背景（上下の矩形を重ねて表現）。"""
    big = rect(slide, 0, 0, SW, SH, c1)
    # XMLでグラデーションを設定
    sp = big.fill._xPr
    # 既存solidFillを除去
    for tag in ('a:solidFill', 'a:noFill', 'a:gradFill'):
        for el in sp.findall(qn(tag)):
            sp.remove(el)
    grad = sp.makeelement(qn('a:gradFill'), {})
    lst = grad.makeelement(qn('a:gsLst'), {})
    for pos, col in ((0, c1), (100000, c2)):
        gs = grad.makeelement(qn('a:gs'), {'pos': str(pos)})
        srgb = grad.makeelement(qn('a:srgbClr'), {'val': '%02X%02X%02X' % (col[0], col[1], col[2])})
        gs.append(srgb)
        lst.append(gs)
    grad.append(lst)
    lin = grad.makeelement(qn('a:lin'), {'ang': str(angle * 60000), 'scaled': '1'})
    grad.append(lin)
    # 挿入位置（lnの前）
    ln = sp.find(qn('a:ln'))
    if ln is not None:
        ln.addprevious(grad)
    else:
        sp.append(grad)
    return big


def sun(slide, cx, cy, r, color, alpha=None):
    s = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx - r, cy - r, r * 2, r * 2)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    s.shadow.inherit = False
    if alpha is not None:
        # 透過設定
        sf = s.fill.fore_color._xFill
        srgb = sf.find(qn('a:srgbClr'))
        a = srgb.makeelement(qn('a:alpha'), {'val': str(int(alpha * 1000))})
        srgb.append(a)
    return s


# 共通：コンテンツスライドのヘッダー
def header(slide, kicker, title, num):
    bg(slide, WHITE)
    # 左の縦アクセント
    rect(slide, 0, 0, Inches(0.22), SH, ORANGE)
    # ヘッダーバー帯
    _, tf = textbox(slide, Inches(0.7), Inches(0.45), Inches(11.8), Inches(0.4))
    setpar(tf.paragraphs[0], kicker, 14, ORANGE, bold=True, space_after=2)
    _, tf2 = textbox(slide, Inches(0.7), Inches(0.78), Inches(11.8), Inches(0.95))
    setpar(tf2.paragraphs[0], title, 30, NAVY, bold=True)
    # 下線
    rect(slide, Inches(0.72), Inches(1.62), Inches(2.4), Pt(3), YELLOW)
    # ページ番号
    _, pf = textbox(slide, Inches(12.4), Inches(6.95), Inches(0.7), Inches(0.4))
    setpar(pf.paragraphs[0], str(num), 11, GRAY, align=PP_ALIGN.RIGHT)


def bullets(slide, items, x, y, w, h, size=17, gap=10, color=INK):
    tb, tf = textbox(slide, x, y, w, h)
    for i, (mark, txt) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if mark:
            run = p.add_run(); run.text = mark + "  "
            run.font.size = Pt(size); run.font.bold = True
            run.font.color.rgb = ORANGE; run.font.name = FONT
        run2 = p.add_run(); run2.text = txt
        run2.font.size = Pt(size); run2.font.color.rgb = color; run2.font.name = FONT
        p.space_after = Pt(gap); p.line_spacing = 1.2
    return tb


def card(slide, x, y, w, h, title, body, accent=BLUE):
    c = rect(slide, x, y, w, h, LIGHT)
    rect(slide, x, y, w, Inches(0.12), accent)
    tb, tf = textbox(slide, x + Inches(0.25), y + Inches(0.3), w - Inches(0.5), h - Inches(0.5))
    setpar(tf.paragraphs[0], title, 17, NAVY, bold=True, space_after=6)
    for line in body:
        p = tf.add_paragraph()
        setpar(p, line, 13, GRAY, line=1.2, space_after=3)
    return c


# =====================================================================
# Slide 1 — タイトル
# =====================================================================
s = add_slide()
gradient_bg(s, NAVY, BLUE, angle=60)
# 太陽
sun(s, Inches(10.7), Inches(2.0), Inches(1.6), YELLOW, alpha=85)
sun(s, Inches(10.7), Inches(2.0), Inches(1.1), ORANGE, alpha=90)
# キャッチ
_, tf = textbox(s, Inches(0.9), Inches(2.25), Inches(9.5), Inches(0.6))
setpar(tf.paragraphs[0], "ACTIVITY  PROFILE", 16, SKY, bold=True, space_after=2)
_, tf = textbox(s, Inches(0.85), Inches(2.75), Inches(11.0), Inches(1.6))
setpar(tf.paragraphs[0], "太陽の下で、自分らしく。", 46, WHITE, bold=True, line=1.1)
_, tf = textbox(s, Inches(0.9), Inches(4.25), Inches(10.5), Inches(1.0))
setpar(tf.paragraphs[0], "倉田 速音 ／ Hayato Kurata", 26, YELLOW, bold=True, space_after=4)
setpar(tf.add_paragraph(), "尋常性白斑から生まれた UVカット・ファッションブランド「HAYATO KURATA」", 16, WHITE)
rect(s, Inches(0.92), Inches(5.55), Inches(3.0), Pt(3), ORANGE)

# =====================================================================
# Slide 2 — 人物紹介 / プロフィール
# =====================================================================
s = add_slide()
header(s, "WHO IS HE?", "倉田速音さんとは", 2)
# 左：プロフィールカード
panel = rect(s, Inches(0.7), Inches(2.0), Inches(4.4), Inches(4.7), NAVY)
sun(s, Inches(2.9), Inches(3.2), Inches(0.95), YELLOW, alpha=90)
_, tf = textbox(s, Inches(0.95), Inches(4.35), Inches(3.9), Inches(2.2))
setpar(tf.paragraphs[0], "倉田 速音", 28, WHITE, bold=True, align=PP_ALIGN.CENTER, space_after=4)
setpar(tf.add_paragraph(), "Hayato Kurata", 15, SKY, align=PP_ALIGN.CENTER, space_after=12)
setpar(tf.add_paragraph(), "株式会社HAYATO KURATA 代表（CEO）", 13, WHITE, align=PP_ALIGN.CENTER, space_after=4)
setpar(tf.add_paragraph(), "角川ドワンゴ学園 N高等学校 起業部 出身", 13, WHITE, align=PP_ALIGN.CENTER)
# 右：箇条書き
bullets(s, [
    ("●", "尋常性白斑（難病）と向き合いながら活動する若き起業家。"),
    ("●", "小学5年生で発症し、紫外線を避ける生活を余儀なくされた当事者。"),
    ("●", "自身の経験を起点に、同じ悩みを持つ人のための洋服づくりを決意。"),
    ("●", "高校在学中（N高 起業部）にファッションブランドを起業。"),
    ("●", "掲げるビジョンは「5年後には世界へ」。"),
], Inches(5.5), Inches(2.15), Inches(7.2), Inches(4.4), size=18, gap=16)

# =====================================================================
# Slide 3 — 尋常性白斑とは
# =====================================================================
s = add_slide()
header(s, "BACKGROUND", "原点 ── 尋常性白斑という難病", 3)
bullets(s, [
    ("", "尋常性白斑（じんじょうせいはくはん）は、皮膚の色素が失われ"),
    ("", "白い斑点が広がる難病。倉田さんは小学5年生で発症した。"),
], Inches(0.7), Inches(2.0), Inches(12.0), Inches(1.2), size=18, gap=6, color=INK)
# 3つのデータカード
card(s, Inches(0.7),  Inches(3.4), Inches(3.85), Inches(3.0), "約100人に1人",
     ["国内の患者は約100万人と", "いわれ、決して珍しくない。", "しかし社会の認知は低い。"], accent=BLUE)
card(s, Inches(4.75), Inches(3.4), Inches(3.85), Inches(3.0), "紫外線が大敵",
     ["日光を浴びると肌が腫れ、", "皮膚がんのリスクも。外出を", "避ける生活を強いられた。"], accent=ORANGE)
card(s, Inches(8.8),  Inches(3.4), Inches(3.85), Inches(3.0), "見た目の悩み",
     ["顔や体に広がる白い斑点。", "いじめや偏見を経験し、", "自己肯定感も低下した。"], accent=YELLOW)

# =====================================================================
# Slide 4 — 困難から決意へ
# =====================================================================
s = add_slide()
header(s, "TURNING POINT", "「避ける」から「楽しむ」へ", 4)
# 大きな引用
qbox = rect(s, Inches(0.7), Inches(2.1), Inches(12.0), Inches(1.9), LIGHT)
rect(s, Inches(0.7), Inches(2.1), Inches(0.14), Inches(1.9), ORANGE)
_, tf = textbox(s, Inches(1.15), Inches(2.25), Inches(11.2), Inches(1.6), anchor=MSO_ANCHOR.MIDDLE)
setpar(tf.paragraphs[0],
       "「同じ病気の人が、太陽の下でも安心して楽しめる洋服をつくりたい。」",
       24, NAVY, bold=True, line=1.25)
bullets(s, [
    ("→", "紫外線を避け、人目を気にする日々。その経験を“ばね”に変えた。"),
    ("→", "「自分の難病を、みんなと一緒に克服する」という想いへ。"),
    ("→", "当事者だからこそ届けられる価値を、ファッションで形にすると決意。"),
], Inches(0.7), Inches(4.5), Inches(12.0), Inches(2.4), size=18, gap=16)

# =====================================================================
# Slide 5 — 会社・ブランド設立
# =====================================================================
s = add_slide()
header(s, "FOUNDING", "株式会社 HAYATO KURATA の設立", 5)
bullets(s, [
    ("●", "N高 起業部から生まれた法人。アパレル企業（アミアズ株式会社）に"),
    ("",  "    企画を持ち込み、2年余りの指導を受けて事業化を進めた。"),
    ("●", "起業部からの法人登記 第3号として会社を設立。"),
    ("●", "2021年2月、クラウドファンディング（CAMPFIRE / GoodMorning）に挑戦。"),
    ("",  "    目標金額 250万円。サンプル製作・商品化の資金を募った。"),
], Inches(0.7), Inches(2.0), Inches(12.2), Inches(2.6), size=17, gap=12)
card(s, Inches(0.7),  Inches(5.0), Inches(3.85), Inches(1.7), "起業部 発",
     ["高校在学中に法人化した", "学生起業家として注目。"], accent=BLUE)
card(s, Inches(4.75), Inches(5.0), Inches(3.85), Inches(1.7), "目標 250万円",
     ["クラウドファンディングで", "想いに共感する仲間を集めた。"], accent=ORANGE)
card(s, Inches(8.8),  Inches(5.0), Inches(3.85), Inches(1.7), "産学連携",
     ["プロのアパレル企業の", "指導を受け本気で商品化。"], accent=YELLOW)

# =====================================================================
# Slide 6 — ブランドコンセプト・製品
# =====================================================================
s = add_slide()
header(s, "PRODUCT", "ブランドが届けるもの", 6)
bullets(s, [
    ("", "「紫外線を気にせず、おしゃれを楽しめる」。"),
    ("", "UVカット機能とデザイン性を両立したエシカルファッションブランド。"),
], Inches(0.7), Inches(2.0), Inches(12.0), Inches(1.1), size=18, gap=6, color=INK)
card(s, Inches(0.7),  Inches(3.3), Inches(3.85), Inches(3.1), "UVカットの服",
     ["紫外線を避ける必要がある", "人が、太陽の下で安心して", "外を歩けるための一着。"], accent=BLUE)
card(s, Inches(4.75), Inches(3.3), Inches(3.85), Inches(3.1), "色が変わる服",
     ["紫外線に反応して色が変わる", "デザインも展開。“弱点”だった", "紫外線を遊び心に変えた。"], accent=ORANGE)
card(s, Inches(8.8),  Inches(3.3), Inches(3.85), Inches(3.1), "誰のために",
     ["尋常性白斑・光線過敏症・", "アルビノなど、UVを避けたい", "すべての人へ。"], accent=YELLOW)

# =====================================================================
# Slide 7 — 作品「ソラ時々グラデーション」
# =====================================================================
s = add_slide()
gradient_bg(s, BLUE, ORANGE, angle=60)
rect(s, 0, 0, Inches(0.22), SH, YELLOW)
sun(s, Inches(11.0), Inches(1.7), Inches(1.2), YELLOW, alpha=88)
_, tf = textbox(s, Inches(0.8), Inches(0.7), Inches(10.0), Inches(0.5))
setpar(tf.paragraphs[0], "DESIGN WORK", 15, WHITE, bold=True)
_, tf = textbox(s, Inches(0.8), Inches(1.15), Inches(10.5), Inches(1.0))
setpar(tf.paragraphs[0], "ソラ時々グラデーション", 36, WHITE, bold=True)
bullets(s, [
    ("◯", "ファッションコンペ「FASHION FRONTIER PROGRAM」ファイナリストに選出。"),
    ("◯", "空の移ろい＝白斑やコンプレックスも“グラデーション”として肯定するメッセージ。"),
    ("◯", "「弱さ」を隠すのではなく、その人らしい美しさとして表現する姿勢。"),
], Inches(0.8), Inches(2.7), Inches(11.0), Inches(2.6), size=19, gap=18, color=WHITE)
_, tf = textbox(s, Inches(0.85), Inches(5.7), Inches(11.0), Inches(1.0))
setpar(tf.paragraphs[0],
       "── 当事者の物語を、社会へ伝えるクリエイションへ。",
       18, NAVY, bold=True)

# =====================================================================
# Slide 8 — 歩み（タイムライン）
# =====================================================================
s = add_slide()
header(s, "TIMELINE", "これまでの歩み", 8)
# 横ライン
line_y = Inches(4.3)
rect(s, Inches(0.9), line_y, Inches(11.5), Pt(3), BLUE)
steps = [
    ("小5", "発症", "尋常性白斑を発症。紫外線を避ける生活が始まる。", NAVY),
    ("在学中", "起業へ", "N高 起業部で、当事者発のブランド構想を始動。", BLUE),
    ("2020", "会社設立", "株式会社HAYATO KURATA を起業（登記第3号）。", ORANGE),
    ("2021", "CF挑戦", "クラウドファンディングで商品化へ。目標250万円。", YELLOW),
    ("2022〜", "展開", "色が変わる服など新展開。受賞・メディアでも注目。", BLUE),
]
n = len(steps)
x0 = Inches(0.9)
span = Inches(11.5)
for i, (yr, ttl, desc, col) in enumerate(steps):
    cx = Emu(int(x0) + int(span) * i // (n - 1))
    # ノード
    sun(s, cx, line_y + Pt(1), Inches(0.16), col)
    up = (i % 2 == 0)
    bx = Emu(int(cx) - int(Inches(1.05)))
    if up:
        by = Inches(2.25)
    else:
        by = Inches(4.75)
    cardw = Inches(2.1)
    box = rect(s, bx, by, cardw, Inches(1.7), LIGHT)
    rect(s, bx, by, cardw, Inches(0.1), col)
    _, tf = textbox(s, bx + Inches(0.12), by + Inches(0.2), cardw - Inches(0.24), Inches(1.45))
    setpar(tf.paragraphs[0], yr, 13, col, bold=True, space_after=1)
    setpar(tf.add_paragraph(), ttl, 16, NAVY, bold=True, space_after=4)
    setpar(tf.add_paragraph(), desc, 10.5, GRAY, line=1.15)

# =====================================================================
# Slide 9 — 評価・メディア
# =====================================================================
s = add_slide()
header(s, "RECOGNITION", "広がる共感と注目", 9)
card(s, Inches(0.7),  Inches(2.2), Inches(3.85), Inches(2.0), "メディア掲載",
     ["テレビ東京「生きるを伝える」", "産経新聞 ほか各メディアで", "活動が紹介された。"], accent=BLUE)
card(s, Inches(4.75), Inches(2.2), Inches(3.85), Inches(2.0), "コンペ実績",
     ["FASHION FRONTIER", "PROGRAM ファイナリスト。", "創作面でも高い評価。"], accent=ORANGE)
card(s, Inches(8.8),  Inches(2.2), Inches(3.85), Inches(2.0), "若手起業家",
     ["MAKERS UNIVERSITY U-18", "など、次世代の挑戦者として", "取り上げられる。"], accent=YELLOW)
# 帯メッセージ
band = rect(s, Inches(0.7), Inches(4.6), Inches(11.95), Inches(1.9), NAVY)
_, tf = textbox(s, Inches(1.1), Inches(4.8), Inches(11.2), Inches(1.5), anchor=MSO_ANCHOR.MIDDLE)
setpar(tf.paragraphs[0],
       "「難病 × 起業 × ファッション」── 一人の当事者の挑戦が、",
       20, WHITE, bold=True, space_after=4)
setpar(tf.add_paragraph(),
       "同じ悩みを抱える人と社会の意識を、少しずつ変えている。",
       20, YELLOW, bold=True)

# =====================================================================
# Slide 10 — 現在とこれから
# =====================================================================
s = add_slide()
header(s, "NOW & NEXT", "現在、そしてこれから", 10)
bullets(s, [
    ("●", "ブランド「HAYATO KURATA」のCEOとして事業を継続。"),
    ("●", "10代向けメディア／コミュニティ「Steenz」などでも活動を広げる。"),
    ("",  "    事業開発・イベント・コミュニティ運営・SNS運用などに携わる。"),
    ("●", "同じ悩みを持つ人が前を向ける「選択肢」を増やし続けている。"),
], Inches(0.7), Inches(2.0), Inches(12.2), Inches(2.6), size=18, gap=14)
goal = rect(s, Inches(0.7), Inches(4.9), Inches(11.95), Inches(1.7), ORANGE)
_, tf = textbox(s, Inches(1.1), Inches(5.05), Inches(11.2), Inches(1.4), anchor=MSO_ANCHOR.MIDDLE)
setpar(tf.paragraphs[0], "VISION ── 5年後には、世界へ。", 26, WHITE, bold=True, space_after=4)
setpar(tf.add_paragraph(),
       "紫外線に悩む世界中の人へ、太陽の下で自分らしくいられる選択肢を。",
       16, WHITE)

# =====================================================================
# Slide 11 — クロージング
# =====================================================================
s = add_slide()
gradient_bg(s, NAVY, BLUE, angle=60)
sun(s, Inches(6.66), Inches(2.5), Inches(1.5), YELLOW, alpha=88)
sun(s, Inches(6.66), Inches(2.5), Inches(1.0), ORANGE, alpha=92)
_, tf = textbox(s, Inches(1.0), Inches(4.0), Inches(11.3), Inches(1.4))
setpar(tf.paragraphs[0], "弱さは、その人だけの色になる。", 38, WHITE, bold=True,
       align=PP_ALIGN.CENTER, line=1.15)
_, tf = textbox(s, Inches(1.0), Inches(5.4), Inches(11.3), Inches(0.8))
setpar(tf.paragraphs[0], "倉田 速音 ／ HAYATO KURATA", 20, YELLOW, bold=True,
       align=PP_ALIGN.CENTER)

# =====================================================================
# Slide 12 — 出典
# =====================================================================
s = add_slide()
bg(s, LIGHT)
rect(s, 0, 0, Inches(0.22), SH, ORANGE)
_, tf = textbox(s, Inches(0.7), Inches(0.6), Inches(11.0), Inches(0.7))
setpar(tf.paragraphs[0], "出典・参考（ネット上の公開情報）", 24, NAVY, bold=True)
rect(s, Inches(0.72), Inches(1.35), Inches(2.4), Pt(3), YELLOW)
srcs = [
    "FINDERS「Z世代の挑戦者たち（1）」 finders.me/articles.php?id=2706",
    "株式会社HAYATO KURATA プレスリリース（PR TIMES / value-press / @Press）",
    "N高等学校 ニュース「起業部法人登記第3号誕生」 nnn.ed.jp",
    "CAMPFIRE / GoodMorning クラウドファンディング camp-fire.jp/projects/344843",
    "FASHION FRONTIER PROGRAM「ソラ時々グラデーション」 ffp.jp",
    "ストレートプレス「紫外線で色が変わる服」 straightpress.jp",
    "MAKERS UNIVERSITY U-18 インタビュー u-18.makers-u.jp",
    "テレビ東京「生きるを伝える」 tv-tokyo.co.jp/ikiru",
    "本人 lit.link / Instagram・X（@hayato_uv）",
]
tb, tf = textbox(s, Inches(0.7), Inches(1.85), Inches(12.0), Inches(5.0))
for i, src in enumerate(srcs):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    run = p.add_run(); run.text = "・ " + src
    run.font.size = Pt(14); run.font.color.rgb = GRAY; run.font.name = FONT
    p.space_after = Pt(9); p.line_spacing = 1.2
_, tf = textbox(s, Inches(0.7), Inches(6.95), Inches(12.0), Inches(0.4))
setpar(tf.paragraphs[0],
       "※ 公開情報を基にした紹介資料です。最新の活動状況は本人の各SNS等をご確認ください。",
       11, GRAY)

# =====================================================================
# 発表者ノート（話す原稿）を各スライドへ
# =====================================================================
NOTES = [
    "【導入】本日は、尋常性白斑という難病と向き合いながらファッションブランドを立ち上げた"
    "倉田速音さんの活動を紹介します。テーマは『太陽の下で、自分らしく』です。"
    "（つかみ）皆さんは、日光を浴びられないとしたら何を諦めるでしょうか？",
    "【人物紹介】倉田速音さんは、株式会社HAYATO KURATAの代表。N高等学校の起業部出身です。"
    "小5で発症した尋常性白斑の当事者であり、自身の経験を起点に高校在学中に起業しました。"
    "ビジョンは『5年後には世界へ』。まず人物像を押さえてください。",
    "【背景】活動の原点は病気です。尋常性白斑は約100人に1人、国内に約100万人といわれます。"
    "紫外線で肌が腫れ皮膚がんのリスクもあり、外出を避ける生活に。見た目の悩みからいじめや"
    "自己肯定感の低下も経験しました。3つの困難を具体的に伝えます。",
    "【転機】ここが物語の核心です。『避ける』生活を、『楽しむ』に変えたい。"
    "同じ病気の人が太陽の下でも安心して楽しめる洋服をつくりたい――。"
    "“自分の難病をみんなと克服する”という前向きな決意に変わった瞬間を強調します。",
    "【設立】想いを形にしたのが起業です。N高起業部からアパレル企業アミアズに企画を持ち込み、"
    "2年余りの指導を受けて事業化。起業部の法人登記第3号として設立し、2021年2月には"
    "目標250万円のクラウドファンディングに挑戦しました。学生起業のリアルを伝えます。",
    "【製品】ブランドが届ける価値は『紫外線を気にせず、おしゃれを楽しめる』こと。"
    "UVカットの服に加え、紫外線で色が変わる服も展開し、弱点だった紫外線を遊び心に変えました。"
    "対象は白斑・光線過敏症・アルビノなどUVを避けたいすべての人です。",
    "【作品】『ソラ時々グラデーション』はFASHION FRONTIER PROGRAMのファイナリスト作品。"
    "空の移ろいになぞらえ、白斑やコンプレックスも“グラデーション”として肯定するメッセージです。"
    "弱さを隠さず、その人らしい美しさとして表現する姿勢を語ります。",
    "【歩み】ここまでの流れをタイムラインで整理します。発症→起業構想→会社設立→"
    "クラウドファンディング→新展開と受賞。一つの困難が、行動を通じて広がっていく様子を"
    "俯瞰で見せ、聞き手に全体像を掴んでもらいます。",
    "【評価】活動はテレビ東京『生きるを伝える』や産経新聞などで紹介され、"
    "コンペでも評価されています。『難病×起業×ファッション』という掛け算が、"
    "同じ悩みを持つ人と社会の意識を少しずつ変えている――というメッセージで締めます。",
    "【現在とこれから】今もHAYATO KURATAのCEOを続けつつ、10代向けメディア『Steenz』などへ"
    "活動を広げています。掲げるのは『5年後には世界へ』。紫外線に悩む世界中の人へ、"
    "自分らしくいられる選択肢を届ける――未来の話で前向きに展望します。",
    "【締め】最後はメッセージで締めます。『弱さは、その人だけの色になる』。"
    "倉田さんの挑戦が伝えるのは、コンプレックスも自分らしさに変えられるということ。"
    "聞き手に一言、行動や応援を促して終えます。",
    "【出典】本資料はネット上の公開情報（プレスリリース、メディア記事、本人SNS等）に基づきます。"
    "質疑では最新状況は本人の各SNSを参照する旨を案内してください。",
]
for slide, note in zip(prs.slides, NOTES):
    slide.notes_slide.notes_text_frame.text = note

out = "/home/user/cc-company/slides/倉田速音_活動紹介.pptx"
prs.save(out)
print("saved:", out, "slides:", len(prs.slides._sldIdLst), "notes:", len(NOTES))
