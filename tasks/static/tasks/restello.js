var $card = $('#card');
var $list = $('#list');

$.get('http://127.0.0.1:8000/tasks/', function(card){
    var card = card['results']

})
