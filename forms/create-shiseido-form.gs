/**
 * 資生堂イベント アンケート（感想フォーム）自動生成スクリプト
 *
 * ■ 使い方
 *   1. https://script.google.com を開き「新しいプロジェクト」を作成
 *   2. このファイルの中身をすべて貼り付け
 *   3. （任意）下の CONTENTS のコンテンツ名を実際のプログラム名に書き換え
 *   4. 関数「createShiseidoForm」を選択して実行（▶）
 *   5. 初回は権限の承認が求められるので許可
 *   6. 実行ログ（表示 → ログ）に出力される「編集URL / 回答URL」を開く
 *
 * ■ 仕様：匿名・全8問・満足度中心（参加前後の期待ギャップ／コンテンツごとの感想を含む）
 */

// 実際のプログラム名に書き換えてください
const CONTENTS = [
  'コンテンツA（例：オープニング）',
  'コンテンツB（例：体験ワークショップ）',
  'コンテンツC（例：トークセッション）'
];

function createShiseidoForm() {
  const form = FormApp.create('資生堂イベント アンケート');

  form.setDescription(
    '本日は資生堂のイベントにご参加いただき、ありがとうございました。\n' +
    '今後の改善のため、簡単なアンケートにご協力ください（2〜3分）。\n' +
    '本アンケートは匿名です。お名前やメールアドレスなど個人が特定される情報はいただきません。'
  );

  // --- 匿名化設定 ---
  form.setCollectEmail(false);            // メールアドレスを収集しない
  form.setLimitOneResponsePerUser(false); // ログイン必須にしない
  form.setProgressBar(true);
  form.setConfirmationMessage(
    'アンケートへのご協力、ありがとうございました。\n' +
    'いただいたご意見は今後のイベントの向上に活用させていただきます。'
  );

  // ===== セクション1：満足度 =====
  form.addPageBreakItem().setTitle('セクション1：満足度');

  // Q1 総合満足度（5段階）
  form.addScaleItem()
    .setTitle('Q1. 本日のイベントの総合的な満足度を教えてください。')
    .setBounds(1, 5)
    .setLabels('まったく満足していない', 'とても満足している')
    .setRequired(true);

  // Q2 満足度の理由
  form.addParagraphTextItem()
    .setTitle('Q2. その満足度を選んだ理由を教えてください。')
    .setRequired(false);

  // ===== セクション2：参加前と参加後 =====
  form.addPageBreakItem().setTitle('セクション2：参加前と参加後');

  // Q3 参加前の期待度（5段階）
  form.addScaleItem()
    .setTitle('Q3. 参加する前、このイベントにどのくらい期待していましたか。')
    .setBounds(1, 5)
    .setLabels('まったく期待していなかった', 'とても期待していた')
    .setRequired(true);

  // Q4 参加後の期待との比較
  form.addMultipleChoiceItem()
    .setTitle('Q4. 参加した後、その期待と比べてどうでしたか。')
    .setChoiceValues([
      '期待を大きく上回った',
      '期待を上回った',
      '期待どおりだった',
      '期待を下回った',
      '期待を大きく下回った'
    ])
    .setRequired(true);

  // ===== セクション3：コンテンツごとの感想 =====
  form.addPageBreakItem().setTitle('セクション3：コンテンツ（プログラム）ごとの感想');

  // Q5 コンテンツごとの満足度（グリッド）
  form.addGridItem()
    .setTitle('Q5. 各コンテンツの満足度を教えてください。')
    .setRows(CONTENTS)
    .setColumns(['とても良かった', '良かった', 'ふつう', 'いまひとつ', '良くなかった'])
    .setRequired(false);

  // Q6 良かったコンテンツと良かった点
  form.addParagraphTextItem()
    .setTitle('Q6. 特に良かったコンテンツと、その良かった点を教えてください。')
    .setRequired(false);

  // ===== セクション4：研究協力 =====
  form.addPageBreakItem().setTitle('セクション4：今後の研究協力について');

  // Q7 研究協力の意向（はい/いいえ）
  form.addMultipleChoiceItem()
    .setTitle('Q7. 今後、資生堂のイベントや活動に関する研究（アンケート・インタビュー等）にご協力いただけますか。')
    .setHelpText('匿名アンケートのため意向のみ伺います。実際にご協力いただける方は、別途ご案内する登録フォームからお申し込みください（任意・このアンケートとは紐づきません）。')
    .setChoiceValues(['はい', 'いいえ'])
    .setRequired(true);

  // ===== セクション5：自由記述 =====
  form.addPageBreakItem().setTitle('セクション5：自由記述');

  // Q8 自由意見
  form.addParagraphTextItem()
    .setTitle('Q8. その他、ご意見・ご感想・ご要望があれば自由にお書きください。')
    .setRequired(false);

  // --- 出力 ---
  Logger.log('編集URL : ' + form.getEditUrl());
  Logger.log('回答URL : ' + form.getPublishedUrl());
}
