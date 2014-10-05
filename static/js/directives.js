"use strict";

var timelineDirectives = angular.module('timelineDirectives', []);

timelineDirectives.directive('timeLine', function () {
    return {
        restrict: 'E',
        replace: true,
        template: '<div id="my-timeline"></div>',
        link: function (scope, element, attrs) {
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
