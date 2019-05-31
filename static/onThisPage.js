$(document).ready(function() {
    anchors.elements.forEach(element => {
        let id = $(element).attr('id')
        let text = $(element).text()
        $('#onthispage').append(`<li class="nav-item"><a class="nav-link" href='#${id}'>${text}<a></li>`)
    });
})