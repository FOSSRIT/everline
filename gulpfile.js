var gulp        = require('gulp'),
    bowerSrc    = require('gulp-bower'),
    uglify      = require('gulp-uglify'),
    rimraf      = require('rimraf'),
    concat      = require('gulp-concat');

gulp.task('bower', function () {
    return bowerSrc()
        .pipe(gulp.dest('bower'));
});

gulp.task('bower-concat', ['bower'], function () {
    return gulp
        .src([
            'bower_components/angularjs/angular.js',
            'bower_components/timeline/timeline.min.js'
        ])
        .pipe(concat('bower-deps.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/js/'));
});

gulp.task('scripts', ['bower-concat'], function () {
    return gulp.
        src('static/js/src/*.js')
        .pipe(concat('main-deps.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/js/'));
});


gulp.task('default', ['scripts'], function () {
    rimraf('bower_components', function () {
    });

    rimraf('bower', function () {
    });
});
