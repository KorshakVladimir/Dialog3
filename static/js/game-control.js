$( function(){

	var refresh_game = function(){
		$("#game_list").load("/game/refresh_game/ li")
	}

	$("body").on("click","#new_form", function(){

		$.post( "/game/add_game/",$("#foorm_add_game").serialize() )
		  .done(function( data ) {
		  		$data = $(data);
		    	$("#page-wrapper").html($data);
		  });
		refresh_game();
		return false;
	});

	$("body").on("click","#cancel-buttom", function(){
		
		$("#page-wrapper").load("/ #ajax-wrapper");
		return false;
	});

	$("body").on("click",".button_del_game",function(e){
		var game_id = $(e.target).parent().attr("game_id");
		$.post("/game/del_game/",{"game_id":game_id})
		
		$("#"+game_id).remove();
		refresh_game();
	});

});