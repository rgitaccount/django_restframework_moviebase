from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer, \
    MovieWithReviewsSerializer, DirectorValidateSerializer, MovieValidateSerializer, \
    ReviewValidateSerializer
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data['name']
        director = Director.objects.create(
            name=name
        )
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Director added',
                              'director': DirectorDetailSerializer(director).data})


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    if request.method == 'GET':
        data = DirectorDetailSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'message': 'Director entry deleted'})
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        director.name = serializer.validated_data['name']
        director.save()
        return Response(data=DirectorDetailSerializer(director).data)


@api_view(['GET', 'POST'])
def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        director_id = serializer.validated_data['director_id']
        movie = Movie.objects.create(
            title=title,
            description=description,
            director_id=director_id
        )
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Movie created',
                              'movie': MovieDetailSerializer(movie).data})


@api_view(['GET'])
def movies_list_reviews(request):
    movies = Movie.objects.all()
    data = MovieWithReviewsSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    if request.method == 'GET':
        data = MovieDetailSerializer(movies, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(data={'message': 'Movie removed'})
    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        movies.title = serializer.validated_data['title']
        movies.description = serializer.validated_data['description']
        movies.director_id = serializer.validated_data['director_id']
        movies.save()
        return Response(data=MovieDetailSerializer(movies).data)


@api_view(['GET', 'POST'])
def reviews_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        stars = serializer.validated_data['stars']
        text = serializer.validated_data['text']
        movie_id = serializer.validated_data['movie_id']
        review = Review.objects.create(
            stars=stars,
            text=text,
            movie_id=movie_id
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Review created',
                              'reviews': ReviewDetailSerializer(review).data})


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    if request.method == 'GET':
        data = ReviewDetailSerializer(reviews, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(data={'message': 'Review deleted'})
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        reviews.stars = serializer.validated_data['stars']
        reviews.text = serializer.validated_data['text']
        reviews.movie_id = serializer.validated_data['movie_id']
        reviews.save()
        return Response(data=ReviewDetailSerializer(reviews).data)

