function refreshChoiceGet(id) {
    $.ajax({
        type:"GET",
        url: "/polls/ajax/get/",
        data:{ id: id },
        success: function(data){
            console.log(JSON.parse(data))
        }
    })
}

function refreshChoicePost(id) {
    $.ajax({
        type:"POST",
        url: "/polls/ajax/post/",
        dataType: 'json',
        data:{ id: id },
        success: function(data){
            console.log(JSON.parse(data))
        }
    })
}


function refreshChoiceJson(id) {
    $.ajax({
        type:"POST",
        url: "/polls/ajax/json/",
        dataType: 'json',
        data:{ id: id },
        success: function(data){
            let html = ''
            for(let i=0 ;i<data.length; i++) {
                html += '<input type="radio" name="choice" id="'+data[i].pk+'" value="'+data[i].pk+'">\n' +
                    '            <label for="'+data[i].pk+'">'+data[i].fields.choice_text+'</label><br>'
            }
            $("#choice").html(html)
        }
    })
}