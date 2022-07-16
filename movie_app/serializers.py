from rest_framework import serializers
from .models import Director, Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description reviews'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.all().count()


class DirectorDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration reviews director'.split()


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    # reviews_list = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title rating reviews_list'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
