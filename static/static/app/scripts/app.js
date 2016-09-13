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

            .when('/download-interest-reports', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadInterstReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })
            .when('/download-paid-money-reports', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadPaidReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-append-reports', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadAppendReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-remain-stock-reports', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadRemainAppendReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/create-expenditure', {
                templateUrl: '/static/app/views/admin/create_expenditure.html',
                controller: "createExpenditureCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/append-stock-reports', {
                templateUrl: '/static/app/views/admin/append_stock_report.html',
                controller: "append_stock_reports_ctrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/expenditure-reports', {
                templateUrl: '/static/app/views/admin/expenditure_reports.html',
                controller: "expenditureReportsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/interest-reports', {
                templateUrl: '/static/app/views/admin/interest_reports.html',
                controller: "interestCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

             .when('/edit-expenditures', {
                templateUrl: '/static/app/views/admin/edit_expenditures.html',
                controller: "editExpenditureCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })





            .when('/harvester-payments/:person_id/:harvester_name', {
                templateUrl: '/static/app/views/admin/specific-harvester-payments.html',
                controller: "specificHarvesterPaymentsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-customer-reports/:status', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadCustomerReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-expenditure-reports', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadExpenditureReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

             .when('/download-product-sale-reports/:status', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadProductSaleReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-harvester-reports/:status', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadHarvesterReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

            .when('/download-farmer-reports/:status', {
                templateUrl: '/static/app/views/admin/download_temp.html',
                controller: "downloadFarmerReports",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })



             .when('/farmer-interests', {
                templateUrl: '/static/app/views/admin/farmer-interests.html',
                controller: "farmerInterests",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

             .when('/edit-stock-names', {
                templateUrl: '/static/app/views/admin/edit-stock-names.html',
                controller: "editStockNamesController",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
             })


           .when('/harvester-payments', {
                templateUrl: '/static/app/views/admin/harvester-payments.html',
                controller: "harvesterPaymentsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
           })



            .when('/farmer-payments/:person_id/:farmer_name', {
                templateUrl: '/static/app/views/admin/specific-farmer-payments.html',
                controller: "specificFarmerPaymentsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })


           .when('/farmer-payments', {
                templateUrl: '/static/app/views/admin/farmer-payments.html',
                controller: "farmerPaymentsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
           })


            .when('/labour-payments/:person_id', {
                templateUrl: '/static/app/views/admin/specific-labour-payments.html',
                controller: "specificLabourPaymentsCtrl",
                resolve: {
                    authenticated: function($location, $auth) {
                        if (!$auth.isAuthenticated()) {
                            return $location.path('/');
                        }
                    }
                }
            })

           .when('/labour-payments', {
            templateUrl: '/static/app/views/admin/labour-payments.html',
            controller: "labourPaymentsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/edit-purchases/:purchase_id', {
            templateUrl: '/static/app/views/admin/edit-purchase.html',
            controller : "purchaseDetailsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/append-stock', {
            templateUrl: '/static/app/views/admin/append_stock.html',
            controller : "appendStockController",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/edit-purchases', {
            templateUrl: '/static/app/views/admin/edit-purchases.html',
            controller : "purchasesDetailsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })


          .when('/create-purchase', {
            templateUrl: '/static/app/views/admin/create-purchase.html',
            controller : "createPurchaseCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/edit-harvester', {
            templateUrl: '/static/app/views/admin/edit-harvester-details.html',
            controller : "editHarvesterDetailsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })



          .when('/create-harvester', {
            templateUrl: '/static/app/views/admin/create-harvester.html',
            controller : "createHarvesterCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

           .when('/add-former-sold-stock', {
            templateUrl: '/static/app/views/admin/add-farmer-sold-stock.html',
            controller : "addFarmerSoldStockCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/create-farmer', {
            templateUrl: '/static/app/views/admin/create-farmer.html',
            controller : "createFarmerCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/edit-farmer-details', {
            templateUrl: '/static/app/views/admin/farmers-details.html',
            controller : "editFarmerDetailsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/create-labour', {
            templateUrl: '/static/app/views/admin/create-labour.html',
            controller : "createLabourCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })

          .when('/edit-labour-details', {
            templateUrl: '/static/app/views/admin/labour-details.html',
            controller : "editLabourDetailsCtrl",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
          })




          .when('/customer-payments/:person_id/:customer_name', {
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

          .when('/change-password', {
            templateUrl: '/static/app/views/admin/change_password.html',
            controller: "changePasswordCtrl",
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
        .when('/farmers-report', {
            templateUrl: '/static/app/views/admin/farmer_reports.html',
            controller: "farmerReport",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/harvesters-report', {
            templateUrl: '/static/app/views/admin/harvester_reports.html',
            controller: "harvesterReport",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/customers-report', {
            templateUrl: '/static/app/views/admin/customer_reports.html',
            controller: "customerReport",
            resolve: {
                authenticated: function($location, $auth) {
                    if (!$auth.isAuthenticated()) {
                        return $location.path('/');
                    }
                }
            }
        })
        .when('/labours-report', {
            templateUrl: '/static/app/views/admin/labour_reports.html',
            controller: "labourReport",
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






        .when('/', {
            templateUrl: '/static/app/views/login.html',
            controller: 'loginController',
            resolve: {
                authenticated: function($location, $auth) {
                    if ($auth.isAuthenticated()) {
                        return $location.path('/create-purchase');
                    }
                }
            }
        })
       /* .when('/signup', {
            templateUrl: '/static/app/views/signup.html',
            controller: 'loginController',
            resolve: {
                authenticated: function($location, $auth) {
                    if ($auth.isAuthenticated()) {
                        return $location.path('/home');
                    }
                }
            }
        })*/
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