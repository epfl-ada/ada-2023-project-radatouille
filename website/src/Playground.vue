<template>
  <div class="flex flex-col gap-3 pt-6">
    <select v-model="selectedCriteriaType" @change="updateCriteria">
      <option value="genre">Genre</option>
      <option value="actor">Actor</option>
      <option value="trope">Tropes</option>
      <option value="award">Award</option>
      <option value="country">Countries</option>
      <option value="year">Year</option>
    </select>

    <div class="flex gap-3">
      <input type="range" v-if="selectedCriteriaType === 'year'" v-model="selectedYear" :min="yearRange[0]"
        :max="yearRange[yearRange.length - 1]" @change="updateYearSlider" class="w-full" />
      <span v-if="selectedCriteriaType === 'year'">{{ selectedYear }}</span>
    </div>

    <select class="mb-3" v-if="selectedCriteriaType !== 'year'" v-model="selectedCriteria" @change="updateGraph">
      <option v-for="option in criteriaOptions" :key="option" :value="option">{{ option }}</option>
    </select>

    <div ref="playgroundScatterPlot"></div>
    <div ref="playgroundHistogramPlot"></div>
  </div>
</template>
  
<script setup>
import Plotly from 'plotly.js-dist-min';

import { onMounted, ref } from 'vue';

import movies_data from '../data/playground-movies.json';
import genres_data from '../data/playground-genres.json';
import actors_data from '../data/playground-actors.json';
import years_data from '../data/playground-releaseyear.json';
import tropes_data from '../data/playground-tropes.json';
//import awards_data from '../data/playground-awards.json';
import countries_data from '../data/playground-countries.json';

const moviesData = ref([]);

const genresData = ref({});
const actorsData = ref({});
const yearsData = ref({});
const tropesData = ref({});
const awardsData = ref({});
const countriesData = ref({});

const yearRange = ref([]);

const selectedYear = ref(null);

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

const updateYearSlider = () => {
  // Find the closest year in the range to the current slider value
  let closest = yearRange.value.reduce((a, b) => {
    return Math.abs(b - selectedYear.value) < Math.abs(a - selectedYear.value) ? b : a;
  });

  selectedYear.value = closest;
  selectedCriteria.value = closest.toString();
  updateGraph();
};


onMounted(async () => {
  yearRange.value = [...Object.keys(years_data).map(year => parseInt(year))].sort((a, b) => a - b);
  moviesData.value = movies_data;
  genresData.value = genres_data;
  actorsData.value = actors_data;
  yearsData.value = years_data;
  tropesData.value = tropes_data;
  //awardsData.value = awards_data;
  countriesData.value = countries_data;
  initGraph();
  updateCriteria();
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
      range: [0, 100],
      title: 'Metascore'
    },
    yaxis: {
      range: [0, 100],
      title: 'IMDB Rating Scaled',
      scaleratio: 1
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
      selectedIds = genresData.value[selectedCriteria.value];
      break;
    case 'actor':
      selectedIds = actorsData.value[selectedCriteria.value];
      break;
    case 'year':
      selectedIds = yearsData.value[selectedCriteria.value];
      break;
    case 'trope':
      selectedIds = tropesData.value[selectedCriteria.value];
      break;
    case 'award':
      selectedIds = awardsData.value[selectedCriteria.value];
      break;
    case 'country':
      selectedIds = countriesData.value[selectedCriteria.value];
      break;
  }

  // Filter movies
  const filteredMovies = moviesData.value.filter(movie => selectedIds.includes(movie.imdb_id));
  const notFilteredMovies = moviesData.value.filter(movie => !selectedIds.includes(movie.imdb_id));

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
      range: [0, 100],
      title: 'Metascore',
      automargin: true
    },
    yaxis: {
      range: [0, 100],
      title: 'IMDB Rating Scaled',
      // Make plot square
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

  // Data for histogram
  const histogramData = [{
    x: filteredMovies.map(movie => movie.rating_difference),
    type: 'histogram',
    name: selectedCriteria.value,
    marker: {
      color: '#d62728',
      opacity: 0.5
    }
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
    }
  }, {
    x: [global_mean_rating_difference, global_mean_rating_difference],
    y: [0, 'max'],
    mode: 'lines',
    type: 'scatter',
    line: {
      width: 2,
      color: 'blue'
    },
    name: 'Global Mean'
  }, {
    x: [selectedMeanRatingDiff, selectedMeanRatingDiff],
    y: [0, 'max'],
    mode: 'lines',
    type: 'scatter',
    line: {
      width: 2,
      color: '#d62728'
    },
    name: 'Selected Mean'
  }];

  // Layout for histogram
  const histogramLayout = {
    title: 'Rating Difference Histogram',
    xaxis: { title: 'Rating Difference' },
    yaxis: { title: 'Count' },
    shapes: [
      // Line at x = 0
      {
        type: 'line',
        x0: 0,
        y0: 0,
        x1: 0,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: 'grey',
          width: 2,
          dash: 'dot'
        }
      },
      // Line for global mean
      {
        type: 'line',
        x0: global_mean_rating_difference,
        y0: 0,
        x1: global_mean_rating_difference,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: 'blue',
          width: 2
        }
      },
      // Line for histogram mean
      {
        type: 'line',
        x0: selectedMeanRatingDiff,
        y0: 0,
        x1: selectedMeanRatingDiff,
        y1: 1,
        xref: 'x',
        yref: 'paper',
        line: {
          color: '#d62728',
          width: 2
        }
      }
    ]
  };

  // Create playground histogram plot
  Plotly.react(playgroundHistogramPlot.value, histogramData, histogramLayout);
};


const global_mean_rating_difference = -8.038996138996138;

</script>
