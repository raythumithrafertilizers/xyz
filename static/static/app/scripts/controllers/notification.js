angular.module("App")

.controller("notificationController", function($http, $scope, $timeout){
		$scope.load = $http({
		  method: 'GET',
		  url: '/superuser/addloyaltycard'
		}).then(function successCallback(response) {

		    $scope.storelist = [];
		    var storesdata = JSON.parse(response.data.storedata);
		    console.log(storesdata);
		   	$.each(storesdata, function(i){
		    	var obj ={};
		    	obj.storeid = String(storesdata[i].pk);
		    	obj.storename = storesdata[i].fields.storeName;	
		    	$scope.storelist.push(obj);
		    });
		    
		  }, function errorCallback(response) {
		    // called asynchronously if an error occurs
		    // or server returns response with an error status.
		    console.log(response);
		  });


		$scope.createNotification = function(){
			// 
			$scope.load = $http({
			  method: 'post',
			  url: '/superuser/create-notification',
			  data: {
                    "notification" :  $scope.notification,
                },
			  headers: {
			  	'Content-Type': 'application/x-www-form-urlencoded'}
					}).then(function (response) 
						{
				    		alert(response.data.res);

						}, function errorCallback(response) 
						{
				    		console.log(response);
						});
		}
})