/* ----------------------------------------------------------------------------------------
* Author        : Ambidextrousbd
* Template Name : Korprate - One Page Corporate Html5 Template
* File          : Korprate main JS file
* Version       : 1.0
* URL: http://www.bootstrapmb.com
* ---------------------------------------------------------------------------------------- */




    
/* INDEX
----------------------------------------------------------------------------------------

01. Preloader js

02. change Menu background on scroll js 

03. Navigation js

04. Smooth scroll to anchor

05. Portfolio js

06. Magnific Popup js

07. Portfolio js  

08. Testimonial js

09. client js

10. News js

11. Google Map js   

12. Ajax Contact Form js

13. MailChimp js   

-------------------------------------------------------------------------------------- */





(function($) {
'use strict';


/*-------------------------------------------------------------------------*
*                  01. Preloader js                                       *
*-------------------------------------------------------------------------*/
   $(window).on( 'load', function(){
     
       $('#preloader').delay(300).fadeOut('slow',function(){
         $(this).remove();
       });    

   }); // $(window).on end



  $(document).ready(function(){



/*-------------------------------------------------------------------------*
*             02. change Menu background on scroll js                     *
*-------------------------------------------------------------------------*/
   $(window).on('scroll', function () {
       var menu_area = $('.menu-area');
       if ($(window).scrollTop() > 50) {
           menu_area.addClass('sticky-menu');
       } else {
           menu_area.removeClass('sticky-menu');
       }
   }); // $(window).on('scroll' end




/*-------------------------------------------------------------------------*
*                   03. Navigation js                                     *
*-------------------------------------------------------------------------*/
   $(document).on('click', '.navbar-collapse.in', function (e) {
       if ($(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle') {
           $(this).collapse('hide');
       }
   });

   $('body').scrollspy({
       target: '.navbar-collapse',
       offset: 195
   });



/*-------------------------------------------------------------------------*
*                   04. Smooth scroll to anchor                           *
*-------------------------------------------------------------------------*/
   $('a.smooth_scroll').on("click", function (e) {
       e.preventDefault();
       var anchor = $(this);
       $('html, body').stop().animate({
           scrollTop: $(anchor.attr('href')).offset().top - 50
       }, 1000);
   });



/*-------------------------------------------------------------------------*
*                  06. Magnific Popup js                                  *
*-------------------------------------------------------------------------*/
   $('.work-popup').magnificPopup({
     type: 'image',
     gallery: {
         enabled: true
     }
   });
   $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
       disableOn: 700,
       type: 'iframe',
       mainClass: 'mfp-fade',
       removalDelay: 160,
       preloader: false,
       fixedContentPos: false
   });


/*-------------------------------------------------------------------------*
*                  07. Portfolio js                                       *
*-------------------------------------------------------------------------*/
   $('.portfolio').mixItUp();



/*-------------------------------------------------------------------------*
*                  08. Testimonial js                                     *
*-------------------------------------------------------------------------*/
   $(".testimonial-list").owlCarousel({
      slideSpeed      : 1000,
      paginationSpeed : 500,
      singleItem      : true,
      lazyLoad        : false,
      pagination      : true,
      navigation      : false,
      autoPlay        : true,
   });

        
 /*-------------------------------------------------------------------------*
*                       09. client js                                     *
*-------------------------------------------------------------------------*/
   $(".owl-client").owlCarousel({
       items               : 5,
       autoPlay            : true,
       itemsDesktop        : [1199, 5],
       itemsDesktopSmall   : [980, 4],
       itemsTablet         : [768, 3],
       itemsMobile         : [479, 2],
       pagination          : false,
       navigation          : false,
       autoHeight          : true,
   });
/*-------------------------------------------------------------------------*
*                       10. News js                                     *
 *-------------------------------------------------------------------------*/      

 $(".news-list").owlCarousel({
    items               : 3,
    autoPlay            : true,
    itemsDesktop        : [1200, 2],
    itemsDesktopSmall   : [980, 2],
    itemsTablet         : [768, 2],
    itemsTabletSmall    : [767, 1],
    itemsMobile         : [480, 1],
    pagination          : true,
    navigation          : false,
    autoHeight          : true,
    navigationText      : ['<span class="ti-layout-line-solid"></span>', '<span class="ti-layout-line-solid"></span>'],
});

     


/*-------------------------------------------------------------------------*
*                       11. Google Map js                                 *
*-------------------------------------------------------------------------*/



/*-------------------------------------------------------------------------*
*                  12. Ajax Contact Form js                               *
*-------------------------------------------------------------------------*/


/*-------------------------------------------------------------------------*
*                   13. MailChimp js                                    *
*-------------------------------------------------------------------------*/






  }); // $(document).ready end

})(jQuery);