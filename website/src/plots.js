import Plotly from 'plotly.js-basic-dist-min'
const BASE_URL = import.meta.env.VITE_BASE_URL;


const flareColorScale = [
    [0, '#f6e8c3'],
    [0.2, '#fddbc7'],
    [0.4, '#f4a582'],
    [0.6, '#d6604d'],
    [0.8, '#b2182b'],
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

export function transformDataForPlotly(data, x_column, y_column, text_function = null, stringDivide=true) {
    let maxAbsValue = Math.max(...data.map(item => Math.abs(item[x_column])));

    const lower_ci = data.map(item => item['lower_ci'] ? item[x_column] - item['lower_ci'] : item['sem'] * 1.96)
    const upper_ci = data.map(item => item['upper_ci'] ? item['upper_ci'] - item[x_column] : item['sem'] * 1.96)


    // Normalize data to -1 to 1 scale
    let normalizedColors = data.map(item => item[x_column] / maxAbsValue);

    let trace = {
        x: data.map(item => item[x_column]),
        y: data.map(item => stringDivide ? stringDivider(item[y_column], 20, "<br>"): item[y_column]),
        hovertext: text_function ? data.map(item => text_function(item)) : null,
        error_x: {
            type: 'data',
            symetric: false,
            array: upper_ci,
            arrayminus: lower_ci,
            visible: true
        },
        type: 'bar',
        orientation: 'h',
        marker: {
            color: normalizedColors,
            colorscale: flareColorScale,
            cmin: -1,
            cmax: 1,
            showscale: true,
            colorbar: {
                tickvals: [-1, 0, 1],
                ticktext: ['Users<br>Oriented', '', 'Critics<br>Oriented'],
                tickwidth: 0.5,
                thickness: 15,
                orientation: 'h',
                yanchor: 'bottom',
                y: 0,
                yref: 'container',
            }
        }
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
        width: Array(Object.values(imdb_ratings_counts).length).fill(0.5),
        name: 'Count',
        type: 'bar',
        marker: {
            color: '#d6604d'
        },
        opacity: 0.75,
        showlegend: false
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
        legend: {
            xanchor: "center",
            yanchor: "top",
            yref: "container",
            y: 0.15,
            x: 0.5,
            orientation: 'v'
        }
    });
}


export function callbackMetascore(data, chartRef) {
    const metascore_counts = calculateBins(data.map(item => item.metascore), 5)

    const trace = [{
        x: Object.keys(metascore_counts),
        y: Object.values(metascore_counts),
        width: Array(Object.values(metascore_counts).length).fill(5),
        name: 'Count',
        type: 'bar',
        marker: {
            color: '#d6604d'
        },
        opacity: 0.75,
        showlegend: false
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
        legend: {
            xanchor: "center",
            yanchor: "top",
            yref: "container",
            y: 0.15,
            x: 0.5,
            orientation: 'v'
        }
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
            opacity: 0.2,
        },
        showlegend: false
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
        },
        showlegend: false
    }, {
        x: [0, 105],
        y: [50, 50],
        mode: 'lines',
        type: 'scatter',
        name: 'y=50',
        line: {
            dash: 'dot',
            width: 2,
            color: 'black'
        },
        showlegend: false
    }, {
        x: [50, 50],
        y: [0, 105],
        mode: 'lines',
        type: 'scatter',
        name: 'x=50',
        line: {
            dash: 'dot',
            width: 2,
            color: 'black'
        },
        showlegend: false
    },  {
        x: [data.map(movie => movie.metascore).reduce((a, b) => a + b, 0) / data.length],
        y: [data.map(movie => movie.imdb_rating_scaled).reduce((a, b) => a + b, 0) / data.length],
        mode: 'markers',
        type: 'scatter',
        name: 'Mean',
        marker: {
            color: 'red',
            size: 5,
            line: {
                color: 'red',
                width: 5
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
            size: 5,
            line: {
                color: 'blue',
                width: 5
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
        legend: {
            xanchor: "center",
            yanchor: "top",
            yref: "container",
            y: 0.15,
            x: 0.5,
            orientation: 'v'
        }
    };

    plotChart(chartRef, trace, layout)
}


export function callbackUsersCritics2(data, chartRef) {
    const rating_difference_counts = calculateBins(data.map(item => item.rating_difference), 5)

    const trace = [{
        x: Object.keys(rating_difference_counts),
        y: Object.values(rating_difference_counts),
        width: Array(Object.values(rating_difference_counts).length).fill(5),
        type: 'bar',
        name: 'Count',
        marker: {
            color: '#d6604d',
        },
        opacity: 0.75,
        showlegend: false
    }, {
        x: [data.map(item => item.rating_difference).reduce((a, b) => a + b, 0) / data.length],
        y: [Math.max(...Object.values(rating_difference_counts))],
        width: 0.5,
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
        width: 0.5,
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
        legend: {
            xanchor: "center",
            yanchor: "top",
            yref: "container",
            y: 0.15,
            x: 0.5,
            orientation: 'v'
        }
    });
}

export function callbackCountries1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {


        data.sort((a, b) => {
            return a.mean - b.mean;
        });

        const trace = transformDataForPlotly(data, 'mean', 'countries', function (item) {
            return `Number of movies: ${item.count.toFixed(0)}`;
        }, false)

        plotChart(chartRef, trace, {
            title: 'Mean Rating Difference for Countries',
            xaxis: {
                title: 'Rating difference',
                automargin: true
            },
            yaxis: {
                title: {
                    text: 'Country',
                    standoff: 0
                },
                automargin: true,
                ticklen: 5,
                tickfont: {
                    size: 10
                },
                tickmode: "array",
                nticks: data.length +1,
                tickvals: data.map(item => item.countries),
                ticktext: data.map(item => stringDivider(item.countries, 20, "<br>")),
            },
            autosize: true,
            responsive: true,
            height: 1000,
        });
    });
}


export function callbackCountries2(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.correlation - b.correlation;
        });

        const trace = transformDataForPlotly(data, 'correlation', 'Country', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                },
                ticklen: 5
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

        const trace = transformDataForPlotly(data, 'coef', 'Country', function (item) {
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

        const trace = transformDataForPlotly(genres1_filtered, 'rating_difference', 'genres', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                },
                ticklen: 5
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

        const trace = transformDataForPlotly(genres2_filtered, 'correlation', 'Genre', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                },
                ticklen: 5
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

        const trace = transformDataForPlotly(data, 'coef', 'Genre', function (item) {
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
                tickcolor: 'white',
                tickfont: {
                    size: 10
                }
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackAwards1(chartRef, fileUrl) {

    fetchData(fileUrl).then(data => {

        data.sort((a, b) => {
            return a.rating_difference - b.rating_difference;
        });

        const maxAbsValue = Math.max(...data.map(item => Math.abs(item.rating_difference)));

        const normalizedColors = data.map(item => item.rating_difference / maxAbsValue);

        const lower_ci = data.map(item => item['lower_ci'] ? item['rating_difference'] - item['lower_ci'] : item['sem'] * 1.96)
        const upper_ci = data.map(item => item['upper_ci'] ? item['upper_ci'] - item['rating_difference'] : item['sem'] * 1.96)

        const trace = [{
            x: data.map(item => item.rating_difference),
            y: data.map(item => stringDivider(item['Award'], 20, "<br>")),
            type: 'bar',
            hovertext: data.map(item => `Number of movies: ${item.number_of_movies.toFixed(0)}`),
            error_x: {
                type: 'data',
                symetric: false,
                array: upper_ci,
                arrayminus: lower_ci,
                visible: true
            },
            marker: {
                color: normalizedColors,
                colorscale: flareColorScale,
                cmin: -1,
                cmax: 1,
                showscale: true,
                colorbar: {
                    tickvals: [-1, 0, 1],
                    ticktext: ['Users<br>Oriented', '', 'Critics<br>Oriented'],
                    tickwidth: 0.5,
                    thickness: 15,
                    orientation: 'h',
                    yanchor: 'bottom',
                    y: 0,
                    yref: 'container',
                }
            },
            opacity: 0.75,
            orientation: 'h',

        }]

        plotChart(chartRef, trace, {
            title: 'Average rating diffence of Awards',
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
            marker: {
                color: normalizedColors,
                colorscale: flareColorScale,
                cmin: -1,
                cmax: 1,
                showscale: true,
                colorbar: {
                    tickvals: [-1, 0, 1],
                    ticktext: ['Users<br>Oriented', '', 'Critics<br>Oriented'],
                    tickwidth: 0.5,
                    thickness: 15,
                    orientation: 'h',
                    yanchor: 'bottom',
                    y: 0,
                    yref: 'container',
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

        const maxAbsValue = Math.max(...data.map(item => Math.abs(item.correlation)));

        const lower_ci = data.map(item => item['lower_ci'] ? item['correlation'] - item['lower_ci'] : item['sem'] * 1.96)
        const upper_ci = data.map(item => item['upper_ci'] ? item['upper_ci'] - item['correlation'] : item['sem'] * 1.96)

        const normalizedColors = data.map(item => item.correlation / maxAbsValue);

        const trace = [{
            x: data.map(item => item.correlation),
            y: data.map(item => stringDivider(item['Awards'], 20, "<br>")),
            type: 'bar',
            hovertext: data.map(item => `P-value: ${item.p_value}`),
            error_x: {
                type: 'data',
                symetric: false,
                array: upper_ci,
                arrayminus: lower_ci,
                visible: true
            },
            marker: {
                color: normalizedColors,
                colorscale: flareColorScale,
                cmin: -1,
                cmax: 1,
                showscale: true,
                colorbar: {
                    tickvals: [-1, 0, 1],
                    ticktext: ['Users<br>Oriented', '', 'Critics<br>Oriented'],
                    tickwidth: 0.5,
                    thickness: 15,
                    orientation: 'h',
                    yanchor: 'bottom',
                    y: 0,
                    yref: 'container',
                }
            },
            opacity: 1,
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

        const maxAbsValue = Math.max(...data.map(item => Math.abs(item.coef)));

        // if lower_ci in item, then use it, otherwise use sem
        const lower_ci = data.map(item => item['lower_ci'] ? item['coef'] - item['lower_ci'] : item['sem'] * 1.96)
        const upper_ci = data.map(item => item['upper_ci'] ? item['upper_ci'] - item['coef'] : item['sem'] * 1.96)

        const normalizedColors = data.map(item => item.coef / maxAbsValue);

        const trace = [{
            x: data.map(item => item.coef),
            y: data.map(item => stringDivider(item['Awards'], 20, "<br>")),
            type: 'bar',
            error_x: {
                type: 'data',
                symetric: false,
                array: upper_ci,
                arrayminus: lower_ci,
                visible: true
            },
            hovertext: data.map(item => `P-value: ${item.p_value}`),
            marker: {
                color: normalizedColors,
                colorscale: flareColorScale,
                cmin: -1,
                cmax: 1,
                showscale: true,
                colorbar: {
                    tickvals: [-1, 0, 1],
                    ticktext: ['Users<br>Oriented', '', 'Critics<br>Oriented'],
                    tickwidth: 0.5,
                    thickness: 15,
                    orientation: 'h',
                    yanchor: 'bottom',
                    y: 0,
                    yref: 'container',
                }
            },
            opacity: 1,
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

        const trace = transformDataForPlotly(actors1_filtered, 'correlation', 'actor_name', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
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

        const trace = transformDataForPlotly(data, 'coef', 'actor_name', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
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

        const trace = transformDataForPlotly(tropes1_filtered, 'correlation', 'Trope', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
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

        const trace = transformDataForPlotly(tropes2_filtered, 'coef', 'Trope', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
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

        const trace = transformDataForPlotly(global1_filtered, 'correlation', 'Feature', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
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

        const trace = transformDataForPlotly(global2_filtered, 'coef', 'Feature', function (item) {
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
                automargin: true,
                tickfont: {
                    size: 10
                }
            },
            autosize: true,
            responsive: true,
        });
    })
}

export function callbackReleaseYear(chartRef1, chartRef2, fileUrl) {
    fetchData(fileUrl).then(data => {

        // Metascore and IMDb Rating on plot 1
        const years = Object.keys(data);
        const imdbRatings = years.map(year => data[year].imdb_rating_scaled_mean);
        const imdbRatingCI = years.map(year => data[year].imdb_rating_scaled_sem * 1.96);
        const metascores = years.map(year => data[year].metascore_mean);
        const metascoreCI = years.map(year => data[year].metascore_sem * 1.96);


        const traceIMDbMean = {
            x: years,
            y: imdbRatings,
            type: 'scatter',
            mode: 'lines',
            name: 'IMDb Rating',
            line: { color: '#f4a582' },
            legendgroup: 'IMDb Rating',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };

        const traceMetascoreMean = {
            x: years,
            y: metascores,
            type: 'scatter',
            mode: 'lines',
            name: 'Metascore',
            line: { color: '#67001f' },
            legendgroup: 'Metascore',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };


        // Create traces for error regions (upper and lower bounds)
        const traceIMDbErrorUpper = {
            x: years,
            y: imdbRatings.map((r, i) => r + imdbRatingCI[i]),
            type: 'scatter',
            mode: 'lines',
            fill: 'tonexty',
            fillcolor: 'rgba(244, 165, 130, 0.4)',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'IMDb Rating',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };

        const traceIMDbErrorLower = {
            x: years,
            y: imdbRatings.map((r, i) => r - imdbRatingCI[i]),
            type: 'scatter',
            mode: 'lines',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'IMDb Rating',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };

        const traceMetascoreErrorUpper = {
            x: years,
            y: metascores.map((m, i) => m + metascoreCI[i]),
            type: 'scatter',
            mode: 'lines',
            fill: 'tonexty',
            fillcolor: 'rgba(103, 0, 31, 0.2)',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'Metascore',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };

        const traceMetascoreErrorLower = {
            x: years,
            y: metascores.map((m, i) => m - metascoreCI[i]),
            type: 'scatter',
            mode: 'lines',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'Metascore',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        };

        const trace1 = [
            traceIMDbErrorLower, traceIMDbErrorUpper, traceIMDbMean,
            traceMetascoreErrorLower, traceMetascoreErrorUpper, traceMetascoreMean
        ];

        plotChart(chartRef1, trace1, {
            title: 'Mean IMDb Rating and Metascore<br>by Release Year',
            xaxis: {
                title: 'Release Year',
                automargin: true
            },
            legend: {
                showlegend: true,
                xanchor: "center",
                yanchor: "top",
                y: -0.2,
                x: 0.5,
                orientation: 'h'
              },
            yaxis: {
                title: 'Mean Rating',
                automargin: true
            },
            autosize: true,
            responsive: true,
        });

        // Rating difference on plot 2
        const ratingDifference = years.map(year => data[year].rating_difference_mean);
        const ratingDifferenceCI = years.map(year => data[year].rating_difference_sem * 1.96);

        const trace2 = [{
            x: years,
            y: ratingDifference.map((r, i) => r - ratingDifferenceCI[i]),
            type: 'scatter',
            mode: 'lines',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'Rating Difference',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)

        }, {
            x: years,
            y: ratingDifference.map((r, i) => r + ratingDifferenceCI[i]),
            type: 'scatter',
            mode: 'lines',
            fill: 'tonexty',
            fillcolor: 'rgba(214, 96, 77, 0.2)',
            line: { color: 'transparent' },
            showlegend: false,
            legendgroup: 'Rating Difference',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        }, {
            x: years,
            y: ratingDifference,
            type: 'scatter',
            mode: 'lines',
            name: 'Rating Difference',
            line: { color: '#d6604d' },
            legendgroup: 'Rating Difference',
            hovertext: years.map(year => `Number of movies: ${data[year].number_of_movies.toFixed(0)}`)
        },]

        plotChart(chartRef2, trace2, {
            title: 'Mean Rating Difference<br>by Release Year',
            xaxis: {
                title: 'Release Year',
                automargin: true
            },
            yaxis: {
                title: 'Mean Rating Difference',
                automargin: true
            },
            legend: {
                showlegend: true,
                xanchor: "center",
                yanchor: "top",
                yref: "paper",
                y: -0.2,
                x: 0.5,
                orientation: 'h'
              },
            autosize: true,
            responsive: true,
        })
    })
}