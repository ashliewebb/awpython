(function ($) {
    AW = window.AW || {};

    AW.Menu = (function () {
        var self = {};

        var body = $('body'),
            menu = $('.js-menu'),
            menuOpenBtn = $('.js-menu-open-button'),
            menuCloseBtn = $('.js-menu-close-button');

        self.open = function () {
            menuOpenBtn.on('click', function () {
                menu.addClass('active');
                body.addClass('menu-open');
            });
        };

        self.close = function () {
            menuCloseBtn.on('click', function () {
                menu.removeClass('active');
                body.removeClass('menu-open');
            });
        };

        return self;

    })($);

})(jQuery);