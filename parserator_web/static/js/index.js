/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// add on click
console.log("adding on click method")
let submit_button = document.getElementById("submit");
submit_button.addEventListener("click", parse_address => {
   console.log("Parsing address");

   // grab input data from url
   let input_address = document.getElementById("address").value;
   // let input_address = window.location.href.split("&")[1].split("=")[1].split("+").join(" ")
   console.log(input_address);
   let params = {"address": input_address};
   let url = "http://localhost:8000/api/parse/?" + new URLSearchParams(params).toString()
   console.log(url)

   // call api
   let request = fetch(url)   
   request.then((response) => {
      if (response['status'] == 200) {
         response.json()
         .then(data => {
            console.log(data)
            console.log(data["address_type"])
            let addr_results_div = document.getElementById("address-results");
            addr_results_div.style.display = 'block';
            let addr_type_strong = document.getElementById("parse-type");
            // var paragraph = document.getElementById("p");
            let addr_type_text = document.createTextNode(data["address_type"]);
            addr_type_strong.appendChild(addr_type_text);

            // var comp_table_body = addr_results_div.children[2].children[1]
            // // console.log(data["address_components"])
            // for (const [key, value] of Object.entries(data["address_components"])) {
            //    console.log(key);
            //    console.log(value);
            //    let tr = document.createElement("tr");
            //    let th1 = document.createElement("th");
            //    let th2 = document.createElement("th");
            //    let addr_comp_type = document.createTextNode(key);
            //    let addr_comp_text = document.createTextNode(value);
            //    th1.appendChild(addr_comp_type);
            //    th2.appendChild(addr_comp_text);
            //    tr.appendChild(th1);
            //    tr.appendChild(th2);

            //    comp_table_body.appendChild(tr);
            //    console.log(comp_table_body);
            // }
         })
      } else {
         console.log("API error", response["status"]);
      }
})});