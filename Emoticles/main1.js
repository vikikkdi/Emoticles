var addArticle = document.getElementById("addArticle");
var viewArticle = document.getElementById("viewArticle");
var query = { active: true, currentWindow: true };
chrome.tabs.query(query, callback);

function callback(tabs) {
  var currentTab = tabs[0];
  var url = currentTab.url;
  sendURL(url);
}

function sendURL()
{
        var url = arguments[0];
        //alert(url);
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {

            if(this.readyState==4 && this.status==200)
            {
                $(document).ready(function() {
                    $('#loading').hide();
                });
                $('#header').append("<label>Emoticles</label>");
                var emotionsTemp=xmlHttp.responseText;
                emotionsTemp = emotionsTemp.split("`");
                var eList = document.getElementById("emotionsList");
                for(var i=0;i<emotionsTemp.length-3;i++)
                {
                    var label = document.createElement("label");
                    var input = document.createElement("input");
                    var span = document.createElement("span");
                    input.type="checkbox";
                    input.setAttribute("class", "emotions");
                    label.setAttribute("class", "container");
                    span.setAttribute("class", "checkmark");
                    input.value = emotionsTemp[i];
                    input.name="categories";
                    label.appendChild(input);
                    label.appendChild(span);
                    var text = document.createTextNode(emotionsTemp[i]);
                    label.appendChild(text);
                    var br = document.createElement("br");
                    label.appendChild(br);
                    if(eList)
                        eList.appendChild(label);
                }
                var len = emotionsTemp.length-1
                sessionStorage.setItem("url", emotionsTemp[len]);
                sessionStorage.setItem("description", emotionsTemp[len-1]);
                sessionStorage.setItem("title", emotionsTemp[len-2]);              
            }
        }
        xmlHttp.open("POST", "http://localhost:5000/sendURL", true);
        xmlHttp.send(url);
}

if(viewArticle) {
viewArticle.addEventListener("click",function() {
    window.open("articles.html","_blank");
});
}

if(addArticle) {
addArticle.addEventListener("click",function() {

    //alert("k");
    var url = sessionStorage.getItem("url");
    var des = sessionStorage.getItem("description");
    var title = sessionStorage.getItem("title");
    var emotions = document.querySelectorAll('input[type=checkbox]:checked');
    var string = "";
    for(var i=0;i<emotions.length;i++)
    {
        string+=emotions[i].value+"`";
    }
    string+=url+"`"+des+"`"+title;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "http://192.168.43.74:5000/addArticles", true);
    xmlHttp.send(string);
    xmlHttp.onreadystatechange = function() {
        if(this.readyState==4 && this.status==200)
        {
            var ret = xmlHttp.responseText;
            if(ret==="done")
                alert("Added Article");
        }
    }
});
}

/*

<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>

*/