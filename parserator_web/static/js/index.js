const submitButton = document.querySelector(".btn")
const addressInput = document.querySelector(".form-control")
const addressResults = document.querySelector(".address-results")
const resultsTable = document.querySelector(".results-table")

/** check if input is correct type before sending query
  * @param {string} input - user's address input
  * @returns {boolean} - is the input longer than 0 
  */

const checkInput = input => {
   return input.length
}

/**
 * @param {string} userInput - user's address input
 * @returns {Promise<void>} - async call parse input address using await to parse response body
 */

const fetchAddress = async (userInput) => {
   const response = await fetch(`api/parse/?address=${userInput}`)
   const body = await response.json()
   return body
}

/**
 * @param {Object} addressComponents - results from query
 * key - component tag, value - parsed input section
 * @returns {string} - html table sections, joined into string
 */

const formatParsedAddress = addressComponents => {
   const components = Object.keys(addressComponents)
   const componentHTML = components.map(component => 
      `
      <tr>
         <th>${addressComponents[component]}</th>
         <th>${component}</th>
      </tr>
      `
   )
   return componentHTML.join('')
}

const setInnerHTML = (id, insert) => {
   const element = document.querySelector(id)
   element.innerHTML = insert
}

/**
 * 
 * @param {boolean} isShown - should table be displayed? 
 * @param {string} id - id/class used to query select element from html
 * updates the dom, doesn't return anything
 */

const toggleView = (isShown, id) => {
   const showDiv = document.querySelector(id)
   showDiv.style = isShown ? "" : "display:none"
}

const displayError = () => {
   //add error area in HTML?
}


const displayResults = (e) => {
   e.preventDefault()
   if (Event.target == submitButton) {
      sendAddress(addressInput.value)
         .then((result) => {

         })
   }
}

submitButton.addEventListener("click", displayResults)


