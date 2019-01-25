$("button").on("click", function() {
  $(this).html('<i class="fa fa-check"></i>');
  $(this).css('background-color', '#4CD698');
  
  
  setTimeout(function() {
    $("button").html('Send');
    $("button").css('background-color', '#40B4DE');
    }, 1500);
});

