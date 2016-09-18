var App = angular.module('App')
.controller('changePasswordCtrl', function($scope, $auth,$http,toastr,  $location,$rootScope) {
     $scope.change_password = function() {
            $scope.load = $http({
                  method: 'post',
                  url: '/auth/change-password',
                  data: {'new_password': $scope.new_password},
                  headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function (response){
                toastr.success('successfully changed')
                $location.path("/")
            }, function(error){
                console.log('hellow')
                toastr.error('failed to change')
            })
     }
})
.controller('loginController', function ($localStorage,$scope, $auth, $location, $alert,$rootScope) {

    // login with facebook or google
    $scope.authenticate = function(provider) {
        $auth.authenticate(provider)
            .then(function(response) {
                console.log('response is ->>>', response);
                $auth.setToken(response.data.token);
                $localStorage.counter = response.data.role

                $location.path('/dashboard');
            })
            .catch(function(response) {
                // Something went wrong.
                console.log('error is ->>', response);
            });
    };// end

     $scope.login = function($localStorage, $rootScope) {
        $scope.load = $auth.login($scope.user)
            .then(function(response) {
                // Redirect user here after a successful log in.
            //console.log(response.data.role, response.data.token)
                
                $auth.setToken(response.data.token);

                localStorage.setItem('role',response.data.role);
                

                if (response.data.role == "admin" || response.data.role == "subadmin"){
                    //$location.path('/dashboard')
                    window.location.reload();
                }else{
                    console.log('invalid role')
                }
            })
            .catch(function(response) {
                $alert({
                    title: response.data.response,
                    placement: 'top', type: 'danger',
                    show: true
                });
                // Handle errors here, such as displaying a notification
                // for invalid email and/or password.
            });
    };// end

    $scope.signup = function() {
        $scope.load = $auth.signup($scope.user).then(function(response) {
            // Redirect user here after a successful log in.

            $scope.master = {};
            $scope.myForm = angular.copy($scope.master);

            $alert({
                title: "Details saved successfully, We'll keep you updated!",
                placement: 'top', type: 'success',
                show: true
            });
            console.log(response);
            $scope.user = {};
            // $location.path('/home');
        }, function(err) {
            console.log(err)
            $alert({
                title: err.data.err,
                placement: 'top', type: 'danger',
                show: true
            });
        })
    }; // end

})
.controller('authCtrl', function($scope, $auth,$http, $window, $location,$rootScope) {



        $scope.isAuthenticated = function() {
            return $auth.isAuthenticated();
        };

        /*$rootScope.get_expired_notification = function(){
             if($scope.isAuthenticated()){
                 $scope.load =
                 $http({
                      method: 'post',
                      url: '/superuser/get-graph-data',
                      data: {
                            'notification_data': true
                      },
                      headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                 }).then(function (response){
                    $rootScope.data = {}
                    $rootScope.data['server_data'] = response.data.info;
                    $rootScope.notification_ids = []
                    $.each($rootScope.data['server_data'], function(i){
                        $rootScope.notification_ids.push($rootScope.data['server_data'][i].stock_id)
                    })
                    console.log($rootScope.notification_ids, 'server data')

                 }, function(error){
                    console.log('hellow')
                 })
            }
        }*/

        /*$rootScope.get_detailed_notifications = function(){
            console.log($rootScope.notification_ids, '---------------')
            var get_ids =  $rootScope.notification_ids
            var data = {}
            data['get_details_of_notifications'] = true
            if(get_ids.length){
                data['notification_ids'] = get_ids
            }

            $scope.load =
            $http({
                  method: 'post',
                  url: '/superuser/get-graph-data',
                  data: data,
                  headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function (response){
                console.log(' notification data', response.data.info)
                $rootScope.data = {}
                $rootScope.data['server_data'] = response.data.info;
            }, function(error){
                console.log('hellow')
            })

        }
*/
        //$rootScope.get_expired_notification();


        $scope.role=localStorage.getItem("role")

        $scope.logout = function() {
            $scope.load =
            $http({
                  method: 'post',
                  url: '/auth/logout',
                  headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function (response){
                localStorage.removeItem("role")
                localStorage.removeItem("store_id")
                localStorage.removeItem("customer_id")
                $auth.logout();
                $location.path('/')

                //$location.reload()
            }, function(error){
                console.log('hellow')
            })
        }



        $scope.goto = function(path){
            $location.path(path)
        }

});

angular.module('UserValidation', []).directive('validPasswordC', function () {
    return {
        require: 'ngModel',
        link: function (scope, elm, attrs, ctrl) {
            ctrl.$parsers.unshift(function (viewValue, $scope) {
                var noMatch = viewValue != scope.myForm.password.$viewValue
                ctrl.$setValidity('noMatch', !noMatch)
            })
        }
    }
});