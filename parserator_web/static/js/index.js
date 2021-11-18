/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

   const fillAddressResults = (data) => {
      document.getElementById('address-results').style = "display:block";
      tblbdy = document.querySelector('table.table tbody');

      for ( let i = 0; i < 2; i++) {
         let row = document.createElement("tr");

         for ( let j = 0; j < 2; j++) {
            let cell = document.createElement("td");
            let cellText = document.createTextNode("Test"+i)

            cell.appendChild(cellText)
            row.appendChild(cell)
         }

         tblbdy.appendChild(row)
      }


   }
 

   document.getElementById('submit').addEventListener('click', function(event) {

      event.preventDefault();

      $.ajax({
         url: 'http://localhost:8000/api/parse',
         datatype: 'json',
         type: 'GET',
         data: {
            input_string: document.getElementById('address').value
         },
         success: function(data) {
            fillAddressResults(data)
         }
      })

   })
