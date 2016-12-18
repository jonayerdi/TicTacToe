
var $board_area;
var boardUpdateIntervalID;

//AJAX request to update board state
function updateBoard() {
	$.ajax({
		url: '/get_board_state/'+game_id,
		success: function(data) {
			for(var i = 0 ; i < 36 ; i++) {
				var value;
				switch (data[i]) {
					case 'X':
						value='X';
					break;
					case 'O':
						value='O';
					break;
					default:
						value='';
					break;
				}
				$('#s'+i+'').html(value);
			}
		},
		failure: function(data) { 
			
		}
	}); 
}

//Called when the user clicks a cell from the board
function cell_clicked(n) {
	
}

//Builds the board table
function buildBoard() {
	var device_width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
	var device_height = (window.innerHeight > 0) ? window.innerHeight : screen.height;
	var size = (device_width > device_height) ? (device_height-100)/6 : (device_width-100)/6;
	$board_area.empty();
	$board_area.append("<table class=\"board-table\"></table>");
	var $board_table = $(".board-table");
	for(var i = 0 ; i < 6 ; i++) {
		$board_table.append("<tr id=\"row"+i+"\" height='"+size+"' width='"+size+"'></tr>");
		var $board_row = $("#row"+i);
		for(var j = 0 ; j < 6 ; j++) {
			$board_row.append("<td onclick=\"cell_clicked("+((6*i)+j)+")\" id=\"s"+((6*i)+j)+"\" height='"+size
			+"' width='"+size+"' style=\"font-size:"+size/2+"px;\"></td>");
		}
	}
}

//Wait till all is loaded
$(document).ready(function() {
	//Get jQuery variables
	$board_area = $('#board_area');
	//Build the board
	buildBoard();
	updateBoard();
	//Set interval for board update
	boardUpdateIntervalID = setInterval(function(){updateBoard()}, 1000);
});