var API_ENDPOINT = "https://2vs27ns228.execute-api.eu-west-2.amazonaws.com/dev"

document.getElementById("actionButton").onclick = function(){
		//"voice": $('#taskSelected option:selected').val(),
		//"text" : $('#emailText').val()
	if ($('#taskSelected option:selected').val() == 'Create') {
		window.confirm("Do you want to request a desktop for " + $('#emailText').val());
		$.ajax({
			url: API_ENDPOINT + '?email=' + $('#emailText').val() + '&duration=' + $('#durationSelected option:selected').val() + '&firstname=' + $('#firstText').val() + '&starttime=' + $('#hourSelected option:selected').val() + ":" + $('#minuteSelected option:selected').val() + '&date=21032018&lastname=' + $('#lastText').val(),
			type: 'POST',
			//data:  JSON.stringify(inputData)  ,
			contentType: 'application/json; charset=utf-8',
			success: function (response) {
						document.getElementById();//"postIDreturned").textContent="Post ID: " + response;
			}
		});
	} else {
		window.confirm("Do you want to DELETE the desktop for " + $('#emailText').val());
		$.ajax({
			url: API_ENDPOINT + '?email=' + $('#emailText').val(),
			type: 'DELETE',
			//data:  JSON.stringify(inputData)  ,
			contentType: 'application/json; charset=utf-8',
			success: function (response) {
						document.getElementById();//"postIDreturned").textContent="Post ID: " + response;
			}
		});
	}
}


document.getElementById("searchButton").onclick = function(){

	//var postId = $('#postId').val();


	$.ajax({
				url: API_ENDPOINT + '?email='+postId,
				type: 'GET',
				success: function (response) {

					//$('#posts tr').slice(1).remove();
					$("#posts").find("tr:not(:first)").remove();
	        jQuery.each(response['Body']['Items'], function(i,data) {
				
						//var player = "<audio controls><source src='" + data['url'] + "' type='audio/mpeg'></audio>"

						//if (typeof data['url'] === "undefined") {
	    				//var player = ""
						//}

						$("#posts").append("<tr> \
								<td>" + data['email']['S'] + "</td> \
								<td>" + data['workspaceCode']['S'] + "</td> \
								<td>" + data['username']['S'] + "</td> \
								<td>" + data['password']['S'] + "</td> \
								<td>" + data['startTime']['S'] + "</td> \
								<td>" + data['duration']['S'] + "</td> \
								<td>" + data['status']['S'] + "</td> \
								</tr>");
			});
			console.log($("#posts"))
				},
				error: function () {
						alert("error");
				}
		});
}

//document.getElementById("emailText").onkeyup = function(){
//	var length = $(emailText).val().length;
//	document.getElementById("charCounter").textContent="Characters: " + length;
//}
