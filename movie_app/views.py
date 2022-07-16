from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer, \
    MovieWithReviewsSerializer
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    else:
        name = request.data.get('name', '')
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
        director.name = request.data.get('name', '')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data)


@api_view(['GET', 'POST'])
def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    else:
        title = request.data.get('title', '')
        description = request.data.get('description', '')
        director_id = request.data.get('director_id', '')
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
        movies.title = request.data.get('title', '')
        movies.description = request.data.get('description', '')
        movies.director_id = request.data.get('director_id', '')
        movies.reviews.set = request.data.get('reviews', [])
        movies.save
        return Response(data=MovieDetailSerializer(movies).data)


@api_view(['GET', 'POST'])
def reviews_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    else:
        stars = request.data.get('stars', '')
        text = request.data.get('text', '')
        movie_id = request.data.get('movie_id', '')
        review = Review.objects.create(
            stars=stars,
            text=text,
            movie_id=movie_id
        )
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
        reviews.star = request.data.get('star', '')
        reviews.text = request.data.get('text', '')
        reviews.movie_id = request.data.get('movie_id', '')
        reviews.save()
        return Response(data=ReviewDetailSerializer(reviews).data)

