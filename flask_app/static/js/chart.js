let coinDataKey = [];
let coinDataPrice = [];

function fetchMarketData(element, event) {
  fetch(
    "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=60&interval=daily"
  )
    .then((res) => res.json())
    .then((data) => {
      data.prices.forEach((e) => {
        coinDataKey.push(new Date(e[0]).toLocaleDateString("en-US"));
        coinDataPrice.push(e[1]);
      });
      const ctx = document.getElementById("myChart").getContext("2d");
      const myChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: coinDataKey,
          datasets: [
            {
              label: "Bitcoin",
              data: coinDataPrice,
            },
          ],
        },
      });
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchMarketData();
console.log(coinDataKey);
console.log(coinDataPrice);
