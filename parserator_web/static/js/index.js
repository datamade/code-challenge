/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

var divblock = document.getElementById("address-results");
var form = document.querySelector(".form");
var t = document.getElementById('table-body');
var parseType = document.getElementById('parse-type');
var addressString = document.getElementById('address-string');


// when the form is submitted, send API request
form.addEventListener("submit", (event) => {
  event.preventDefault();
  
  // if the address input is an empty string
  if(document.getElementById("address").value == '') {
    alert('Hey! You forgot to type an address in the box!')
    return;
  }

  let apiurl = '/api/parse/' + '?address=' + document.getElementById("address").value;
  fetch(apiurl)
  .then((response) => {
    var status = response.status;
    console.log(status);
    let rowhtml = "";

    // if request is successful
    if (status==200) { 
      return response.json()
      .then(data => {
        divblock.style = "display: inline-block";
        let address = data['Address'];
        let addressType = data['Address Type'];
        let addressComponents = data['Address Components'];

        parseType.innerText = addressType;
        addressString.innerText = address;
        for (const [key, value] of Object.entries(addressComponents)) {
          rowhtml += `
          <tr>
            <td>${key}</td>
            <td>${value}</td>
          </tr>
        `;
      };
      t.innerHTML = rowhtml;
    });
    } else { // if request is not successful
      return response.json()
      .then(data => {
        divblock.style = "display: inline-block";
        let error_desc = data['error']
        let addressType = `Not found. ${error_desc}`; // replaces addressType with error message
        let address = data['Original String'];
        let parsedString = data['Parsed String'];
        for (const [key, value] of Object.entries(parsedString)) {
          rowhtml += `
          <tr>
            <td>${value[0]}</td>
            <td>${value[1]}</td>
          </tr>
          `;
        };
        parseType.innerText = addressType; 
        addressString.innerText = address;
        t.innerHTML = rowhtml; 
      }); 
    }; 
    
});
event.target.reset(); // reset address form after submitting
addressString.innerText = ''; 
})