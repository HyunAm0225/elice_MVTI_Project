def test_sum_emotion():
    data = [[('positive', 1.0), ('fear', 0.1)], 
            [('fear', 0.16666666666666666), ('anger', 0.16666666666666666)]]
    emotion_dict = {}

    for top_emo in data:
        for emo in top_emo:
            emotion = emotion_dict.get(emo[0])
            if not emotion:
                emotion_dict[emo[0]] = emo[1]
            else:
                emotion_dict[emo[0]] += emo[1]

    assert emotion_dict == {'fear': 0.26666666666666666, 'positive': 1.0, 'anger': 0.16666666666666666}
