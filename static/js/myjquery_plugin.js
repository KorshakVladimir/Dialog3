_$ = {};

_$.get_href_a = function(e){
		var a_href;
		if (e.target.tagName != "A"){
			a_href = $(e.target).closest("a");
		}else{
			a_href = e.target;
		}

		return $(a_href).attr("href");
	};
