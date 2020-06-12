import re
import json
from collections import OrderedDict

except_chars = ['.', '*', '+', '#', '10:30', '?', '#quarantine', '-e', '11:30']
except_words = ['https', 'U000', '🤣', "U200E"]
texts = r'C:\Users\username\Downloads\data\file.txt'
encoding = 'UTF-8'
flag = ''  # surname


def get_word_count():
    msg_count, line, text = dict(), list(), ''
    with open(texts, 'r', encoding=encoding) as f:
        s = f.readlines()
    s.pop(0)
    msg_count.get('a')
    p = re.compile("{flag}: (.+)")
    msgs = [re.findall(p, c)[0] for c in s if re.findall(p, c) != []]
    for m in msgs:
        if any(a in m for a in except_words):
            continue
        line = '.'.join(m.split(' ')).split('.')
        for w in line:
            w = get_clean_word(w)
            if w is None:
                continue
            msg_count[w] = msg_count.get(w) + 1 if msg_count.get(w, None) else 1
    # sorted_dict = OrderedDict(sorted(msg_count.items(), key=lambda t: t[1], reverse=True))

    def write_json():
        with open('target/test1.json', 'w', encoding=encoding) as wf:
            # for k, v in sorted_dict.items():
            # wf.write(f'{k}: {v}\n')
            json.dump(msg_count, wf)
    # write_json()
    # return msg_count
    return ' '.join(msg_count.keys())


def get_clean_word(w):
    w = remove_emoji(w)
    w = str(w.lower().strip('‘').strip('¿'))
    w = w.replace("’", '').replace("?", '').replace("!", '')
    if w == '' or w == '\\n' or w in except_chars or len(w) == 1 or w.isnumeric():
        return
    return w


def remove_emoji(string):
    # https://stackoverflow.com/a/49146722/330558
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001F92A-\U0001F97A"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def visualize(text=None):
    import numpy as np
    import pandas as pd
    from PIL import Image
    from wordcloud import WordCloud, ImageColorGenerator
    import matplotlib.pyplot as plt

    def get_df():
        imp_words = ['ankush', 'yes', 'haan', 'love', 'sex', 'lund', 'lodu', 'butt', 'dick', 'tyagi', 'boo', 'pyaar',
                     'chutiya', 'bc', 'boob', 'kiss', 'shadi', 'break', 'pagal']
        not_imp_words = ['hai', 'mujhe', 'yaar', 'chahye', 'ha', 'thi', 'for', 'the', 'rhi', 'kya', 'toh', 'bhi', 'tha',
                         'par', 'aur', 'woh', 'and', 'tujhe', 'kyu', 'kuch', 'okay', 'mere', 'maine', 'raha', 'kar',
                         'fir', 'kia', 'sab', 'abhi', 'bola', 'hota', 'you', 'mein', 'baat', 'time', 'that', 'kaise',
                         'bol', 'hua', 'rahe', 'with', 'koi', 'this', 'liye', 'karne', 'krne', 'bht', 'rha', 'are',
                         'kyuki', 'meri', 'pata', 'tere', 'what', 'hoga', 'phle', 'will', 'but', 'theek', 'krna',
                         'pass', 'have', 'chaiye', 'aaj', 'was', 'know', 'mera', 'gya', 'khud', 'bta', 'aisa', 'apne',
                         'aaya', 'kahan', 'rhi', 'rahi', 'kaam', 'hoti', 'kisi', 'ghar', 'dia', 'kal', 'dekh', 'bas',
                         'thats', 'gyi', 'hogya', 'teri', 'its', 'how', 'when', 'skta', 'chali', 'chal', 'mtlb', 'just',
                         'usse', 'din', 'karle', 'krle', 'hui', 'waise', 'about', 'yehi', 'sath']
        i = 0
        with open('target/test.json', 'r', encoding=encoding) as jf:
            json_ob = json.load(jf)
        df = pd.DataFrame(columns=['Word', 'Count'])
        for k, v in json_ob.items():
            if (int(v) > 17 and len(k) > 2 and k not in not_imp_words) or k in imp_words:
                i += 1
                df.loc[i] = [k, v]
        return df

    def create_word_heatmap():
        wordcloud = WordCloud(max_font_size=70, max_words=3500, background_color="white").generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        wordcloud.to_file("img/word_count.png")

    def create_word_hist():
        df = get_df()
        plt.figure(figsize=(100, 100))
        df = df.sort_values('Count', ascending=False)
        plt.bar(df['Word'], df['Count'])
        plt.xticks(rotation=50)
        plt.xlabel("Word")
        plt.ylabel("Count")
        plt.show()

    def mask_image():
        df = get_df()
        mask = np.array(Image.open("img/pic.png"))
        fra = " ".join(word for word in df['Word'])
        wordcloud_fra = WordCloud(background_color="white", mode="RGBA", max_words=1000,
                                  mask=mask).generate(fra)
        # create coloring from image
        image_colors = ImageColorGenerator(mask)
        plt.figure(figsize=[7, 7])
        plt.imshow(wordcloud_fra.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        # store to file
        plt.savefig("img/text_img.png", format="png")
    create_word_heatmap()
    # mask_image()


if __name__ == '__main__':
    data = get_word_count()
    visualize(data)
