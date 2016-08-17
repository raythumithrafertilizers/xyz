angular.module("App")
.controller("editStockNamesController", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){

    $scope.showPopUpNewStockName = function(){
        console.log('add new name')
        $("#addNewStockName1").modal("show");
    }

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

    $scope.showPopUp = function(stock){
        $scope.modified_stock_name = stock
        $("#EditStockName").modal("show");
    }

    $scope.DeletePopUp = function(stock){
        $scope.modified_stock_name = stock
        $("#deleteStockPopUp").modal("show");
    }

    $scope.addNewStockName = function(){
        $scope.load = $http({
            method: 'post',
            url: '/superuser/stock-names',
            data: {
                    'name': $scope.new_stock_name,
                    'update': false
                  },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function successCallback(response){

                    $("#addNewStockName1").modal("hide");
                     toastr.success('successfully saved')
                    $timeout(function(){
                        $route.reload()
                    },1000)




        }, function errorCallback(response)
        {
            toastr.success('unable to  save....')
            // console.log("not sent");
        });
    }

    $scope.updateStockName = function(){
        $scope.load = $http({
            method: 'post',
            url: '/superuser/stock-names',
            data: {
                    'name': $scope.modified_stock_name.name,
                    'id': $scope.modified_stock_name.id,
                    'update': true
                  },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function successCallback(response){
                    toastr.success('successfully saved')
                     $("#EditStockName").modal("hide");

        }, function errorCallback(response)
        {
            toastr.success('unable to  save....')
             $("#EditStockName").modal("hide");
            // console.log("not sent");
        });
    }

    $scope.delete_stock_name = function(){
        console.log($scope.modified_stock_name.id)
        $scope.load = $http({
            method: 'post',
            url: '/superuser/delete-stock-name',
            data: {
                    'id': $scope.modified_stock_name.id
                  },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function successCallback(response){
                    toastr.success('successfully deleted')
                     $("#deleteStockPopUp").modal("hide");


                    $timeout(function(){
                        $route.reload()
                    },1000)

        }, function errorCallback(response)
        {
            toastr.success('unable to  delete....')
             $("#deleteStockPopUp").modal("hide");
            // console.log("not sent");
        });

    }


})

.controller("editStockController", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/stock-names',
			}).then(function (response){
		    		$scope.stock_names = response.data.stock_names;

			}, function errorCallback(response){
		    		console.log(response);
			});



    $timeout(function(){
        $('#datepicker') .datepicker({
            format: 'dd/mm/yyyy'

        })
    },500)


    $scope.updateStock = function(){
        $scope.load = $http({
					  method: 'post',
					  url: '/superuser/edit-stock',
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
						    		$location.path("/modify-stock")
						    		toastr.success('successfully updated...')
								}, function errorCallback(response)
								{
						    		// console.log("not sent");
						    		toastr.error('failed  to add new stock...')
								});

    }

    function dateString(date){
        if(date){
            var splitedOne = date.split('-')
            return splitedOne[2]+"/"+splitedOne[1]+"/"+splitedOne[0]
        }
    }
	$scope.editstock = function () {
    	$scope.load = $http({
			  method: 'post',
			  url: '/superuser/editstock',
			  data: {
	                "stockdata" : $scope.stock,
	            },
			  headers: {
			  	'Content-Type': 'application/x-www-form-urlencoded'}
					}).then(function successCallback(response)
						{
				    		$alert({
					                title: "stock details saved successfully",
					                placement: 'top', type: 'success',
					                show: true
					            });
						}, function errorCallback(response)
						{
				    		// console.log("not sent");
						});

	}


	$scope.load = $http({
		method : 'GET',
		url : "/superuser/get-one-stock",
		params : {
			"stockId" : $routeParams.stockId,
		}
	}).then(function successsCallBack(response){

		var stockdata = JSON.parse(response.data.stockdata);
		console.log('dddddddddgot stock data is', stockdata)
		$scope.stock = {};
		$scope.stock.stockId = stockdata[0].pk;
        $scope.stock.stock_name = stockdata[0].fields.item_name;

        $scope.stock.created_date =  dateString(stockdata[0].fields.create_date)
        $scope.stock.a_stock = stockdata[0].fields.available_stock
        $scope.stock.i_stock = stockdata[0].fields.inital_stock
        $scope.stock.remarks = stockdata[0].fields.remarks;


	}, function errorCallBack(error){
		console.log(error);
	})


})

.controller("addStockController", function ($scope,$timeout, $q, $http, $alert, toastr){
     $scope.load = $http({
        method: 'GET',
          url: '/superuser/stock-names',
        }).then(function (response){
                $scope.stock_names = response.data.stock_names;


        }, function errorCallback(response){
                console.log(response);
        });

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
					  url: '/superuser/add-stock',
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


.controller("appendStockController", function ($scope,$timeout, $q, $http, $alert, toastr){
     $scope.load = $http({
        method: 'GET',
          url: '/superuser/stock-names',
        }).then(function (response){
                $scope.stock_names = response.data.stock_names;


        }, function errorCallback(response){
                console.log(response);
        });

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
					  url: '/superuser/append-stock',
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


.controller("modifyStockCtrl", function ($scope,toastr, $http, $q, $route, $location, $timeout){
		$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/stock-list',
			}).then(function (response) 
				{

				    console.log(response)
		    		$scope.stockslist = [];
		    		var stockdata = JSON.parse(response.data.stockslist);
		    		$.each(stockdata, function(i){
				    			var obj = {};
				    			obj.stockId = stockdata[i].pk;
				    			obj.stock_name = stockdata[i].fields.stock_name;
				    			obj.created_date =  stockdata[i].fields.create_date;
				    			obj.a_stock = stockdata[i].fields.available_stock;
				    			obj.i_stock = stockdata[i].fields.inital_stock;
				    			$scope.stockslist.push(obj);
				    			$timeout(function(){
								    $("#example1_modify_stock").DataTable();
								},500)
				    		})
				}, function errorCallback(response) 
				{
		    		console.log(response);
				});

		$scope.EditStock =  function(stockId){
			 $location.path("/edit-stock-details/"+stockId);
			 // console.log("storage data: ", window.localStorage.getItem('stock_id'));
		}

        $scope.confirmDelete = function(stockId){
            $("#myModal3").modal("show");
            $scope.deletingStock = stockId;
        }

        $scope.hideModel = function(){
                $("#myModal3").modal("hide");
        }

		$scope.deleteStock = function(){

		    $scope.load = $http({
	  		method: 'post',
			  url: '/superuser/delete-stock',
			  data:{
			  	"stockId" : $scope.deletingStock,
			  }
			}).then(function (response) 
				{    $scope.hideModel()
                     toastr.success('stock is deleted successfully')

                     $timeout(function(){
                        $route.reload();
                     },500)

				}, function errorCallback(response)
				{
		    		toastr.error('unable to delete stock')
				});
		}

})