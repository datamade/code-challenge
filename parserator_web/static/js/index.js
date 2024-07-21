/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form')
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const address = document.querySelector('#address').value
    fetch(`/api/parse/?address=${encodeURIComponent(address)}`)
      .then(response => {
        return response.json()
      })
      .then(data => {
        const resultsDiv = document.querySelector('#address-results')
        const errorDiv = document.querySelector('#error-message')
        if (data.error) {
          resultsDiv.style.display = 'none'
          errorDiv.style.display = 'block'
          errorDiv.textContent = data.error
        } else {
          errorDiv.style.display = 'none'
          resultsDiv.style.display = 'block'
          document.querySelector('#parse-type').textContent = data.address_type
          const tbody = resultsDiv.querySelector('tbody')
          tbody.innerHTML = ''
          for (const [key, value] of Object.entries(data.address_components)) {
            const row = document.createElement('tr')
            const cell1 = document.createElement('td')
            cell1.textContent = key
            const cell2 = document.createElement('td')
            cell2.textContent = value
            row.appendChild(cell1)
            row.appendChild(cell2)
            tbody.appendChild(row)
          }
        }
      })
      .catch(error => {
        console.error('Error:', error)
      })
  })
})
