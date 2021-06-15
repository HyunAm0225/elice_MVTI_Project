import numpy as np
from .utils import format_data, calculate_cos_sim
from .models import Character


class SentimentAnalyzer():
    def get_sentiment_df(self, dataset):
        df = format_data(dataset)
        return df

    def get_mvti_type(self, dataset):
        df = self.get_sentiment_df(dataset)

        P = float(df.loc['positive'].values)
        N = float(df.loc['negative'].values)
        J = float(df.loc['joy'].values)
        S = float(df.loc['sadness'].values)
        Ag = float(df.loc['anger'].values)
        T = float(df.loc['trust'].values)
        At = float(df.loc['anticipation'].values)
        F = float(df.loc['fear'].values)

        first_type = "P" if max(P, N) == P else "N"
        second_type = "J" if max(J, S) == J else "S"
        third_type = "T" if max(T, Ag) == T else "A"
        fourth_type = "A" if max(At, F) == At else "F"

        return f'{first_type}{second_type}{third_type}{fourth_type}'

    def get_cos_sim_rate(self, user_data, villain_data):
        user_df = self.get_sentiment_df(user_data)
        user = np.squeeze(user_df.to_numpy())
        villain = np.array(list(villain_data.values()))

        cos_sim_rate = calculate_cos_sim(user, villain)
        return round(cos_sim_rate, 2)

    def get_matched_villain(self, dataset):
        villains = Character.objects.all()
        cos_sim_rate_dict = {}

        for vil in villains:
            cos_sim_rate = self.get_cos_sim_rate(dataset, vil.sentiment)
            cos_sim_rate_dict[vil.name] = cos_sim_rate

        sorted_dict = sorted(cos_sim_rate_dict.items(), key=lambda x: x[1])
        print(sorted_dict)
        return sorted_dict[-1][0]

    def add_count(self, name):
        villain = Character.objects.filter(name__exact=name).get()
        villain.add_count()
        villain.save()


sentiment_analyzer = SentimentAnalyzer()
