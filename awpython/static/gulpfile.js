'use strict';

/* global module, require */

var gulp = require('gulp'),
    path = require('path'),
    mqRemove = require('gulp-mq-remove'),
    $ = require('gulp-load-plugins')({
        pattern: ['gulp-*']
    });

var banner = [
    '/* \n' +
    'We want a header here' +
    '*/\n\n'
];

gulp.task('sass', function() {
    return gulp.src([
        './scss/style.scss'])
        .pipe($.sass({
            includePaths: ['./scss/'],
            outputStyle: 'compressed'
        }))
        .pipe($.autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false,
            grid: false
        }))
        .pipe($.header(banner))
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest('./css'));
});


gulp.task('print', function () {
    return gulp.src([
            './scss/print.scss'])
        .pipe($.sass({
            includePaths: [
                './scss'
            ],
            outputStyle: 'compressed'
        }))
        .pipe(mqRemove({
            width: '64em'
        }))
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest('../assets/css'));
});

//
//gulp.task('bn-css-to-scss', ['bn-css-copy'], function () {
//    // Create scss version of stylesheet for import into other projects
//    return gulp.src([
//            '../assets/scss/birdsnest.css'])
//        .pipe($.rename('birdsnest-prod.scss'))
//        .pipe($.header(sassBanner))
//        .pipe(gulp.dest('../assets/scss'));
//});
//
//gulp.task('bn-css-rm-copy', ['bn-css-to-scss'], function() {
//    return gulp.src([
//        '../assets/scss/birdsnest.css'], {
//            read: false // much faster
//        })
//        .pipe($.rimraf({ force: true}));
//});

//gulp.task('sg-sass', function() {
//    return gulp.src([
//            './scss/style-guide/style-guide.scss'])
//        .pipe($.sass({
//            includePaths: [
//                './node_modules/bourbon/app/assets/stylesheets',
//                './node_modules/bourbon-neat/app/assets/stylesheets',
//                './scss/style-guide'
//            ],
//            outputStyle: 'compressed'
//        }))
//        .pipe($.rename('style-guide.css'))
//        .pipe($.header(styleGuideBanner))
//        .pipe(gulp.dest('../assets/css'));
//});

//gulp.task('lib-copy', function () {
//    return gulp.src([
//            '../_assets/lib/highlightjs/*.js',
//            '../_assets/lib/highlightjs/styles/github.css',
//            '!../_assets/lib/highlightjs/styles/*.css',
//            '../_assets/lib/**/*.min.js',
//            '../_assets/lib/*.js'
//        ])
//        .pipe($.copy('../assets/lib', {
//            prefix: 1
//        }));
//});

// gulp.task('images-copy', ['svg'], function () {
//     return gulp.src([
//             './images/*.{jpg,png}',
//             './images/svg/*.svg'
//         ])
//         .pipe($.copy('../assets/images', {
//             prefix: 1
//         }));
// });
//
// gulp.task('fonts-copy', function () {
//     return gulp.src([
//             './fonts/*.{eot,ttf,woff,svg}'
//         ])
//         .pipe($.copy('../assets/fonts', {
//             prefix: 1
//         }));
// });

gulp.task('svg', function () {
    var svgs = gulp.src('./images/svg/src/*.svg')
        .pipe($.svgmin(function (file) {
            var prefix = path.basename(file.relative, path.extname(file.relative));
            return {
                plugins: [{
                    cleanupIDs: {
                        prefix: prefix + '-',
                        minify: true
                    }
                },
                {
                    removeStyleElement: true
                }]
            }
        }))
        .pipe($.svgstore({ inlineSvg: true }));

    function fileContents (filePath, file) {
        return file.contents.toString();
    }

    return gulp.src('../templates/inline_svg.txt')
        .pipe($.rename('inline_svg.html'))
        .pipe($.inject(svgs, { transform: fileContents }))
        .pipe(gulp.dest('../templates'));
});

gulp.task('watch', function () {
    gulp.watch(['./scss/**/*.scss', './scss/**/**/*.scss'], ['sass']);
});

gulp.task('default', ['sass', 'print', 'svg']);
gulp.task('watch', ['watch']);