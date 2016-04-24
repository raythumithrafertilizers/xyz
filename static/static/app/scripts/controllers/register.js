angular.module("App")

.controller("registerCtrl", function ($http, $scope, $q, toastr){
	
	$scope.UserRegistration = function(){

		$scope.load = $http({
			  method: 'post',
			  url: '/user/register',
			  data: {
                    'firstname': $scope.user.firstname,
                    "lastname": $scope.user.lastname,
                    "email" : $scope.user.email,
                    "phone" : $scope.user.phone,
                    "password" : $scope.user.password,
                },
			  headers: {
			  	'Content-Type': 'application/x-www-form-urlencoded'}
					}).then(function (response) 
						{
				    		toastr.success(response);
				    		$scope.master = {};
				    		$scope.formData = angular.copy($scope.master);

						}, function errorCallback(response) 
						{
				    		
				    		toastr.error("user already exists!");


						});
	}

})