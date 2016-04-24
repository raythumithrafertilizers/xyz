var app = angular.module('myApp', []);

app.controller('NewTableCtrl', function($scope) {
  
  $scope.table = { fields: [], values : [] };

  $scope.addFormField = function() {
    $scope.table.fields.push('');
    $scope.table.values.push('');
  }

  $scope.submitTable = function() {
    console.log($scope.table);
  }
  
});