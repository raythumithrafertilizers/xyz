function process_image_path(path){
    var image_path = path.split('/')
    console.log('path is ', image_path[image_path.length-1])
    return 'static/uploads/'+image_path[image_path.length-1]

}
angular.module("App")
.controller("getBillCtrl", function($http,$location,$localStorage, $q, $timeout,toastr,$route, $scope){
    $scope.getting_bill = function(){
        $scope.load =
        $http({
                method: 'POST',
                url: '/superuser/get-bill-by-number',
                data: {'bill_id': $scope.bill_number}
        }).then(function (response){
                    $location.path("/print-bill/"+$scope.bill_number)
        }, function errorCallback(response){
                    toastr.error('bill not found')
        });


    }

})


.controller("printBillCtrl", function($http, $q,$location,$routeParams,
                                             $timeout,toastr,$route, $scope){
            console.log($routeParams.bill_id)
            $scope.load =
            $http({
                method: 'post',
                url: '/superuser/print-bill',
                data: {'bill_id':$routeParams.bill_id},
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(function successCallback(response){

                        $scope.bill_info = response.data.data;
                        console.log($scope.bill_info)

                        if(response.data.data['due']){
                            $scope.bill_type_display = "CREDIT"
                        }else{
                            $scope.bill_type_display = "CASH"
                        }


            }, function errorCallback(response)
            {
                toastr.error('unable to create bill')
                // console.log("not sent");
            });







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

     $timeout(function(){
            $('#datepicker_sale_products_reports_1') .datepicker({
                format: 'dd/mm/yyyy',
                //startDate: new Date()
                //endDate: '01/12/2020'
            })
        },500)

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

     /*$scope.calculatePrice = function(){

        var dt = $scope.products_list;

        var price = 0;

        for(var j in dt){
           price = price + parseFloat(dt[j]['product_price']);
        }
         $scope.bill.price = price;
     }*/

     $scope.calculateDue = function(){
        $scope.bill.due = parseFloat($scope.bill.price) - parseFloat($scope.bill.paid)

     }



    /*$scope.addToReturns = function(product, status){
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

    }*/

    $scope.updateBill = function(){
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

                    $scope.bill.vehicle_number = bills_data[0].fields.vehicle_number
                    $scope.bill.contact_number = bills_data[0].fields.contact_number
                    $scope.bill.remarks = bills_data[0].fields.remarks

                    $scope.bill.vat_percentage = bills_data[0].fields.vat_percentage
                    $scope.bill.vat_money = bills_data[0].fields.vat_money

                    var pda= bills_data[0].fields.bill_date.split("-")
                    $scope.bill.bill_date = pda[2]+"/"+pda[1]+"/"+pda[0]

                    //$scope.bill.bill_date = new Date(bills_data[0].fields.bill_date)
                    //$scope.bill.bill_date = new Date(bills_data[0].fields.bill_date)

                    $scope.customers = JSON.parse(response.data.customers)
                    var temp_customers = []
		    	    $.each($scope.customers, function(i){

		    	        var obj = {}
		    	        obj.name = $scope.customers[i].fields.name
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
                        obj.per_kg_price = products[i].per_kg_price;
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
        console.log('customer is ', $localStorage.customer)
        $scope.selectedProductsList = $localStorage.selectedItems

        $scope.total_quantity = $localStorage.total_quantity;
        $scope.amount_paid = $localStorage.amount_paid;
        $scope.vat = $localStorage.vat;

        $scope.vehicle_number = $localStorage.vehicle_number
        $scope.contact_number = $localStorage.contact_number
        $scope.remarks = $localStorage.remarks



        $scope.total_price = $localStorage.total_price;

        $scope.vat_money = ($scope.vat/100)*$scope.total_price

        $scope.total_price += ($scope.vat/100)*$scope.total_price

        $scope.due = $scope.total_price - $scope.amount_paid;

        $scope.saveBill = function(){

            var data = {
                'products': $scope.selectedProductsList,
                'total_price': $scope.total_price,
                'total_quantity': $scope.total_quantity,
                'vat_percentage': $scope.vat,
                'vat_money': $scope.vat_money,
                'amount_paid': $scope.amount_paid,
                'due': $scope.due,
                'customerId': $scope.user.userid,
                'bill_date': $localStorage.bill_date,
                'remarks': $scope.remarks,
                'contact_number': $scope.contact_number,
                'vehicle_number': $scope.vehicle_number
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
                        $location.path('/print-bill/'+response.data.bill_pk)
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
			  url: '/superuser/persons-list/customer',
			}).then(function (response)
				{
		    		$scope.userslist = [];
		    		var usersdata = response.data.userdata;
		    		$.each(usersdata, function(i){
                        var obj = {};
                        obj.userid = usersdata[i].user_id;
                        obj.username = usersdata[i].name;
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
        $scope.vat = 0.0
        $scope.selectedProductsList = $localStorage.selectedItems

         var dt = $scope.selectedProductsList;

          $timeout(function(){
                $('#datepicker_sale_products_reports_1') .datepicker({
                    format: 'dd/mm/yyyy',
                    //startDate: new Date()
                    //endDate: '01/12/2020'
                })
          },500)

         var ids = []
         for(var j in dt){
            ids.push($scope.selectedProductsList[j]['id'])
            $scope.selectedProductsList[j]['quantity'] = '';
            $scope.selectedProductsList[j]['price'] = ''
            $scope.selectedProductsList[j]['kgrate'] = ''

         }
         console.log(ids, '=============')
         $scope.load = $http({
                      method: 'post',
                      url: '/superuser/get_complete_stock_info',
                      data: {'ids':ids},
                      headers: {
                        'Content-Type': 'application/json'}
               }).then(function (response)
                {   var data = response.data.data

                    for(var i in data){
                        for(var j in $scope.selectedProductsList){
                            if($scope.selectedProductsList[j]['id'] == data[i]['id']){
                                $scope.selectedProductsList[j]['avaible_stock'] = data[i]['available_stock']
                                break;
                            }
                        }
                    }


                }, function errorCallback(response)
                {
                    toastr.error("user already exists!");
                });



         $scope.submitRateQuantity = function(){
                $localStorage.selectedItems =$scope.selectedProductsList
                $localStorage.amount_paid = $scope.amount_paid;
                $localStorage.vat = $scope.vat;
                $localStorage.bill_date = $scope.bill_date
                $localStorage.contact_number = $scope.contact_number
                $localStorage.vehicle_number = $scope.vehicle_number
                $localStorage.remarks = $scope.remarks
                $location.path('/finsh-create-sale')
         }
        $scope.calculateQuantity = function(){
            console.log('calculating', $scope.selectedProductsList)
            var dt = $scope.selectedProductsList;
            $scope.total_quantity = 0;

             for(var j in dt){
                if(dt[j].quantity > dt[j].avaible_stock){
                    toastr.error('stock not available.....')
                    dt[j].quantity = 0;
                    dt[j].price = 0;
                }
                $scope.total_quantity = $scope.total_quantity + $scope.selectedProductsList[j]['quantity'];

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

        



})
.controller("selectItemsController", function ($scope, $http, $q,$location,toastr,
                                        $timeout, $route, toastr, $localStorage){


 $scope.processed = function(){

    $localStorage.selectedItems = $scope.output_temp_array
    console.log('selected Item', $localStorage.selectedItems)
    $location.path("/enter-quantity-price")
 }

 $scope.load = $http({
                      method: 'get',
                      url: '/superuser/billing-stock-names',
                      headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'}
               }).then(function (response)
                {   var data = response.data.stock_names
                    console.log(data)
                    $scope.input_temp_array = []
                    for(var i in data){
                        var obj = {}
                        obj.name = data[i].name
                        obj.ticked = false
                        obj.id = data[i].id
                        $scope.input_temp_array.push(obj)
                    }


                }, function errorCallback(response)
                {
                    toastr.error("user already exists!");
                });



})

