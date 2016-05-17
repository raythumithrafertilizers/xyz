angular.module("App")


.controller("legalCategoryProductCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){
    console.log('productSaleCtrl')

  
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
.controller("downLoadInvoiceBillReportsCtrl", function ($scope,toastr, $routeParams, $http, $q, $route, $location, $alert, $timeout){


    $http({method: 'GET', url: '/superuser/invoice-bill-reports'}).
  success(function(data, status, headers, config) {
     var anchor = angular.element('<a/>');
     anchor.attr({
         href: 'data:attachment/csv;charset=utf-8,' + encodeURI(data),
         target: '_blank',
         download: 'test.csv'
     })[0].click();
    $location.path("/invoice-bill-report")
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
    console.log('productSaleCtrl')

    // pie chart data initlizations and ajax data access
  var PieData = [
  {
    value: 0,
    color: "#f56954",
    highlight: "#f56954",
    label: "Seeds"
  },
  {
    value: 0,
    color: "#00a65a",
    highlight: "#00a65a",
    label: "Pesticides"
  },
  {
    value: 0,
    color: "#f39c12",
    highlight: "#f39c12",
    label: "Fertilizers"
  },
  {
    value: 0,
    color: "#00c0ef",
    highlight: "#00c0ef",
    label: "Bio Pesticides"
  },
  {
    value: 0,
    color: "#3c8dbc",
    highlight: "#3c8dbc",
    label: "Bio Fertilizers"
  }

];

var pieOptions = {
  //Boolean - Whether we should show a stroke on each segment
  segmentShowStroke: true,
  //String - The colour of each segment stroke
  segmentStrokeColor: "#fff",
  //Number - The width of each segment stroke
  segmentStrokeWidth: 2,
  //Number - The percentage of the chart that we cut out of the middle
  percentageInnerCutout: 50, // This is 0 for Pie charts
  //Number - Amount of animation steps
  animationSteps: 100,
  //String - Animation easing effect
  animationEasing: "easeOutBounce",
  //Boolean - Whether we animate the rotation of the Doughnut
  animateRotate: true,
  //Boolean - Whether we animate scaling the Doughnut from the centre
  animateScale: false,
  //Boolean - whether to make the chart responsive to window resizing
  responsive: true,
  // Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
  maintainAspectRatio: true,
  //String - A legend template
  legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>"
};
// Get context with jQuery - using jQuery's .get() method.
var pieChartCanvas = $("#pieChart").get(0).getContext("2d");
var pieChart = new Chart(pieChartCanvas);


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
                    $scope.stock_data = [];
                    console.log(response.data)
		    		$scope.stock_data = response.data.stocks_list
		    		$scope.customer_data = response.data.customer_details
		    		$timeout(function(){
                            $("#example1_modify_stock").DataTable();
                    },500)

                    var data = response.data.types_data
                    for(temp in PieData){
                        console.log(data[PieData[temp].label])
                        if(data[PieData[temp].label] != undefined){
                            PieData[temp].value = data[PieData[temp].label]
                        }
                    }

                    pieChart.Doughnut(PieData, pieOptions);




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