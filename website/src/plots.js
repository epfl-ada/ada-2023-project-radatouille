import Plotly from 'plotly.js-basic-dist-min'
const BASE_URL = import.meta.env.VITE_BASE_URL;


const flareColorScale = [
    [0, '#f6e8c3'],
    [0.28, '#fddbc7'],
    [0.42, '#f4a582'],
    [0.56, '#d6604d'],
    [0.70, '#b2182b'],
    [1.0, '#67001f']
];


export const fetchData = async (path) => {
    const originUrl = window.location.origin;
    if (BASE_URL && BASE_URL !== '/') return await fetch(`${originUrl}/${BASE_URL}/${path}`).then(response => response.json());
    return await fetch(`${originUrl}/${path}`).then(response => response.json());
};


// Example function to calculate bins and counts
export function calculateBins(data, binSize) {
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

    return counts;
}

export function stringDivider(str, width, spaceReplacer) {
    if (str.length > width) {
        var p = width
        for (; p > 0 && str[p] != ' '; p--) {
        }
        if (p > 0) {
            var left = str.substring(0, p);
            var right = str.substring(p + 1);
            return left + spaceReplacer + stringDivider(right, width, spaceReplacer);
        }
    }
    return str;
}

export function transformDataForPlotly(data, x_column, y_column, error_x_column, text_function = null) {
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

export function plotChart(chartRef, data, layout) {
    Plotly.newPlot(chartRef.value, data, layout);
}

export function loadChart(url, callback) {
    fetchData(url).then(data => {
        callback(data);
    });
}



// Users Bar Chart
export function callbackUser(data, chartRef) {

    const imdb_ratings_counts = calculateBins(data.map(item => item.imdb_rating_scaled / 10), 0.5)
    const trace = [{
        x: Object.keys(imdb_ratings_counts),
        y: Object.values(imdb_ratings_counts),
        name: 'Count',
        type: 'bar',
        marker: {
            color: '#d6604d',
            line: {
                color: '#d6604d',
                width: 10
            }
        },
        opacity: 0.75
    }, {
        x: [data.map(item => item.imdb_rating_scaled / 10).reduce((a, b) => a + b, 0) / data.length],
        y: [Math.max(...Object.values(imdb_ratings_counts))],
        type: 'bar',
        name: 'Mean',
        marker: {
            color: 'red',
            line: {
                color: 'red',
                width: 0.5
            }
        }
    }, {
        x: [data.map(item => item.imdb_rating_scaled / 10).sort((a, b) => a - b)[Math.floor(data.length / 2)]],
        y: [Math.max(...Object.values(imdb_ratings_counts))],
        type: 'bar',
        name: 'Median',
        marker: {
            color: 'blue',
            line: {
                color: 'blue',
                width: 0.5
            }
        },
        opacity: 1
    }]

    plotChart(chartRef, trace, {
        title: 'IDMb Average Users Rating',
        xaxis: {
            title: 'Users Rating',
            automargin: true,
            range: [0, 11]
        },
        yaxis: {
            title: 'Movies (count)',
            automargin: true
        },
        autosize: true,
        responsive: true,
    });
}


export function callbackMetascore(data, chartRef) {
    const metascore_counts = calculateBins(data.map(item => item.metascore), 5)

    const trace = [{
        x: Object.keys(metascore_counts),
        y: Object.values(metascore_counts),
        name: 'Count',
        type: 'bar',
        marker: {
            color: '#d6604d',
            line: {
                color: '#d6604d',
                width: 10
            }
        },
        opacity: 0.75
    }, {
        x: [data.map(item => item.metascore).reduce((a, b) => a + b, 0) / data.length],
        y: [Math.max(...Object.values(metascore_counts))],
        type: 'bar',
        name: 'Mean',
        marker: {
            color: 'red',
            line: {
                color: 'red',
                width: 0.25
            }
        }
    }, {
        x: [data.map(item => item.metascore).sort((a, b) => a - b)[Math.floor(data.length / 2)]],
        y: [Math.max(...Object.values(metascore_counts))],
        type: 'bar',
        name: 'Median',
        marker: {
            color: 'blue',
            line: {
                color: 'blue',
                width: 0.25
            }
        },
        opacity: 1
    }]

    plotChart(chartRef, trace, {
        title: 'Metascores',
        xaxis: {
            title: 'Metascore',
            automargin: true,
            range: [0, 105]
        },
        yaxis: {
            title: 'Movies (count)',
            automargin: true
        },
        autosize: true,
        responsive: true,
    });
}

export function callbackUsersCritics1(data, chartRef) {
    const trace = [{
        x: data.map(movie => movie.metascore),
        y: data.map(movie => movie.imdb_rating_scaled),
        mode: 'markers',
        type: 'scatter',
        hovertext: data.map(movie => movie.name),
        marker: {
            color: '#67001f',
            opacity: 0.2
        }
    }, {
        x: [0, 105],
        y: [0, 105],
        mode: 'lines',
        type: 'scatter',
        name: 'x=y',
        line: {
            dash: 'dot',
            width: 2,
            color: 'grey'
        }
    }, {
        x: [data.map(movie => movie.metascore).reduce((a, b) => a + b, 0) / data.length],
        y: [data.map(movie => movie.imdb_rating_scaled).reduce((a, b) => a + b, 0) / data.length],
        mode: 'markers',
        type: 'scatter',
        name: 'Mean',
        marker: {
            color: 'red',
            line: {
                color: 'red',
                width: 2
            }
        }
    }, {
        x: [data.map(movie => movie.metascore).sort((a, b) => a - b)[Math.floor(data.length / 2)]],
        y: [data.map(movie => movie.imdb_rating_scaled).sort((a, b) => a - b)[Math.floor(data.length / 2)]],
        mode: 'markers',
        type: 'scatter',
        name: 'Median',
        marker: {
            color: 'blue',
            line: {
                color: 'blue',
                width: 2
            }
        },
        opacity: 1
    }];

    const layout = {
        title: "IMDb Users Rating vs Metascore",
        xaxis: {
            range: [0, 105],
            title: 'Metascore',
            automargin: true
        },
        yaxis: {
            range: [0, 105],
            title: 'IMDB Users Rating Scaled',
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

    plotChart(chartRef, trace, layout)
}


export function callbackUsersCritics2(data, chartRef) {
    const rating_difference_counts = calculateBins(data.map(item => item.rating_difference), 5)

    const trace = [{
        x: Object.keys(rating_difference_counts),
        y: Object.values(rating_difference_counts),
        type: 'bar',
        name: 'Count',
        marker: {
            color: '#d6604d',
            line: {
                color: '#d6604d',
                width: 5
            }
        },
        opacity: 0.75
    }, {
        x: [data.map(item => item.rating_difference).reduce((a, b) => a + b, 0) / data.length],
        y: [Math.max(...Object.values(rating_difference_counts))],
        type: 'bar',
        name: 'Mean',
        marker: {
            color: 'red',
            line: {
                color: 'red',
                width: 2
            }
        }
    }, {
        x: [data.map(item => item.rating_difference).sort((a, b) => a - b)[Math.floor(data.length / 2)]],
        y: [Math.max(...Object.values(rating_difference_counts))],
        type: 'bar',
        name: 'Median',
        marker: {
            color: 'blue',
            line: {
                color: 'blue',
                width: 2
            }
        },
        opacity: 1

    }]

    plotChart(chartRef, trace, {
        title: 'Rating Differences',
        xaxis: {
            title: 'Rating Difference',
            automargin: true,
            range: [-105, 105]
        },
        yaxis: {
            title: {
                text: 'Movies (count)',
                standoff: 0
            },
            automargin: true
        },
        autosize: true,
        responsive: true,
    });
}

export function callbackCountries1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {


        data.sort((a, b) => {
            return a.mean - b.mean;
        });

        const trace = transformDataForPlotly(data, 'mean', 'countries', 'sem', function (item) {
            return `Number of movies: ${item.count.toFixed(0)}`;
        })

        plotChart(chartRef, trace, {
            title: 'Mean Rating difference for Countries',
            xaxis: {
                title: 'Rating difference',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Country',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    });
}


export function callbackCountries2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        const trace = transformDataForPlotly(data, 'correlation', 'Country', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for Countries',
            xaxis: {
                title: 'Pearson correlation coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Country',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    });
}

export function callbackCountries3(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        const trace = transformDataForPlotly(data, 'coef', 'Country', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for Countries',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Country',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackGenres1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.rating_difference - b.rating_difference;
        });

        // keep the top 10 and bottom 10
        let bottom = data.slice(0, 10);
        let top = data.slice(-10);
        let genres1_filtered = bottom.concat(top);

        const trace = transformDataForPlotly(genres1_filtered, 'rating_difference', 'genres', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}`;
        })

        plotChart(chartRef, trace, {
            title: 'Mean rating difference for Genres',
            xaxis: {
                title: 'Rating difference',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Genre',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackGenres2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        let top = data.slice(-10);
        let bottom = data.slice(0, 10);
        let genres2_filtered = bottom.concat(top);

        const trace = transformDataForPlotly(genres2_filtered, 'correlation', 'Genre', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for Genres',
            xaxis: {
                title: 'Pearson correlation coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Genre',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackGenres3(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        const trace = transformDataForPlotly(data, 'coef', 'Genre', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for Genres',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Genre',
                    standoff: 0
                },
                automargin: true,
                ticklen: 10,
                tickcolor: 'white'
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackAwards1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.number_of_movies - b.number_of_movies;
        });

        // keep the top 10 and bottom 10
        let bottom = data.slice(0, 10);
        let top = data.slice(-10);
        let awards1_filtered = bottom.concat(top);

        const trace = [{
            x: awards1_filtered.map(item => item.number_of_movies),
            y: awards1_filtered.map(item => stringDivider(item.awards_received, 20, "<br>")),
            type: 'bar',
            hovertext: awards1_filtered.map(item => `Number of movies: ${item.number_of_movies.toFixed(0)}`),
            marker: {
                color: '#67001f'
            },
            opacity: 0.75,
            orientation: 'h',

        }]

        plotChart(chartRef, trace, {
            title: 'Mean rating difference for Awards',
            xaxis: {
                title: 'Rating difference',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Award',
                    standoff: 0,
                },
                automargin: true,
                ticklen: 10,
                tickcolor: 'white',
                tickfont: {
                    size: 11
                }
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackAwards2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        const maxValue = data.length - 1;

        const trace = [{
            x: data.map(item => item.correlation),
            y: data.map(item => stringDivider(item['Awards'], 20, "<br>")),
            type: 'bar',
            hovertext: data.map(item => `P-value: ${item.p_value}`),
            error_x: {
                type: 'data',
                array: data.map(item => item['sem']),
                visible: true
            },
            marker: {
                color: data.map((_, index) => index / maxValue), // Assign a normalized value based on index
                colorscale: flareColorScale
            },
            opacity: 0.75,
            orientation: 'h',
        }]

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for Awards',
            xaxis: {
                title: 'Pearson correlation coefficient',
                automargin: true
            },

            yaxis: {
                title: {
                    text: 'Award',
                    standoff: 10
                },
                automargin: true,
                ticklen: 10,
                tickcolor: 'white',
                tickfont: {
                    size: 11
                }
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackAwards3(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        const maxValue = data.length - 1;

        const trace = [{
            x: data.map(item => item.coef),
            y: data.map(item => stringDivider(item['Awards'], 20, "<br>")),
            type: 'bar',
            error_x: {
                type: 'data',
                array: data.map(item => item['sem']),
                visible: true
            },
            hovertext: data.map(item => `P-value: ${item.p_value}`),
            marker: {
                color: data.map((_, index) => index / maxValue), // Assign a normalized value based on index
                colorscale: flareColorScale
            },
            opacity: 0.75,
            orientation: 'h',
        }]

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for Awards',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Award',
                    standoff: 10
                },
                automargin: true,
                ticklen: 10,
                tickcolor: 'white'
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackActors1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        // keep the top 10 and bottom 10
        let bottom = data.slice(0, 10);
        let top = data.slice(-10);
        let actors1_filtered = bottom.concat(top);

        const trace = transformDataForPlotly(actors1_filtered, 'correlation', 'actor_name', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for Actors',
            xaxis: {
                title: 'Pearson correlation coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Actor',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackActors2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        const trace = transformDataForPlotly(data, 'coef', 'actor_name', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for Actors',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Actor',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackTropes1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        // keep the top 10 and bottom 10
        let bottom = data.slice(0, 10);
        let top = data.slice(-10);
        let tropes1_filtered = bottom.concat(top);

        const trace = transformDataForPlotly(tropes1_filtered, 'correlation', 'Trope', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for Tropes',
            xaxis: {
                title: 'Pearson correlation coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Trope',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackTropes2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        let top = data.slice(-10);
        let bottom = data.slice(0, 10);
        let tropes2_filtered = bottom.concat(top);

        const trace = transformDataForPlotly(tropes2_filtered, 'coef', 'Trope', 'sem', function (item) {
            return `Number of movies: ${item.number_of_movies.toFixed(0)}<br>P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for Tropes',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Trope',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackGlobal1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        // keep the top 10 and bottom 10
        let global1_filtered = data;
        if (data.length > 20) {
            let bottom = data.slice(0, 10);
            let top = data.slice(-10);
            global1_filtered = bottom.concat(top);
        }

        const trace = transformDataForPlotly(global1_filtered, 'correlation', 'Feature', 'sem', function (item) {
            return `P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'Pearson correlation for global features',
            xaxis: {
                title: 'Pearson correlation',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Feature',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackGlobal2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {
        data.sort((a, b) => {
            return a.coef - b.coef;
        });

        let global2_filtered = data
        if (data.length > 20) {
            let top = data.slice(-10);
            let bottom = data.slice(0, 10);
            global2_filtered = bottom.concat(top);
        }

        const trace = transformDataForPlotly(global2_filtered, 'coef', 'Feature', 'sem', function (item) {
            return `P-value: ${item.p_value}`;
        })

        plotChart(chartRef, trace, {
            title: 'OLS coefficient for global features',
            xaxis: {
                title: 'OLS coefficient',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Feature',
                    standoff: 0
                },
                automargin: true
            },
            autosize: true,
            responsive: true,
        });
    })
}