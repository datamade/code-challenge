/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

   $('.form').on('submit', function () {
      var address = document.getElementById('address').value;
      alert(`Submitted form with: ${address}`);
  });
  