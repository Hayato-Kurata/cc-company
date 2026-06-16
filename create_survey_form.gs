/**
 * 2026年 秋山・内山研究会　春学期アンケート 自動生成スクリプト（詳細版）
 *
 * 【使い方】
 * 1. https://script.google.com にアクセスし「新しいプロジェクト」を作成
 * 2. このコードを全て貼り付けて保存
 * 3. 上部の関数選択で createSurveyForm を選び「実行」
 * 4. 初回は権限の承認を求められるので許可する
 * 5. 実行ログ（表示 > ログ）に作成したフォームの編集URL・回答URLが出力されます
 *
 * 設計方針：所要時間より「ちゃんと聞ける」ことを優先。各評価には理由欄を付け、
 *           ファシリ準備時間は項目別に取得。学年は選択式（学部は不問）。
 */
function createSurveyForm() {
  var form = FormApp.create('2026年秋山・内山研究会 春学期アンケート');

  form.setDescription(
    'このアンケートは来季の研究会の進め方に反映させるためのもので、成績には反映しません。'
  );
  form.setCollectEmail(false);

  var scale5 = ['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり良くない', '⑤良くない'];
  var scale5do = ['①良くやった', '②やややった', '③どちらとも言えない', '④あまりやっていない', '⑤やっていない'];
  var scaleAgree = ['①とてもそう思う', '②ややそう思う', '③どちらとも言えない', '④あまりそう思わない', '⑤そう思わない'];

  // ===== 基本情報 =====
  form.addTextItem().setTitle('学籍番号').setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('学年')
    .setChoiceValues(['1年', '2年', '3年', '4年'])
    .showOtherOption(true)
    .setRequired(true);
  form.addTextItem().setTitle('氏名').setRequired(true);

  // ===== A 4限・5限共通事項 =====
  form.addSectionHeaderItem().setTitle('A 4限・5限共通事項');

  form.addSectionHeaderItem()
    .setTitle('（１）マイプロ発表')
    .setHelpText('今回マイプロ発表は1回目先行研究、2回目マイプロについてと2種類の発表形式としました。');

  form.addMultipleChoiceItem()
    .setTitle('Q１：発表回数（2回）について')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり必要ない', '⑤必要ない'])
    .setRequired(true);
  form.addParagraphTextItem().setTitle('Q１ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q２：先行研究に関する発表について')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり必要ない', '⑤必要ない'])
    .setRequired(true);
  form.addParagraphTextItem().setTitle('Q２ 上記回答した理由');

  form.addSectionHeaderItem().setTitle('（２）担当大臣（係）について');

  form.addTextItem().setTitle('Q3 あなたは何か係ですか？（係名を記入。なければ「なし」）');

  form.addMultipleChoiceItem()
    .setTitle('Q4 係として仕事をしましたか？')
    .setChoiceValues(scale5do.concat(['⑥まだ実作業が発生していない']));
  form.addParagraphTextItem().setTitle('Q4 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q５ 同じ係の人と作業分担して仕事をしましたか？')
    .setChoiceValues(scale5do);
  form.addParagraphTextItem().setTitle('Q５ 上記回答した理由');

  // ===== B 4限事項 =====
  form.addSectionHeaderItem().setTitle('B 4限事項');

  form.addSectionHeaderItem()
    .setTitle('（１）輪読本')
    .setHelpText('今回の輪読本「14歳からの哲学」「これからの正義の話をしよう」でした。');

  form.addMultipleChoiceItem()
    .setTitle('Q６：この２冊の輪読本について')
    .setChoiceValues(scale5)
    .setRequired(true);
  form.addParagraphTextItem().setTitle('Q６ 上記回答した理由');

  form.addCheckboxItem()
    .setTitle('Q７：秋学期の輪読本についてどの分野を希望しますか？（複数選択可）')
    .setChoiceValues([
      '①well・being（コミュニティヘルス）全般',
      '②社会福祉',
      '③AI関連',
      '④公共哲学',
      '⑤統計解析手法（回帰分析や検定など）',
      '⑥研究手法（混合研究など）'
    ])
    .showOtherOption(true);

  form.addSectionHeaderItem().setTitle('（２）ファシリについて');

  form.addMultipleChoiceItem()
    .setTitle('Q８：ファシリ回数について（今回はファシリ係を2回していただきました）')
    .setChoiceValues(scale5);
  form.addParagraphTextItem().setTitle('Q８ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q９：ファシリ係を経験して')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり良くなかった', '⑤良くなかった']);
  form.addParagraphTextItem().setTitle('Q９ 上記回答した理由');

  form.addSectionHeaderItem()
    .setTitle('Q１０：ファシリの準備時間について')
    .setHelpText('1回あたりのファシリ係としての準備時間を教えて下さい。');
  form.addTextItem().setTitle('本読み（時間）');
  form.addTextItem().setTitle('ペアのファシリ係との打ち合わせ（時間）');
  form.addTextItem().setTitle('先生との相談（時間）');
  form.addTextItem().setTitle('課題作成（時間）');
  form.addTextItem().setTitle('パワポ作成（時間）');
  form.addTextItem().setTitle('合計時間');

  form.addParagraphTextItem()
    .setTitle('Q１１：ファシリ内容について')
    .setHelpText('ファシリ係を経験し、またグループワークを経験して気づいた点を教えて下さい。（自由記述）');

  // ===== C 5限事項 =====
  form.addSectionHeaderItem().setTitle('C 5限事項');

  form.addParagraphTextItem().setTitle('Q１２：あなたの所属する班内での主な役割は何ですか？');

  form.addMultipleChoiceItem()
    .setTitle('Q１３：他の班活動に参加する機会を望みますか？')
    .setHelpText('例えば、日を決めて「セカサポ班」全員が、自分が興味がある他の班にバラバラに体験参加する日を設けるなど。')
    .setChoiceValues(['①希望する', '②希望しない', '③どちらとも言えない']);

  // ===== D 研究会全体について =====
  form.addSectionHeaderItem()
    .setTitle('D 研究会全体について')
    .setHelpText('この春学期の研究会全体を振り返ってお答えください。');

  form.addMultipleChoiceItem()
    .setTitle('Q１４：この春学期の研究会全体として、満足していますか？')
    .setChoiceValues(['①とても満足', '②やや満足', '③どちらとも言えない', '④やや不満', '⑤不満'])
    .setRequired(true);
  form.addParagraphTextItem().setTitle('Q１４ 上記回答した理由');

  form.addParagraphTextItem()
    .setTitle('Q１５：この半年で最も成長した・身についたと思うことは何ですか？')
    .setHelpText('（自由記述）');

  form.addMultipleChoiceItem()
    .setTitle('Q１６：あなた自身は研究会に主体的・積極的に参加できましたか？')
    .setChoiceValues(scaleAgree);
  form.addParagraphTextItem().setTitle('Q１６ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q１７：課題やファシリ準備などの負荷は適切でしたか？')
    .setChoiceValues(['①多すぎる', '②やや多い', '③ちょうど良い', '④やや少ない', '⑤少なすぎる']);

  form.addMultipleChoiceItem()
    .setTitle('Q１８：教員からの指導・フィードバックは役立ちましたか？')
    .setChoiceValues(scale5);
  form.addParagraphTextItem().setTitle('Q１８ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q１９：発言や質問がしやすい雰囲気でしたか？')
    .setChoiceValues(scaleAgree);

  form.addMultipleChoiceItem()
    .setTitle('Q２０：この研究会を後輩に勧めたいと思いますか？')
    .setChoiceValues(['①強く勧めたい', '②勧めたい', '③どちらとも言えない', '④あまり勧めない', '⑤勧めない']);

  // ===== E 研究（マイプロ）の進捗について =====
  form.addSectionHeaderItem()
    .setTitle('E 研究（マイプロ）の進捗について');

  form.addMultipleChoiceItem()
    .setTitle('Q２１：自分の研究テーマ（マイプロ）は、今学期で前進したと思いますか？')
    .setChoiceValues(['①とても前進した', '②やや前進した', '③どちらとも言えない', '④あまり進まなかった', '⑤ほとんど進まなかった'])
    .setRequired(true);
  form.addParagraphTextItem().setTitle('Q２１ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q２２：研究会の活動（輪読・発表・ファシリ・グループワークなど）は、あなた自身の研究の役に立ちましたか？')
    .setChoiceValues(['①とても役に立った', '②やや役に立った', '③どちらとも言えない', '④あまり役に立たなかった', '⑤役に立たなかった'])
    .setRequired(true);
  form.addParagraphTextItem()
    .setTitle('Q２２ 具体的に役立った点／物足りなかった点があれば教えて下さい。');

  form.addParagraphTextItem()
    .setTitle('Q２３：現在の研究（マイプロ）の進捗状況を教えて下さい。')
    .setHelpText('例：テーマ設定／先行研究レビュー／リサーチクエスチョン／調査・分析 など、どこまで進んだか。');

  form.addParagraphTextItem()
    .setTitle('Q２４：研究を進める上でつまずいている点・相談したいことがあれば教えて下さい。');

  // ===== F 自由記述 =====
  form.addSectionHeaderItem().setTitle('F 自由記述');

  form.addParagraphTextItem()
    .setTitle('Q２５：今後も「続けてほしい」と思うことを自由に記述して下さい。');

  form.addParagraphTextItem()
    .setTitle('Q２６：今後「変えてほしい・改善してほしい」と思うことを自由に記述して下さい。');

  form.addParagraphTextItem()
    .setTitle('Q２７：その他、研究会のあり方や進め方についてご意見や要望があれば自由に記述して下さい。');

  // ===== 出力 =====
  Logger.log('✅ フォームを作成しました（詳細版）');
  Logger.log('編集用URL: ' + form.getEditUrl());
  Logger.log('回答用URL: ' + form.getPublishedUrl());
}
