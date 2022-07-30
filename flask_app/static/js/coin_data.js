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

function fetchCoinData(coin) {
  coinData.innerHTML = "";
  fetch(
    `https://api.coingecko.com/api/v3/coins/${coin}/history?date=${day}-${month}-${year}`
  )
    .then((res) => res.json())
    .then((data) => {
      coinData.innerHTML += `
        <table class="table">
          <tr>
            <td class="text-end pe-3"><h2>Symbol:</h2></td>
            <td class="text-start"><h2>${data.symbol.toUpperCase()}</h2></td>
          </tr>
          <tr>
            <td class="text-end pe-3"><h4>Today's Average Price:</h4></td>
            <td class="text-start"><h4>$${data.market_data.current_price.usd.toFixed(
              2
            )}</h4></td>
          </tr>
          <tr>
            <td class="text-end pe-3"><h4>MC as of ${month}-${day}-${year}:</h4></td>
            <td class="text-start"><h4>$${data.market_data.market_cap.usd.toFixed(
              2
            )}</h4></td>
          </tr>
          <tr>
            <td class="text-end pe-3"><h4>24H Total Volume:</h4></td>
            <td class="text-start"><h4>$${data.market_data.total_volume.usd.toFixed(
              2
            )}</h4></td>
          </tr>
        </table>
      `;
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchCoinData("bitcoin");
