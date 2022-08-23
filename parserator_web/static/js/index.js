/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// add on click
console.log("adding on click method")
let submit_button = document.getElementById("submit");
submit_button.addEventListener("click", parse_address());

function parse_address() {
   console.log("Parsing address");
   // grab input data
   let input_address = document.getElementById("address").value;

   // call api
   let request = fetch("",
                       {method: 'POST',
                        body: JSON.stringify({"address": input_address})});
   
   request.then((response) => response.json())
          .then(data => {
            // display data in html
          })
}
