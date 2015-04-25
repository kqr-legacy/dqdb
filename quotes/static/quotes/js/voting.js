(function($){$(function() {
  $('article a[data-action=vote]').on('click', function() {
    var $quote = $(this).closest('article');
    var quoteId = $quote.attr('id').substring(6);

    $.get('/vote/' + quoteId, function(res) {
      $quote.find('.score .number').html(res.count);
      if (res.err === null) {
        $quote.find('a[data-action=vote]').addClass('disabled');
      } else {
        console.error('AJAX vote request failed: ' + res.err);
      }
    });
  });
});})(jQuery);

