angular.module("App")
.controller("specificCustomerPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route,$routeParams, $scope){
    console.log('specificCustomerPaymentsCtrl')
    $scope.show_customer_name = $routeParams.customer_name
    $scope.amount = {}
    $scope.amount.details = ""
    $scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-specific-person-payments',
              data: {
                    'person_id': $routeParams.person_id,
                    'get_data': true,
                    'person_type': 'customer'
                    },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            $scope.payments =  response.data.response

            for(var i in $scope.payments){
                   console.log()
                 var pda= $scope.payments[i].fields.paid_date.split("-")
                 $scope.payments[i].fields.paid_date_format = $scope.payments[i].fields.paid_date;
                 var converted_date = pda[2]+"/"+pda[1]+"/"+pda[0]
                 $scope.payments[i].fields.paid_date = converted_date;

            }

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

         var pda= $scope.amount.details.fields.paid_date.split("-")
         var converted_date = pda[2]+"/"+pda[1]+"/"+pda[0]

        $scope.load = $http({
            method: 'post',
            url: '/superuser/get-specific-person-payments',
            data: {
                    'get_data': false,
                    'id': $scope.amount.details.pk,
                    'amount':$scope.amount.details.fields.amount,
                    'paid_date': $scope.amount.details.fields.paid_date,
                    'remarks': $scope.amount.details.fields.remarks,
            },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
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
        $location.path("/customer-payments/"+customer.user_id)
    }

})
.controller("customerPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route, $scope){
    $scope.amount = {}
    $scope.amount.enter_amount = 0

    $scope.load =
         $http({
              method: 'GET',
              url: '/superuser/persons-list/customer',

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

     $timeout(function(){
            $('#datepicker_sale_products_reports_1') .datepicker({
                format: 'dd/mm/yyyy',
                //startDate: new Date()
                //endDate: '01/12/2020'
            })
        },500)

    $scope.addPayment = function(){
        console.log($scope.amount.enter_amount, $scope.current_customer.user_id)
        $scope.load = $http({
            method: 'post',
            url: '/superuser/add-person-amount',
            data: {
                    'person_id': $scope.current_customer.user_id,
                    'paid_amount':$scope.amount.enter_amount,
                    'paid_date':$scope.amount.paid_date,
                    'remarks':$scope.amount.remarks,
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
        $location.path("/customer-payments/"+customer.user_id+"/"+customer.name)
    }

})
.controller("editCustomerController", function($http, $q, $timeout,toastr,$route, $scope){
		$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/persons-list/customer',
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

.controller("createCustomerCtrl", function ($scope, $http, $q,$location,
                                        $timeout, $route, toastr){
        $scope.user = {}

        $scope.user.name = ''
        $scope.user.phone = ''
        $scope.user.address = ''

        $scope.addNewCustomer = function(){

            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-farmer',
                                  data: {
                                        'name': $scope.user.first_name,
                                        "address" : $scope.user.address,
                                        "phone" : $scope.user.phone,
                                        "type": "customer"
                                    },
                                  headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                           }).then(function (response)
                            {
                                toastr.success("Successfully Created ...");
                                $scope.master = {};
                                $scope.formData = angular.copy($scope.master);
                                //$location.path("/view-modify-customers")

                            }, function errorCallback(response)
                            {
                                toastr.error("customer is already exists!");
                            });
	    }




});
