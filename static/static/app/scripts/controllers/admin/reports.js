angular.module("App")
.controller("downloadExpenditureReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


  $http({method: 'GET', url: '/superuser/download-expenditure-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/interest-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("expenditureReportsCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $scope.stock_names = [{
        'name': 'Personal',
        'id': 'personal'
    }, {
        'name': 'Industrial',
        'id': 'industrial'
    }]

    $scope.selected_farmer = function(){
        var stock_id = false
        if($scope.selected_stock_object){

            stock_id = $scope.selected_stock_object
        }


        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/expenditure-reports',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'stock_id': stock_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.data = response.data.data
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})

.controller("downloadInterstReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


  $http({method: 'GET', url: '/superuser/download-interest-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/interest-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("downloadPaidReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


  $http({method: 'GET', url: '/superuser/download-paid-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/interest-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})

.controller("interestCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


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
        var farmer_id = false
        if($scope.selected_farmer_object){
            farmer_id = $scope.selected_farmer_object.user_id
        }

        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/interest-reports',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'farmer_id': farmer_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.stock_data = [];
                    console.log(response.data)
                    $scope.interest_data = response.data.interest_data
                    $scope.paid_amounts = response.data.paid_amounts
                    $scope.specific_farmer_data = response.data.specific_farmer_data
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})


.controller("downloadAppendReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


  $http({method: 'GET', url: '/superuser/download-append-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/append-stock-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})

.controller("downloadRemainAppendReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


  $http({method: 'GET', url: '/superuser/download-remain-stock-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/append-stock-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})

.controller("append_stock_reports_ctrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/stock-names',
			}).then(function (response)
				{
                    console.log(response)
		    		$scope.stock_names = [];
		    		var stock_names = response.data.stock_names

		    		$.each(stock_names, function(i){
                        var obj = {};
                        obj.id = stock_names[i].id;
                        obj.name = stock_names[i].name;
                        $scope.stock_names.push(obj);
                    })

                    console.log($scope.stock_names)
				}, function errorCallback(response)
				{
		    		console.log(response);
				});

    $scope.selected_farmer = function(){
        var stock_id = false
        if($scope.selected_stock_object){

            stock_id = $scope.selected_stock_object
        }


        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/stock-append-reports',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'stock_id': stock_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.data = response.data.data
                    $scope.stock_name = response.data.stock_name
                    $scope.remain = response.data.remain
                    $scope.remaining_all_stock = response.data.remaining_all_stocks
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})


.controller("farmerReport", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){
    $scope.farmer_name = ''

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
        var farmer_id = false
        if($scope.selected_farmer_object){
            farmer_id = $scope.selected_farmer_object.user_id
            $scope.farmer_name = $scope.selected_farmer_object.username

        }

        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/farmers-report',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'farmer_id': farmer_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.stock_data = [];
                    console.log(response.data)
                    $scope.borrowers = response.data.specific_farmer_data
                    for(var t in $scope.borrowers){
                        console.log($scope.borrowers[t].farmer_name, $scope.farmer_name)
                        if($scope.borrowers[t].name == $scope.farmer_name){
                            $scope.farmer_due = $scope.borrowers[t]['due']
                        }
                    }
                    $scope.all_farmers = response.data.credits
                    $scope.specific_farmer_data = response.data.debits
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})

.controller("harvesterReport", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){



    $scope.farmer_name = ''

    $scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/persons-list/harvester',
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
        var farmer_id = false
        if($scope.selected_farmer_object){
            farmer_id = $scope.selected_farmer_object.user_id
            $scope.farmer_name = $scope.selected_farmer_object.username

        }

        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/harvesters-reports',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'farmer_id': farmer_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.stock_data = [];
                    console.log(response.data)
                    $scope.borrowers = response.data.specific_farmer_data
                    for(var t in $scope.borrowers){
                        console.log($scope.borrowers[t].farmer_name, $scope.farmer_name)
                        if($scope.borrowers[t].name == $scope.farmer_name){
                            $scope.farmer_due = $scope.borrowers[t]['due']
                        }
                    }
                    $scope.all_farmers = response.data.credits
                    $scope.specific_farmer_data = response.data.debits
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})
.controller("customerReport", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){



    $scope.farmer_name = ''

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
                        $scope.userslist.push(obj);
                    })

                    console.log($scope.userslist)
				}, function errorCallback(response)
				{
		    		console.log(response);
				});

    $scope.selected_farmer = function(){
        var farmer_id = false
        if($scope.selected_farmer_object){
            farmer_id = $scope.selected_farmer_object.user_id
            $scope.farmer_name = $scope.selected_farmer_object.username

        }

        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/customers-reports',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'farmer_id': farmer_id
              }
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.stock_data = [];
                    console.log(response.data)
                    $scope.borrowers = response.data.specific_farmer_data
                    for(var t in $scope.borrowers){
                        console.log($scope.borrowers[t].farmer_name, $scope.farmer_name)
                        if($scope.borrowers[t].name == $scope.farmer_name){
                            $scope.farmer_due = $scope.borrowers[t]['due']
                        }
                    }
                    $scope.all_farmers = response.data.debits
                    $scope.specific_farmer_data = response.data.credits
                    $timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }

    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            if(s_split.length >= 3 && e_split.length >= 3){
                $scope.selected_farmer()
            }

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();
})
.controller("labourReport", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){



    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/products-sale-report',
              data: {'start_date': $scope.start_date, 'end_date':$scope.end_date}
            }).then(function (response){
                    console.log(response, 'report data is')
                    $scope.stock_data = [];
                    console.log(response.data)
		    		$scope.stock_data = response.data.stocks_list
		    		$scope.customer_data = response.data.customer_details
		    		$timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})
.controller("legalCategoryProductCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){

  
    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/legal-category-report',
              data: {'start_date': $scope.start_date,
                     'end_date':$scope.end_date
                     }
            }).then(function (response){
                    console.log(response)
                    $scope.report_objects = response.data.stocks_list

		    		$timeout(function(){
                            $("#example1_legal_stock").DataTable();
                    },500)


            }, function errorCallback(response){
                    console.log(response);
            });

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})
.controller("downloadFarmerReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/download-farmer-report/'+$routeParams.status}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    //$location.path("/farmers-report")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("downloadHarvesterReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/download-harvester-report/'+$routeParams.status}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/harvesters-report")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("downloadProductSaleReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/download-product-sale-report/'+$routeParams.status}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/customers-report")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("downloadCustomerReports", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/download-customers-report/'+$routeParams.status}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/product-sale-report")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})
.controller("legalCategoryReportsCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/legal-category-report'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'legaltest.csv'
     })[0].click();
    $location.path("/legal-category-sold-reports")
  }).error(function(data, status, headers, config) {
    // handle error
  });
})


.controller("invoiceBillReportsCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){



    var d = new Date()

    $scope.start_date = "8/5/2016" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = "8/6/2016"//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")


        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/invoice-bill-reports',
              data: {'start_date': $scope.start_date, 'end_date':$scope.end_date}
            }).then(function (response){
                    console.log(response)

                    $scope.final_report_data = response.data.invoice_final_report
                    for(temp in $scope.final_report_data){

                    }

		    		$timeout(function(){
                            $("#example1_invoice_bill_data").DataTable();
                    },500)


            }, function errorCallback(response){
                    console.log(response);
            });

        }
    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})
.controller("productSaleCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){



    var d = new Date()

    $scope.start_date = "" //d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()
    $scope.end_date = ""//d.getDate()+"/"+d.getMonth()+"/"+d.getFullYear()

     $scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/stock-names',
			}).then(function (response)
				{
                    console.log(response)
		    		$scope.stock_names = [];
		    		var stock_names = response.data.stock_names

		    		$.each(stock_names, function(i){
                        var obj = {};
                        obj.id = stock_names[i].id;
                        obj.name = stock_names[i].name;
                        $scope.stock_names.push(obj);
                    })

                    console.log($scope.stock_names)
				}, function errorCallback(response)
				{
		    		console.log(response);
				});

    $scope.selected_farmer = function(){
        var stock_id = false
        if($scope.selected_stock_object){

            stock_id = $scope.selected_stock_object
        }


        // getting former sold details
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
            toastr.error('start date must less than end date')
            return false;
        }else{
            $scope.load = $http({
            method: 'POST',
              url: '/superuser/products-sale-report',
              data: {
                    'start_date': $scope.start_date,
                    'end_date':$scope.end_date,
                    'stock_id': stock_id
              }
            }).then(function (response){
                        console.log(response, 'report data is')
                        $scope.stock_data = response.data.stocks_list
                        $timeout(function(){
                                $("#example1_modify_stock").DataTable();
                        },500)

            }, function errorCallback(response){
                    console.log(response);
            });

        }


    }


    $scope.check_dates = function(){
        var s_split = $scope.start_date.split("/")
        var e_split = $scope.end_date.split("/")

        if(s_split.length >= 3 && e_split.length >= 3){
            console.log(s_split.length, s_split)
            if(new Date(s_split[1]+"/"+s_split[0]+"/"+s_split[2]) > new Date(e_split[1]+"/"+e_split[0]+"/"+e_split[2])){
                toastr.error('start date must less than end date')
                return false;
            }else{
                $scope.selected_farmer();
            }
        }

    }

     $timeout(function(){
        $('#datepicker_sale_products_reports_1') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: new Date()
            //endDate: '01/12/2020'
        })
    },500)

    $timeout(function(){
        $('#datepicker_sale_products_reports_2') .datepicker({
            format: 'dd/mm/yyyy',
            //startDate: '01/03/2016',
            //endDate: '01/12/2020'
        })
    },500)


    $scope.call_date_change = function(){
        $scope.check_dates();
    }

    $scope.check_dates();

})