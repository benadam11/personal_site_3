$('html').hide()

$(document).ready(function(){

  //Set Date to Current Year
  var date = new Date().getFullYear();
  console.log(date)
  $('#footer-date').html(date);

  $('html').fadeIn(300)

	// Social toggle
  $('#social-click').click(function(){
    $('.social-icon').toggle( 'slide' );
  });

  $('.navigation-toggle').on('click',function() {

    if($('.navigation-target').hasClass('clicked')){
      $('.navigation-target').removeClass('clicked');
      $('.dropdown-menu').slideUp();
    }
    else{
      $('.navigation-target').addClass('clicked');
      $('.dropdown-menu').slideDown();
    }
  });

  //Fade In Images On Load
  $('img').load(function() {
    $(this).fadeIn('slow');
  });

  $('.transition-link').on("click", function () {

    // get the href attribute
    var newUrl = $(this).attr("href");

    // veryfy if the new url exists or is a hash
    if (!newUrl || newUrl[0] === "#") {
        // set that hash
        location.hash = newUrl;
        return;
    }

    // fade out content
    $('html').fadeOut(300, function () {
        // when the animation is complete, set the new location
        location = newUrl;
    });

    // prevent the default browser behavior.
    return false;
  });

});
