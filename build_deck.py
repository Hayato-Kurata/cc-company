# -*- coding: utf-8 -*-
"""指づくりワークショップ スタッフマニュアル(はじめてのスタッフ向け)
ダーク・ホラー調 PowerPoint 生成スクリプト
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---- パレット（ダーク・ホラー）----
BG        = RGBColor(0x0B, 0x0B, 0x0D)   # ほぼ黒
PANEL     = RGBColor(0x15, 0x15, 0x18)   # 少し明るい黒（パネル）
BLOOD     = RGBColor(0xB7, 0x12, 0x1C)   # 血のような赤
BLOOD_HI  = RGBColor(0xE6, 0x1A, 0x1A)   # 明るい赤(強調)
INK       = RGBColor(0xEC, 0xEC, 0xEC)   # オフホワイト
MUTE      = RGBColor(0x9A, 0x9A, 0x9E)   # ミュートグレー
LINEC     = RGBColor(0x3A, 0x10, 0x12)   # 暗い赤(罫線)

JP_FONT   = "Yu Gothic UI"   # 日本語フォント(Officeに広く搭載)

EMU_W = Inches(13.333)
EMU_H = Inches(7.5)


def set_ea_font(run, name=JP_FONT):
    """東アジア(日本語)フォントを明示指定。"""
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {})
            rPr.append(el)
        el.set("typeface", name)


def add_bg(slide, color=BG):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, EMU_W, EMU_H)
    s.fill.solid(); s.fill.fore_color.rgb = color
    s.line.fill.background()
    s.shadow.inherit = False
    # 背面へ
    sp = s._element; sp.getparent().remove(sp)
    slide.shapes._spTree.insert(2, sp)
    return s


def rect(slide, x, y, w, h, color, line=None):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = color
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False
    return s


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0
    tf.margin_top = 0; tf.margin_bottom = 0
    return tf


def run(p, text, size, color, bold=False, font=JP_FONT):
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color
    set_ea_font(r, font)
    return r


# ---- スライド内容 ----
# bullets: list of dict {t:text, lv:level(0/1), em:emphasis(bool), kicker:str|None}
SLIDES = []

SLIDES.append({
    "kind": "cover",
    "title": "指づくりワークショップ\nスタッフマニュアル",
    "sub": "はじめてのスタッフ向け 完全ガイド",
    "lines": [
        "ピエロ大好き人間（@I_LOVE_Clown）× Steenz",
        "自分の指の複製キーホルダーづくり ワークショップ",
        "このスライドを読めば、はじめてでも当日動けます",
    ],
    "foot": "迷ったら「進行統括」に聞けばOK",
})

SLIDES.append({
    "no": "01", "title": "このイベントって何をするの？",
    "lead": "まず全体像をつかもう",
    "bullets": [
        {"t": "お客さんが「自分の指のキーホルダー」を作る体験ワークショップ"},
        {"t": "料金は 3,000円／1回 約20分", "em": True},
        {"t": "席は6席（180cmテーブル×2台・各3席）＋講師席"},
        {"t": "主力イベントはデザインフェスタ／ニコニコ超会議"},
        {"t": "スタッフのメイン業務＝ワークショップ運営＋お客さんへの声かけ集客"},
    ],
})

SLIDES.append({
    "no": "02", "title": "当日の1日の流れ（集合〜撤収）",
    "lead": "10:00開場の場合の目安。実際の時刻は朝礼で共有",
    "bullets": [
        {"t": "集合・点呼（出展者証・身分証を忘れずに）"},
        {"t": "搬入 → ブース設営 → ディスプレイ仕上げ"},
        {"t": "レジ・釣り銭セット → WS道具スタンバイ・制作練習"},
        {"t": "朝礼（最終ブリーフィング） → 開場"},
        {"t": "開場中：接客・WS進行・物販・呼び込み"},
        {"t": "閉場後：撤収・売上集計・搬出・振り返り"},
    ],
})

SLIDES.append({
    "no": "03", "title": "開場前にやること",
    "lead": "開場までの準備の要点",
    "bullets": [
        {"t": "なるべくまとまって入場（バラバラだと時間がかかる）"},
        {"t": "設営は進行統括の指示に従って動く"},
        {"t": "釣り銭3〜4万円をセット（Steenzスタッフ2人で金額確認・1人では数えない）", "em": True},
        {"t": "PayPay用QRコードを設置"},
        {"t": "初参加スタッフは制作を1回通しで練習"},
        {"t": "朝礼で：役割分担・動線・休憩ローテ・緊急時対応・SNSルールを確認"},
    ],
})

SLIDES.append({
    "no": "04", "title": "ワークショップの作り方①（材料・道具・席）",
    "lead": "1人あたりに使う材料と道具",
    "bullets": [
        {"t": "かたと〜る 20g（型取り）"},
        {"t": "エコフレックス35：A剤10g＋B剤10g（必ず同量！）", "em": True},
        {"t": "キーホルダー金具 1個"},
        {"t": "道具：計量カップ／紙コップ／混ぜ棒／振動機／爪楊枝／絵具・筆／接着剤／タイマー"},
        {"t": "席は6席で確定＋整理券でタイムスロット運用（並ばせず時間に戻ってもらう）"},
    ],
})

SLIDES.append({
    "no": "05", "title": "ワークショップの進め方②（20分台本）",
    "lead": "台本通りに進めれば、はじめてでも20分で回せる",
    "bullets": [
        {"t": "受付・アイスブレイク＋アレルギー確認（ラテックス・シリコン）", "kicker": "0-2分"},
        {"t": "型取り（かたと〜る）→ 硬化を待つ（約10分・待ち時間は会話）", "kicker": "2-7分"},
        {"t": "流し込み（A剤＋B剤を同量で混合 → 気泡抜き → 流す）", "kicker": "7-12分"},
        {"t": "着色・仕上げ（ノーマル／ちょいグロ／ガチグロ）", "kicker": "12-17分"},
        {"t": "金具取付・撮影・SNS＆アンケート案内・お見送り", "kicker": "17-20分"},
    ],
})

SLIDES.append({
    "no": "06", "title": "安全・NG事項（必ず守る）",
    "lead": "ここだけは絶対に守ること",
    "danger": True,
    "bullets": [
        {"t": "アレルギー申告者（ラテックス・シリコン）にはお断りする", "em": True},
        {"t": "エコフレックスのA剤・B剤は必ず同量で混ぜる（比率ミスは未硬化の原因）", "em": True},
        {"t": "材料を皮膚に長時間つけたまま放置しない"},
        {"t": "WSの手順を勝手にアレンジしない"},
        {"t": "動画撮影は参加者の許可を取ってから"},
        {"t": "苦手・体調不良の素振りがあれば即中断、無理させない"},
    ],
})

SLIDES.append({
    "no": "07", "title": "接客・呼び込みトーク例",
    "lead": "そのまま使える声かけのことば",
    "bullets": [
        {"t": "呼び込み「ちょいグロな“自分の指のキーホルダー”作れまーす！」「20分でできます！」"},
        {"t": "通路を妨げない位置で声かけ。手が空いたら大きな声で集客"},
        {"t": "硬化待ちの会話：作家（@I_LOVE_Clown）の紹介、人気作の話、お客さんの趣味から広げる"},
        {"t": "会計時「お支払いは現金かPayPayです（カード不可）」「領収書いりますか？」"},
    ],
})

SLIDES.append({
    "no": "08", "title": "受付・会計のルール",
    "lead": "お金まわりは特に慎重に",
    "bullets": [
        {"t": "受付は基本1名、残りはWS作業へ"},
        {"t": "お釣りは3〜4万円（1,000円札中心＋5,000円札も数枚）"},
        {"t": "現金は最初と最後にSteenzスタッフ2人で確認・1人では絶対数えない → 収益シートに記録", "em": True},
        {"t": "予約客優先。当日枠は整理券で案内"},
        {"t": "売上は現金／電子決済別にその場で即メモ"},
        {"t": "値引き・サービスを個人判断でしない"},
    ],
})

SLIDES.append({
    "no": "09", "title": "SNS・アンケートの案内",
    "lead": "お見送り時にお願いすること",
    "bullets": [
        {"t": "「Xに #指キーホルダー で投稿いただけると作家が見にいきます」と案内"},
        {"t": "タグは #指キーホルダー ／ @I_LOVE_Clown"},
        {"t": "アンケートは全イベント共通の1本（印刷QRコードを見せて案内）"},
        {"t": "「1分で終わるアンケートにご協力お願いします！」"},
        {"t": "強制はしない。答えてくれたら一言お礼"},
    ],
})

SLIDES.append({
    "no": "10", "title": "スタッフの基本ルール",
    "lead": "参加前に必ず一読",
    "bullets": [
        {"t": "服装：黒基調・汚れてもいい服。スカート一律禁止。スニーカー（終日立ち仕事）"},
        {"t": "持ち物：スマホ・モバイルバッテリー・飲み物軽食・着替え・常備薬絆創膏"},
        {"t": "連絡：遅刻欠席は気づいた時点でLINEへ。朝が早い日は起きたら一言"},
        {"t": "休憩：1人合計1時間。全員同時はNG、30分ずつずらして交代"},
    ],
})

SLIDES.append({
    "no": "11", "title": "お金のこと（報酬・交通費）",
    "lead": "スタッフへの支払いについて",
    "bullets": [
        {"t": "報酬は日給 14,000円＋交通費", "em": True},
        {"t": "イベント終了後に銀行振込（振込先は終了後に個別確認）"},
        {"t": "交通費は「外部協力者用経費精算シート」に記入 → PDFにして渡邊さんへDM"},
        {"t": "電車・バスは領収書不要"},
        {"t": "詳しくは交通費・経費精算マニュアルを参照"},
    ],
})

SLIDES.append({
    "no": "12", "title": "緊急時対応",
    "lead": "何かあったら、まず進行統括へエスカレーション",
    "danger": True,
    "bullets": [
        {"t": "体調不良（軽度）：WS中断・休憩・水分。回復しなければ救護室へ"},
        {"t": "体調不良（重度・出血）：救護室に即連絡、119の判断は早めに", "em": True},
        {"t": "アレルギー反応：WS即中断・材料除去・救護室・LINE共有", "em": True},
        {"t": "PayPay不調：現金切替を最優先"},
        {"t": "釣り銭切れ：近隣ATM・両替所へ"},
        {"t": "クレーム：その場で謝罪 → 進行統括へ"},
    ],
})

SLIDES.append({
    "no": "13", "title": "持ち物チェックリスト ＆ まとめ",
    "lead": "搬入前の最終チェックと心構え",
    "bullets": [
        {"t": "WS用：材料・道具・見本サンプル・アレルギー確認用紙・タイマー"},
        {"t": "ブース：出展者証・什器・看板・整理券・QRコード・台車・ゴミ袋"},
        {"t": "会計：レジ箱・釣り銭・PayPay QR・予約表・領収書"},
        {"t": "個人：スマホ・着替え・飲み物・常備薬"},
        {"t": "困ったら・迷ったら、すべて進行統括へ。今日もよろしくお願いします！", "em": True},
    ],
})


# ---- 描画 ----
prs = Presentation()
prs.slide_width = EMU_W
prs.slide_height = EMU_H
blank = prs.slide_layouts[6]

TOTAL = len(SLIDES)

for idx, sd in enumerate(SLIDES):
    slide = prs.slides.add_slide(blank)
    add_bg(slide)

    if sd.get("kind") == "cover":
        # 左の太い血赤バー
        rect(slide, 0, 0, Inches(0.35), EMU_H, BLOOD)
        # うっすらパネル
        rect(slide, Inches(0.9), Inches(1.7), Inches(11.5), Inches(0.06), BLOOD)
        # タイトル
        tf = textbox(slide, Inches(0.95), Inches(1.95), Inches(11.4), Inches(2.6))
        first = True
        for ln in sd["title"].split("\n"):
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.line_spacing = 1.05
            run(p, ln, 46, INK, bold=True)
        # サブ
        tf2 = textbox(slide, Inches(0.95), Inches(4.35), Inches(11.4), Inches(0.6))
        p = tf2.paragraphs[0]
        run(p, sd["sub"], 22, BLOOD_HI, bold=True)
        # 行
        tf3 = textbox(slide, Inches(0.95), Inches(5.05), Inches(11.4), Inches(1.6))
        first = True
        for ln in sd["lines"]:
            p = tf3.paragraphs[0] if first else tf3.add_paragraph()
            first = False
            p.space_after = Pt(4)
            run(p, "▸ ", 15, BLOOD_HI, bold=True)
            run(p, ln, 15, MUTE)
        # フッター
        rect(slide, 0, Inches(6.95), EMU_W, Inches(0.55), PANEL)
        tff = textbox(slide, Inches(0.95), Inches(6.95), Inches(11.4), Inches(0.55), MSO_ANCHOR.MIDDLE)
        p = tff.paragraphs[0]
        run(p, "⚠ ", 14, BLOOD_HI, bold=True)
        run(p, sd["foot"], 14, INK, bold=True)
        continue

    # 通常スライド
    danger = sd.get("danger")
    head = BLOOD if not danger else BLOOD_HI

    # ヘッダ帯
    rect(slide, 0, 0, EMU_W, Inches(1.45), PANEL)
    rect(slide, 0, Inches(1.45), EMU_W, Inches(0.05), BLOOD)
    # ページ番号(大きく薄い赤)
    tfn = textbox(slide, Inches(0.55), Inches(0.18), Inches(1.5), Inches(1.1), MSO_ANCHOR.MIDDLE)
    p = tfn.paragraphs[0]
    run(p, sd["no"], 40, BLOOD, bold=True)
    # タイトル
    tft = textbox(slide, Inches(1.9), Inches(0.2), Inches(10.9), Inches(1.05), MSO_ANCHOR.MIDDLE)
    p = tft.paragraphs[0]
    if danger:
        run(p, "⚠ ", 28, BLOOD_HI, bold=True)
    run(p, sd["title"], 28, INK, bold=True)

    # リード文
    y = Inches(1.75)
    if sd.get("lead"):
        tfl = textbox(slide, Inches(0.95), y, Inches(11.4), Inches(0.5))
        p = tfl.paragraphs[0]
        run(p, sd["lead"], 16, BLOOD_HI, bold=True)
        y = Inches(2.45)

    # 箇条書き
    tfb = textbox(slide, Inches(0.95), y, Inches(11.6), Inches(7.2) - y)
    first = True
    for b in sd["bullets"]:
        p = tfb.paragraphs[0] if first else tfb.add_paragraph()
        first = False
        p.space_after = Pt(11)
        p.line_spacing = 1.06
        kicker = b.get("kicker")
        if kicker:
            run(p, kicker + "　", 18, BLOOD_HI, bold=True)
        else:
            run(p, "▌ ", 18, head, bold=True)
        col = BLOOD_HI if b.get("em") else INK
        run(p, b["t"], 18, col, bold=bool(b.get("em")))

    # フッター
    tff = textbox(slide, Inches(0.95), Inches(7.0), Inches(9.0), Inches(0.4), MSO_ANCHOR.MIDDLE)
    p = tff.paragraphs[0]
    run(p, "指づくりWS スタッフマニュアル", 10, MUTE)
    tfp = textbox(slide, Inches(11.4), Inches(7.0), Inches(1.4), Inches(0.4), MSO_ANCHOR.MIDDLE)
    p = tfp.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
    run(p, f"{idx}/{TOTAL-1}", 10, MUTE)

out = "指づくりWS_スタッフマニュアル_ダーク.pptx"
prs.save(out)
print("saved:", out)
