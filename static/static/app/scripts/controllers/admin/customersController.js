angular.module("App")

.controller("editCustomerController", function($http, $q, $timeout,toastr,$route, $scope){
	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/customers-list',
			}).then(function (response)
				{
		    		$scope.userslist = [];
		    		var usersdata = JSON.parse(response.data.userdata);
		    		$.each(usersdata, function(i){
                        var obj = {};
                        obj.userid = usersdata[i].userid;
                        obj.username = String(usersdata[i].firstname)+ " "  + String(usersdata[i].lastname);
                        obj.address =  usersdata[i].address;
                        obj.phone = usersdata[i].phone;
                        $scope.userslist.push(obj);
                        $timeout(function(){
                         $("#example1").DataTable();
                        },500)
                    })
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
                                url: '/superuser/delete-rythu-customer',
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
        console.log(this.firstname, this.lastname, this.phone, this.password, this.re_password, this.user_id)
        var self = this;
        var data = {}

        if(!(self.firstname)){
            toastr.error('first name missing');
            return;
        }

        data.first_name = self.firstname;


        if(!(self.user_id)){
            console.log('some thing went wrong...')
            return;
        }

        if(self.lastname){
            data.last_name = self.lastname;
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
                                url: '/superuser/edit-customer',
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


	$scope.viewUserData = function(userid, modal){
		// $("#myModal").modal("show");
		$scope.load = $http({
				  	method: 'post',
					url: '/superuser/customer-data',
					data: {
		                   "userid" : userid,
		                },
				  	headers: {
				  		'Content-Type': 'application/x-www-form-urlencoded'}
						}).then(function successCallback(response)
							{
								var userdata = response.data.userdata;
								var userdetails =  JSON.parse(userdata);
								$scope.firstname = userdetails.firstname;
								$scope.lastname = userdetails.lastname;
								$scope.address = userdetails.address;
								$scope.phone  = userdetails.phone;
								$scope.user_id = userid;
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
        console.log('called created user controller')
        $scope.user = {}

        $scope.user.first_name = ''
        $scope.user.last_name = ''
        $scope.user.phone = ''
        $scope.user.email = ''
        $scope.user.password = ''
        $scope.user.password_c = ''
        $scope.user.active = false;




        $scope.addNewCustomer = function(){

            $scope.load = $http({
                                  method: 'post',
                                  url: '/superuser/add-customer',
                                  data: {
                                        'firstname': $scope.user.first_name,
                                        "lastname": $scope.user.last_name,
                                        "address" : $scope.user.address,
                                        "phone" : $scope.user.phone,
                                    },
                                  headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                           }).then(function (response)
                            {
                                toastr.success("Successfully Created ...");
                                $scope.master = {};
                                $scope.formData = angular.copy($scope.master);
                                $location.path("/view-modify-customers")

                            }, function errorCallback(response)
                            {
                                toastr.error("user already exists!");
                            });
	    }

});
