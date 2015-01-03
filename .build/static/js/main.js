//Set Date to Current Year
$('#footer-date').html(new Date().getFullYear());

//Hide all of the content before the page loads 
$(".content").css('visibility','hidden');

$(document).ready(function(){
	
	// Social toggle 
  $('#social-click').click(function(){
    $('.social-icon').toggle( 'slide' );
  });

  //Fade In Images On Load 
  $('img').load(function() {
    $(this).fadeIn('slow');
  });

  //Fade In Content
  $('.content').css('visibility','visible').hide().fadeIn(1200);
  
});


