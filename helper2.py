from collections import Counter
import pandas as pd
import emoji


def fetch_stats(selected_review, df):
    if selected_review != 'Overall':
        df = df[df['Stars'] == selected_review]
    num_review = df.shape[0]
    words = []
    for Review in df['Review']:
        words.extend(Review.split())
    return num_review, len(words)


def most_common_words(selected_review, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_review != 'Overall':
        df = df[df['Stars'] == selected_review]
        words = []
        for Review in df['Review']:
            for word in Review.lower().split():
                if word not in stop_words:
                    words.append(word)
        most_common_df = pd.DataFrame(Counter(words).most_common(20))
        return most_common_df


def emoji_helper(selected_review, df):
    if selected_review != 'Overall':
        df = df[df['Stars'] == selected_review]
    emojis = []
    for message in df['Review']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df
