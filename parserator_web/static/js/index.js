
/**
 * query selectors for button, user input, and query results
 */
const submitButton = document.querySelector(".btn")
const addressInput = document.querySelector(".form-control")
const addressResults = document.querySelector(".address-results")

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

/**
 * clean up function to set up input for new address inputs
 */
const resetDisplay = () => {
   toggleView(false, addressResults)
   setInnerHTML(false, '.error')
   setInnerHTML('.table')
   setInnerHTML('#parse-type')
}

/**
 * @param {Object} result - parsed query body
 * displays user results if query is successful 
 */
const displayResults = result => {
   const addressType = result['address_type']
   const addressComponents = result['address_components']
   setInnerHTML('.table', formatParsedAddress(addressComponents))
   setInnerHTML('#parse-type', addressType)
   toggleView(true, '#address-results')
}

/**
 * @param {event} - submit button event
 */

const parseUserInput = event => {
   event.preventDefault()
   resetDisplay()
   try {
      const input = addressInput.value
      if(!checkInput) {
         return   
      }
      fetchAddress(input)
         .then((result) => {
            if(result['error']) {
               toggleView(true, '.error')
               return
            }
         displayResults(result)
      })
   } catch(error) {
      toggleView(true, '.error')
      console.error('Error found in parseUserInput', error)
   }
}


submitButton.addEventListener("click", displayResults)


