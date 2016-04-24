angular.module("App")


.controller("GalleryCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){
// gallery start here

function process_gallery_image_path(path){
    var image_path = path.split('/')
    console.log('path is ', image_path[image_path.length-1])
    return 'static/upload_gallary_images/'+image_path[image_path.length-1]

}

$scope.load =
$http({
    method: 'GET',
      url: '/superuser/gallery-image',
    }).then(function (response){
            console.log('response iamges', response)
            $scope.images = [];
            var imagesList = JSON.parse(response.data.gallery_images);

            $.each(imagesList, function(i){
                var obj = {};
                obj.thumb = process_gallery_image_path(imagesList[i].fields.gallery_image);
                obj.img = obj.thumb
                $scope.images.push(obj);
            })

    }, function errorCallback(response){
            console.log(response);
    });

})