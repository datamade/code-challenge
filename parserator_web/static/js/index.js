/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

document.addEventListener('DOMContentLoaded', () => {
   const addressForm = document.querySelector('form');
   addressForm.onsubmit = () => {
      let addressInput = document.querySelector('#address').value;
      fetch(`api/parse/?input=${addressInput}`)
      .then(response => response.json())
      .then(data => {
         console.log(data);
      });
   }
});
