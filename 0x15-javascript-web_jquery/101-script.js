document.addEventListener('DOMContentLoaded', function() {
  $('DIV#add_itme').click(function() {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function() {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(function() {
    $('UL.my_list').empty();
  });
});
