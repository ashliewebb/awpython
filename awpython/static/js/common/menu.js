(function ($) {
    AW = window.AW || {};

    AW.Menu = (function () {
        var self = {};

        var menu = $('.js-menu'),
            menuOpenBtn = $('.js-menu-open-button'),
            menuCloseBtn = $('.js-menu-close-button');

        self.open = function () {
            menuOpenBtn.on('click', function () {
                menu.addClass('active');
            });
        };

        self.close = function () {
            menuCloseBtn.on('click', function () {
                menu.removeClass('active');
            });
        };

        return self;

    })($);

})(jQuery);