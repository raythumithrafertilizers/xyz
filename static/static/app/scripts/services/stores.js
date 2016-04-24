var app = angular.module('App', []);
    
app.factory('storeFactory', function($http){
    var getStores = function(){
    	$http({
	  		method: 'GET',
			  url: '/superuser/storeslist',
			}).then(function (response) 
				{
		    		this.storelist = [];
		    		var self = this;
		    		var storedata = JSON.parse(response.data.storeslist);
		    		console.log(storedata);
		    		/*$.each(storedata, function(i){
				    			var obj = {};
				    			obj.sid = storedata[i].pk;
				    			obj.sname = storedata[i].fields.storeName;
				    			obj.email =  storedata[i].fields.email;
				    			obj.phone = storedata[i].fields.phone;
				    			obj.storeobj = storedata[i].fields.storeId;
				    			self.storelist.push(obj);
				    			$timeout(function(){
								 $("#example1").DataTable();
								},500)
				    		})*/
				}, function errorCallback(response) 
				{
		    		console.log(response);
				});

    }    

    return getStores         
});