angular.module("cgBusy",[]),angular.module("cgBusy").factory("_cgBusyTrackerFactory",["$timeout","$q",function(a,b){return function(){var c={};c.promises=[],c.delayPromise=null,c.durationPromise=null,c.delayJustFinished=!1,c.reset=function(b){c.minDuration=b.minDuration,c.promises=[],angular.forEach(b.promises,function(a){a&&!a.$cgBusyFulfilled&&d(a)}),0!==c.promises.length&&(c.delayJustFinished=!1,b.delay&&(c.delayPromise=a(function(){c.delayPromise=null,c.delayJustFinished=!0},parseInt(b.delay,10))),b.minDuration&&(c.durationPromise=a(function(){c.durationPromise=null},parseInt(b.minDuration,10)+(b.delay?parseInt(b.delay,10):0))))},c.isPromise=function(a){var b=a&&(a.then||a.$then||a.$promise&&a.$promise.then);return"undefined"!=typeof b},c.callThen=function(a,c,d){var e;a.then||a.$then?e=a:a.$promise?e=a.$promise:a.denodeify&&(e=b.when(a));var f=e.then||e.$then;f.call(e,c,d)};var d=function(a){if(!c.isPromise(a))throw new Error("cgBusy expects a promise (or something that has a .promise or .$promise");-1===c.promises.indexOf(a)&&(c.promises.push(a),c.callThen(a,function(){a.$cgBusyFulfilled=!0,-1!==c.promises.indexOf(a)&&c.promises.splice(c.promises.indexOf(a),1)},function(){a.$cgBusyFulfilled=!0,-1!==c.promises.indexOf(a)&&c.promises.splice(c.promises.indexOf(a),1)}))};return c.active=function(){return c.delayPromise?!1:c.delayJustFinished?(c.delayJustFinished=!1,0===c.promises.length&&(c.durationPromise=null),c.promises.length>0):c.durationPromise?!0:c.promises.length>0},c}}]),angular.module("cgBusy").value("cgBusyDefaults",{}),angular.module("cgBusy").directive("cgBusy",["$compile","$templateCache","cgBusyDefaults","$http","_cgBusyTrackerFactory",function(a,b,c,d,e){return{restrict:"A",link:function(f,g,h){var i=g.css("position");("static"===i||""===i||"undefined"==typeof i)&&g.css("position","relative");var j,k,l,m,n,o=e(),p={templateUrl:"angular-busy.html",delay:0,minDuration:0,backdrop:!0,message:"Please Wait...",wrapperClass:"cg-busy cg-busy-animation"};angular.extend(p,c),f.$watchCollection(h.cgBusy,function(c){if(c||(c={promise:null}),angular.isString(c))throw new Error("Invalid value for cg-busy. cgBusy no longer accepts string ids to represent promises/trackers.");(angular.isArray(c)||o.isPromise(c))&&(c={promise:c}),c=angular.extend(angular.copy(p),c),c.templateUrl||(c.templateUrl=p.templateUrl),angular.isArray(c.promise)||(c.promise=[c.promise]),m||(m=f.$new()),m.$message=c.message,angular.equals(o.promises,c.promise)||o.reset({promises:c.promise,delay:c.delay,minDuration:c.minDuration}),m.$cgBusyIsActive=function(){return o.active()},j&&l===c.templateUrl&&n===c.backdrop||(j&&j.remove(),k&&k.remove(),l=c.templateUrl,n=c.backdrop,d.get(l,{cache:b}).success(function(b){if(c.backdrop="undefined"==typeof c.backdrop?!0:c.backdrop,c.backdrop){var d='<div class="cg-busy cg-busy-backdrop cg-busy-backdrop-animation ng-hide" ng-show="$cgBusyIsActive()"></div>';k=a(d)(m),g.append(k)}var e='<div class="'+c.wrapperClass+' ng-hide" ng-show="$cgBusyIsActive()">'+b+"</div>";j=a(e)(m),angular.element(j.children()[0]).css("position","absolute").css("top",0).css("left",0).css("right",0).css("bottom",0),g.append(j)}).error(function(a){throw new Error("Template specified for cgBusy ("+c.templateUrl+") could not be loaded. "+a)}))},!0)}}}]),angular.module("cgBusy").run(["$templateCache",function(a){"use strict";a.put("angular-busy.html",'<div class="cg-busy-default-wrapper">\n\n   <div class="cg-busy-default-sign">\n\n      <div class="cg-busy-default-spinner">\n         <div class="bar1"></div>\n         <div class="bar2"></div>\n         <div class="bar3"></div>\n         <div class="bar4"></div>\n         <div class="bar5"></div>\n         <div class="bar6"></div>\n         <div class="bar7"></div>\n         <div class="bar8"></div>\n         <div class="bar9"></div>\n         <div class="bar10"></div>\n         <div class="bar11"></div>\n         <div class="bar12"></div>\n      </div>\n\n      <div class="cg-busy-default-text">{{$message}}</div>\n\n   </div>\n\n</div>')}]);