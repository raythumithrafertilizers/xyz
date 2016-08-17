angular.module("App")

angular.module("App")
.controller("specificLabourPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route,$routeParams, $scope){
    $scope.amount = {}
    $scope.amount.details = ""
    $scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-specific-person-payments',
              data: {
                    'person_id': $routeParams.person_id,
                    'get_data': true,
                    'person_type': 'labour'
                    },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            $scope.payments =  response.data.response
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
        $scope.load = $http({
            method: 'post',
            url: '/superuser/get-specific-person-payments',
            data: {
                    'get_data': false,
                    'id': $scope.amount.details.pk,
                    'amount':$scope.amount.details.fields.amount
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


})
.controller("labourPaymentsCtrl", function($http, $q,$location, $timeout,toastr,$route, $scope){
    $scope.amount = {}
    $scope.amount.enter_amount = 0

    $scope.load =
         $http({
              method: 'GET',
              url: '/superuser/persons-list/labour',

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
        console.log($scope.amount.enter_amount, $scope.current_customer.user_id)
        $scope.load = $http({
            method: 'post',
            url: '/superuser/add-person-amount',
            data: {
                    'person_id': $scope.current_customer.user_id,
                    'paid_amount':$scope.amount.enter_amount,
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
        $location.path("/labour-payments/"+customer.user_id)
    }

})

.controller("editLabourDetailsCtrl", function($http, $q, $timeout,toastr,$route, $scope){


		$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/persons-list/labour',
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


.controller("createLabourCtrl", function ($scope, $http, $q,$location,$timeout, $route, toastr){
        console.log('called created user controller')

                $scope.user = {}

        $scope.user.name = ''
        $scope.user.phone = ''
        $scope.user.address = ''

        $scope.addNewLabour = function(){

            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-farmer',
                                  data: {
                                        'name': $scope.user.name,
                                        "address" : $scope.user.address,
                                        "phone" : $scope.user.phone,
                                        "type": "labour"
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
                                toastr.error("Former is already exists!");
                            });
	    }





});
