# imports
from rest_framework.views import (
    APIView,
    Response,
    status,
)
from news.serializers import (
    NewsSerializer,
    AuthorSerializer,
)
from news.models import(
    Attachment,
    Author,
    News,
    Tag,
)
import requests
import json

# ApiView
class NewsAPIView(APIView):

    # when request method is get
    def get(self,request):

        # try to get data from api and handle possible errors
        try:
            req = requests.get('https://feeds.npr.org/1004/feed.json')
        except requests.exceptions.ConnectionError:
            return Response({"Connection Error":"Please check your connection"},status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            return Response({'Unexpected Error':'Somethig went wrong'},status.HTTP_503_SERVICE_UNAVAILABLE)

        # extracting data
        req_json = json.loads(req.content)
        data = req_json['items']

        # saving all news to select 5-LATEST ones (it's better to save as much information as possible) and decide on
        # them later:
        for item in data:

            # id is an Integer in news models
            item['id'] = int(item['id'])

            # get author if exists, else create it
            try:
                author, _ = Author.objects.get_or_create(**item['author'])
                item['author'] = author
            except Exception as e:
                pass

            # detach and save attachment from news model data to use later
            attachments = None
            try:
                attachments = item['attachments']
                del item['attachments']
            except Exception as e:
                pass

            # detach and save tag from news model data to use later
            try:
                tags = item['tags']
                del item['tags']
            except Exception as e:
                pass

            # create a news item and save it to DB
            news = News(**item)
            news.save()

            # if news has attachments, create them with this current news instance
            if attachments:
                for attachment in attachments:
                    a , _ = Attachment.objects.get_or_create(news=news,**attachment)

            # if news has tags, create them with this current news instance
            if tags:
                for tag in tags:
                    t = Tag(tag=tag)
                    t , _ = Tag.objects.get_or_create(tag=tag,news=news)

        # after all news are saved filter 5 latest of them, then serialize it and send response with 200 code
        news = News.objects.all().order_by('-date_published')
        serialized = NewsSerializer(news,many=True).data[0:5]
        return Response(serialized,status.HTTP_200_OK)
