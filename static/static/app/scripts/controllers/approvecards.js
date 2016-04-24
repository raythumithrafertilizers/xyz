angular.module("App")

.controller("approvalController", function ($scope, $http, $q, $timeout, $route){
	$scope.load = $scope.load =  $http({
		 method: 'GET',
		 url: '/superuser/approve-card'
		}).then(function successResponse(response){
			var cards = response.data.response;
			$scope.details = [];
			$.each(cards, function(i){
				var obj = {}
				var card_details = JSON.parse(cards[i].card);
				obj.storename =  cards[i].storename
				obj.cardno = card_details[0].fields.loyality_card_no;
				obj.cid = card_details[0].pk;
				$scope.details.push(obj);
			})
		},function errorResponse(response){
			alert("something went wrong");
		})

	$scope.viewCardOffers =  function(offerid){
		// $location.path("/view-card-offer")

		$scope.load =  $http({
		 method: 'GET',
		 url: '/superuser/get-card-details',
		 params:{
		 	"cardid" : offerid,
		 }
		}).then(function successResponse(response){
			card_data = JSON.parse(response.data.carddetails)
			stamps_data = JSON.parse(response.data.stampoffers)
			console.log("card details",JSON.parse(response.data.carddetails));
			$scope.loyalty_card_number = card_data[0].fields.loyality_card_no;
			$scope.max_stamp = card_data[0].fields.max_stamp;
			$scope.is_active = card_data[0].fields.is_active;
			$scope.cardid = card_data[0].pk;
			$scope.stampslist = [];
			$.each(stamps_data, function(i){
				var obj = {};
				obj.stampcount = stamps_data[i].fields.no_of_stamp;
				obj.desc = stamps_data[i].fields.stamp_description;
				$scope.stampslist.push(obj);
			})

			$("#myModal").modal("show");
		},function errorResponse(response){
			alert("something went wrong");
		})
	}


	$scope.Approve =  function(offerid, boolval){
		console.log(boolval);
		// $scope.load =  $http({
		//  method: 'GET',
		//  url: '/superuser/activate-card',
		//  params:{
		//  	"cardid" : offerid,
		//  }
		// }).then(function successResponse(response){
		// 	alert("activated successfully");
		// },function errorResponse(response){
		// 	alert("something went wrong");
		// })

		$scope.load = $http({
			  method: 'post',
			  url: '/superuser/approve-card',
			  data: {				                    
	                "cardid" : offerid,
	                "is_approve" : boolval,
	            },
			  headers: {
			  	'Content-Type': 'application/x-www-form-urlencoded'}
					}).then(function successCallback(response) 
						{
				    		alert(response.data.response);

				
						}, function errorCallback(response) 
						{						    		
				    		// console.log("not sent");
						});
	}

})