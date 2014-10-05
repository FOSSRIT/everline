"use strict";

var timelineDirectives = angular.module('timelineDirectives', []);

timelineDirectives.directive('timeLine', ['$http', function ($http) {
    return {
        restrict: 'E',
        replace: true,
        template: '<div id="my-timeline"></div>',
        link: function (scope, element, attrs) {
            $http({method: 'GET', url: '/getevernote'})
                .success(function(data, status) {
                    console.log(data);
                    createStoryJS({
                        type:       'timeline',
                        width:      '100%',
                        height:     '600',
                        source:     data,
                        embed_id:   'my-timeline'
                    });
                })
                .error(function (data, status) {
                    console.error("error getting data");
                });
        }
    };
}]);
