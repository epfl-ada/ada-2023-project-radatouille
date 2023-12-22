<template>
  <div class="flex flex-col gap-2 pt-6">
    <select v-model="selectedCriteriaType" @change="updateCriteria"
      class="p-3 rounded-xl bg-slate-700 text-white font-semibold">
      <option value="genre">Genres</option>
      <option value="actor">Actors</option>
      <option value="trope">Tropes</option>
      <option value="award">Awards</option>
      <option value="country">Countries</option>
      <option value="year">Years</option>
    </select>

    <div class="flex gap-3">
      <input type="range" v-if="selectedCriteriaType === 'year'" v-model="selectedYear" :min="yearRange[0]"
        :max="yearRange[yearRange.length - 1]" @change="updateYearSlider" class="w-full" @input="inputYearSlider" />
      <span v-if="selectedCriteriaType === 'year'">{{ selectedYear }}</span>
    </div>

    <select class="mb-3 p-3 rounded-xl bg-slate-400 text-white font-semibold" v-if="selectedCriteriaType !== 'year'"
      v-model="selectedCriteria" @change="updateGraph">
      <option v-for="option in criteriaOptions" :key="option" :value="option">{{ option }}</option>
    </select>

    <span><span class="text-black font-semibold ml-1">Number of movies:</span> {{ nMoviesSelected }}</span>
    <span><span class="text-black font-semibold ml-1 mb-3">Mean rating difference:</span> {{ meanRatingDiffSelected
    }}</span>
    <span v-if="olsCoefficient"><span class="text-black font-semibold ml-1 mb-3">OLS coefficient:</span> {{ olsCoefficient
    }} ({{ olsCoefficient > 0 ? "Critics Oriented" : "Users Oriented" }})</span>

    <div ref="playgroundScatterPlot" class="aspect-square"></div>
    <div ref="playgroundHistogramPlot"></div>
  </div>
</template>
  
<script setup>
import Plotly from 'plotly.js-basic-dist-min'
import { onMounted, ref } from 'vue';
const BASE_URL = import.meta.env.VITE_BASE_URL;

const moviesData = ref([]);

const genresData = ref({});
const actorsData = ref({});
const yearsData = ref({});
const tropesData = ref({});
const awardsData = ref({});
const countriesData = ref({});

const yearRange = ref([]);

const selectedYear = ref(null);

const nMoviesSelected = ref(0);
const meanRatingDiffSelected = ref(0);
const olsCoefficient = ref(0);

const playgroundScatterPlot = ref(null);
const playgroundHistogramPlot = ref(null);

const selectedCriteriaType = ref('genre'); // Default criteria type
const selectedCriteria = ref(null);
const criteriaOptions = ref([]);

const updateCriteria = () => {
  // Reset selected criteria
  selectedCriteria.value = null;

  // Update criteria options based on selected criteria type
  switch (selectedCriteriaType.value) {
    case 'genre':
      criteriaOptions.value = Object.keys(genresData.value);
      break;
    case 'actor':
      criteriaOptions.value = Object.keys(actorsData.value);
      break;
    case 'year':
      criteriaOptions.value = Object.keys(yearsData.value);
      selectedYear.value = criteriaOptions.value[0];
      break;
    case 'trope':
      criteriaOptions.value = Object.keys(tropesData.value);
      break;
    case 'award':
      criteriaOptions.value = Object.keys(awardsData.value);
      break;
    case 'country':
      criteriaOptions.value = Object.keys(countriesData.value);
      break;
  }

  selectedCriteria.value = criteriaOptions.value[0];
  updateGraph()
};

const inputYearSlider = () => {
  let closest = yearRange.value.reduce((a, b) => {
    return Math.abs(b - selectedYear.value) < Math.abs(a - selectedYear.value) ? b : a;
  });

  selectedYear.value = closest;
}

const updateYearSlider = () => {
  selectedCriteria.value = selectedYear.value.toString();
  updateGraph();
};

const fetchData = async (path) => {
  const originUrl = window.location.origin;

  if (BASE_URL && BASE_URL !== '/') return await fetch(`${originUrl}/${BASE_URL}/${path}`).then(response => response.json());

  return await fetch(`${originUrl}/${path}`).then(response => response.json());
};


onMounted(async () => {

  fetchData('/data/playground-movies.json').then(data => {
    moviesData.value = data;
  });
  fetchData('/data/playground-genres.json').then(data => {
    genresData.value = data;
    initGraph()
    updateCriteria();
  });
  fetchData('/data/playground-actors.json').then(data => {
    actorsData.value = data;
  });
  fetchData('/data/playground-releaseyear.json').then(data => {
    yearsData.value = data;
    yearRange.value = [...Object.keys(yearsData.value).map(year => parseInt(year))].sort((a, b) => a - b);
  });
  fetchData('/data/playground-tropes.json').then(data => {
    tropesData.value = data;
  });
  fetchData('/data/playground-awards.json').then(data => {
    awardsData.value = data;
  });
  fetchData('/data/playground-countries.json').then(data => {
    countriesData.value = data;
  });


});

const initGraph = () => {
  const scatterData = [{
    x: moviesData.value.map(movie => movie.metascore),
    y: moviesData.value.map(movie => movie.imdb_rating_scaled),
    mode: 'markers',
    type: 'scatter',
    hovertext: moviesData.value.map(movie => movie.name)
  }, {
    x: [0, 100],
    y: [0, 100],
    mode: 'lines',
    type: 'scatter',
    name: 'x=y',
    line: {
      dash: 'dot',
      width: 2,
      color: 'grey'
    }
  }]

  const scatterLayout = {
    xaxis: {
      range: [0, 105],
      title: 'Metascore'
    },
    yaxis: {
      range: [0, 105],
      title: 'IMDB Rating Scaled',
      scaleratio: 1,
      automargin: true
    },
    margin: {
      l: 70,
      r: 50,
      b: 70,
      t: 50,
      pad: 4
    },
    showlegend: false
  };

  const filteredMovies = []

  // Data for histogram
  const histogramData = [{
    x: filteredMovies.map(movie => movie.rating_difference),
    type: 'histogram',
    marker: { color: '#d62728' }
  }];

  // Layout for histogram
  // Define layout for histogram
  const histogramLayout = {
    title: 'Rating Difference Histogram',
    xaxis: { title: 'Rating Difference' },
    yaxis: { title: 'Count' }
  };

  // Create playground histogram plot
  Plotly.newPlot(playgroundHistogramPlot.value, histogramData, histogramLayout);

  // Create playground scatter plot
  Plotly.newPlot(playgroundScatterPlot.value, scatterData, scatterLayout);
};

const updateGraph = () => {
  let selectedIds;
  switch (selectedCriteriaType.value) {
    case 'genre':
      selectedIds = genresData.value[selectedCriteria.value].ids;
      olsCoefficient.value = genresData.value[selectedCriteria.value].ols_coefficient;
      break;
    case 'actor':
      selectedIds = actorsData.value[selectedCriteria.value].ids;
      olsCoefficient.value = actorsData.value[selectedCriteria.value].ols_coefficient;
      break;
    case 'year':
      selectedIds = yearsData.value[selectedCriteria.value];
      olsCoefficient.value = null;
      //olsCoefficient.value = yearsData.value[selectedCriteria.value].ols_coefficient;
      yearRange.value = [...Object.keys(yearsData.value).map(year => parseInt(year))].sort((a, b) => a - b);
      break;
    case 'trope':
      selectedIds = tropesData.value[selectedCriteria.value].ids;
      olsCoefficient.value = tropesData.value[selectedCriteria.value].ols_coefficient;
      break;
    case 'award':
      selectedIds = awardsData.value[selectedCriteria.value].ids;
      olsCoefficient.value = awardsData.value[selectedCriteria.value].ols_coefficient;
      break;
    case 'country':
      selectedIds = countriesData.value[selectedCriteria.value].ids;
      olsCoefficient.value = countriesData.value[selectedCriteria.value].ols_coefficient;
      break;
  }

  // Filter movies
  const filteredMovies = moviesData.value.filter(movie => selectedIds.includes(movie.imdb_id));
  const notFilteredMovies = moviesData.value.filter(movie => !selectedIds.includes(movie.imdb_id));

  nMoviesSelected.value = selectedIds.length;
  meanRatingDiffSelected.value = Math.round(filteredMovies.reduce((sum, movie) => sum + movie.rating_difference, 0) / filteredMovies.length * 100, 4) / 100;

  // Update graph
  const data = [{
    x: notFilteredMovies.map(movie => movie.metascore),
    y: notFilteredMovies.map(movie => movie.imdb_rating_scaled),
    mode: 'markers',
    type: 'scatter',
    hovertext: notFilteredMovies.map(movie => movie.name),
    marker: {
      color: '#1f77b4',
      opacity: 0.1
    }
  }, {
    x: filteredMovies.map(movie => movie.metascore),
    y: filteredMovies.map(movie => movie.imdb_rating_scaled),
    name: selectedCriteria.value,
    mode: 'markers',
    type: 'scatter',
    hovertext: filteredMovies.map(movie => movie.name),
    marker: {
      color: '#d62728'
    }
  }, {
    x: [0, 100],
    y: [0, 100],
    mode: 'lines',
    type: 'scatter',
    name: 'x=y',
    line: {
      dash: 'dot',
      width: 2,
      color: 'grey'
    }
  }];

  const layout = {
    xaxis: {
      range: [0, 105],
      title: 'Metascore',
      automargin: true
    },
    yaxis: {
      range: [0, 105],
      title: 'IMDB Rating Scaled',
      scaleratio: 1,
      automargin: true
    },
    margin: {
      l: 70,
      r: 50,
      b: 70,
      t: 50,
      pad: 4
    },
    showlegend: false
  };

  Plotly.react(playgroundScatterPlot.value, data, layout);


  // Line for histogram mean
  const selectedMeanRatingDiff = filteredMovies.reduce((sum, movie) => sum + movie.rating_difference, 0) / filteredMovies.length;

  // Example function to calculate bins and counts
  function calculateBins(data, binSize) {
    let min = Math.min(...data);
    let max = Math.max(...data);
    let bins = [];
    let counts = {};

    // Create bins
    for (let i = min; i <= max; i += binSize) {
      bins.push(i);
      counts[i] = 0;
    }

    // Count data points in each bin
    data.forEach(value => {
      let bin = Math.floor(value / binSize) * binSize;
      counts[bin] = (counts[bin] || 0) + 1;
    });

    return { bins, counts };
  }

  // Use this function to transform your data
  const { bins, counts } = calculateBins(filteredMovies.map(movie => movie.rating_difference), 1); // Adjust bin size as needed

  // Data for histogram
  const histogramData = [{
    x: Object.keys(counts),
    y: Object.values(counts),
    type: 'bar',
    name: selectedCriteria.value,
    marker: {
      color: '#d62728',
      opacity: 0.5
    },
    showlegend: false
  }, {
    x: [0, 0],
    y: [0, 'max'],
    mode: 'lines',
    type: 'scatter',
    name: 'No Difference',
    line: {
      dash: 'dot',
      width: 2,
      color: 'grey'
    },
    id: 'lineAtZero'
  }, {
    x: [global_mean_rating_difference, global_mean_rating_difference],
    y: [0, 'max'],
    mode: 'lines',
    type: 'scatter',
    line: {
      width: 2,
      color: 'blue'
    },
    name: 'Global Mean',
    id: 'lineAtGlobalMean'
  }, {
    x: [selectedMeanRatingDiff, selectedMeanRatingDiff],
    y: [0, 'max'],
    mode: 'lines',
    type: 'scatter',
    line: {
      width: 2,
      color: '#d62728'
    },
    name: 'Selected Mean',
    id: 'lineAtSelectedMean'
  }];

  // Layout for histogram
  const histogramLayout = {
    title: 'Rating Difference Histogram',
    xaxis: { title: 'Rating Difference' },
    yaxis: { title: 'Count' },
    legend: {
      showlegend: true,
      xanchor: "center",
      yanchor: "top",
      y: -0.3, // play with it
      x: 0.5,
      orientation: 'h'
    },
    shapes: [
      // Line at x = 0
      {
        id: 'lineAtZero',
        type: 'line',
        x0: 0,
        y0: 0,
        x1: 0,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: 'grey',
          width: 3,
          dash: 'dot'
        }
      },
      // Line for global mean
      {
        id: 'lineAtGlobalMean',
        type: 'line',
        x0: global_mean_rating_difference,
        y0: 0,
        x1: global_mean_rating_difference,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: 'blue',
          width: 3
        }
      },
      // Line for histogram mean
      {
        id: 'lineAtSelectedMean',
        type: 'line',
        x0: selectedMeanRatingDiff,
        y0: 0,
        x1: selectedMeanRatingDiff,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: '#d62728',
          width: 3
        }
      }
    ]
  };

  // Create playground histogram plot
  Plotly.react(playgroundHistogramPlot.value, histogramData, histogramLayout);
};


const global_mean_rating_difference = -8.038996138996138;

</script>
