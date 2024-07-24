/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
var api_url = "/api/parse";
var button = document.getElementById("submit");
var address = document.getElementById("address");
var parse_type = document.getElementById("parse-type")
button.addEventListener("click", function (event) {
   event.preventDefault();
   fetch(api_url + "?address=" + address.value).then(response => response.json())
      .then(data => {
         const table_body = document.getElementById("table_body")
         table_body.innerHTML = '';
         document.getElementById("address-results").style.display = "none";
         const errors = document.getElementById('errors');
         errors.style.display = "none"
         if (data.errors) {
            errors.innerText = data.errors;
            errors.style.display = "block"
         }
         else {
            let address_parts, address_type;
            [address_parts, address_type] = data.payload;
            parse_type.innerText = address_type
            for (const key in address_parts) {
               let r1 = document.createElement("tr")
               let c1 = document.createElement("td")
               c1.innerText = key
               let c2 = document.createElement("td")
               c2.innerText = address_parts[key]
               r1.appendChild(c1);
               r1.appendChild(c2);
               table_body.appendChild(r1);
            }

            document.getElementById("address-results").style.display = "block";
         }
      })
      .catch(error => {
         console.error('Error', error);
      });

});