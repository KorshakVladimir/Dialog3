// Fixed Sidebar
$(window).bind("load", function () {
    
    var element=document.getElementById('GamePlayForm');

    if (!element) {
        
        $("body").toggleClass("mini-navbar");
        SmoothlyMenu();
    }

})