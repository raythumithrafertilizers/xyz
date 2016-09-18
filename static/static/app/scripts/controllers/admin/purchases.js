angular.module("App")
.controller("purchaseDetailsCtrl", function ($scope, $http, $q,$location,$timeout,$routeParams, $route, toastr){


         $scope.load =
         $http({
              method: 'get',
              url: '/superuser/stock-names',
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            $scope.stock_names =  response.data.stock_names
            $timeout(function(){
                $("#example1").DataTable();
            },500)

         }, function(error){
            console.log('hellow')
         })

         $timeout(function(){
            $('#datepicker_sale_products_reports_1') .datepicker({
                format: 'dd/mm/yyyy',
                //startDate: new Date()
                //endDate: '01/12/2020'
            })
        },500)

        $scope.user = {}
        $scope.user['common_advance'] = 0

        $scope.quantity_changed = function(){
            $scope.user.harvester_total_payment = $scope.user.quantity * $scope.user.harvester_rate_per_ton
            $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton
        }


        $scope.calculate_final_total_mis_detections = function(){
            console.log('called miscleanous caluclation')
            if($scope.user.quantity &&  $scope.user.farmer_rate_per_ton){
                if($scope.user.miscellaneous_detections){
                    $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton
                    $scope.user.farmer_total_payment -= $scope.user.miscellaneous_detections;
                }else{
                    $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton

                }

            }
        }



    $scope.load = $http({
                        method: 'post',
                        url: '/superuser/get-specific-purchase-details',
                        data: {'purchase_id': $routeParams.purchase_id},
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'}
                    }).then(function successCallback(response){
                                console.log(response)
                                $scope.user = {}
                                var basic_info = response.data.response;
                                var data = response.data.users
                                console.log(basic_info)
                                if (basic_info['farmer_id'] == basic_info['harvester_id']){
                                    $scope.user.same_farmer_harvester = true;
                                }else{
                                    $scope.user.same_farmer_harvester = false
                                }

                                $scope.user['quantity'] = basic_info['quantity']
                                $scope.user['quality'] = basic_info['quality']

                                var pda= basic_info['purchased_date'].split("-")
                                var converted_date = pda[2]+"/"+pda[1]+"/"+pda[0]
                                $scope.user['purchase_date'] = converted_date
                                $scope.user['remarks'] = basic_info['remarks']

                                $scope.user['purchase_id'] = $routeParams.purchase_id

                                $scope.user['harvester_total_payment'] = basic_info['harvester_amount']
                                $scope.user['harvester_advance'] = basic_info['harvester_advance']
                                $scope.user['harvester_rate_per_ton'] = basic_info['harvester_rate_per_ton']

                                $scope.user['farmer_rate_per_ton'] = basic_info['farmer_rate_per_ton']
                                $scope.user['farmer_total_payment'] = basic_info['farmer_amount']
                                $scope.user['farmer_advance'] = basic_info['farmer_advance']
                                $scope.user['miscellaneous_detections'] = basic_info['miscellaneous_detections']
                                $scope.user['need_to_append'] = true
                                $scope.user['stock_name'] = basic_info['stock_id']
                                $scope.user['temp_stock_name'] = basic_info['stock_name']



                                $scope.input_temp_array = []
                                for(var i in data){
                                    var obj = {}
                                    obj.name = data[i].name
                                    obj.type = data[i].type
                                    obj.userid = data[i].userid
                                    obj.ticked = data[i].ticked

                                    $scope.input_temp_array.push(obj)
                                }





                    }, function errorCallback(response)
                    {
                        toastr.error('unable to  updated')
                        // console.log("not sent");
                    });


    $scope.update_purchase_details = function(){
        var farmer_count = 0
        var harvester_count = 0;

        $scope.farmer_id = ''
        $scope.harvester_id = ''

        for (temp in $scope.output_temp_array){
            if($scope.output_temp_array[temp]['type'] == 'farmer'){
                farmer_count += 1

                $scope.farmer_id = $scope.output_temp_array[temp]['userid']
            }else{
                harvester_count += 1
                $scope.harvester_id = $scope.output_temp_array[temp]['userid']
            }
        }

        if(harvester_count == 1 && farmer_count == 1){
                if($scope.user.same_farmer_harvester){
                    toastr.error('please uncheck harvester and farmer same option')
                    return;
                }else{
                    $scope.user['harvester_id'] = $scope.harvester_id
                    $scope.user['farmer_id'] = $scope.farmer_id
                }
            }

            if(harvester_count == 0){

                if(farmer_count == 1){
                    if($scope.user.same_farmer_harvester){
                        $scope.user['harvester_id'] = $scope.farmer_id
                        $scope.user['farmer_id'] = $scope.farmer_id
                    }else{
                        toastr.error("you must select single farmer harvester option")
                        return;
                    }

                }else{
                    toastr.error('you must select atleast single farmer or harvester ..')
                    return;
                }

            }

            if(farmer_count == 0){
                if(harvester_count == 1){
                    if($scope.user.same_farmer_harvester){
                        $scope.user['farmer_id'] = $scope.harvester_id
                        $scope.user['harvester_id'] = $scope.harvester_id
                    }else{
                        toastr.error("you must select single farmer harvester option")
                        return;
                    }

                }else{
                    toastr.error('you must select atleast single farmer or harveste.')
                    return;
                }

            }

             if(harvester_count != 1 && farmer_count != 1){
                toastr.error('you must select atleast single farmer or harvester')
                return;
            }


            console.log('final data is', $scope.user)

        console.log('final data is', $scope.user, $scope.harvester_id, $scope.farmer_id)

         $scope.load = $http({
                        method: 'post',
                        url: '/superuser/update-specific-purchase-details',
                        data: $scope.user,
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'}
                    }).then(function successCallback(response){
                                toastr.success("successfully updated")
                                $location.path("/edit-purchases")

                    }, function(error){

                        toastr.error("failed to update")
                    })


    }


})
.controller("purchasesDetailsCtrl", function ($scope, $http, $q,$location,$timeout, $route, toastr){
    $scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/add-purchase-details',
			}).then(function (response)
				{
                    console.log(response)
		    		$scope.userslist = [];
		    		var usersdata = response.data.response;

		    		$.each(usersdata, function(i){
                        var obj = {};

                        obj.purchaseId = usersdata[i].purchaseId;
                        obj.farmer_name = usersdata[i].farmer_name;

                        obj.harvester_name =  usersdata[i].harvester_name;
                        obj.quantity = usersdata[i].quantity;
                        obj.quality = usersdata[i].quality;
                        obj.farmer_amount = usersdata[i].farmer_amount
                        obj.harvester_amount = usersdata[i].harvester_amount
                        obj.date = usersdata[i].date
                        $scope.userslist.push(obj);
                        $timeout(function(){
                         $("#example1").DataTable();
                        },500)
                    })

                    console.log($scope.userslist)
				}, function errorCallback(response)
				{
		    		console.log(response);
				});


    $scope.deleteUser = function(){


        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/delete-purchase-details',
                                data: {'purchase_id': $scope.delete_purchase.purchaseId},
                                headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                            }).then(function successCallback(response){
                                        toastr.success('successfully deleted')
                                        $("#myModal3").modal("hide");
                                        $timeout(function(){
                                          $route.reload()

                                        },2000)
                            }, function errorCallback(response)
                            {
                                toastr.error('unable to  updated')
                                // console.log("not sent");
                            });



     }


	$scope.viewUserData = function(purchase, modal){
		// $("#myModal").modal("show");
		$("#myModal"+modal).modal("show");
		$scope.delete_purchase = purchase;
	}

})



.controller("createPurchaseCtrl", function ($scope, $http, $q,$location,$timeout, $route, toastr){

        $scope.user = {}
        $scope.user.name = ''
        $scope.user.phone = ''
        $scope.user.address = ''

        $scope.load =
         $http({
              method: 'get',
              url: '/superuser/stock-names',
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            $scope.stock_names =  response.data.stock_names
            $timeout(function(){
                $("#example1").DataTable();
            },500)

         }, function(error){
            console.log('hellow')
         })


        $scope.user.same_farmer_harvester = false
        $scope.user.need_to_append = true;

        $scope.calculate_final_total_mis_detections = function(){
            console.log('called miscleanous caluclation')
            if($scope.user.quantity &&  $scope.user.farmer_rate_per_ton){
                if($scope.user.miscellaneous_detections){
                    $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton
                    $scope.user.farmer_total_payment -= $scope.user.miscellaneous_detections;
                }else{
                    $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton
                }

            }
        }


        $scope.quantity_changed = function(){
            $scope.user.harvester_total_payment = $scope.user.quantity * $scope.user.harvester_rate_per_ton
            $scope.user.farmer_total_payment = $scope.user.quantity * $scope.user.farmer_rate_per_ton
        }

         $scope.quantity_changed2 = function(){
            $scope.user.harvester_total_payment = $scope.user.quantity * $scope.user.harvester_rate_per_ton
        }

         $timeout(function(){
            $('#datepicker_sale_products_reports_1') .datepicker({
                format: 'dd/mm/yyyy',
                //startDate: new Date()
                //endDate: '01/12/2020'
            })
        },500)

        $scope.processed = function(){
            console.log('final data is', $scope.purchase_date)
            var farmer_count = 0
            var harvester_count = 0;


            $scope.farmer_id = ''
            $scope.harvester_id = ''

            for (temp in $scope.output_temp_array){
                if($scope.output_temp_array[temp]['type'] == 'farmer'){
                    farmer_count += 1

                    $scope.farmer_id = $scope.output_temp_array[temp]['userid']
                }else{
                    harvester_count += 1
                    $scope.harvester_id = $scope.output_temp_array[temp]['userid']
                }
            }

            console.log(harvester_count, farmer_count)



            if(harvester_count == 1 && farmer_count == 1){
                if($scope.user.same_farmer_harvester){
                    toastr.error('please uncheck harvester and farmer same option')
                    return;
                }else{
                    $scope.user['harvester_id'] = $scope.harvester_id
                    $scope.user['farmer_id'] = $scope.farmer_id
                }
            }

            if(harvester_count == 0){

                if(farmer_count == 1){
                    if($scope.user.same_farmer_harvester){
                        $scope.user['harvester_id'] = $scope.farmer_id
                        $scope.user['farmer_id'] = $scope.farmer_id
                    }else{
                        toastr.error("you must select single farmer harvester option")
                        return;
                    }

                }else{
                    toastr.error('you must select atleast single farmer or harvester ..')
                    return;
                }

            }

            if(farmer_count == 0){
                if(harvester_count == 1){
                    if($scope.user.same_farmer_harvester){
                        $scope.user['farmer_id'] = $scope.harvester_id
                        $scope.user['harvester_id'] = $scope.harvester_id
                    }else{
                        toastr.error("you must select single farmer harvester option")
                        return;
                    }

                }else{
                    toastr.error('you must select atleast single farmer or harveste.')
                    return;
                }

            }

             if(harvester_count != 1 && farmer_count != 1){
                toastr.error('you must select atleast single farmer or harvester')
                return;
            }

            if(harvester_count == 1 && farmer_count == 0){
                toastr.error('you can not select single harvester')
                return;
            }







            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-purchase-details',
                                  data: $scope.user,
                                  headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                           }).then(function (response){
                                toastr.success("Successfully Created ...");
                                $scope.master = {};
                                $scope.formData = angular.copy($scope.master);
                                $location.path("/edit-purchases")
                            }, function errorCallback(response){
                                toastr.error("Former is already exists!");
                            });


        }

        $scope.addNewFarmer = function(){
            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-harvester',
                                  data: {
                                        'name': $scope.user.name,
                                        "address" : $scope.user.address,
                                        "phone" : $scope.user.phone,
                                    },
                                  headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                           }).then(function (response){
                                toastr.success("Successfully Created ...");
                                $scope.master = {};
                                $scope.formData = angular.copy($scope.master);
                                //$location.path("/view-modify-customers")
                            }, function errorCallback(response){
                                toastr.error("something went wrong...");
                            });
	    }


	    // loading farmers and harvesters to select

 $scope.load = $http({
                      method: 'post',
                      url: '/superuser/get-farmers-harvesters',
                      headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'}
               }).then(function (response)
                {


                    var data = JSON.parse(response.data.users)
                    console.log(data)
                    $scope.input_temp_array = []
                    for(var i in data){
                        var obj = {}
                        obj.name = data[i].name
                        obj.type = data[i].type
                        obj.userid = data[i].userid

                        $scope.input_temp_array.push(obj)
                    }


                }, function errorCallback(response)
                {
                    toastr.error("user already exists!");
                });




})