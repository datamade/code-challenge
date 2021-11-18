/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

 

   document.getElementById('submit').addEventListener('click', function() {


      $.ajax({
         url: 'http://localhost:8000/api/parse',
         datatype: 'json',
         type: 'GET',
         data: {
            input_string: document.getElementById('address').value
         },
         success: function(data) {
            alert(data['input_string'])
         }
      })

   })
