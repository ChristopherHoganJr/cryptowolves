let coinData = document.getElementById("coinData");
let x = new Date();
let day = x.getDate();
let month = x.getMonth();
let year = x.getFullYear();
if (day < 10) {
  day = `0${day}`;
}

month += 1;
if (month < 10) {
  month = `0${month}`;
}

function fetchCoinData() {
  fetch(
    `https://api.coingecko.com/api/v3/coins/ethereum/history?date=${day}-${month}-${year}`
  )
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      coinData.innerHTML += `
        <table>
          <tr>
            <td class="text-end pe-3">Symbol:</td>
            <td class="text-start">${data.symbol}</td>
          </tr>
          <tr>
            <td class="text-end pe-3">Current Price:</td>
            <td class="text-start">$${data.market_data.current_price.usd.toFixed(
              2
            )}</td>
          </tr>
          <tr>
            <td class="text-end pe-3">Market Cap:</td>
            <td class="text-start">$${data.market_data.market_cap.usd.toFixed(
              2
            )}</td>
          </tr>
          <tr>
            <td class="text-end pe-3">Total Volume:</td>
            <td class="text-start">$${data.market_data.total_volume.usd.toFixed(
              2
            )}</td>
          </tr>
        </table>
      `;
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchCoinData();
