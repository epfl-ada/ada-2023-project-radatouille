<script setup>
import Navbar from './Navbar.vue'
import { onMounted, ref } from 'vue';
import Chart from 'chart.js/auto';
import countries1 from '../data/countries-1.json';
import countries2 from '../data/countries-2.json';
import countries3 from '../data/countries-3.json';

const activeLamp = ref(true)

function toggleLamp() {
  activeLamp.value = !activeLamp.value
}

const chartCountries1 = ref(null);
const chartCountries2 = ref(null);
const chartCountries3 = ref(null);

onMounted(() => {
  if (chartCountries1.value) {
    const sortedData1 = countries1.sort((a, b) => a.mean - b.mean);
    const ctx1 = chartCountries1.value.getContext('2d');

    const datasets1 = [{
      label: 'Rating difference',
      data: sortedData1.map(item => item.mean),
      backgroundColor: sortedData1.map(item => item.mean > 0 ? 'rgba(0, 0, 255, 0.2)' : 'rgba(255, 0, 0, 0.2)'),
      borderColor: sortedData1.map(item => item.mean > 0 ? 'rgba(0, 0, 255, 1)' : 'rgba(255, 0, 0, 1)'),
      borderWidth: 1
    }];

    const chartData1 = sortedData1.map(item => ({
      label: item.countries,
      value: item.mean,
      error: item.sem
    }));

    const tooltip1 = {
      callbacks: {
        label: (context) => {
          const label = context.dataset.label;
          const value = context.raw;
          const item = chartData1[context.dataIndex];
          return [`${label}: ${value}`, `CI: ${item.error}`];
        }
      }
    };

    renderChart(chartData1, ctx1, datasets1, "Average rating difference by country");
  }
  if (chartCountries2.value) {
    const sortedData2 = countries2.sort((a, b) => a.correlation - b.correlation);
    const ctx2 = chartCountries2.value.getContext('2d');

    const datasets2 = [{
      label: 'Pearson coefficient',
      data: sortedData2.map(item => item.correlation),
      backgroundColor: sortedData2.map(item => item.correlation > 0 ? 'rgba(0, 0, 255, 0.2)' : 'rgba(255, 0, 0, 0.2)'),
      borderColor: sortedData2.map(item => item.correlation > 0 ? 'rgba(0, 0, 255, 1)' : 'rgba(255, 0, 0, 1)'),
      borderWidth: 1
    }]

    const chartData2 = sortedData2.map(item => ({
      label: item.country,
      value: item.correlation,
      error: item.upper_ci - item.correlation,
      upper_ci: item.upper_ci,
      lower_ci: item.lower_ci,
      p_value: item.p_value
    }));

    const tooltip2 = {
      callbacks: {
        label: (context) => {
          const label = context.dataset.label;
          const value = context.raw;
          const item = chartData2[context.dataIndex];
          return [`${label}: ${value}`, `P-value: ${item.p_value}`, `Upper CI: ${item.upper_ci}`, `Lower CI: ${item.lower_ci}`];
        }
      }
    };


    renderChart(chartData2, ctx2, datasets2, tooltip2, "Pearson coefficient by country for rating difference");
  }
  if (chartCountries3.value) {
    const sortedData3 = countries3.sort((a, b) => a.coef - b.coef);
    const ctx3 = chartCountries3.value.getContext('2d');

    const datasets3 = [{
      label: 'OLS coefficient',
      data: sortedData3.map(item => item.coef),
      backgroundColor: sortedData3.map(item => item.coef > 0 ? 'rgba(0, 0, 255, 0.2)' : 'rgba(255, 0, 0, 0.2)'),
      borderColor: sortedData3.map(item => item.coef > 0 ? 'rgba(0, 0, 255, 1)' : 'rgba(255, 0, 0, 1)'),
      borderWidth: 1
    }]

    const chartData3 = sortedData3.map(item => ({
      label: item.country,
      value: item.coef,
      error: item.upper_ci - item.coef,
      upper_ci: item.upper_ci,
      lower_ci: item.lower_ci,
      p_value: item.p_value
    }));

    const tooltip3 = {
      callbacks: {
        label: (context) => {
          const label = context.dataset.label;
          const value = context.raw;
          const item = chartData3[context.dataIndex];
          return [`${label}: ${value}`, `P-value: ${item.p_value}`, `Upper CI: ${item.upper_ci}`, `Lower CI: ${item.lower_ci}`];
        }
      }
    };


    renderChart(chartData3, ctx3, datasets3, tooltip3, "OLS coefficient by country for rating difference");
  }
});


const renderChart = (chartData, ctx, datasets, tooltip, chart_title = "") => {

  const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: chartData.map(d => d.label),
      datasets: datasets
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scaleShowValues: true,
      indexAxis: 'y', // Horizontal bar chart
      scales: {
        x: {
          beginAtZero: true
        },
        y: {
          ticks: {
            callback: (value, index) => {
              return chartData[index].label;
            },
            autoSkip: false,
            font: {
              size: 12
            }
          },
        }
      },
      plugins: {
        title: {
          display: true,
          text: chart_title,
          font: {
            size: 14
          }
        },
        legend: {
          display: false
        },
        tooltip: tooltip
      },
      'onClick': (event, activeElements, chart) => {
        if (activeElements.length > 0) {
          const activeIndex = activeElements[0].index;
          console.log('Clicked on bar:', chartData[activeIndex]);
        }
      }
    },
    plugins: [{
      id: 'customErrorBars',
      afterDraw: chart => {
        const ctx = chart.ctx;
        chart.data.datasets.forEach((dataset, datasetIndex) => {
          const meta = chart.getDatasetMeta(datasetIndex);
          if (!meta.hidden) {
            meta.data.forEach((element, index) => {
              const errorValue = chartData[index].error;
              const xValue = chart.scales.x.getPixelForValue(chartData[index].value);
              const errorMargin = chart.scales.x.getPixelForValue(errorValue) - chart.scales.x.getPixelForValue(0);

              ctx.save();
              ctx.strokeStyle = 'black';
              ctx.lineWidth = 2;
              ctx.beginPath();
              ctx.moveTo(xValue - errorMargin, element.y);
              ctx.lineTo(xValue + errorMargin, element.y);
              ctx.stroke();
              ctx.restore();
            });
          }
        });
      }
    }]
  });
};

</script>

<template>
  <Navbar />

  <!-- Hero -->
  <div
    class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
    <h1 class="text-3xl lg:text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">Why the New
      York Times
      doesn't like
      Marvel movies</h1>
    <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain movie
      taste differences between users and critics</h3>
    <div class="flex flex-col items-center mt-auto px-5 py-3">
      <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] mt-3">A project by</span>
      <div class="flex flex-wrap gap-1 items-center justify-center mt-2">
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Antonin Faure</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Baptiste Lecoeur</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Enzo Palmisano</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Jamil Maj</span>
        <span class="hidden lg:block drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">&bull;</span>
        <span class="drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">Mariella Daghfal</span>
      </div>
    </div>
  </div>

  <!-- Main -->
  <main class="grid grid-cols-5 w-full items-center overflow-hidden text-justify">
    <!--
    <div class="cols-1 pl-8">
      <div class="lamp-container">
        <img :src="activeLamp ? '/lamp_right.png' : '/lamp_face.png'" alt="lamp face" class="lamp cursor-pointer"
          @click="toggleLamp" />
        <svg v-show="activeLamp" class="light-aura" width="1000" height="600" viewBox="0 0 500 300"
          preserveAspectRatio="xMidYMin slice">
          <polygon points="350,100 800,100 204,6 197,16" fill="yellow" />
        </svg>
      </div>
    </div>
    -->
    <div class="flex col-span-5 px-10 lg:px-8 lg:col-span-3 lg:col-start-2 flex-col py-8 w-full max-w-screen-lg">
      <section id="introduction" class="section">
        <h2 class="text-5xl font-bold mt-5">Introduction</h2>
        <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
          consequat
          aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>


        <section id="users" class="section">
          <h3 class="text-4xl font-bold mt-8">Users</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="critics" class="section">
          <h3 class="text-4xl font-bold mt-8">Critics</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="different-tastes" class="section">
          <h3 class="text-4xl font-bold mt-8">Different tastes</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>
      </section>

      <section id="exploration" class="section">
        <h2 class="text-5xl font-bold mt-8">Exploration</h2>

        <section id="countries" class="section">
          <h3 class="text-4xl font-bold mt-8">Countries</h3>
          <p class="mt-2 text-justify">
            In the grand kitchen of our data-driven analysis, let's craft a narrative as we
            examine the intricate relationship between a film's country of origin and its critical reception. To whet our
            appetites for understanding, we must first visually savor the prepared plots—each a dish to be dissected for
            its unique storytelling flavors.
          </p>

          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <h4 class="text-xl font-bold">Act I: The Visual Appetizer - Rating Difference by Country</h4>
              <p class="mt-2 text-justify">
                This barplot is the first course, served to display the average rating differences by country. The bars
                stretch across the taste spectrum, from the savory highs to the unseasoned lows. The length and direction
                of
                each bar speak to the divergence in cinematic taste—where a film from one country may be the toast of
                critics,
                yet the same film might not suit the public's palate. Countries like France and Italy, with longer bars
                stretching towards the positive side, may suggest a gourmet blend of critical and public agreement. In
                contrast, the United States stands out with a bar extending negatively, indicating a potential
                fast-food-like
                consumption where box office appeal does not translate into critical success.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <canvas ref="chartCountries1" class="h-full min-h-[600px] w-full"></canvas>
              </div>
            </div>
          </div>

          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <h4 class="text-xl font-bold">Act II: The Main Course - Pearson and OLS Coefficients</h4>
              <p class="mt-2 text-justify">
                The Pearson coefficient plot is the main course, providing a more nuanced flavor profile of each country's
                cinematic output. Each bar, with its confidence interval whiskers, indicates the strength and direction of
                the relationship between a film's country of origin and its rating difference. Notice the subtle hints of
                positive correlations for France and Iran, suggesting that films from these regions carry a certain je ne
                sais quoi that resonates with critics. On the flip side, the United States and Canada show negative
                correlations, implying a different critical reception, perhaps due to the commercial seasoning of their
                film industries.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <canvas ref="chartCountries2" class="h-full min-h-[600px] w-full"></canvas>
              </div>
            </div>
          </div>


          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Next to it, we present the OLS coefficients plot, a complementary dish that illustrates the impact of each
                country when other ingredients in our analysis are held constant. Here, Iran's positive coefficient is
                robust, further validating the country's standing with critics. The negative coefficients for powerhouses
                like the United States and India are stark, reinforcing the narrative that commercial success is not a
                guaranteed recipe for critical acclaim.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <canvas ref="chartCountries3" class="h-full min-h-[600px] w-full"></canvas>
              </div>
            </div>
          </div>

          <div class="grid mt-8 w-full gap-5">
            <h4 class="text-xl font-bold">Act III: Decoding the Dish - Dissecting the Differences in Country
              Coefficients</h4>
            <p class="mt-2 text-justify">
              Let's delve deeper into the gourmet guide of global cinema by closely examining and comparing the plots
              that serve as our visual menu.
            </p>
            <p class="text-justify">
              Firstly, the Pearson plot offers us a raw measure of the relationship between the country of origin and
              the rating difference. Countries like France, with a correlation of 0.141 and a p-value strikingly close
              to zero, showcase a strong positive alignment with critic ratings. Iran follows suit but with a lesser
              correlation of 0.065, still significant enough to suggest that its films are savored by critics. The plot
              also reveals the statistical significance (p-value) of these relationships, emphasizing the reliability of
              our findings.
            </p>
            <p>
              In contrast, the OLS coefficients plot refines this relationship by controlling for multiple variables.
              Here, we see Iran's coefficient soaring to 7.383, a testament to its films' critical acclaim when other
              factors are constant. This is contrasted by the United States, which sees a negative coefficient of
              -5.8119, painting a picture of a cinematic giant whose films are, perhaps, too rich in mainstream appeal
              for the critic's more selective taste.
            </p>
          </div>

          <div class="grid lg:grid-cols-3 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2 col-span-2">
              <h4 class="text-xl font-bold">Comparative Analysis: Tasting Notes on Methodologies</h4>
              <p class="mt-3">
                Comparing the two plots, we note a shift in the order of countries and the magnitude of their influence.
                For
                example, while France tops the Pearson plot, Iran takes the lead in the OLS analysis, highlighting how
                controlling for other variables can change the taste profile of our data dish.
                </p>
                <p class="mt-3">
                The Pearson method offers simplicity and a direct taste test of correlation, but it can't account for the
                complex mix of ingredients that go into film ratings. It's like tasting a sauce before it's been fully
                seasoned - useful, but not the complete flavor. Its advantages lie in its straightforward interpretation,
                but it falls short by not considering other potentially confounding spices.
              </p>
              <p class="mt-3">
                The OLS method, however, simmers down the data to control for various elements, akin to a slow-cooked stew
                that melds flavors together for a more comprehensive profile. This method allows us to taste the unique
                contribution of each country, but it can be a complex dish to digest, requiring assumptions like linearity
                and normality that may not always hold. One drawback is that significant results can be influenced by
                outliers, just like how a single overpowering spice can skew the taste of a dish.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <img src="/ego.png" alt="ego"
                  class="w-full mt-4 drop-shadow-xl hover:scale-105 hover:drop-shadow-none transition duration-300" />
              </div>
            </div>
          </div>

          <div class="grid lg:grid-cols-3 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 col-span-2">
              <h4 class="text-xl font-bold">Serving the Final Course: Conclusions with a Pinch of Precision</h4>
              <p class="mt-2">
                Next to it, we present the OLS coefficients plot, a complementary dish that illustrates the impact of each
                country when other ingredients in our analysis are held constant. Here, Iran's positive coefficient is
                robust, further validating the country's standing with critics. The negative coefficients for powerhouses
                like the United States and India are stark, reinforcing the narrative that commercial success is not a
                guaranteed recipe for critical acclaim.
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <img src="/remy.png" alt="remy"
                  class="w-full drop-shadow-xl hover:scale-105 hover:drop-shadow-none transition duration-300" />
              </div>
            </div>
          </div>
          <div class="mt-4">
            <p>
              From our analysis, we draw the following conclusions with a side of statistical seasoning:
            </p>

            <div class="grid grid-cols-4 gap-5 mt-5">
              <div>
                <img src="/fr-flag.gif" alt="france" class="object-contain mr-2 mt-1" />
              </div>
              <div class="col-span-3">
                <span class="font-bold">France's Culinary Cinema:</span> With a Pearson correlation of 0.141 and an OLS
                coefficient of 2.5774, both
                highly
                significant, France stands out as the gourmet capital in the cinematic world. Its films are consistently
                well-received by critics, suggesting a recipe that perfectly balances mainstream appeal with artistic
                depth.
              </div>
              <div>
                <img src="/ir-flag.gif" alt="iran" class="object-contain mr-2 mt-1" />
              </div>
              <div class="col-span-3">
                <span class="font-bold">Iran's Exotic Flavors:</span> Iran's cinema, with a Pearson correlation of 0.065
                and an OLS coefficient of
                7.3831,
                is like a rare spice that has a profound impact when discovered by critics. These numbers suggest that
                Iranian films, while fewer in number (37 films), leave a strong impression, perhaps due to their unique
                storytelling and cultural authenticity.
              </div>
              <div>
                <img src="/us-flag.gif" alt="usa" class="object-contain mr-2 mt-1" />
              </div>
              <div class="col-span-3">
                <span class="font-bold">The United States' Fast Food Film Industry:</span> The U.S. presents a Pearson
                correlation of -0.220
                and an OLS
                coefficient of -5.8119, indicating that while its films may be consumed en masse, they often do not
                satisfy
                the critic's hunger for what they consider a five-star cinematic experience. The negative coefficient
                suggests a consistent critical underestimation, possibly due to the formulaic and commercial nature of
                Hollywood's productions.
              </div>
              <div>
                <img src="/in-flag.gif" alt="india" class="object-contain mr-2 mt-1" />
              </div>
              <div class="col-span-3">
                <span class="font-bold">India's Bollywood Effect:</span> The Indian film industry, with its heart in
                Bollywood, shows a notably negative
                OLS coefficient (-5.1296). Given that this metric studies the difference between IMDb ratings and
                Metascore,
                a negative value here indicates that Indian films, especially those from the Bollywood sector, are
                generally
                rated higher by audiences than by critics. This could point to a cultural divide where the elements that
                make Bollywood films endearing to their large audience—such as song and dance, melodrama, and escapist
                narratives—may not translate into the critical acclaim on an international scale, leading to a lower
                Metascore.
              </div>
            </div>
            <p class="mt-5">
              In the grand dining hall of global cinema, it appears that critics tend to favor films that
              offer a
              distinct cultural voice, complex narratives, and a strong artistic vision—qualities that are often
              highlighted in French and Iranian films. Conversely, industries known for their box office prowess, such as
              Hollywood and Bollywood, might prioritize elements that ensure commercial success—an industry that caters to
              mass appeal rather than the gourmet tastes of critics.
            </p>
          </div>

        </section>

        <section id="awards" class="section">
          <h3 class="text-4xl font-bold mt-8">Awards</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="genres" class="section">
          <h3 class="text-4xl font-bold mt-8">Genres</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="release-year" class="section">
          <h3 class="text-4xl font-bold mt-8">Release Year</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="runtime" class="section">
          <h3 class="text-4xl font-bold mt-8">Runtime</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="actors" class="section">
          <h3 class="text-4xl font-bold mt-8">Actors</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>

        <section id="plot" class="section">
          <h3 class="text-4xl font-bold mt-8">Plot</h3>
          <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
        </section>
      </section>

      <section id="conclusion" class="section">
        <h2 class="text-5xl font-bold mt-8">Conclusion</h2>
        <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
          consequat
          aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
          ipsum
          aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
      </section>
    </div>
  </main>
</template>

<style scoped>
.section {
  padding-top: 50px;
  margin-top: -50px;
}

.lamp-container {
  position: relative;
}


.lamp {
  width: 200px;
  /* Adjust as per your image size */
  display: block;
  z-index: 2;
  left: 0;
  position: relative;
  height: auto;
}

.light-aura {
  position: absolute;
  top: 0;
  left: 0;
  /* Start the aura right at the end of the lamp */
  /* Extend to the rest of the viewport */
  height: 300vh;
  z-index: 1;
  opacity: 0.5;
  /* Ensures the light aura is behind the lamp */
}
</style>
