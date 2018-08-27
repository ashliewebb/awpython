require('es6-promise').polyfill(); // Needed to get autoprefixer working. See bug here http://stackoverflow.com/questions/32490328/gulp-autoprefixer-throwing-referenceerror-promise-is-not-defined

/* global module, require */

var gulp = require('gulp'),
    path = require('path'),
    $ = require('gulp-load-plugins')({
        pattern: ['gulp-*']
    });

gulp.task('sass', function () {
    return gulp.src([
        './scss/style.scss'])
        .pipe($.sass({
            includePaths: [
                './scss/'
            ],
            outputStyle: 'compressed'
        }))
        .pipe($.autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest('./css'));
});

//gulp.task('print', function () {
//    return gulp.src([
//            './scss/print.scss'])
//        .pipe($.sass({
//            includePaths: [
//                './scss'
//            ],
//            outputStyle: 'compressed'
//        }))
//        .pipe(mqRemove({
//            width: '64em'
//        }))
//        .pipe($.cssmin())
//        .pipe($.rename({suffix: '.min'}))
//        .pipe(gulp.dest('../assets/css'));
//});

gulp.task('svg', function () {
    var svgs = gulp.src('./images/svg/*.svg')
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

  function fileContents(filePath, file) {
    return file.contents.toString();
  }

  return gulp.src('../templates/inline_svg.txt')
    .pipe($.rename('inline_svg.html'))
    .pipe($.inject(svgs, { transform: fileContents }))
    .pipe(gulp.dest('../templates'));
});

gulp.task('watch', function () {
  $.watch([
    './scss/**/*.scss',
    './scss/**/**/*.scss'
  ], ['sass']);
});

gulp.task('default', [
  'sass',
  'svg'
//  'assets-copy',
]);