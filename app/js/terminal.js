
function update(){

    
    var v = document.getElementById('uinput').value;
    var url = "/user_input" + "?user_input_field=" + v;
    
    var req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send();

    //used to show working dir
    var url2 = "/pwd" + "?user_input_field=" + v;
    var req2 = new XMLHttpRequest();
    req2.open("GET", url2, false);
    req2.send();

    //send to formatter
    formatLine(req.responseText,req2.responseText,v);


}

function formatLine(Response1, Response2, v){
    //optimize this more
    document.getElementById("uinput").value = "";
    
    var terminal=document.getElementById('terminalWindow');
    var user = "User1@cmdLineLern:";
    var buildLineUser = user + Response2 +"# "+v;
    var buildLine = Response1;

    var node = document.createElement("LI");
    var textnode = document.createTextNode(buildLineUser);
    node.appendChild(textnode);
    node.setAttribute("class", "listsUser")
    terminal.appendChild(node);

    var node1 = document.createElement("LI");
    var textnode1 = document.createTextNode(buildLine);
    node1.appendChild(textnode1);
    node1.setAttribute("class", "lists")
    terminal.appendChild(node1);


    terminal.scrollTo(0,terminal.scrollHeight)
}