angular.module("App")
.controller("editExpenditureCtrl", function($http, $q, $timeout,toastr,$route, $scope){
	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/add-expenditure',
			}).then(function (response)
				{
				    $scope.expenditures =[]
                    var expenditures_list = response.data.expenditures_list
		    		$.each(expenditures_list, function(i){
                        var obj = {};

                        obj.id = expenditures_list[i].id;
                        obj.amount = expenditures_list[i].amount;

                        obj.created_date =  expenditures_list[i].created_date;
                        obj.remarks = expenditures_list[i].remarks;
                        obj.type = expenditures_list[i].type;
                        $scope.expenditures.push(obj);
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
        if(!(this.single_exp.id)){
            toastr.error('unable delete')
            return;
        }
        data.id = this.single_exp.id

        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/delete-expenditure',
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
        console.log(this.single_exp.amount, this.single_exp.created_date)



        var self = this;

        if(!(self.single_exp.amount)){
            toastr.error(' amount missing');
            return;
        }

        if(!(self.single_exp.created_date)){
            console.log('date missing')
            return;
        }

        if(!(self.single_exp.type)){
            toastr.error('type missing')
            return;
        }
        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/edit-expenditure',
                                data: self.single_exp,
                                headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'}
                            }).then(function successCallback(response){
                                        toastr.success('successfully updated')

                                        $("#myModal2").modal("hide");

                                        $timeout(function(){
                                          $route.reload()
                                        },1000)

                            }, function errorCallback(response)
                            {
                                toastr.error('unable to  updated')
                                // console.log("not sent");
                            });


    }


	$scope.viewUserData = function(exp, modal){

		$scope.single_exp ={}
		$scope.single_exp['amount'] = exp.amount
		$scope.single_exp['remarks'] = exp.remarks
		$scope.single_exp['type'] = exp.type
		$scope.single_exp['id'] = exp.id
		$scope.temp_single_exp =  [
            {'id': 'personal', 'name': 'personal'},
            {'id': 'industrial', 'name': 'industrial'},
         ]
		var temp_date = exp.created_date.split("-")
		$scope.single_exp['created_date'] = temp_date[2]+"/"+temp_date[1]+"/"+temp_date[0]
        $("#myModal"+modal).modal("show");

	}
})

.controller("createExpenditureCtrl", function ($scope,$timeout, $q, $http, $alert, toastr){
    $scope.stock_names = [
        {'id': 'personal', 'name': 'personal'},
        {'id': 'industrial', 'name': 'industrial'},
    ]

    $timeout(function(){
        $('#datepicker') .datepicker({
            format: 'dd/mm/yyyy',
        })
    },500)

    $scope.setType = function(type){
        $scope.stockType = type;
    }
    $scope.createStock = function (){

               $scope.load = $http({
					  method: 'post',
					  url: '/superuser/add-expenditure',
					  data: {
		                    "stockdata" : $scope.stock,
		                },
					  headers: {
					  	'Content-Type': 'application/x-www-form-urlencoded'}
							}).then(function successCallback(response)
								{
						    		// toastr.success("stock has been created successfully")
						    		$scope.master = {};
						    		$scope.formData = angular.copy($scope.master);
						    		toastr.success('successfully added new stock...')

								}, function errorCallback(response)
								{
						    		toastr.error(response.data.response)
								});
			}
})
