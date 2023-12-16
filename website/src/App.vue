<script setup>
import Navbar from './Navbar.vue'
import { onMounted, ref } from 'vue';
import Plotly from 'plotly.js-dist-min';

import countries1 from '../data/countries-1.json';
import countries2 from '../data/countries-2.json';
import countries3 from '../data/countries-3.json';
import genres1 from '../data/genres-1.json';
import genres2 from '../data/genres-2.json';
import genres3 from '../data/genres-3.json';
import actors1 from '../data/actors-1.json';
import actors2 from '../data/actors-2.json';
import tropes1 from '../data/tropes-1.json';
import tropes2 from '../data/tropes-2.json';

const chartCountries1 = ref(null);
const chartCountries2 = ref(null);
const chartCountries3 = ref(null);
const chartGenres1 = ref(null);
const chartGenres2 = ref(null);
const chartGenres3 = ref(null);
const chartActors1 = ref(null);
const chartActors2 = ref(null);
const chartTropes1 = ref(null);
const chartTropes2 = ref(null);

const activeLamp = ref(true)

const flareColorScale = [
  [0, '#f6e8c3'],
  [0.28, '#fddbc7'],
  [0.42, '#f4a582'],
  [0.56, '#d6604d'],
  [0.70, '#b2182b'],
  [1.0, '#67001f']
];

function plotChart(chartRef, data, layout) {
  Plotly.newPlot(chartRef.value, data, layout);
}

function transformDataForPlotly(data, x_column, y_column, error_x_column, text_function = null) {
  let maxValue = data.length - 1;
  let trace = {
    x: data.map(item => item[x_column]),
    y: data.map(item => item[y_column]),
    hovertext: text_function ? data.map(item => text_function(item)) : null,
    error_x: {
      type: 'data',
      array: data.map(item => item[error_x_column]),
      visible: true
    },
    type: 'bar',
    orientation: 'h',
    marker: {
      color: data.map((_, index) => index / maxValue), // Assign a normalized value based on index
      colorscale: flareColorScale
    },
  };
  return [trace];
}

onMounted(() => {
  // Countries 1
  if (chartCountries1) {
    countries1.sort((a, b) => {
      return a.mean - b.mean;
    });

    const trace = transformDataForPlotly(countries1, 'mean', 'countries', 'sem', function (item) {
      return `Number of movies: ${item.count.toFixed(0)}`;
    })

    plotChart(chartCountries1, trace, {
      title: 'Mean Rating difference for Countries',
      xaxis: {
        title: 'Rating difference',
        automargin: true
      },
      yaxis: {
        title: 'Country',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Countries 2
  if (chartCountries2) {
    countries2.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    const trace = transformDataForPlotly(countries2, 'correlation', 'Country', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartCountries2, trace, {
      title: 'Pearson correlation coefficient for Countries',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Country',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Countries 3
  if (chartCountries3) {
    countries3.sort((a, b) => {
      return a.coef - b.coef;
    });
    const trace = transformDataForPlotly(countries3, 'coef', 'Country', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartCountries3, trace, {
      title: 'OLS coefficient for Countries',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Country',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 1
  if (chartGenres1) {
    genres1.sort((a, b) => {
      return a.rating_difference - b.rating_difference;
    });

    // keep the top 10 and bottom 10
    let bottom = genres1.slice(0, 10);
    let top = genres1.slice(-10);
    let genres1_filtered = bottom.concat(top);

    console.log(genres1)
    const trace = transformDataForPlotly(genres1_filtered, 'rating_difference', 'genres', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}`;
    })

    plotChart(chartGenres1, trace, {
      title: 'Mean rating difference for Genres',
      xaxis: {
        title: 'Rating difference',
        automargin: true
      },
      yaxis: {
        title: 'Genre',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 2
  if (chartGenres2) {
    genres2.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    let top = genres2.slice(-10);
    let bottom = genres2.slice(0, 10);
    let genres2_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(genres2_filtered, 'correlation', 'Genre', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartGenres2, trace, {
      title: 'Pearson correlation coefficient for Genres',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Genre',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Genres 3
  if (chartGenres3) {
    genres3.sort((a, b) => {
      return a.coef - b.coef;
    });

    const trace = transformDataForPlotly(genres3, 'coef', 'Genre', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartGenres3, trace, {
      title: 'OLS coefficient for Genres',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Genre',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Actors 1
  if (chartActors1) {
    actors1.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    // keep the top 10 and bottom 10
    let bottom = actors1.slice(0, 10);
    let top = actors1.slice(-10);
    let actors1_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(actors1_filtered, 'correlation', 'actor_name', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartActors1, trace, {
      title: 'Pearson correlation coefficient for Actors',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Actor',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Actors 2
  if (chartActors2) {
    actors2.sort((a, b) => {
      return a.coef - b.coef;
    });

    const trace = transformDataForPlotly(actors2, 'coef', 'actor_name', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartActors2, trace, {
      title: 'OLS coefficient for Actors',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Actor',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Tropes 1
  if (chartTropes1) {
    tropes1.sort((a, b) => {
      return a.correlation - b.correlation;
    });

    // keep the top 10 and bottom 10
    let bottom = tropes1.slice(0, 10);
    let top = tropes1.slice(-10);
    let tropes1_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(tropes1_filtered, 'correlation', 'Trope', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartTropes1, trace, {
      title: 'Pearson correlation coefficient for Tropes',
      xaxis: {
        title: 'Pearson correlation coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Trope',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }

  // Tropes 2
  if (chartTropes2) {
    tropes2.sort((a, b) => {
      return a.coef - b.coef;
    });

    let top = tropes2.slice(-10);
    let bottom = tropes2.slice(0, 10);
    let tropes2_filtered = bottom.concat(top);

    const trace = transformDataForPlotly(tropes2_filtered, 'coef', 'Trope', 'sem', function (item) {
      return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
    })

    plotChart(chartTropes2, trace, {
      title: 'OLS coefficient for Tropes',
      xaxis: {
        title: 'OLS coefficient',
        automargin: true
      },
      yaxis: {
        title: 'Trope',
        automargin: true
      },
      autosize: true,
      responsive: true,
    });
  }
});

function toggleLamp() {
  activeLamp.value = !activeLamp.value
}


</script>

<template>
  <Navbar />

  <!-- == HERO == -->
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

        <!-- == COUNTRIES == -->
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
                <div ref="chartCountries1" class="h-full min-h-[600px] w-full"></div>
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
                <div ref="chartCountries2" class="h-full min-h-[600px] w-full"></div>
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
                <div ref="chartCountries3" class="h-full min-h-[600px] w-full"></div>
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
            <div class="flex flex-col col-span-3 order-1 lg:col-span-1 lg:order-1 w-full items-center justify-center">
              <div class="flex flex-col h-full w-full items-center justify-center">
                <img src="/ego.png" alt="ego"
                  class="lg:w-full mt-4 drop-shadow-xl max-h-[400px] lg:max-h-none hover:scale-105 hover:drop-shadow-none transition duration-300" />
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
            <div class="flex flex-col  col-span-3 order-1 lg:col-span-1 lg:order-2 w-full items-center justify-center">
              <div class="flex flex-col  h-full w-full items-center justify-center">
                <img src="/remy.png" alt="remy"
                  class="lg:w-full max-h-[400px] lg:max-h-none drop-shadow-xl hover:scale-105 hover:drop-shadow-none transition duration-300" />
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

        
        <!-- == GENRES == -->
        <section id="genres" class="section">
          <h3 class="text-4xl font-bold mt-8">Genres</h3>
          <h5 class="text-xl italic text-slate-600">Crafting the Narrative of Preference</h5>

          <!-- Basic Viz -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartGenres3" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div> 
        </section>

        <!-- == AWARDS == -->
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

        <!-- == GENRES == -->
        <section id="actors" class="section">
          <h3 class="text-4xl font-bold mt-8">Actors</h3>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartActors1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartActors2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div> 
        </section>

        <!-- == TROPES == -->
        <section id="tropes" class="section">
          <h3 class="text-4xl font-bold mt-8">Tropes</h3>

          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-1 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartTropes1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>

          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <p class="mt-2 text-justify">
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quaerat debitis nemo aliquid vitae
                cum quos necessitatibus soluta reprehenderit officia, exercitationem inventore dolorem incidunt fugit
                repellendus laboriosam laudantium. Esse, facilis?
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde sit tempore quibusdam voluptates iste
                eligendi ipsam, natus molestiae aspernatur. Est porro doloremque sunt quam quae natus aperiam voluptate
                suscipit magnam?
              </p>
            </div>
            <div class="flex flex-col order-1 lg:order-2 w-full">
              <div class="flex flex-col h-full w-full">
                <div ref="chartTropes2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div> 
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
