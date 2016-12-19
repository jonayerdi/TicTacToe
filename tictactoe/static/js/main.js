
var $challenge_list;

//AJAX request to update challenges list
function updateChallenges() {
	$.ajax({
		url: '/get_challenge_list/'+user+'/',
		success: function(data) {
			setBoard(data);
		},
		failure: function(data) { 
			
		}
	}); 
}

//Wait till all is loaded
$(document).ready(function() {
	//Get jQuery variables
	$challenge_list = $('#challenge_list');
	//Set interval for challenges update
	if(user)
		boardUpdateIntervalID = setInterval(function(){updateChallenges()}, 3000);
});