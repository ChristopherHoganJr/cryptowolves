let adaCoin = document.getElementById("adaCoin");
let bitCoin = document.getElementById("bitCoin");
let ethCoin = document.getElementById("ethCoin");

let chartDiv = document.getElementById("chart_div");

let coinDataKey = [];
let coinDataPrice = [];

function fetchMarketData(coin) {
  chartDiv.innerHTML = "";
  chartDiv.innerHTML += `<canvas id="myChart" width="400px" height="500px"></canvas>`;
  coinDataKey = [];
  coinDataPrice = [];
  fetch(
    `https://api.coingecko.com/api/v3/coins/${coin}/market_chart?vs_currency=usd&days=14&interval=daily`
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
              label: `${coin}`,
              data: coinDataPrice,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          plugins: {
            legend: false,
          },
        },
      });
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchMarketData("bitcoin");
