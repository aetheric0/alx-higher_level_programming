$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(response) {
    $('DIV#hello').text(response.hello);
  });
});
