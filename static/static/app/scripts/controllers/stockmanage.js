angular.module("App")


.controller("editStockController", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){

    $timeout(function(){
        $('#datepicker') .datepicker({
            format: 'dd/mm/yyyy',
            startDate: '01/03/2016',
            endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker1') .datepicker({
            format: 'dd/mm/yyyy',
            startDate: '01/03/2016',
            endDate: '01/12/2020'
        })
    },500)


   /* $scope.stockType = [
        {'name': 'Fertilizers', 'id': 'Fertilizers'},
        {'name': 'Pesticides', 'id': 'Pesticides'},
        {'name': 'Seeds', 'id': 'Seeds'}
    ]*/

    $scope.stockType = [
        {'name': 'Fertilizers', 'id': 'Fertilizers'},
        {'name': 'Pesticides', 'id': 'Pesticides'},
        {'name': 'Seeds', 'id': 'Seeds'},
        {'name': 'Bio Pesticides', 'id': 'Bio Pesticides'},
        {'name': 'Bio Chemicals', 'id': 'Bio Chemicals'}
    ]


    $scope.quantityList = [
        {'name': 'kgs', 'id': 'kgs'},
        {'name': 'liters', 'id': 'liters'},
        {'name': 'units', 'id': 'units'}
    ]

    $scope.quantityRateList = [
        {'name': 'kgs', 'id': 'kgs'},
        {'name': 'liters', 'id': 'liters'},
        {'name': 'units', 'id': 'units'}
    ]

     $scope.isLegalProduct = [
        {'name': 'legal', 'id': 'legal'},
        {'name': 'illegal', 'id': 'illegal'},
    ]

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
						    		toastr.success('successfully added new stock...')
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
        $scope.stock.expired_date =  dateString(stockdata[0].fields.expire_date)

        $scope.stock.stockType = stockdata[0].fields.item_type

        $scope.stock.isLegal = stockdata[0].fields.isLegal

        $scope.stock.batch_number = stockdata[0].fields.item_batch_number;
        $scope.stock.mfg_date = dateString(stockdata[0].fields.mfg_date)
        $scope.stock.lot_number = stockdata[0].fields.item_lot_number;
        $scope.stock.purchase_from = stockdata[0].fields.purchase_form;

        $scope.stock.quantity_count = stockdata[0].fields.quantity_weight;
        $scope.stock.quantity = stockdata[0].fields.quantity_type;

        $scope.stock.quantity_rate = stockdata[0].fields.rate_per_type;
        $scope.stock.rate = stockdata[0].fields.item_cost;

	}, function errorCallBack(error){
		console.log(error);
	})


})


.controller("addStockController", function ($scope,$timeout, $q, $http, $alert, toastr){
    $scope.stockType = 'Select Stock Type'

     $timeout(function(){
        $('#datepicker') .datepicker({
            format: 'dd/mm/yyyy',
            startDate: '01/03/2016',
            endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker1') .datepicker({
            format: 'dd/mm/yyyy',
            startDate: '01/03/2016',
            endDate: '01/12/2020'
        })
    },500)



    $scope.stockType = [
        {'name': 'Fertilizers', 'id': 'Fertilizers'},
        {'name': 'Pesticides', 'id': 'Pesticides'},
        {'name': 'Seeds', 'id': 'Seeds'},
        {'name': 'Bio Pesticides', 'id': 'Bio Pesticides'},
        {'name': 'Bio Chemicals', 'id': 'Bio Chemicals'}
    ]

    $scope.isLegalProduct = [
        {'name': 'legal', 'id': 'legal'},
        {'name': 'illegal', 'id': 'illegal'},
    ]

    $scope.quantityList = [
        {'name': 'kgs', 'id': 'kgs'},
        {'name': 'liters', 'id': 'liters'},
        {'name': 'units', 'id': 'units'}
    ]

    $scope.quantityRateList = [
        {'name': 'kgs', 'id': 'kgs'},
        {'name': 'liters', 'id': 'liters'},
        {'name': 'units', 'id': 'units'}
    ]

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
						    		// console.log("not sent");
						    		toastr.error('failed  to add new stock...')
								});
			}



			$scope.getState =  function(){

			$scope.load = $http({
			  		method: 'GET',
					  url: '/superuser/getstates',
					  params:{
					  	"countryid" : $scope.stock.country.cid,
					  }
					}).then(function (response)
						{
				    		$scope.statelist = [];
				    		var statesdata = JSON.parse(response.data.stateslist);

				    		$.each(statesdata, function(i){
				    			var obj = {};
				    			obj.sid = statesdata[i].pk;
				    			obj.sname = statesdata[i].fields.stateName;
				    			$scope.statelist.push(obj);
				    		})


						}, function errorCallback(response)
						{
				    		console.log(response);
						});

			}

			$scope.getCities =  function(){

			$scope.load = $http({
			  		method: 'GET',
					  url: '/superuser/getcities',
					  params:{
					  	"stateid" : $scope.stock.states.sid,
					  }
					}).then(function (response)
						{
				    		$scope.citieslist = [];
				    		var citiesdata = JSON.parse(response.data.citieslist);
				    		$.each(citiesdata, function(i){
				    			var obj = {};
				    			obj.cityid = citiesdata[i].pk;
				    			obj.cityname = citiesdata[i].fields.cityName;
				    			$scope.citieslist.push(obj);
				    		})
						}, function errorCallback(response)
						{
				    		console.log(response);
						});

			}


		$scope.getAreas =  function(){

			$scope.load = $http({
			  		method: 'GET',
					  url: '/superuser/getareas',
					  params:{
					  	"cityid" : $scope.stock.cities.cityid,
					  }
					}).then(function (response)
						{
				    		$scope.areaslist = [];
				    		var areasdata = JSON.parse(response.data.arealist);
				    		$.each(areasdata, function(i){
				    			var obj = {};
				    			obj.areaid = areasdata[i].pk;
				    			obj.areaname = areasdata[i].fields.localityName;
				    			$scope.areaslist.push(obj);
				    		})
						}, function errorCallback(response)
						{
				    		console.log(response);
						});

			}

})




.controller("modifyStockCtrl", function ($scope,toastr, $http, $q, $route, $location, $timeout){
		$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/stock-list',
			}).then(function (response) 
				{
		    		$scope.stockslist = [];
		    		var stockdata = JSON.parse(response.data.stockslist);
		    		$.each(stockdata, function(i){
				    			var obj = {};
				    			obj.stockId = stockdata[i].pk;
				    			obj.stock_name = stockdata[i].fields.item_name;
				    			obj.expired_date =  stockdata[i].fields.expire_date;
				    			obj.stock_type = stockdata[i].fields.item_type;
				    			obj.quantity_weight = stockdata[i].fields.quantity_weight;
				    			$scope.stockslist.push(obj);
				    			$timeout(function(){
								    $("#example1").DataTable();
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