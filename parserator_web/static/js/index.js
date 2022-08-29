/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
/*eslint-env es6*/

/* Add event listener for form submission: send requested address to API, 
unhide the Parsing Results table, and display result */
form.addEventListener("submit", (event) => {
  // Prevent page from reloading on form submission
  event.preventDefault();

  //Toggle on display for the address-results div
  const resultsSection = document.getElementById("address-results");
  resultsSection.style.display = "block";

  // Grab address input from form submission
  const form = document.querySelector("form");
  const addressSubmission = form.querySelector("#address").value;

  // Send request to API with submitted address
  fetch("api/parse/?address='" + addressSubmission + "'")
    .then((response) => response.json())
    .then((data) => {
      // Grab "address type" span and add API reponse text (data.address_type)
      const addressTypeSpan = document.getElementById("parse-type");
      addressTypeSpan.textContent = data.address_type;

      // Grab the body of the address results table and add each key/value pair as a row
      // If error raised, skip the table and display RepeatedLabelError message
      const addressResultTable = document.querySelector("tbody");
      // Clear any existing rows from a prior search
      addressResultTable.innerHTML = "";

      if (data.address_type != "Error") {
        for ([key, val] of Object.entries(data.address_parts)) {
          const addressPartRow = document.createElement("tr");
          addressPartRow.innerHTML = `<td>${String(val)}</td><td>${String(
            key
          )}</td>`;

          addressResultTable.appendChild(addressPartRow);
        }
      } else {
        alert(
          `RepeatedLabel Error (see: https://usaddress.readthedocs.io/en/latest/) ${data.address_parts}`
        );
      }
    });
});
