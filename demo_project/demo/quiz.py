import random
import wikipedia
import os


def prefecture_quiz():
    pref_city_dict = {}
    pref_url_dict = {}

# 'r'とは読み込み専用のモード
    with open(os.path.dirname(os.path.abspath(__file__)) + '/static/demo/pref_office_loc.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # rstrip()は文字列の末尾にある改行コードを削除する
            txt_lines = line.rstrip().split(',')
            pref = txt_lines[0]
            city = txt_lines[1]
            url = txt_lines[2]

            if pref not in pref_city_dict:
                pref_city_dict[pref] = city
            if pref not in pref_url_dict:
                pref_url_dict[pref] = url

    pref_name = []
    for i in pref_city_dict.keys():
        pref_name.append(i)

    # 県をランダムに選択
    random_pref = random.choice(pref_name)

    # 選択した県の県庁所在地と公式サイトのURLを取得
    city_name = pref_city_dict[random_pref]
    pref_url = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url


def quiz():
    qa = []

    with open(os.path.abspath(__file__) + '/static/demo/quiz.txt', 'r', encoding='utf-8') as f:
        for line in f:
            txt_lines = line.rstrip().split(',')
            q = txt_lines[0]
            a = txt_lines[1]
            qa.append([q, a])

    selected_qa = random.sample(qa, 5)

    return selected_qa

# candidate_list = wikipedia.search(word)は，wordを検索して候補のリストを取得する
# wikipedia.page(candidate_list[0])は，候補の中から最初のページを取得する


def wikipy(word):
    wikipedia.set_lang('ja')
    candidate_list = wikipedia.search(word)
    if not candidate_list:
        result = '該当するページがありませんでした。'
    else:
        search_page = wikipedia.page(candidate_list[0])
        # search_page.summaryは，ページの要約を取得する
        result = search_page.summary

    return result
