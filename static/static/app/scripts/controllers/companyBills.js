

angular.module("App")
.controller("addCompanyBillCtrl", function ($scope,$location,$timeout,Upload, $q, $http, $alert, toastr){


    $timeout(function(){
        $('#datepicker_invoice_date') .datepicker({
            format: 'dd/mm/yyyy'
        })
    },500)

     $scope.uploadPic = function(file) {

            file.upload = Upload.upload({
              url: '/superuser/company-bill',
              data: {
                company_name: $scope.company.company_name,
                company_invoice: $scope.company.invoice_number,
                file: file,
                invoice_date: $scope.company.invoice_date,
                tin_number: $scope.company.tin_number
                },
            });

            $scope.load = file.upload.then(function (response) {
                //$timeout(function(){
                    toastr.success('successfully created...')
                    $location.path('/company-bills')

                //},1000)
            }, function (response) {
               console.log(response)
               toastr.error('failed to created...')
            }, function (evt) {
              // Math.min is to fix IE which reports 200% sometimes
              file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
            });

     }

})

.controller("addGalleryImageCtrl", function ($scope,$location,$timeout,Upload, $q, $http, $alert, toastr){



     $scope.uploadPic = function(file) {

            file.upload = Upload.upload({
              url: '/superuser/gallery-image',
              data: {file: file}
            });

            file.upload.then(function (response) {
                $timeout(function(){
                    toastr.success('successfully created...')
                    $location.path('/gallery-images')

                },1000)
            }, function (response) {
               console.log(response)
               toastr.error('failed to created...')
            }, function (evt) {
              // Math.min is to fix IE which reports 200% sometimes
              file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
            });

     }

})


.controller("companyBillingController", function($http,$localStorage, $q, $timeout,toastr,$route, $scope, Upload){


    $scope.viewBillData = function(bill, modal){
        $scope.model_bill_data = bill;
        $("#myModal"+modal).modal("show");
	}

    $scope.deleteCompanyBills = function(bill_id){
        $scope.deleteCompanyBillId = bill_id
        $("#myModal3").modal("show");
    }

    $timeout(function(){
        $('#datepicker_invoice_date') .datepicker({
            format: 'dd/mm/yyyy',
            startDate: new Date(),
            endDate: '01/12/2020'
        })
    })

    $scope.viewBill = function(){
        $("#myModal2").modal("show");
    }

    $scope.updateBillInformation  = function(changedPic){
         console.log($scope.model_bill_data, '--------', changedPic)
         var data = {
                   company_name: $scope.model_bill_data.company_name,
                   company_invoice: $scope.model_bill_data.bill_number,
                   bill_id: $scope.model_bill_data.bill_id,
                   invoice_date: $scope.model_bill_data.invoice_date,
                   tin_number: $scope.model_bill_data.tin_number
              }
         if(changedPic){
            data.file = changedPic
         }

         var uploaded = Upload.upload({
              url: '/superuser/company-bill',
              method: 'post',
              data:data

         });

         uploaded.then(function (response) {
           $timeout(function () {
                    toastr.success('successfully updated')
                    $("#myModal2").modal("hide");
                    $timeout(function(){
                        $route.reload()
                    },1000)
           });
         }, function (response) {
                   console.log(response)
                   toastr.error('unable to  updated')
         }, function (evt) {
            // Math.min is to fix IE which reports 200% sometimes
            //changedPic.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
         });
    }

    $scope.confirmDeleteCompanyBills = function(){


            $scope.load = $http({
                method: 'post',
            url: '/superuser/delete-company-bill',
            data: {'bill_id': $scope.deleteCompanyBillId },
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
        }, function errorCallback(response){
            console.log(response)
            toastr.error('unable to  updated')
            // console.log("not sent");
        });
    }

	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/company-bill',
			}).then(function (response){
		    		$scope.billsList = [];
		    		console.log(response, '0000000')
		    		var blist = JSON.parse(response.data.bills_list);

		    		$.each(blist, function(i){
                        var obj = {};
                        obj.bill_id = blist[i].pk;
                        obj.company_name = blist[i].fields.company_name;
                        obj.bill_number = blist[i].fields.company_invoice_number;
                        obj.invoice_date = blist[i].fields.invoice_date;
                        obj.tin_number = blist[i].fields.company_tin_number;
                        obj.bill_image = process_image_path(blist[i].fields.bill_image);

                        $scope.billsList.push(obj);
                        $timeout(function(){
                            $("#example1").DataTable();
                        },500)
                    })
			}, function errorCallback(response){
		    		console.log(response);
			});




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


.controller("galleryImagesCtrl", function($http,$localStorage, $q, $timeout,toastr,$route, $scope, Upload){

    function process_gallery_image_path(path){
        var image_path = path.split('/')
        console.log('path is ', image_path[image_path.length-1])
        return 'static/upload_gallary_images/'+image_path[image_path.length-1]

    }


    $scope.viewImageData = function(image, modal){
        $scope.model_image_data = image;
        $("#myModal"+modal).modal("show");
	}

    $scope.deleteGalleryImage = function(image_id){
        $scope.deleteGalleryImageId = image_id
        $("#myModal3").modal("show");
    }



    $scope.viewBill = function(){
        $("#myModal2").modal("show");
    }

    $scope.updateImage  = function(changedPic){
         var data = {
                   image_id: $scope.model_image_data.image_id
              }
         if(changedPic){
            data.file = changedPic
         }

         var uploaded = Upload.upload({
              url: '/superuser/gallery-image',
              method: 'post',
              data:data

         });

         uploaded.then(function (response) {
           $timeout(function () {
                    toastr.success('successfully updated')
                    $("#myModal2").modal("hide");
                    $timeout(function(){
                        $route.reload()
                    },500)
           });
         }, function (response) {
                   console.log(response)
                   toastr.error('unable to  updated')
         }, function (evt) {
            // Math.min is to fix IE which reports 200% sometimes
            //changedPic.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
         });
    }

    $scope.confirmDeleteGalleryImage = function(){

        $scope.load =
        $http({
                method: 'post',
            url: '/superuser/delete-gallery-image',
            data: {'image_id': $scope.deleteGalleryImageId },
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(function successCallback(response){
                    toastr.success('successfully deleted')
                    $("#myModal3").modal("hide");
                    $timeout(function(){
                      $route.reload()
                    },500)
        }, function errorCallback(response){
            console.log(response)
            toastr.error('unable to  updated')
            // console.log("not sent");
        });
    }

	$scope.load = $http({
	  		method: 'GET',
			  url: '/superuser/gallery-image',
			}).then(function (response){
			        console.log('response iamges', response)
		    		$scope.tempImages = [];
		    		var imagesList = JSON.parse(response.data.gallery_images);

		    		$.each(imagesList, function(i){
                        var obj = {};
                        obj.image_id = imagesList[i].pk;
                        obj.gallery_image = process_gallery_image_path(imagesList[i].fields.gallery_image);

                        $scope.tempImages.push(obj);
                        $timeout(function(){
                            $("#example1").DataTable();
                        },500)
                    })

			}, function errorCallback(response){
		    		console.log(response);
			});

})


