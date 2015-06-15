// Fixed Sidebar
$(window).bind("load", function () {
    
    var element=document.getElementById('GamePlayForm');

    if (!element) {
        
        $("body").toggleClass("mini-navbar");
        SmoothlyMenu();
    }

})

function f_test () {
	console.log('good');
	// document.querySelect
	doc_el = document.documentElement;
	el_backg =   doc_el.querySelector('.backg');
	if (!el_backg) {
		return;
	}
	height_document = doc_el.clientHeight;
	if (height_document < el_backg.clientHeight){
		el_backg.style.top = height_document + 15 + "px"
	}
}


document.documentElement.addEventListener('onload',f_test());

// document.onload = f_test()