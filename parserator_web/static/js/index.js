/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

var divblock = document.getElementById("address-results");
var form = document.querySelector(".form");
var t = document.getElementById('table-body');
var parseType = document.getElementById('parse-type');

// when the form is submitted, send API request
form.addEventListener("submit", (event) => {
  event.preventDefault();

  let apiurl = '/api/parse/' + '?address=' + document.getElementById("address").value;
  fetch(apiurl)
  .then((response) => response.json())
  .then((data) => {
    let rowhtml = "";
    //if request is successful
    if((data.Address)){
      divblock.style = "display: inline-block";
      let address = data['Address'];
      let addressType = data['Address Type'];
      parseType.innerText = addressType;
      let addressComponents = data['Address Components'];
      // creates a new table row for every key, value pair in the addressComponents dict
      for (const [key, value] of Object.entries(addressComponents)) {
          rowhtml += `
          <tr>
            <td>${key}</td>
            <td>${value}</td>
          </tr>
        `;
      };
    } else{ // if request is unsuccessful
      divblock.style = "display: inline-block";
      let error_desc = data['Error Description']
      let addressType = `Not found. ${error_desc} See parsing attempt below:`;
      parseType.innerText = addressType;
      let parsedString = data['Parsed String'];
      
      for (const [key, value] of Object.entries(parsedString)) {
        rowhtml += `
        <tr>
          <td>${value[0]}</td>
          <td>${value[1]}</td>
        </tr>
      `;
    };
  };
  t.innerHTML = rowhtml;
});

})