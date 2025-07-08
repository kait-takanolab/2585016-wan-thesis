def calculate_score_only(user_text: str, target_text: str):
    # 去除多余空格等
    user_text = user_text.strip().replace(" ", "").replace("　", "")
    target_text = target_text.strip().replace(" ", "").replace("　", "")

    if len(target_text) == 0:
        return 0, ["目标句为空，无法评分。"]

    # 字符逐个比对
    matches = sum(1 for a, b in zip(user_text, target_text) if a == b)
    match_ratio = matches / len(target_text)
    score = round(match_ratio * 100)

    feedback = []
    if score > 90:
        feedback.append("発音はとても良いです！")
    elif score > 70:
        feedback.append("よくできましたが、いくつかの文字が不明瞭です。")
    else:
        feedback.append("文の構造や発音に誤りがあります。再度練習してみましょう。")

    return score, feedback
