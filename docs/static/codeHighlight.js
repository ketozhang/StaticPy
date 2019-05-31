$('document').ready(function() {
    $('.sourceCode').each(function(i, code) {
        lang = $(code).attr('class').split(' ')[1];
        if (typeof lang !== 'undefined') {
            $(code).attr('class', `language-${lang}`);
            $(code).addClass("line-numbers");
        }
    });
});
