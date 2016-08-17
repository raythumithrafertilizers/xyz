angular.module("App")
.controller("payAdvancesCtrl", function($http,$location,$localStorage, $q, $timeout,toastr,$route, $scope){


        $scope.load = $http({
                        method: 'get',
                        url: '/superuser/get-persons',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'}
                    }).then(function successCallback(response){
                                console.log(response)
                                $scope.user = {}
                                var basic_info = response.data.response;
                                var data = response.data.users

                                $scope.user['quantity'] = basic_info['quantity']
                                $scope.user['quality'] = basic_info['quality']

                                $scope.user['purchase_id'] = $routeParams.purchase_id

                                $scope.user['harvester_total_payment'] = basic_info['harvester_amount']
                                $scope.user['harvester_advance'] = basic_info['harvester_advance']
                                $scope.user['harvester_rate_per_ton'] = basic_info['harvester_rate_per_ton']

                                $scope.user['farmer_rate_per_ton'] = basic_info['farmer_rate_per_ton']
                                $scope.user['farmer_total_payment'] = basic_info['farmer_amount']
                                $scope.user['farmer_advance'] = basic_info['farmer_advance']

                                $scope.input_temp_array = []
                                for(var i in data){
                                    var obj = {}
                                    obj.name = data[i].name
                                    obj.type = data[i].type
                                    obj.userid = data[i].userid
                                    obj.ticked = data[i].ticked

                                    $scope.input_temp_array.push(obj)
                                }





                    }, function errorCallback(response)
                    {
                        toastr.error('unable to  updated')
                        // console.log("not sent");
                    });

})