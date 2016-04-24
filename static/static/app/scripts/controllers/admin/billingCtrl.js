function process_image_path(path){
    var image_path = path.split('/')
    console.log('path is ', image_path[image_path.length-1])
    return 'static/uploads/'+image_path[image_path.length-1]

}
angular.module("App")
.controller("dashBoardCtrl", function($http,$location,$localStorage, $q, $timeout,toastr,$route, $scope){
console.log('dashboar controller called')
// gallery start here
function process_gallery_image_path(path){
    var image_path = path.split('/')
    console.log('path is ', image_path[image_path.length-1])
    return 'static/upload_gallary_images/'+image_path[image_path.length-1]

}

$scope.load =
$http({
    method: 'GET',
      url: '/superuser/gallery-image',
    }).then(function (response){
            console.log('response iamges', response)
            $scope.images = [];
            var imagesList = JSON.parse(response.data.gallery_images);

            $.each(imagesList, function(i){
                var obj = {};
                obj.thumb = process_gallery_image_path(imagesList[i].fields.gallery_image);
                obj.img = obj.thumb
                $scope.images.push(obj);
            })

    }, function errorCallback(response){
            console.log(response);
    });


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
    label: "Bio Chemicals"
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
//Create pie or douhnut chart

 $scope.load =
 $http({
      method: 'post',
      url: '/superuser/get-graph-data',
      data: {
            'get_products_quantity': true
      },
      headers: {'Content-Type': 'application/x-www-form-urlencoded'}
 }).then(function (response){
    var data = JSON.parse(response.data.stockslist)
    //console.log(data)
    $.each(data, function(i){

        for(temp in PieData){
             if(data[i].fields.item_type == PieData[temp].label){
                PieData[temp].value += data[i].fields.quantity_weight
             }
        }
    })
    console.log(PieData)
    pieChart.Doughnut(PieData, pieOptions);
 }, function(error){
    console.log('error', error)

 })
 //------------end of donout graph ---------------------



 // Get context with jQuery - using jQuery's .get() method.
        var areaChartCanvas = $("#areaChart").get(0).getContext("2d");
        // This will get the first returned node in the jQuery collection.
        var areaChart = new Chart(areaChartCanvas);
        var areaChartOptions = {
          //Boolean - If we should show the scale at all
          showScale: true,
          //Boolean - Whether grid lines are shown across the chart
          scaleShowGridLines: true,
          //String - Colour of the grid lines
          scaleGridLineColor: "rgba(0,0,0,.05)",
          //Number - Width of the grid lines
          scaleGridLineWidth: 1,
          //Boolean - Whether to show horizontal lines (except X axis)
          scaleShowHorizontalLines: true,
          //Boolean - Whether to show vertical lines (except Y axis)
          scaleShowVerticalLines: true,
          //Boolean - Whether the line is curved between points
          bezierCurve: true,
          //Number - Tension of the bezier curve between points
          bezierCurveTension: 0.3,
          //Boolean - Whether to show a dot for each point
          pointDot: false,
          //Number - Radius of each point dot in pixels
          pointDotRadius: 4,
          //Number - Pixel width of point dot stroke
          pointDotStrokeWidth: 1,
          //Number - amount extra to add to the radius to cater for hit detection outside the drawn point
          pointHitDetectionRadius: 20,
          //Boolean - Whether to show a stroke for datasets
          datasetStroke: true,
          //Number - Pixel width of dataset stroke
          datasetStrokeWidth: 2,
          //Boolean - Whether to fill the dataset with a color
          datasetFill: true,
          //String - A legend template
          legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>",
          //Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
          maintainAspectRatio: true,
          //Boolean - whether to make the chart responsive to window resizing
          responsive: true
        };

        var areaChartData = {
          labels: [],
          datasets: [
            {
              label: "Total Sales",
              fillColor: "rgba(210, 214, 222, 1)",
              strokeColor: "rgba(210, 214, 222, 1)",
              pointColor: "rgba(210, 214, 222, 1)",
              pointStrokeColor: "#c1c7d1",
              pointHighlightFill: "#fff",
              pointHighlightStroke: "rgba(220,220,220,1)",
              data: []
            },
            {
              label: "Paid Amounts",
              fillColor: "rgba(60,141,188,0.9)",
              strokeColor: "rgba(60,141,188,0.8)",
              pointColor: "#3b8bba",
              pointStrokeColor: "rgba(60,141,188,1)",
              pointHighlightFill: "#fff",
              pointHighlightStroke: "rgba(60,141,188,1)",
              data: []
            },
            {
              label: "Due Amounts",
              fillColor: "rgba(60,121,170,0.9)",
              strokeColor: "rgba(60,108,188,0.8)",
              pointColor: "#3b8bba",
              pointStrokeColor: "rgba(60,141,188,1)",
              pointHighlightFill: "#fff",
              pointHighlightStroke: "rgba(60,141,188,1)",
              data: []
            }
          ]
        };


         $scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-graph-data',
              data: {
                    'paid_unpaid_month_wise': true
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            var data = response.data.stockslist
            var months = [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December'
            ]
            for(var j in months){
                $.each(data, function(i){
                        //console.log(data[i], months[j])
                        if(data[i].month == months[j]){
                            console.log('yes', data[i].month)
                            areaChartData.labels.push(data[i].month)
                            areaChartData.datasets[0].data.push(data[i].total_price)
                            areaChartData.datasets[1].data.push(data[i].paid)
                            areaChartData.datasets[2].data.push(data[i].due)

                        }
                })
            }
            console.log(areaChartData)
            areaChart.Line(areaChartData, areaChartOptions);

         }, function(error){
            console.log('error', error)

         })
// -------------end of area chat ---------------

//---getting customers credit and debit------------
$scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-graph-data',
              data: {
                    'customers_credit_debit': true
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log('bills information', response)
            $timeout(function(){
                $("#example1").DataTable();
            },500)
            $scope.customer_pay_info = response.data.bills
         }, function(error){
            console.log('hellow')
         })

//---getting expired and expiring products ------------
$scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-graph-data',
              data: {
                    'expired_expiring_products': true
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log(' product_expired_data', response)
            $timeout(function(){
                $("#example2").DataTable();
            },500)
            $scope.product_expired_data = response.data.info
         }, function(error){
            console.log('hellow')
         })

//---getting low quantity products ------------
$scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-graph-data',
              data: {
                    'low_quantity_avaible_products': true
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log(' product_expired_data', response)
            $timeout(function(){
                $("#example3").DataTable();
            },500)
            $scope.low_product_data = response.data.stock
         }, function(error){
            console.log('hellow')
         })

//---getting count of dashboard  ------------
$scope.load =
         $http({
              method: 'post',
              url: '/superuser/get-graph-data',
              data: {
                    'counts_number': true
              },
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
         }).then(function (response){
            console.log(' product_expired_data', response)

            $scope.counts = response.data.counts
         }, function(error){
            console.log('hellow')
         })
})




.controller("modifySpecificCustomerBillingProducts", function($http,$location,$localStorage, $q, $timeout,toastr,$route, $scope){

	if($localStorage.customer == undefined){
       toastr.error('something went wrong...')
       $location.path('/billing-customers')
    }

    if($localStorage.bill_id == undefined){
        toastr.error('something went wrong...')
        $location.path('/billing-customers')

    }
    else{
        console.log($localStorage.customer)
    }


     $scope.calculateQuantity = function(){
        var dt = $scope.products_list;
        var tq = 0;
         for(var j in dt){
            console.log(dt[j])
            tq = tq + parseFloat(dt[j]['product_quantity']);
         }

        $scope.bill.quantity = tq;
        console.log($scope.bill.quantity)
     }

     $scope.calculatePrice = function(){

        var dt = $scope.products_list;

        var price = 0;

        for(var j in dt){
           price = price + parseFloat(dt[j]['product_price']);
        }
         $scope.bill.price = price;
     }

     $scope.calculateDue = function(){
        $scope.bill.due = parseFloat($scope.bill.price) - parseFloat($scope.bill.paid)

     }



    $scope.addToReturns = function(product, status){
        for(var temp in $scope.products_list){
                if($scope.products_list[temp].bill_product_number == product.bill_product_number){
                    console.log('matched')
                    $scope.products_list[temp].isReturned = status;
                    break;
                }
        }
        console.log($scope.products_list)
        $scope.load = $http({
	  		method: 'put',
			  url: '/superuser/bill-management',
			  data: {
			    'bill_product_number': product.bill_product_number,
			    'status': status
			  }
			})
			.then(function (response){
				    toastr.success(response.data.response)
			}, function(error){
			    toastr.success(response.data.response)
			})

    }

    $scope.updateBill = function(){
        console.log($scope.bill)
        $scope.load = $http({
	  		method: 'put',
			  url: '/superuser/bill-management',
			  data: {
			    'product_details':$scope.products_list,
			    'bill_details': $scope.bill

			  }
			})
			.then(function (response){
				    toastr.success(response.data.response)
				    $location.path('/modify-billing')
			}, function(error){
			    toastr.success(error)
			})


    }

	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/bill-management',
			  params: {
			    'billId': $localStorage.bill_id
			  }
			}).then(function (response)
				{

				    $scope.bill = {}
		    		var bills_data = JSON.parse(response.data.bill_info)
		    		console.log('bills data is', bills_data)



		    	    $scope.bill.bill_id = bills_data[0].pk
                    $scope.bill.customerId = bills_data[0].fields.customer
                    $scope.bill.bill_date = new Date(bills_data[0].fields.bill_date)

                    $scope.bill.quantity = bills_data[0].fields.total_quantity
                    $scope.bill.price = bills_data[0].fields.total_price
                    $scope.bill.paid = bills_data[0].fields.total_paid
                    $scope.bill.due = bills_data[0].fields.due


                    $scope.bill.bill_date = new Date(bills_data[0].fields.bill_date)
                    $scope.bill.bill_date = new Date(bills_data[0].fields.bill_date)

                    $scope.customers = JSON.parse(response.data.customers)
                    var temp_customers = []
		    	    $.each($scope.customers, function(i){
		    	        var obj = {}
		    	        obj.name = $scope.customers[i].fields.first_name+" "+$scope.customers[i].fields.last_name
		    	        obj.id = $scope.customers[i].pk
		    	        temp_customers.push(obj)
		    	    })
		    	    $scope.customers = temp_customers;

                    $scope.products_list = []
		    		var products =  response.data.product_list

		    		$.each(products, function(i){
                        var obj = {};
                        obj.product_id = products[i].product_id;
                        obj.product_name = products[i].product_name;
                        obj.product_price = products[i].product_price;
                        obj.product_quantity =  products[i].product_quantity;
                        obj.bill_product_number = products[i].bill_product_id
                        obj.isReturned = products[i].isReturned

                        $scope.products_list.push(obj);

                        $timeout(function(){
                            $("#example1").DataTable();
                        },500)
                    })
                    console.log($scope.products_list)


				}, function errorCallback(response)
				{
		    		console.log(response);
				});




})

.controller("modifySpecificCustomerBilling", function($http,$localStorage, $q, $timeout,toastr,$route, $scope){

	if($localStorage.customer == undefined){
       $location.path('/billing-customers')
    }else{
        console.log($localStorage.customer)
    }

    $scope.setBillId = function(bill_id){
        $localStorage.bill_id = bill_id;
        console.log('setting bill id', $localStorage.bill_id)
    }

    $scope.deleteBill = function(bill_id){
        $scope.delete_bill_id = bill_id
         $("#myModal2").modal("show");
    }

    $scope.confirmDeleteBill = function(){

        $scope.load = $http({
                                method: 'post',
                                url: '/superuser/delete-bill',
                                data: {'bill_id': $scope.delete_bill_id },
                                headers: {
                                    'Content-Type': 'application/x-www-form-urlencoded'
                                }
                            })
                            .then(function successCallback(response){
                                        toastr.success('successfully deleted')
                                        $("#myModal2").modal("hide");
                                        $timeout(function(){
                                          $route.reload()
                                        },2000)
                            }, function errorCallback(response)
                            {
                                toastr.success('unable to  updated')
                                // console.log("not sent");
                            });



     }


	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/bill-management',
			  params: {
			    'customerId': $localStorage.customer.userid
			  }
			}).then(function (response)
				{
		    		$scope.bills_list_array = [];

		    		var bills_data = JSON.parse(response.data.bills_list);

		    		console.log(bills_data)

		    		$.each(bills_data, function(i){
                        var obj = {};
                        obj.bill_id = bills_data[i].pk;

                        obj.total_price = bills_data[i].fields.total_price;
                        obj.total_quantity =  bills_data[i].fields.total_quantity;
                        obj.total_products =  bills_data[i].fields.products_list.length;
                        obj.total_paid =  bills_data[i].fields.total_paid;
                        obj.due =  bills_data[i].fields.due;
                        obj.bill_date =  bills_data[i].fields.bill_date;

                        $scope.bills_list_array.push(obj);
                        console.log($scope.bills_list_array, '------------')
                        $timeout(function(){
                            $("#example1").DataTable();
                        },500)
                    })
				}, function errorCallback(response)
				{
		    		console.log(response);
				});




})
.controller("finishCreateSaleCtrl", function($http,$localStorage, $q,$location,
                                             $timeout,toastr,$route, $scope){
        $scope.user = $localStorage.customer;
        console.log($scope.user, 'finsih')
        $scope.selectedProductsList = $localStorage.selectedItems
        $scope.total_price = $localStorage.total_price;
        $scope.total_quantity = $localStorage.total_quantity;
        $scope.amount_paid = $localStorage.amount_paid;
        $scope.due = $scope.total_price - $scope.amount_paid;
        console.log($scope.user)
        $scope.saveBill = function(){

            var data = {
                'products': $scope.selectedProductsList,
                'total_price': $scope.total_price,
                'total_quantity': $scope.total_quantity,
                'amount_paid': $scope.amount_paid,
                'due': $scope.due,
                'customerId': $scope.user.userid
            }

            $scope.load =
            $http({
                method: 'post',
                url: '/superuser/bill-management',
                data: data,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function successCallback(response){
                        $localStorage.$reset();
                        toastr.success('successfully created....')
                        $location.path('/billing-customers')
            }, function errorCallback(response)
            {
                toastr.error('unable to create bill')
                // console.log("not sent");
            });

        }


})

.controller("manageBillingController", function($http,$localStorage, $q, $timeout,toastr,$route, $scope){

	$scope.setUserId = function(user){
            $localStorage.customer =  user
    }

    $scope.deleteAllBills = function(customer_id){
        console.log(customer_id)
        $scope.deleteAllBillsCustomerId = customer_id
        $("#myModal3").modal("show");
    }

    $scope.confirmDeleteAllBills = function(){

        $scope.load =
        $http({
                method: 'post',
            url: '/superuser/delete-bill',
            data: {'customer_id': $scope.deleteAllBillsCustomerId },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(function successCallback(response){
                    toastr.success('successfully deleted')
                    $("#myModal3").modal("hide");
                    $timeout(function(){
                      $route.reload()
                    },2000)
        }, function errorCallback(response)
        {   console.log(response)
            toastr.error('unable to  updated')
            // console.log("not sent");
        });
    }

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



})




.controller("enterQuantityPriceCtrl", function ($scope, $http, $q,$location,toastr,
                                        $timeout, $route, toastr, $localStorage){
        $scope.amount_paid = 0;
        console.log('enter quantity and price ctrl')
        $scope.selectedProductsList = $localStorage.selectedItems

         var dt = $scope.selectedProductsList;

         for(var j in dt){
            console.log('selected item details', dt)
            $scope.selectedProductsList[j]['quantity'] = '';
            $scope.selectedProductsList[j]['price'] = ''

         }
         console.log($scope.selectedProductsList)

         $scope.submitRateQuantity = function(){
                $localStorage.selectedItems =$scope.selectedProductsList
                $localStorage.amount_paid = $scope.amount_paid;
                $location.path('/finsh-create-sale')
         }
         $scope.calculateQuantity = function(){
            var dt = $scope.selectedProductsList;
            $scope.total_quantity = 0;
             for(var j in dt){
                if(dt[j].quantity > dt[j].avaible_stock){
                    toastr.error('stock not available.....')
                    dt[j].quantity = 0;
                    dt[j].price = 0;

                }
                $scope.total_quantity = $scope.total_quantity + $scope.selectedProductsList[j]['quantity'];
                dt[j].price = dt[j].item_cost * dt[j].quantity
             }
            $localStorage.total_quantity = $scope.total_quantity;
            $scope.calculatePrice();

         }

         $scope.calculatePrice = function(){
            var dt = $scope.selectedProductsList;
            $scope.total_price = 0;
             for(var j in dt){
                $scope.total_price = $scope.total_price + $scope.selectedProductsList[j]['price'];
             }
             $localStorage.total_price = $scope.total_price;
         }

         console.log(this.amount_paid, $scope.amount_paid)

})
.controller("selectItemsController", function ($scope, $http, $q,$location,toastr,
                                        $timeout, $route, toastr, $localStorage){


 $scope.processed = function(){

    $localStorage.selectedItems = $scope.output_temp_array
    console.log('selected Item', $localStorage.selectedItems)
    $location.path("/enter-quantity-price")
 }

 $scope.load =
               $http({
                      method: 'get',
                      url: '/superuser/stock-list',
                      headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'}
               }).then(function (response)
                {   var data = JSON.parse(response.data.stockslist)
                    console.log(data)
                    $scope.input_temp_array = []
                    for(var i in data){
                        var obj = {}
                        obj.name = data[i].fields.item_name
                        obj.type = data[i].fields.item_type

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

