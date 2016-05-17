var $card = $('#card');
var $list = $('#list');

$.get('/tasks/', function(data){
    data.forEach(function(task){
        $('<li>').text(task.title).appendTo($card)
    })
})
