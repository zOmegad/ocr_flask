$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$("body").html(response);;
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
