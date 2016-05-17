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

App.config(function($routeProvider, $authProvider) {
    $routeProvider

          .when('/customer-payments/:customer_id', {
            templateUrl: '/static/app/views/admin/specific-customer-payments.html',
            controller: "specificCustomerPaymentsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })


          .when('/customer-payments', {
            templateUrl: '/static/app/views/admin/customer-payments.html',
            controller: "customerPaymentsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })
         .when('/get-bill', {
            templateUrl: '/static/app/views/admin/get-bill.html',
            controller: "getBillCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/product-sale-report', {
            templateUrl: '/static/app/views/admin/product_sale_report.html',
            controller: "productSaleCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

        .when('/invoice-bill-report', {
            templateUrl: '/static/app/views/admin/invoice_bill_report.html',
            controller: "invoiceBillReportsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })

       .when('/legal-category-sold-reports', {
            templateUrl: '/static/app/views/admin/legal_category_reports.html',
            controller: "legalCategoryProductCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })


        .when('/download-invoice-file', {
            templateUrl: '/static/app/views/admin/donwload_invoice_bill.html',
            controller: "downLoadInvoiceBillReportsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/download-legal-category-data', {
            templateUrl: '/static/app/views/admin/donwload_invoice_bill.html',
            controller: "legalCategoryReportsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })


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

        .when('/print-bill/:bill_id', {
            templateUrl: '/static/app/views/admin/print-bill.html',
            controller : "printBillCtrl",
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