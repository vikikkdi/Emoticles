var body = document.getElementById("body2");
body.addEventListener("load", setView());


var searchB = document.getElementById("searchB");
searchB.addEventListener("click",sendQuery);

function setView()
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("POST", "http://localhost:5000/displayArticles", true);
	xmlHttp.send();
	xmlHttp.onreadystatechange = function() {
            if(this.readyState==4 && this.status==200)
            {
            	$(document).ready(function() {
                    $('#loading2').hide();
                });
            	var allInfo = xmlHttp.responseText;
            	var dlist = allInfo.split(";");
            	var mainView = document.getElementById("mainView");
            	for(var i=0;i<dlist.length-1;i++)
            	{
            		var emurl = dlist[i].split("|");
            		var currentEmotion = emurl[0];
            		if(emurl.length==2)
            			continue;
            		//console.log(emurl);
            		var li1 = document.createElement("li");
					li1.setAttribute("class", "tree__item hasChildren");
					var span  = document.createElement("span");
					span.setAttribute("style", "background-color: #3c3d3c;");
					var spanDiv = document.createElement("div");
					spanDiv.setAttribute("class","icon");
					//spanDiv.setAttribute("align","center");
					span.appendChild(spanDiv);
					var span_a = document.createElement("a");
					var a_text =document.createTextNode(currentEmotion);
					var aT = currentEmotion;
					//alert(aT);
					span_a.href = "#";
					span_a.appendChild(a_text);
					span.appendChild(span_a);
					li1.appendChild(span);
					var ul1 = document.createElement("ul");
            		for(var j=1;j<emurl.length-1;j++)
            		{
						var k = emurl[j].split("`");
						var url = k[0];
						var title = k[1];
						//alert(url+", "+title);
						var li2 = document.createElement("li");
						var span1 = document.createElement("span");
						var span1_a = document.createElement("a");
						var url_text=document.createTextNode(title);
						span1_a.href = url;
						span1_a.setAttribute("target", "_blank");
						span1_a.appendChild(url_text);
						span1.appendChild(span1_a);
						li2.appendChild(span1);
						ul1.appendChild(li2);
            		}
            		li1.appendChild(ul1);
					mainView.appendChild(li1);
            	}
            	$('.tree .icon').click( function() {
				$(this).parent().toggleClass('expanded').
				closest('li').find('ul:first').
				toggleClass('show-effect');
				});
			}

            }
	
}

function sendQuery()
{
	$(document).ready(function() {
        $('#loading2').show();
    });
    document.getElementById("mainView").innerHTML='';
	var sBox = document.getElementById("searchBox");
	var query = sBox.value;
	alert(query);
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open("POST", "http://localhost:5000/searchArticles", true);
	xmlHttp.send(query);
	xmlHttp.onreadystatechange = function()
	{
		if(this.readyState==4 && this.status==200)
		{
				$(document).ready(function() {
                    $('#loading2').hide();
                });
				var allInfo = this.responseText;
				var dlist = allInfo.split(";");
            	var mainView = document.getElementById("mainView");
            	for(var i=0;i<dlist.length-1;i++)
            	{
            		var emurl = dlist[i].split("|");
            		var currentEmotion = emurl[0];
            		if(emurl.length==2)
            			continue;
            		var li1 = document.createElement("li");
					li1.setAttribute("class", "tree__item hasChildren");
					var span  = document.createElement("span");
					span.setAttribute("style", "background-color: #3c3d3c;");
					var spanDiv = document.createElement("div");
					spanDiv.setAttribute("class","icon");
					//spanDiv.setAttribute("align","center");
					span.appendChild(spanDiv);
					var span_a = document.createElement("a");
					var a_text =document.createTextNode(currentEmotion);
					var aT = currentEmotion;
					//alert(aT);
					span_a.href = "#";
					span_a.appendChild(a_text);
					span.appendChild(span_a);
					li1.appendChild(span);
					var ul1 = document.createElement("ul");
            		for(var j=1;j<emurl.length-1;j++)
            		{
						var k = emurl[j].split("`");
						var url = k[0];
						var title = k[1];
						//alert(url+", "+title);
						var li2 = document.createElement("li");
						var span1 = document.createElement("span");
						var span1_a = document.createElement("a");
						var url_text=document.createTextNode(title);
						span1_a.href = url;
						span1_a.setAttribute("target", "_blank");
						span1_a.appendChild(url_text);
						span1.appendChild(span1_a);
						li2.appendChild(span1);
						ul1.appendChild(li2);
            		}
            		li1.appendChild(ul1);
					mainView.appendChild(li1);
            	}
            	$('.tree .icon').click( function() {
				$(this).parent().toggleClass('expanded').
				closest('li').find('ul:first').
				toggleClass('show-effect');
				});
		}
	};
}


/*

<li class="tree__item hasChildren">
					<span>
				        <div class="icon"></div>
						<a href="#">Sad</a>
					</span>
					<ul>
						<li>
							<span><a href="#">URL1</a></span>
						</li>
						<li>
							<span><a href="#">URL2</a></span>
						</li>
					</ul>
</li>

*/