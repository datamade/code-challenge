// set form action
let form = document.querySelector("form");
form.action = "api/parse/";

// define references for hidden results section, as well as parse-type element
let resultsSection = document.getElementById("address-results");
let parseType = document.getElementById("parse-type");

// define functions
function GET_url_with_body(form){
   // assembles url from html form for GET request with body
   let params = new URLSearchParams(new FormData(form));
   let urlString = form.action.toString() + "?" + params.toString();
   return urlString;
}

function fillTable(parsedAddress) {
   // parses parsedAddress dict from GET response into 
   // viewable table
   let tb = document.querySelector("tbody");
   tb.innerHTML = "";
   for (const [addressPart, tag] of Object.entries(parsedAddress)){
      // console.log(`${key}: ${value}`)
      var row = document.createElement("tr");
      for (let i of [addressPart, tag]){
         var cell = document.createElement("td");
         var cellText = document.createTextNode(i);
         cell.appendChild(cellText);
         row.appendChild(cell);
      }
      tb.appendChild(row);
   }
}

function parseAlert() {
   // create <div> for alert in the event parser returns an error
   var alert_div = document.createElement("div");
   alert_div.className = "alert alert-danger";
   var text = "Address parse failed. Did your submission included any repeated elements?";
   var alert_text = document.createTextNode(text);
   alert_div.appendChild(alert_text);
   resultsSection.insertAdjacentElement('beforebegin', alert_div);
}

// add listener to form, collecting data to send to the GET
// then process the API response, either populating the results in a table 
// or throwing an error.
form.addEventListener('submit', (event) => {
   event.preventDefault();
   var urlString = GET_url_with_body(event.target);
   fetch(urlString)
      .then(response => {
         if (!response.ok) {
            throw new Error(`Server Error; code: ${response.code}`);
         }
         return response.json();
      }).then((data) => {
         if (data["status" == "success"]) {
            parseType.textContent = data["address_type"];
            fillTable(data["tagged_address"]);
            resultsSection.style.display = 'table';
         } else if (data["status"] == "repeatedLabelError") {
            parseAlert(data["original_string"], data["parsed_string"]);
         }
      });
});

