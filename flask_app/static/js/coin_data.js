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
        <h2>${data.name}</h2>
        <img src="${data.image.small}" />
        <p>Symbol: ${data.symbol}</p>
        <p>Current Price: $${data.market_data.current_price.usd}</p>
        <p>Market Cap: $${data.market_data.market_cap.usd}</p>
        <p>Total Volume: $${data.market_data.total_volume.usd}</p>
      `;
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchCoinData();
