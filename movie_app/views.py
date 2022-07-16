from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer, \
    MovieWithReviewsSerializer
from .models import Director, Review, Movie
from rest_framework import status


@api_view(['GET'])
def directors_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def directors_detail_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found'})
    data = DirectorDetailSerializer(directors, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_reviews(request):
    movies = Movie.objects.all()
    data = MovieWithReviewsSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    data = MovieDetailSerializer(movies, many=False).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    data = ReviewDetailSerializer(reviews, many=False).data
    return Response(data=data)

