angular.module("App")
.controller("farmerInterests", function($http, $q,$location, $timeout,toastr,$route,$routeParams, $scope){

    var farmer_id = false

    $scope.calculate_remain_balance = function(){
        $scope.remaining_money = $scope.final_total_advance - $scope.farmer_paid_advance
        console.log($scope.remaining_money)
    }

    $scope.common_closing_date_func = function(){

        for(var i in $scope.advances_list){
            $scope.advances_list[i].closing_date = $scope.common_closing_date
        }
        $scope.calculate_days();
    }

    $scope.calculate_days = function(){

        $scope.farmer_paid_advance = 0
        $scope.total_interest_money = 0
        $scope.total_advance = 0
        $scope.final_total_advance = 0

        for(var temp in $scope.advances_list){
            var item = $scope.advances_list[temp]
            console.log(item)
            var closing_date_array= item.closing_date.split("/")
            if(new Date(closing_date_array[1]+"/"+closing_date_array[0]+"/"+closing_date_array[2]).toString() != "Invalid Date"){
                    var date1 = new Date(closing_date_array[1]+"/"+ closing_date_array[0]+"/"+closing_date_array[2]);
                    var date2 = new Date(item.paid_date);
                    var timeDiff = Math.abs(date2.getTime() - date1.getTime());
                    var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
                    $scope.months = diffDays/30;
                    item.interest_money = $scope.months * $scope.interest_rate * (item.amount/100)
                    $scope.advances_list[temp] = item

                    $scope.total_advance += item.amount
                    $scope.total_interest_money += item.interest_money
                    $scope.final_total_advance += item.interest_money + item.amount


            }

        }
    }

    $scope.get_totals = function(){
        $scope.total_interest_money = 0
        $scope.total_sum_money = 0
        $scope.total_advance_money = 0
        for(var temp in $scope.advances_list){
            $scope.total_interest_money += $scope.advances_list[temp]['interest_money']
            $scope.total_sum_money += $scope.advances_list[temp]['sum_amount']
            $scope.total_advance_money += $scope.advances_list[temp]['amount']
        }
    }

    $scope.load = $http({
        method: 'GET',
        url: '/superuser/persons-list/farmer',
    }).then(function (response)
        {
            console.log(response)
            $scope.userslist = [];
            var usersdata = response.data.userdata

            $.each(usersdata, function(i){
                var obj = {};
                obj.user_id = usersdata[i].user_id;
                obj.username = usersdata[i].name;
                $scope.userslist.push(obj);
            })

            console.log($scope.userslist)
        }, function errorCallback(response)
        {
            console.log(response);
        });

    $scope.selected_farmer = function(){

        if($scope.selected_farmer_object){
            farmer_id = $scope.selected_farmer_object.user_id
        }

        if(farmer_id){
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/get-interests',
              data: {
                    'farmer_id': farmer_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.advances_list = response.data.advances_list
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)
                    $scope.get_totals()

            }, function errorCallback(response){
                    console.log(response);
            });
        }else{
            toastr.error('please select atleast one farmer')
        }


    }

    /*$scope.entered_interest = function(item){
        interested_money = (item['interest_rate']/100)*item['sum_amount']
        console.log(interested_money)
        for(temp in $scope.advances_list){
            if($scope.advances_list[temp]['id'] == item['id']){
                $scope.advances_list[temp]['interest_money'] = interested_money
                $scope.get_totals()
                return;
            }
        }

    }*/
    $scope.save_interest = function(){
        $scope.load =
         $http({
              method: 'post',
              url: '/superuser/save_interest',
              data: {
                    'data':$scope.advances_list,
                    'total_advance': $scope.total_advance,
                    'total_interest_money': $scope.total_interest_money,
                    'final_total_advance': $scope.final_total_advance,
                    'farmer_paid_advance': $scope.farmer_paid_advance,
                    'farmer_paid_date': $scope.farmer_paid_date,
                    'remaining_money': $scope.remaining_money,
                    'interest_rate': $scope.interest_rate,
                    'remarks': $scope.remarks,
                    'farmer_id': farmer_id
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log('save interest response', response)
            toastr.success('saved ...')

         }, function(error){
            console.log('while saving interest got error')
         })
         $scope.get_totals();
    }
    /*$scope.save_interest = function(item){
        $scope.load =
         $http({
              method: 'post',
              url: '/superuser/save_interest',
              data: {
                   'item':item
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log('save interest response', response)
            toastr.success('saved ...')

         }, function(error){
            console.log('while saving interest got error')
         })
         $scope.get_totals();
    }*/



})
.controller("specificFarmerPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route,$routeParams, $scope){
    console.log('specificCustomerPaymentsCtrl')

    $scope.farmer_show_name = $routeParams.farmer_name
    $scope.amount = {}
    $scope.amount.details = ""
    $scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-specific-person-payments',
              data: {
                    'person_id': $routeParams.person_id,
                    'get_data': true,
                    'person_type': 'farmer'
                    },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            $scope.payments =  response.data.response
            for(var i in $scope.payments){

                 var pda= $scope.payments[i].fields.paid_date.split("-")
                 $scope.payments[i].fields.paid_date_format = $scope.payments[i].fields.paid_date;
                 var converted_date = pda[2]+"/"+pda[1]+"/"+pda[0]
                 $scope.payments[i].fields.paid_date = converted_date;


            }
            $timeout(function(){
            $('#datepicker_sale_products_reports_1') .datepicker({
                format: 'dd/mm/yyyy',
                //startDate: new Date()
                //endDate: '01/12/2020'
            })
        },500)
            $timeout(function(){
                $("#example1").DataTable();
            },500)

         }, function(error){
            console.log('hellow')
         })

    $scope.showPopUp = function(amount){

        $scope.amount.details = amount
        $("#amountEditPopUp").modal("show");
    }

    $scope.updatePayment = function(){

        //var pda= $scope.amount.details.fields.paid_date.split("-")
        //var converted_date = pda[2]+"/"+pda[1]+"/"+pda[0]

        $scope.load = $http({
            method: 'post',
            url: '/superuser/get-specific-person-payments',
            data: {
                    'get_data': false,
                    'id': $scope.amount.details.pk,
                    'amount':$scope.amount.details.fields.amount,
                    'paid_date': $scope.amount.details.fields.paid_date,
                    'remarks': $scope.amount.details.fields.remarks
                  },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function successCallback(response){
                    toastr.success('successfully saved')
                    $("#amountEditPopUp").modal("hide");
                    $timeout(function(){
                            $("#example1").DataTable();
                    },5000)

        }, function errorCallback(response)
        {
            toastr.success('unable to  save....')
            // console.log("not sent");
        });
    }

    $scope.editPayment = function(customer){
        $location.path("/customer-payments/"+customer.customer_id)
    }
})
.controller("farmerPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route, $scope){
    console.log('farmer Payments Ctrl')
    $scope.amount = {}
    $scope.amount.enter_amount = 0
    $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $scope.load =
         $http({
              method: 'GET',
              url: '/superuser/persons-list/farmer',

              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log('farmers  information', response)
            $timeout(function(){
                $("#example1").DataTable();
            },500)
            $scope.customer_pay_info = response.data.userdata
            console.log($scope.customer_pay_info)
         }, function(error){
            console.log('hellow')
         })

    $scope.showPopUp = function(customer){
        $scope.amount.enter_amount = 0
        $scope.current_customer = customer
        $("#amountEditPopUp").modal("show");
    }

    $scope.addPayment = function(){
        console.log($scope.amount.details.fields.paid_date)
        $scope.load = $http({
            method: 'post',
            url: '/superuser/add-person-amount',
            data: {
                    'person_id': $scope.current_customer.user_id,
                    'paid_amount':$scope.amount.enter_amount,
                    'paid_date':$scope.amount.details.fields.paid_date,
                    'remarks':$scope.amount.details.fields.remarks
                  },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function successCallback(response){
                    toastr.success('successfully saved')
                    $("#amountEditPopUp").modal("hide");

        }, function errorCallback(response)
        {
            toastr.success('unable to  save....')
            // console.log("not sent");
        });
    }

    $scope.editPayment = function(customer){
        $location.path("/farmer-payments/"+customer.user_id+"/"+customer.name)
    }

})

.controller("addFarmerSoldStockCtrl", function($http, $q, $timeout,toastr,$route, $scope){


$scope.load = $http({
                      method: 'get',
                      url: '/superuser/get-harvesters-list',
                      headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'}
               }).then(function (response)
                {   var data = JSON.parse(response.data.stockslist)
                    console.log(data)
                    $scope.input_temp_array = []
                    for(var i in data){
                        var obj = {}
                        obj.name = data[i].fields.item_name
                        obj.type = "--"+data[i].fields.item_type+"--"+data[i].fields.company_invoice_number

                        obj.quantity_weight = data[i].fields.quantity_weight
                        obj.quantity_weight_type = data[i].fields.quantity_type

                        obj.item_cost_type = data[i].fields.rate_per_type
                        obj.item_cost = data[i].fields.item_cost

                        obj.avaible_stock = data[i].fields.available_stock


                        obj.ticked = false
                        obj.id = data[i].pk
                        $scope.input_temp_array.push(obj)
                    }


                }, function errorCallback(response)
                {
                    toastr.error("user already exists!");
                });


})

.controller("editFarmerDetailsCtrl", function($http, $q, $timeout,toastr,$route, $scope){
	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/persons-list/farmer',
			}).then(function (response)
				{
                    console.log(response)
		    		$scope.userslist = [];
		    		var usersdata = response.data.userdata

		    		$.each(usersdata, function(i){
                        var obj = {};

                        obj.user_id = usersdata[i].user_id;
                        obj.username = usersdata[i].name;

                        obj.address =  usersdata[i].address;
                        obj.phone = usersdata[i].phone;
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
        var data = {}
        if(!(this.user_id)){
            toastr.error('unable delete')
            return;
        }
        data.user_id = this.user_id

        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/delete-person',
                                data: data,
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
                                toastr.success('unable to  updated')
                                // console.log("not sent");
                            });



     }
    $scope.updateInfo = function(){
        console.log(this.name, this.phone, this.user_id)
        var self = this;
        var data = {}

        if(!(self.name)){
            toastr.error(' name missing');
            return;
        }

        data.name = self.name;


        if(!(self.user_id)){
            console.log('some thing went wrong...')
            return;
        }



         if(self.address){
            data.address = self.address;
        }


        if(self.phone){
            if(self.phone.length < 10){
                toastr.error('phone number atleast 10 characters')
                return;
            }
            data.phone = self.phone;
        }

        data.user_id = self.user_id;

        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/edit-person',
                                data: data,
                                headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                            }).then(function successCallback(response){
                                        toastr.success('successfully updated')

                                        $("#myModal2").modal("hide");

                                        $timeout(function(){
                                          $route.reload()
                                        },1000)

                                        /*var userdata = response.data.userdata;
                                        var userdetails =  JSON.parse(userdata);
                                        $scope.firstname = userdetails.firstname;
                                        $scope.lastname = userdetails.lastname;
                                        $scope.email = userdetails.email;
                                        $scope.phone  = userdetails.phone;
                                        $scope.user_id = userid;
                                        console.log('user details are', userdetails)

                                       */
                            }, function errorCallback(response)
                            {
                                toastr.success('unable to  updated')
                                // console.log("not sent");
                            });


    }


	$scope.viewUserData = function(user_id, modal){
		// $("#myModal").modal("show");
		$scope.load = $http({
				  	method: 'GET',
					url: '/superuser/person-data/'+user_id,

				  	headers: {
				  		'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function successCallback(response)
							{
								var userdata = response.data.userdata;
								var userdetails =  JSON.parse(userdata);
								$scope.name = userdetails.name;

								$scope.address = userdetails.address;
								$scope.phone  = userdetails.phone;
								$scope.user_id = user_id;
								console.log('user details are', userdetails)

					    		$("#myModal"+modal).modal("show");
							}, function errorCallback(response)
							{
								alert("something went wrong");
					    		// console.log("not sent");
							});
	}
})


.controller("createFarmerCtrl", function ($scope, $http, $q,$location,$timeout, $route, toastr){
        console.log('called created user controller')
        $scope.user = {}

        $scope.user.name = ''
        $scope.user.phone = ''
        $scope.user.address = ''

        $scope.addNewFarmer = function(){

            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-farmer',
                                  data: {
                                        'name': $scope.user.name,
                                        "address" : $scope.user.address,
                                        "phone" : $scope.user.phone,
                                        "type": "farmer"
                                    },
                                  headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                           }).then(function (response)
                            {
                                toastr.success("Successfully Created ...");
                                $scope.master = {};
                                $scope.formData = angular.copy($scope.master);
                                $location.path("/edit-farmer-details")

                            }, function errorCallback(response)
                            {
                                toastr.error("Former is already exists!");
                            });
	    }

});
