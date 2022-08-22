/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

document.addEventListener('DOMContentLoaded', () => {

   // Get the relevant page elements
   const addressForm = document.querySelector('form');
   const addressField = document.querySelector('#address');
   const addressResults = document.querySelector('#address-results');
   const parseType = document.querySelector('#parse-type');
   const addressTableBody = document.querySelector('tbody');

   // Parse and display address or error when form is submitted
   addressForm.onsubmit = () => {
      let addressInput = document.querySelector('#address').value;

      // Clear any prior errors
      if (document.querySelector('#error')) {
         document.querySelector('#error').remove();
      }
      // Hide any prior results 
      if (addressResults.style.display === 'block') {
         addressResults.style.display === 'none';
      }

      fetch(`api/parse/?input=${addressInput}`)
      .then(response => response.json())
      .then(data => {
         if (data.error) {
            // Clear the form field for the next attempt
            addressField.value = '';
            // Display the error message
            let errorDiv = document.createElement('div');
            errorDiv.id = 'error';
            let error = document.createElement('h4');
            error.className = 'error';
            error.textContent = `Error: ${data.error}`;
            let message = document.createElement('p');
            message.textContent = data.message;
            errorDiv.append(error, message);
            document.querySelector('.container').append(errorDiv);
         } else {
            // Display the address type and components table
            let addressType = data.address_type;
            parseType.textContent = addressType;
            let addressComponents = data.address_components;
            for (const component in addressComponents) {
               let row = document.createElement('tr');
               let addressPart = document.createElement('td');
               addressPart.textContent = addressComponents[component];
               let tag = document.createElement('td');
               tag.textContent = component;
               row.append(addressPart, tag);
               addressTableBody.append(row);
            }
            // Unhide the results div
            addressResults.style.display = 'block';
         }
      });
      // Stop the form from actually submitting
      return false;
   }
});
