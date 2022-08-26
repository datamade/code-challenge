/* Connects the form to the API and render results
   in the #address-results div. */

$('.form').on('submit', function (event) {
   // Prevent default form submission behavior
   event.preventDefault();

   var address = getAddress();
   submitAddress(address);
});

function getAddress() {
   return $("#address").val().trim();
}

async function submitAddress(address) {
   var preparedAddress = address.replaceAll(" ", "+");
   try {
      fetch("api/parse?address=" + preparedAddress)
         .then((res) => handleResponse(res));
   } catch (error) {
      showError();
   }
}

async function handleResponse(response) {
   if (response.ok) {
      var jsonData = await response.json();
      writeResults(jsonData.address_type, jsonData.address_components);
   } else {
      showError();
   }
}

function writeResults(addressType, addressComponents) {
   // Write Address Type text
   $("#parse-type").text(addressType);

   // TODO Write Address Components table
   console.log(addressComponents);

   showResults();
}

function showResults() {
   showOrHideById("error", false)
   showOrHideById("address-results", true)
}

function showError() {
   showOrHideById("address-results", false)
   showOrHideById("error", true)
}

function showOrHideById(id, show) {
   var setting = show ? '' : 'none';
   $(`#${id}`).css("display", setting);
}
