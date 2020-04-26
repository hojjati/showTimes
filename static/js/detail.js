var app = angular.module('myApp1', []);

/*
* Enabling html5 to be able to use $location
* */
app.config(['$locationProvider', function ($locationProvider) {
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    })
}]);

/*
* Controller gets the details of a movie with id provided by $location
* from API and puts it into movie variable
* */
app.controller('detailsCtrl', function ($scope, $http, $location) {
    const id = $location.search()["id"];
    url = "http://localhost:8000/api/movies/" + id;
    $http.get(url)
        .then(function (response) {
            $scope.movie = response.data;
        });
    $scope.backToList = function () {
        window.location = "/static/list.html";
    }
});
