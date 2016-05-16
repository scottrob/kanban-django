var $tasks = $('#tasks');

$.get('http://localhost:8000/tasks/', function(tasks){
  tasks.results.forEach(function(card) {
    console.log(card)
    var $li = $('');
    $li.text(card.name)
    $li.appendTo($tasks);
  })
})


var $card = $('#card');
var $title = $('input[name="name"]');
var $comments = $('input[name="damage"]');
var $description = $('input[name="rarity"]');

$card.submit(function() {
  console.log('you submitted the form');

  $.ajax({
    method: 'post',
    url: 'http://localhost:8000/tasks/',
    username: 'admin',
    password: 'password123',
    data: {
      name: $name.val(),
      damage: $damage.val(),
      icon: $icon.val(),
      rarity: $rarity.val()
    },
    success: function(newcard) {
      console.log(newcard)
      var $li = $('<li>');
      $li.text(newcard.name)
      $li.appendTo($tasks);
    }
  });

  return false;
});
