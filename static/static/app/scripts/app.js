var App = angular.module('App', [
            'ngRoute',
            'cgBusy',
            'ngAnimate',
            'satellizer',
             'UserValidation',
             'mgcrea.ngStrap',
             'ngStorage',
             'toastr',
             'isteven-multi-select',
             'ngMaterial',
             'ngFileUpload',
             'jkuri.gallery'
             ]);

App.config(function($httpProvider) {
    $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
    $httpProvider.defaults.headers.put['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
    $httpProvider.defaults.headers.patch['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
    //$httpProvider.defaults.headers['delete']['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();


});
App.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

App.config(function(toastrConfig) {
  angular.extend(toastrConfig, {
    allowHtml: false,
    closeButton: false,
    closeHtml: '<button>&times;</button>',
    extendedTimeOut: 1000,
    iconClasses: {
      error: 'toast-error',
      info: 'toast-info',
      success: 'toast-success',
      warning: 'toast-warning'
    },
    messageClass: 'toast-message',
    onHidden: null,
    onShown: null,
    onTap: null,
    progressBar: true,
    tapToDismiss: true,
    templates: {
      toast: 'directives/toast/toast.html',
      progressbar: 'directives/progressbar/progressbar.html'
    },
    timeOut: 3000,
    titleClass: 'toast-title',
    toastClass: 'toast'
  });
});

App.config(function($authProvider) {
    $authProvider.facebook({
        clientId: '1566678290273052'
    });

    $authProvider.google({
        clientId: '787091751000-iat8i189qa2qgkn4vor0ae1u2vaf10tl.apps.googleusercontent.com'
    });

    $authProvider.linkedin({
        clientId: '75qhzn82g3tfk2'
    });

    // Facebook
    $authProvider.facebook({
        name: 'facebook',
        url: '/auth/facebook',
        authorizationEndpoint: 'https://www.facebook.com/v2.5/dialog/oauth',
        redirectUri: window.location.origin + '/',
        requiredUrlParams: ['display', 'scope'],
        scope: ['email'],
        scopeDelimiter: ',',
        display: 'popup',
        type: '2.0',
        popupOptions: { width: 580, height: 400 }
    });

    // Google
    $authProvider.google({
        url: '/auth/google',
        authorizationEndpoint: 'https://accounts.google.com/o/oauth2/auth',
        redirectUri: window.location.origin,
        requiredUrlParams: ['scope'],
        optionalUrlParams: ['display'],
        scope: ['profile', 'email'],
        scopePrefix: 'openid',
        scopeDelimiter: ' ',
        display: 'popup',
        type: '2.0',
        popupOptions: { width: 452, height: 633 }
    });

    // Twitter
    $authProvider.twitter({
        url: '/auth/twitter',
        authorizationEndpoint: 'https://api.twitter.com/oauth/authenticate',
        redirectUri: window.location.origin,
        type: '1.0',
        popupOptions: { width: 495, height: 645 }
    });

    // LinkedIn
    $authProvider.linkedin({
      url: '/auth/linkedin',
      authorizationEndpoint: 'https://www.linkedin.com/uas/oauth2/authorization',
      redirectUri: window.location.origin,
      requiredUrlParams: ['state'],
      scope: ['r_emailaddress'],
      scopeDelimiter: ' ',
      state: 'STATE',
      type: '2.0',
      popupOptions: { width: 527, height: 582 }
    });
});

App.config(function($routeProvider, $authProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/app/views/login.html',
            controller: 'loginController',
            resolve: {
                authenticated: function($location, $auth) {
                    if ($auth.isAuthenticated()) {
                        return $location.path('/dashboard');
                    }
                }
            }
        })
        .when('/signup', {
            templateUrl: '/static/app/views/signup.html',
            controller: 'loginController',
            resolve: {
                authenticated: function($location, $auth) {
                    if ($auth.isAuthenticated()) {
                        return $location.path('/home');
                    }
                }
            }
        })
        .when('/add-stock', {
            templateUrl: '/static/app/views/admin/add-stock.html',
            controller : "addStockController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/create-company-bill', {
            templateUrl: '/static/app/views/admin/add-company-bill.html',
            controller : "addCompanyBillCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

         .when('/uplpad-gallery-image', {
            templateUrl: '/static/app/views/admin/add-gallery-image.html',
            controller : "addGalleryImageCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/create-user', {
            templateUrl: '/static/app/views/admin/create-user.html',
            controller : "createUserCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/create-customer', {
            templateUrl: '/static/app/views/admin/create-customer.html',
            controller : "createCustomerCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/dashboard', {
            templateUrl: '/static/app/views/admin/dashboard.html',
            controller: 'dashBoardCtrl',
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        console.log('not authenticated', $auth.isAuthenticated())
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/modify-stock', {
            templateUrl: '/static/app/views/admin/modifyStock.html',
            controller: "modifyStockCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/edit-stock-details/:stockId', {
            templateUrl: '/static/app/views/admin/editStock.html',
            controller : "editStockController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

       .when('/create-notification', {
            templateUrl: '/static/app/views/admin/create-notification.html',
            controller : "notificationController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/view-modify-users', {
            templateUrl: '/static/app/views/admin/modifyUsers.html',
            controller : "editUsersController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/view-modify-customers', {
            templateUrl: '/static/app/views/admin/modifyCustomers.html',
            controller : "editCustomerController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/billing-customers', {
            templateUrl: '/static/app/views/admin/BillingCustomers.html',
            controller : "manageBillingController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

         .when('/company-bills', {
            templateUrl: '/static/app/views/admin/companyBills.html',
            controller : "companyBillingController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

         .when('/gallery-images', {
            templateUrl: '/static/app/views/admin/galleryImages.html',
            controller : "galleryImagesCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })


        .when('/select-items', {
            templateUrl: '/static/app/views/admin/select-items.html',
            controller : "selectItemsController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/enter-quantity-price', {
            templateUrl: '/static/app/views/admin/enter-quantity-price.html',
            controller : "enterQuantityPriceCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/finsh-create-sale', {
            templateUrl: '/static/app/views/admin/finish-create-sale.html',
            controller : "finishCreateSaleCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/print-bill', {
            templateUrl: '/static/app/views/admin/print-bill.html',
            /*controller : "finishCreateSaleCtrl",*/
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/gallery', {
            templateUrl: '/static/app/views/admin/gallery.html',
            controller : "GalleryCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/profile', {
            templateUrl: '/static/app/views/admin/profile.html',
            /*controller : "GalleryCtrl",*/
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })


        .when('/modify-billing', {
            templateUrl: '/static/app/views/admin/modifyBilling.html',
            controller : "modifySpecificCustomerBilling",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/get-bill-edit-products', {
            templateUrl: '/static/app/views/admin/edit-bill-products.html',
            controller : "modifySpecificCustomerBillingProducts",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/404', {
            templateUrl: '/static/app/views/404.html'
        })


        .otherwise({
            redirectTo: '/404'
        });
});