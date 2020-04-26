var app = angular.module('myApp', []);
/*
* Contoller gets list of all movies from API and performs custom filtering by weekday and movie name
* */
app.controller('moviesCtrl', function ($scope, $http) {
    $http.get("http://localhost:8000/api/movies/")
        .then(function (response) {
            $scope.movies = response.data;
        });

    $scope.customFilter = {};

    $scope.$watch('selectedWeekday', function (value) {
        $scope.customFilter.showTimes = (value === null || value === undefined) ? null : {day: value};
        if (!$scope.customFilter.showTimes) { // when any is selected as the filter
            delete $scope.customFilter.showTimes;
        }
    });

    $scope.$watch('movieNameFilter', function (value) {
        $scope.customFilter.name = (value === null || value === undefined) ?
            '' : value;
    });
});

