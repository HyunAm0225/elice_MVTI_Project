from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Character
from .serializers import UserSerializer, CharacterSerializer, SentimentSerializer
from .sentimentAnalyzer import sentiment_analyzer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    lookup_field = "name"
    serializer_class = CharacterSerializer


class SentimentAnalyzeView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user_data = serializer.validated_data['words']

            matched = sentiment_analyzer.get_matched_villain(user_data)
            matched_villain = Character.objects.filter(
                name__exact=matched).get()

            mvti_type = sentiment_analyzer.get_mvti_type(user_data)
            user_sentiment_df = sentiment_analyzer.get_sentiment_df(user_data)
            user_sentiment = user_sentiment_df.to_dict()['emotions']

            # 각 타입 별 카운트 증가시키기
            sentiment_analyzer.add_count(matched)

            character_serializer = SentimentSerializer({
                'name': matched_villain.name,
                'user_mvti': mvti_type,
                'user_sentiment': user_sentiment,
                'wc_url': matched_villain.wc_url,
                'sentiment': matched_villain.sentiment,
                'bar_url': matched_villain.bar_url,
                'mvti_type': matched_villain.mvti_type,
                'rival': matched_villain.rival,
                'partner': matched_villain.partner,
                'count': matched_villain.count,
                'character_img_url': matched_villain.character_img_url,
                'best_talk': matched_villain.best_talk
            })

            return Response(character_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
