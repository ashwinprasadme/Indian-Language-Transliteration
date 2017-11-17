 $("#next-button").click(function(event){
	document.getElementById("overlay").style.display = "block";
	var target = document.getElementById('spinner')
	var opts = {color: '#fff', length: 30 , width: 10 , radius: 30}
	var spinner = new Spinner(opts).spin()
	target.appendChild(spinner.el)
	// document.getElementById("next-button").disabled = true;
});