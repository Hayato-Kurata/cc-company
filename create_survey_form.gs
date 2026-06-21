/**
 * 2026年 秋山・内山研究会　春学期アンケート 自動生成スクリプト
 *
 * 【使い方】
 * 1. https://script.google.com にアクセスし「新しいプロジェクト」を作成
 * 2. このコードを全て貼り付けて保存
 * 3. 上部の関数選択で createSurveyForm を選び「実行」
 * 4. 初回は権限の承認を求められるので許可する
 * 5. 実行ログ（表示 > ログ）に作成したフォームの編集URL・回答URLが出力されます
 *
 * 内容：配布された原本の質問（Q1〜Q14）＋「研究会全体（満足度など）」「研究の進捗」を追加。
 *       基本情報は「学籍番号／学年（選択式）／氏名」。
 */
function createSurveyForm() {
  var form = FormApp.create('2026年秋山・内山研究会 春学期の研究会の進め方についてのアンケート');

  form.setDescription(
    'このアンケートは来季の研究会の進め方に反映させるためのもので、成績には反映しません。'
  );
  form.setCollectEmail(false);

  var scaleAgree = ['①とてもそう思う', '②ややそう思う', '③どちらとも言えない', '④あまりそう思わない', '⑤そう思わない'];
  var scale5 = ['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり良くない', '⑤良くない'];

  // ===== 基本情報 =====
  form.addTextItem().setTitle('学籍番号').setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('学年')
    .setChoiceValues(['1年', '2年', '3年', '4年'])
    .showOtherOption(true)
    .setRequired(true);
  form.addTextItem().setTitle('氏名').setRequired(true);

  // ===== A 4限・5限共通事項 =====
  form.addSectionHeaderItem()
    .setTitle('A. マイプロ発表・担当係について【4限・5限 共通】')
    .setHelpText('マイプロ発表のやり方と、担当している係（担当大臣）についてうかがいます。');

  form.addSectionHeaderItem()
    .setTitle('（１）マイプロ発表')
    .setHelpText('今回マイプロ発表は1回目先行研究、2回目マイプロについてと2種類の発表形式としました。');

  form.addMultipleChoiceItem()
    .setTitle('Q１：発表回数（2回）について')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり必要ない', '⑤必要ない']);
  form.addParagraphTextItem().setTitle('Q１ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q２：先行研究に関する発表について')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり必要ない', '⑤必要ない']);
  form.addParagraphTextItem().setTitle('Q２ 上記回答した理由');

  form.addSectionHeaderItem().setTitle('（２）担当大臣（係）について');

  form.addTextItem().setTitle('Q3 あなたは何か係ですか？（係名を記入）');

  form.addMultipleChoiceItem()
    .setTitle('Q4 係として仕事をしましたか？')
    .setChoiceValues(['①良くやった', '②やややった', '③どちらとも言えない', '④あまりやっていない', '⑤やっていない', '⑥まだ実作業が発生していない']);
  form.addParagraphTextItem().setTitle('Q4 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q５ 同じ係の人と作業分担して仕事をしましたか？')
    .setChoiceValues(['①良くやった', '②やややった', '③どちらとも言えない', '④あまりやっていない', '⑤やっていない']);
  form.addParagraphTextItem().setTitle('Q５ 上記回答した理由');

  // ===== B 4限事項 =====
  form.addSectionHeaderItem()
    .setTitle('B. 輪読本・ファシリについて【4限】')
    .setHelpText('輪読本の内容と、ファシリ（進行役）の経験についてうかがいます。');

  form.addSectionHeaderItem()
    .setTitle('（１）輪読本')
    .setHelpText('今回の輪読本「14歳からの哲学」「これからの正義の話をしよう」でした。');

  form.addMultipleChoiceItem()
    .setTitle('Q６：この２冊の輪読本について')
    .setChoiceValues(scale5);
  form.addParagraphTextItem().setTitle('Q６ 上記回答した理由');

  form.addCheckboxItem()
    .setTitle('Q７：秋学期の輪読本についてどの分野を希望しますか？')
    .setChoiceValues([
      '①well・being（コミュニティヘルス）全般',
      '②社会福祉',
      '③AI関連',
      '④公共哲学',
      '⑤統計解析手法（回帰分析や検定など）',
      '⑥研究手法（混合研究など）'
    ])
    .showOtherOption(true);
  form.addTextItem().setTitle('Q７ ⑦その他を選んだ場合の分野を記入して下さい');

  form.addSectionHeaderItem().setTitle('（２）ファシリについて');

  form.addMultipleChoiceItem()
    .setTitle('Q８：ファシリ回数について（今回はファシリ係を2回していただきました）')
    .setChoiceValues(scale5);
  form.addParagraphTextItem().setTitle('Q８ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q９：ファシリ係を経験して')
    .setChoiceValues(['①とても良かった', '②やや良かった', '③どちらとも言えない', '④あまり良くなかった', '⑤良くなかった']);
  form.addParagraphTextItem().setTitle('Q９ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q１０：ファシリの準備時間について（1回あたりの合計）')
    .setHelpText('1回あたりのファシリ係としての準備時間（本読み・打ち合わせ・先生との相談・課題作成・パワポ作成などの合計）を教えて下さい。')
    .setChoiceValues(['①1時間未満', '②1〜2時間', '③2〜4時間', '④4〜6時間', '⑤6時間以上']);

  form.addParagraphTextItem()
    .setTitle('Q１１：ファシリ内容について')
    .setHelpText('ファシリ係を経験し、またグループワークを経験して気づいた点を教えて下さい。（自由記述）');

  // ===== C 5限事項 =====
  form.addSectionHeaderItem()
    .setTitle('C. 班活動について【5限】')
    .setHelpText('所属する班での役割や、他の班との関わりについてうかがいます。');

  form.addParagraphTextItem().setTitle('Q１２：あなたの所属する班内での主な役割は何ですか？');

  form.addMultipleChoiceItem()
    .setTitle('Q１３：他の班活動に参加する機会を望みますか？')
    .setHelpText('例えば、日を決めて「セカサポ班」全員が、自分が興味がある他の班にバラバラに体験参加する日を設けるなど。')
    .setChoiceValues(['①希望する', '②希望しない', '③どちらとも言えない']);

  // ===== D 研究会全体について（満足度など・追加） =====
  form.addSectionHeaderItem()
    .setTitle('D. 研究会全体について【満足度・振り返り】')
    .setHelpText('この春学期の研究会全体を振り返ってお答えください。');

  form.addMultipleChoiceItem()
    .setTitle('Q１４：この春学期の研究会全体として、満足していますか？')
    .setChoiceValues(['①とても満足', '②やや満足', '③どちらとも言えない', '④やや不満', '⑤不満']);
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

  // ===== E 研究（マイプロ）の進捗について（追加） =====
  form.addSectionHeaderItem()
    .setTitle('E. 研究（マイプロ）の進捗について')
    .setHelpText('ご自身の研究テーマ（マイプロ）の進み具合についてうかがいます。');

  form.addMultipleChoiceItem()
    .setTitle('Q２１：自分の研究テーマ（マイプロ）は、今学期で前進したと思いますか？')
    .setChoiceValues(['①とても前進した', '②やや前進した', '③どちらとも言えない', '④あまり進まなかった', '⑤ほとんど進まなかった']);
  form.addParagraphTextItem().setTitle('Q２１ 上記回答した理由');

  form.addMultipleChoiceItem()
    .setTitle('Q２２：研究会の活動（輪読・発表・ファシリ・グループワークなど）は、あなた自身の研究の役に立ちましたか？')
    .setChoiceValues(['①とても役に立った', '②やや役に立った', '③どちらとも言えない', '④あまり役に立たなかった', '⑤役に立たなかった']);
  form.addParagraphTextItem()
    .setTitle('Q２２ 具体的に役立った点／物足りなかった点があれば教えて下さい。');

  form.addParagraphTextItem()
    .setTitle('Q２３：現在の研究（マイプロ）の進捗状況を教えて下さい。')
    .setHelpText('例：テーマ設定／先行研究レビュー／リサーチクエスチョン／調査・分析 など、どこまで進んだか。');

  form.addParagraphTextItem()
    .setTitle('Q２４：研究を進める上でつまずいている点・相談したいことがあれば教えて下さい。');

  // ===== F その他・自由記述 =====
  form.addSectionHeaderItem()
    .setTitle('F. その他・ご意見【自由記述】')
    .setHelpText('今後の研究会の進め方について、自由にご記入ください。');

  form.addParagraphTextItem()
    .setTitle('Q２５：今後の研究会のあり方、進め方について何かご意見や要望があれば自由に記述して下さい。');

  // ===== 出力 =====
  Logger.log('✅ フォームを作成しました');
  Logger.log('編集用URL: ' + form.getEditUrl());
  Logger.log('回答用URL: ' + form.getPublishedUrl());
}
