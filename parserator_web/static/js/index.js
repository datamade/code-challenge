const $form = $(".form");
const $addressInput = $("#address");
const $addressResults = $("#address-results");
const $parseType = $("#parse-type");
const $resultsTableBody = $("tbody");
const $errorMessage = $("<p>")
   .attr("id", "error-message")
   .addClass("text-danger d-inline-block mx-4");
const DEFAULT_ERROR_MESSAGE = "Could not parse address";
const API_URL = "/api/parse/"

$form.on("submit", (evt) => {
   evt.preventDefault();
   handleSubmit();
});

/** handleSubmit:
 * Handles user form input;
 * calls functions to fetch parsed data and display results/errors
 */
async function handleSubmit() {
   const input = $addressInput.val();

   try {
      const parsedAddressData = await fetchParsedAddressData(input);
      renderResults(
         parsedAddressData.address_components,
         parsedAddressData.address_type
      );
   } catch (e) {
      renderErrorMessage(e.message);
   }
}

/** fetchParsedAddressData:
 * fetches parsed address data from API
 * @param {String} address
 * @returns {Object} parsed address data, from JSON response
 * @throws Error on bad request
 */
async function fetchParsedAddressData(address) {
   const params = new URLSearchParams({ address });
   const response = await fetch(`${API_URL}?${params}`);
   const parsedAddressData = await response.json();

   if (response.status != 200) {
      throw new Error(parsedAddressData.error || DEFAULT_ERROR_MESSAGE);
   }

   return parsedAddressData;
}

/** renderResults:
 * Displays parsed address components and information in UI
 * @param {Object} addressComponents tagged address components
 * @param {String} addressType
 */
function renderResults(addressComponents, addressType) {
   clearResultsDisplay();

   $parseType.text(addressType);
   fillResultsTableBody(addressComponents);
}

/** renderErrorMessage:
 * Displays an error message in UI
 * @param {String} message error message
 */
function renderErrorMessage(message) {
   $errorMessage.text(message);
   $form.append($errorMessage);
}

/** fillResultsTableBody:
 * builds displayed table of address components in UI
 * @param {Object} addressComponents like {component: tag, ...}
 */
function fillResultsTableBody(addressComponents) {
   for (const addressPart in addressComponents) {
      const $row = $("<tr>");
      const tag = addressComponents[addressPart];
      $row.append(
         $("<td>").text(addressPart),
         $("<td>").text(tag)
      );
      $resultsTableBody.append($row);
   }
}

/** clearResultsDisplay:
 * resets UI, in order to display new results
 */
function clearResultsDisplay() {
   $errorMessage.remove();
   $resultsTableBody.empty();
   $addressResults.removeClass("d-none");
}
