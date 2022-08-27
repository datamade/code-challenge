/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

let submit_button = document.getElementById("submit");

// add on click
console.log("adding on click method");
submit_button.addEventListener("click", () => {
   console.log("Parsing address");

   // grab input data
   let input_address = document.getElementById("address").value;
   console.log(input_address);
   let params = {"address": input_address};
   let url = "http://localhost:8000/api/parse/?" + new URLSearchParams(params).toString();
   console.log(url);

   // call api
   let request = fetch(url);
   request.then((response) => {
      if (response['status'] == 200) {
         response.json()
         .then(data => {
            let addr_results_div = document.getElementById("address-results");
            
            // Show hidden html element
            addr_results_div.style.display = 'block';

            // Append elements to html
            let addr_type_strong = document.getElementById("parse-type");
            let addr_type_text = document.createTextNode(data["address_type"]);
            addr_type_strong.appendChild(addr_type_text);

            var comp_table_body = addr_results_div.children[2].children[1]
            for (const [key, value] of Object.entries(data["address_components"])) {
               let tr = document.createElement("tr");
               let th1 = document.createElement("th");
               let th2 = document.createElement("th");
               let addr_comp_type = document.createTextNode(key);
               let addr_comp_text = document.createTextNode(value);
               th1.appendChild(addr_comp_type);
               th2.appendChild(addr_comp_text);
               tr.appendChild(th1);
               tr.appendChild(th2);

               comp_table_body.appendChild(tr);
            }
         })
      } else {
         // Display error message
         let addr_results_div = document.getElementById("address-results");
         addr_results_div.style.display = 'block';
         let h3 = document.createElement("h3");
         let h3_text = document.createTextNode("Invalid address. Please try again with a valid address.");
         h3.appendChild(h3_text);
         addr_results_div.appendChild(h3);
         
         console.log("API error", response["status"]);
      }
})});