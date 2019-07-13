$(document).ready(function() {
    let generateList = function(list, elements) {
        var addChild = function (list, elements) {
            let element = elements.shift();
            let id = $(element).attr('id');
            let text = $(element).text();
            $(list).append(`<li><ul class="no-list-style" id=${id}><a href='#${id}'>${text}<a></ul></li>`);

            while (elements.length > 0 && elements[0].nodeName > element.nodeName && elements[0].nodeName < "H4") {
                generateList($(`ul#${id}`), elements), list;
            }
            return;
        }

        while (elements.length > 0) {
            addChild(list, elements)
        }

    }
    generateList($("#onthispage-list"), anchors.elements.slice());
    // anchors.elements.forEach(element => {
    //     if (element.nodeName === 'H2') {
    //         let id = $(element).attr('id')
    //         let text = $(element).text()
    //         $('#onthispage').append(`<li class="nav-item"><a class="nav-link" href='#${id}'>${text}<a></li>`)
    //     }
    // });
})