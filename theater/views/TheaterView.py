from rest_framework.views import APIView
from rest_framework.response import Response
from theater.models import Theater, ShowTiming



class TheaterView(APIView):

    def get(self, request):
        city = request.query_params.get('city')
        movie_id = request.query_params.get('movie_id')
        
        theaters = Theater.objects.filter(cities__name=city).values(
        "id",
        "name",
        "cities__area"
        )
        response = {
            "theaters":[]
        }
        for theater in theaters:
            response['theaters'].append(
                {
                    "id": theater["id"],
                    "name": theater["name"],
                    "city": city,
                    "area": theater["cities__area"]
                }
            )
        if city and not movie_id:    
            return Response(data=response)
        
        elif city and movie_id:
            updated_response = {
                "theaters": []
            }

            for theater in response['theaters']:

                show_timing = ShowTiming.objects.filter(
                    movie_id=movie_id,
                    screen_theater__theater__id=theater['id']
                ).values(
                    "id",
                    "start_time"
                )
                theater["show_timings"] = [{'id':i['id'], 'start_time':str(i['start_time'])}for i in show_timing]
                updated_response["theaters"].append(theater)
            
            return Response(data=updated_response)
        return Response(data={})