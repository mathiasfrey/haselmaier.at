$(function() {

    
    
    //--------------------------------------------------------------------------
    // init affix    
    $('#myAffix').affix({
       offset: {
         top: function() {
           return ($('#start_affix_contentarea').offset().top)
         }
         , bottom: function () {
           return (this.bottom = $('#call2action').outerHeight(true))
         }
       }
     })




    //--------------------------------------------------------------------------
    // nice scrolling
    //$("ul.nav li a[href^='#']").on('click', function(e) {
    $(".innerside-nav").on('click', function(e) {
        
       target = this.hash;
       // prevent default anchor click behavior
       e.preventDefault();
    
       // store hash
       var hash = this.hash;
    
       // animate
       $('html, body').animate({
           scrollTop: $(this.hash).offset().top
         }, 600, function(){
    
           // when done, add hash to url
           // (default click behaviour)
           window.location.hash = target;
         });
    
    });
    //--------------------------------------------------------------------------
        

});
