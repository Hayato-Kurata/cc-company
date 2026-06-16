/**
 * 2026年 秋山・内山研究会　春学期アンケート 自動生成スクリプト（約5分版）
 *
 * 【使い方】
 * 1. https://script.google.com にアクセスし「新しいプロジェクト」を作成
 * 2. このコードを全て貼り付けて保存
 * 3. 上部の関数選択で createSurveyForm を選び「実行」
 * 4. 初回は権限の承認を求められるので許可する
 * 5. 実行ログ（表示 > ログ）に作成したフォームの編集URL・回答URLが出力されます
 *
 * 設計方針：回答時間 約5分。選択式（タップ）中心、自由記述は最後の2問のみ。
 */
function createSurveyForm() {
  var form = FormApp.create('2026年秋山・内山研究会 春学期アンケート');

  form.setDescription(
    'このアンケートは来季の研究会の進め方に反映させるためのもので、成績には反映しません。所要時間は約5分です。'
  );
  form.setCollectEmail(false);

  var scale5 = ['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり良くない', '⑤良くない'];

  // ===== 基本情報 =====
  form.addTextItem().setTitle('学籍番号').setRequired(true);
  form.addTextItem().setTitle('学部学年').setRequired(true);
  form.addTextItem().setTitle('氏名').setRequired(true);

  // ===== A 授業内容 =====
  form.addSectionHeaderItem().setTitle('A 授業内容');

  form.addMultipleChoiceItem()
    .setTitle('Q１：マイプロ発表（1回目=先行研究、2回目=マイプロの2回形式）は良かったですか？')
    .setChoiceValues(scale5)
    .setRequired(true);

  form.addTextItem()
    .setTitle('Q２：あなたの担当している係は何ですか？（なければ「なし」）');

  form.addMultipleChoiceItem()
    .setTitle('Q３：係として仕事に取り組めましたか？')
    .setChoiceValues(['①良くやった', '②やややった', '③どちらとも言えない', '④あまりやっていない', '⑤やっていない', '⑥まだ実作業が発生していない'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q４：輪読本（「14歳からの哲学」「これからの正義の話をしよう」）は良かったですか？')
    .setChoiceValues(scale5)
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Q５：秋学期の輪読本はどの分野を希望しますか？（複数選択可）')
    .setChoiceValues([
      '①well・being（コミュニティヘルス）全般',
      '②社会福祉',
      '③AI関連',
      '④公共哲学',
      '⑤統計解析手法（回帰分析や検定など）',
      '⑥研究手法（混合研究など）'
    ])
    .showOtherOption(true);

  form.addMultipleChoiceItem()
    .setTitle('Q６：ファシリ係（今回2回担当）の経験は良かったですか？')
    .setChoiceValues(scale5)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q７：ファシリ1回あたりの準備時間（合計）はどれくらいでしたか？')
    .setChoiceValues(['①1時間未満', '②1〜2時間', '③2〜4時間', '④4〜6時間', '⑤6時間以上']);

  form.addMultipleChoiceItem()
    .setTitle('Q８：他の班活動に体験参加する機会を望みますか？')
    .setHelpText('例：日を決めて、自分が興味のある他の班にバラバラに体験参加する日を設けるなど。')
    .setChoiceValues(['①希望する', '②希望しない', '③どちらとも言えない']);

  // ===== B 研究会全体 =====
  form.addSectionHeaderItem().setTitle('B 研究会全体について');

  form.addMultipleChoiceItem()
    .setTitle('Q９：この春学期の研究会全体として満足していますか？')
    .setChoiceValues(['①とても満足', '②やや満足', '③どちらとも言えない', '④やや不満', '⑤不満'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q１０：あなた自身は研究会に主体的・積極的に参加できましたか？')
    .setChoiceValues(['①とてもそう思う', '②ややそう思う', '③どちらとも言えない', '④あまりそう思わない', '⑤そう思わない'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Q１１：課題やファシリ準備などの負荷は適切でしたか？')
    .setChoiceValues(['①多すぎる', '②やや多い', '③ちょうど良い', '④やや少ない', '⑤少なすぎる']);

  form.addMultipleChoiceItem()
    .setTitle('Q１２：この研究会を後輩に勧めたいと思いますか？')
    .setChoiceValues(['①強く勧めたい', '②勧めたい', '③どちらとも言えない', '④あまり勧めない', '⑤勧めない']);

  // ===== C 自由記述（任意） =====
  form.addSectionHeaderItem().setTitle('C 自由記述（任意）');

  form.addParagraphTextItem()
    .setTitle('Q１３：この半年で最も成長した・身についたと思うことは何ですか？');

  form.addParagraphTextItem()
    .setTitle('Q１４：今後「続けてほしいこと」「変えてほしいこと」があれば自由に記述して下さい。');

  // ===== 出力 =====
  Logger.log('✅ フォームを作成しました（約5分版）');
  Logger.log('編集用URL: ' + form.getEditUrl());
  Logger.log('回答用URL: ' + form.getPublishedUrl());
}
