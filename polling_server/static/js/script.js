// script.js

function manage() {
    let xhrObject = false;
    let self = this;

    self.xhrObject = new XMLHttpRequest();
    self.xhrObject.open("POST", "/", true);
    self.xhrObject.onreadystatechange = function() {
        if (self.xhrObject.readyState == 4 && self.xhrObject.status == 200)
            updatePage(self.xhrObject.response);
    }

    self.xhrObject.send();
}

function updatePage(response) {
    response = JSON.parse(response);
    element = document.getElementById("demo");
    element.src = response.message;
    element.style.display = "block";
}
