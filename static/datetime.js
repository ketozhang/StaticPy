// $(document).ready(function () {
//     $(".datetime").each(function (i, datetime) {
//         let isoDate = datetime.innerHTML;
//         localDate = new Date(isoDate);
//         datetime.innerHTML = localDate.toLocaleString([], { formatMatcher: 'basic' });
//     });
// });

$(document).ready(function () {
    $("time").each(function (i, datetime) {
        let isoDate = $(datetime).attr('datetime');
        localDate = new Date(isoDate);
        $(datetime).html(localDate.toLocaleString([], { formatMatcher: 'basic' }));
    });
});