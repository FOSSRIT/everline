var gulp        = require('gulp'),
    bowerSrc    = require('gulp-bower'),
    uglify      = require('gulp-uglify'),
    rimraf      = require('rimraf'),
    concat      = require('gulp-concat');

gulp.task('bower', function () {
    return bowerSrc();
});

gulp.task('bower-extract-bootstrap-fonts', ['bower'], function () {
    return gulp
        .src([
            'bower_components/bootstrap/fonts/*'
        ])
        .pipe(gulp.dest('static/fonts/'));
});

gulp.task('bower-concat-css', ['bower'], function () {
    return gulp
        .src([
            'bower_components/bootstrap/dist/css/bootstrap.css',
            'bower_components/bootstrap/dist/css/bootstrap-theme.css',
            'bower_components/pace/themes/blue/pace-theme-barber-shop.css',
        ])
        .pipe(concat('bower-deps.min.css'))
        .pipe(gulp.dest('static/css/'));
});

gulp.task('bower-concat-js', ['bower'], function () {
    return gulp
        .src([
            'bower_components/angularjs/angular.js',
            'bower_components/jquery/dist/jquery.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
            'bower_components/pace/pace.js',
            'bower_components/bootstrap/js/carousel.js',
        ])
        .pipe(gulp.dest('static/js/deps/'));
});

gulp.task('scripts', ['bower-concat-js', 'bower-concat-css', 'bower-extract-bootstrap-fonts'], function () {
    return gulp.
        src('static/js/src/*.js')
        .pipe(gulp.dest('static/js/'));
});


gulp.task('default', ['scripts'], function () {
    rimraf('bower_components', function () {
    });
});
