/**
 * 「白斑の会 〜肌と人。〜」アンケート（感想フォーム）自動生成スクリプト
 *
 * ■ 使い方
 *   1. https://script.google.com を開き「新しいプロジェクト」を作成
 *   2. このファイルの中身をすべて貼り付け
 *   3. 関数「createShiseidoForm」を選択して実行（▶）
 *   4. 初回は権限の承認が求められるので許可
 *   5. 実行ログ（表示 → ログ）に出力される「編集URL / 回答URL」を開く
 *
 * ■ 対象イベント：白斑の会 〜肌と人。〜（白斑のある方限定／主催：倉田速音／supported by 資生堂）
 * ■ 仕様：匿名・満足度中心（参加前後の期待ギャップ／コンテンツごとの感想／研究協力の意向）
 * ■ 配慮：白斑の部位・範囲などの詳細は尋ねない／商品の売り込みは含めない
 */

// 当日のコンテンツ（告知の「当日のコンテンツ」に準拠）
const CONTENTS = [
  '① 白斑とは？（わかりやすく解説）',
  '② 白斑とともに生きる（倉田の活動のお話）',
  '③ カバーメイクのコツ（プロによるテクニック紹介）',
  '④ おしゃべり＆個別相談会（お茶を飲みながら交流）'
];

function createShiseidoForm() {
  const form = FormApp.create('白斑の会 〜肌と人。〜 アンケート');

  form.setDescription(
    '本日は「白斑の会 〜肌と人。〜」にご参加いただき、ありがとうございました。\n' +
    'よりよい会にしていくため、簡単なアンケートにご協力ください（3分ほど）。\n' +
    '本アンケートは匿名です。お名前など個人が特定される情報はいただきません。\n' +
    'なお、いただいた満足度やご感想は、匿名で今後の会の紹介・告知に使わせていただくことがあります（最後の設問で同意を確認します）。'
  );

  // --- 匿名化設定 ---
  form.setCollectEmail(false);            // メールアドレスを収集しない
  form.setLimitOneResponsePerUser(false); // ログイン必須にしない
  form.setProgressBar(true);
  form.setConfirmationMessage(
    'アンケートへのご協力、ありがとうございました。\n' +
    'いただいたお声を、これからの「白斑の会」づくりに活かしていきます。'
  );

  // ===== セクション1：全体の満足度 =====
  form.addPageBreakItem().setTitle('セクション1：全体の満足度');

  form.addScaleItem()
    .setTitle('Q1. 本日の会の総合的な満足度を教えてください。')
    .setBounds(1, 5)
    .setLabels('まったく満足していない', 'とても満足している')
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Q2. その満足度を選んだ理由を教えてください。')
    .setRequired(false);

  // ===== セクション2：コンテンツごとの感想 =====
  form.addPageBreakItem().setTitle('セクション2：コンテンツごとの感想');

  form.addGridItem()
    .setTitle('Q3. 各コンテンツの満足度を教えてください。')
    .setRows(CONTENTS)
    .setColumns(['とても良かった', '良かった', 'ふつう', 'いまひとつ', '参加していない'])
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Q4. 特に良かったコンテンツと、その良かった点を教えてください。')
    .setRequired(false);

  // ===== セクション3：今後について =====
  form.addPageBreakItem().setTitle('セクション3：今後について');

  form.addMultipleChoiceItem()
    .setTitle('Q5. 今後、白斑やカバーメイクに関する研究（アンケート・インタビュー等）にご協力いただけますか。')
    .setHelpText('匿名アンケートのため意向のみ伺います。実際にご協力いただける方は、別途ご案内する登録フォームからお申し込みください（任意・このアンケートとは紐づきません）。')
    .setChoiceValues(['はい', 'いいえ'])
    .setRequired(true);

  // ===== セクション4：要望・自由記述・掲載について =====
  form.addPageBreakItem().setTitle('セクション4：要望・自由記述・掲載について');

  form.addParagraphTextItem()
    .setTitle('Q6. 次回への要望・リクエストがあれば教えてください。')
    .setHelpText('取り上げてほしいテーマ、やってほしい企画、開催時間・場所・頻度など、どんなことでも歓迎です。')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Q7. その他、ご感想・ご意見など、自由にお書きください。')
    .setRequired(false);

  form.addCheckboxItem()
    .setTitle('Q8. いただいた満足度や感想を、今後の会の告知・宣伝に使わせていただくことがあります。差し支えなければチェックしてください。')
    .setHelpText('チェックがない回答は宣伝に引用しません。集計した数値（満足度の平均など）は匿名情報のため掲載に使う場合があります。')
    .setChoiceValues(['匿名（個人が特定されない形）での掲載に同意します'])
    .setRequired(false);

  // --- 出力 ---
  Logger.log('編集URL : ' + form.getEditUrl());
  Logger.log('回答URL : ' + form.getPublishedUrl());
}
