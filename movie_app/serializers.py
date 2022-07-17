from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(required=False, default='')
    director_id = serializers.IntegerField(allow_null=True, required=False, default=None)

    def validate_director_id(self, director_id):
        directors = Director.objects.filter(id=director_id)
        if directors.count() == 0:
            raise ValidationError(f'Director id not found for {director_id}')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    stars = serializers.IntegerField(min_value=1, max_value=5)
    text = serializers.CharField(required=False, default='')
    movie_id = serializers.IntegerField(allow_null=True, required=False, default=None)


    def validate_movie_id(self, movie_id):
        movies = Review.objects.filter(id=movie_id)
        if movies.count() == 0:
            raise ValidationError(f'Movie not found for id {movie_id}')
        return movie_id



