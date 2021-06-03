$(function(){
	$(".search-button").on('click', function(){
		var user = $('#inputQuestion').val();
		$.ajax({
			url: '/',
			data: $('form').serialize(),
			type: 'POST',
			beforeSend: function () { // Before we send the request, remove the .hidden class from the spinner and default to inline-block.
                $('#loader').addClass('imageLoader')
            },
			success: function(response){
				$("body").html(response);
			},
			error: function(error){
				console.log(error);
			},
			complete: function () { // Set our complete callback, adding the .hidden class and hiding the spinner.
                $('#loader').removeClass('imageLoader')
            }
		});
	});
});
