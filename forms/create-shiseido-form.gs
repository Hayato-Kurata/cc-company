/**
 * 資生堂イベント アンケート（感想フォーム）自動生成スクリプト
 *
 * ■ 使い方
 *   1. https://script.google.com を開き「新しいプロジェクト」を作成
 *   2. このファイルの中身をすべて貼り付け
 *   3. 関数「createShiseidoForm」を選択して実行（▶）
 *   4. 初回は権限の承認が求められるので許可
 *   5. 実行ログに出力される「編集URL / 回答URL」を開く
 *
 * ■ 仕様：匿名・全14問・全体満足度調査＋研究協力の意向確認（はい/いいえ）
 */
function createShiseidoForm() {
  // フォーム作成
  const form = FormApp.create('資生堂イベント アンケート');

  form.setDescription(
    '本日は資生堂のイベントにご参加いただき、誠にありがとうございました。\n' +
    '今後のイベントや商品・サービスの改善に役立てるため、アンケートへのご協力をお願いいたします。\n' +
    '所要時間は3〜5分ほどです。\n' +
    '本アンケートは匿名です。お名前やメールアドレスなど個人が特定される情報はいただきません。'
  );

  // --- 匿名化設定 ---
  form.setCollectEmail(false);          // メールアドレスを収集しない
  form.setLimitOneResponsePerUser(false); // ログイン必須にしない（個人が紐づかない）
  form.setProgressBar(true);
  form.setConfirmationMessage(
    'アンケートへのご協力、誠にありがとうございました。\n' +
    'いただいたご意見は、今後のイベントや商品・サービスの向上に活用させていただきます。'
  );

  // ===== セクション1：全体満足度 =====
  form.addPageBreakItem().setTitle('セクション1：イベント全体の満足度');

  // Q1 総合満足度（5段階）
  form.addScaleItem()
    .setTitle('Q1. 本日のイベントの総合的な満足度を教えてください。')
    .setBounds(1, 5)
    .setLabels('まったく満足していない', 'とても満足している')
    .setRequired(true);

  // Q2 満足度の理由（自由記述）
  form.addParagraphTextItem()
    .setTitle('Q2. その満足度を選んだ理由を教えてください。')
    .setRequired(false);

  // Q3 期待との比較
  form.addMultipleChoiceItem()
    .setTitle('Q3. イベントは期待していた内容と比べてどうでしたか。')
    .setChoiceValues([
      '期待を大きく上回った',
      '期待を上回った',
      '期待どおりだった',
      '期待を下回った',
      '期待を大きく下回った'
    ])
    .setRequired(true);

  // ===== セクション2：各項目評価 =====
  form.addPageBreakItem().setTitle('セクション2：各項目の評価');

  // Q4 項目別満足度（グリッド）
  form.addGridItem()
    .setTitle('Q4. 以下の項目について、それぞれの満足度を教えてください。')
    .setRows([
      '内容・プログラムの充実度',
      '進行・運営のスムーズさ',
      'スタッフの対応',
      '会場の雰囲気・環境',
      '所要時間（長さ）の適切さ'
    ])
    .setColumns(['とても満足', '満足', 'ふつう', '不満', 'とても不満'])
    .setRequired(true);

  // Q5 良かった点
  form.addParagraphTextItem()
    .setTitle('Q5. 特に良かった点・印象に残った点があれば教えてください。')
    .setRequired(false);

  // Q6 改善点
  form.addParagraphTextItem()
    .setTitle('Q6. 改善してほしい点・気になった点があれば教えてください。')
    .setRequired(false);

  // ===== セクション3：商品・ブランド関心 =====
  form.addPageBreakItem().setTitle('セクション3：商品・ブランドへの関心');

  // Q7 興味の高まり（5段階）
  form.addScaleItem()
    .setTitle('Q7. 本日のイベントを通じて、資生堂の商品・サービスへの興味は高まりましたか。')
    .setBounds(1, 5)
    .setLabels('まったく高まらなかった', 'とても高まった')
    .setRequired(true);

  // Q8 関心を持った商品
  form.addParagraphTextItem()
    .setTitle('Q8. 本日のイベントで特に関心を持った商品・サービスがあれば教えてください。')
    .setRequired(false);

  // Q9 NPS（0〜10）
  form.addScaleItem()
    .setTitle('Q9. 今回のイベントを友人・知人にすすめたいと思いますか。')
    .setBounds(0, 10)
    .setLabels('まったくすすめたくない', 'ぜひすすめたい')
    .setRequired(true);

  // ===== セクション4：研究協力 =====
  form.addPageBreakItem().setTitle('セクション4：今後の研究協力について');

  // Q10 研究協力の意向（はい/いいえ）
  form.addMultipleChoiceItem()
    .setTitle('Q10. 今後、資生堂の商品開発やイベントに関する研究（アンケート・モニター・インタビュー等）にご協力いただけますか。')
    .setHelpText('匿名アンケートのため、ここでは意向のみ伺います。実際にご協力いただける方は、別途ご案内する登録フォームからお申し込みください（任意・このアンケートとは紐づきません）。')
    .setChoiceValues(['はい', 'いいえ'])
    .setRequired(true);

  // ===== セクション5：属性 =====
  form.addPageBreakItem()
    .setTitle('セクション5：回答者について')
    .setHelpText('集計のための任意項目です。差し支えなければご回答ください。');

  // Q11 年代
  form.addMultipleChoiceItem()
    .setTitle('Q11. 年代')
    .setChoiceValues(['10代', '20代', '30代', '40代', '50代', '60代以上'])
    .setRequired(false);

  // Q12 性別
  form.addMultipleChoiceItem()
    .setTitle('Q12. 性別')
    .setChoiceValues(['女性', '男性', 'その他', '回答しない'])
    .setRequired(false);

  // Q13 認知経路
  form.addCheckboxItem()
    .setTitle('Q13. このイベントを何で知りましたか。')
    .setChoiceValues([
      '店頭・店員からの案内',
      '公式サイト・公式アプリ',
      'SNS（Instagram / X など）',
      'メールマガジン',
      '友人・知人の紹介',
      'その他'
    ])
    .setRequired(false);

  // ===== セクション6：自由記述 =====
  form.addPageBreakItem().setTitle('セクション6：自由記述');

  // Q14 自由意見
  form.addParagraphTextItem()
    .setTitle('Q14. 資生堂やイベントへのご意見・ご要望・応援メッセージなど、自由にお書きください。')
    .setRequired(false);

  // --- 出力 ---
  Logger.log('編集URL : ' + form.getEditUrl());
  Logger.log('回答URL : ' + form.getPublishedUrl());
}
