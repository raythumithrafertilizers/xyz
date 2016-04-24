angular.module("App")
.controller("customer_dashboard", function ($scope, $q, $http,$timeout, $rootScope){
	
	$http({
        method: 'get',
        url: '/customer/dashboard',
        params: {
                    'user_id': localStorage.getItem('enduser_id')
                },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'}
          }).then(function (response) 
            {
              // console.log(response.data.user_details)
              // console.log("store details:", response.data.store_list)
              storeslist = response.data.store_list
              $scope.storesdata = [];
              $.each(storeslist, function(i){
                storedata =  JSON.parse(storeslist[i])
                // console.log("storedata:", storedata[0]);
                var obj = {};
                obj.storename = storedata[0].fields.storeName;
                obj.email =  storedata[0].fields.email;
                obj.phone = storedata[0].fields.phone;
                obj.storeid = storedata[0].pk;
                obj.currentstamp = storedata[0].currentstamp;
                obj.totalstamp = storedata[0].totalstamp;
                $scope.storesdata.push(obj);
              })
              
              $scope.user_details=response.data.user_details;
              console.log($scope.user_details);
          
            }, function errorCallback(response) 
            {
                
          });

    $scope.viewOffers = function(storeid){
      console.log(storeid);

      $http({
        method: 'GET',
        url: '/customer/viewoffers',
        params: {
          "storeid" : storeid,
        }
      }).then(function (response) 
        {
          var loyaltycard = JSON.parse(response.data.loyaltycard);
          console.log(loyaltycard[0]);
          $scope.loyalty_card_number =  loyaltycard[0].fields.loyality_card_no;
          $scope.max_stamp = loyaltycard[0].fields.max_stamp;
          var loyaltycard_offer_details = JSON.parse(response.data.loyaltyoffers);
            console.log(loyaltycard_offer_details);
            $scope.offerslist = [];
            $.each(loyaltycard_offer_details, function(i){
              var obj = {}
              obj.stampid = loyaltycard_offer_details[i].fields.stamp_offer_id;
              obj.stampcount =  loyaltycard_offer_details[i].fields.no_of_stamp;
              obj.desc = loyaltycard_offer_details[i].fields.stamp_description;
              $scope.offerslist.push(obj);
            })
            $("#myModal").modal("show");
            
        }, function errorCallback(response) 
        {
            $("#NoOffersModal").modal("show");
        });
    }
});