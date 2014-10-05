"use strict";

var timelineDirectives = angular.module('timelineDirectives', []);
console.log('directive');

timelineDirectives.directive('timeLine', function () {
    console.log('fuck');
    return {
        restrict: 'E',
        replace: true,
        template: '<div id="my-timeline"></div>',
        link: function (scope, element, attrs) {
            console.log('timeline-controller');
            createStoryJS({
                type:       'timeline',
                width:      '100%',
                height:     '600',
                source:     '/static/data/example_json.json',
                embed_id:   'my-timeline'
            });
        }
    }
});
