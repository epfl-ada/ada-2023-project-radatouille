<template>
    <!-- == HERO == -->
    <div
      class="flex flex-col w-full items-center bg-[url(/banner.webp)] bg-center bg-cover bg-no-repeat justify-center text-light p-6 shadow-lg min-h-[400px]">
      <h1 class="text-3xl lg:text-5xl font-bold mt-auto drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] text-center">
        Screen Tastes: The User-Critic Divide in Cinema
      </h1>
      <h3 class="text-xl font-thin mt-2 text-center drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">An attempt to explain movie
        taste differences between users and critics</h3>
      <div class="flex flex-col items-center mt-auto px-5 py-3">
        <span class="font-bold drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] mt-3">A project served by the Team
          rADAtouille</span>
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
      <div class="flex col-span-5 px-10 lg:px-8 lg:col-span-3 lg:col-start-2 flex-col py-8 w-full mx-auto max-w-screen-lg">
        <section id="introduction" class="section">
          <h2 class="text-4xl lg:text-5xl font-bold mt-5">Introduction</h2>
  
          <div class="flex flex-col lg:flex-row">
            <div>
              <p class="text-justify mt-4 lg:max-w-screen-md">
                As aspiring chefs, we are eager to learn how to prepare the most exquisite movie
                possible. We are aware that Anton Ego, a renowned critic, will soon be evaluating our skills.
              </p>
              <p class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4 font-semibold">
                Can we find a
                movie
                that pleases everyone, from the average viewer to the most sophisticated cinephile?
              </p>
              <p>
                This is the challenge we
                aim
                to conquer. Our initial task is to ascertain whether their tastes differ significantly. Let's examine what
                needs
                to be done to achieve this.
              </p>
            </div>
            <img src="/remy.png" alt="remy"
              class="w-[180px] lg:w-[180px] mt-4 drop-shadow-xl lg:max-h-none hover:scale-105 hover:drop-shadow-none transition duration-300 mx-auto lg:ml-8" />
          </div>
  
          <section id="fridge" class="section text-justify">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start gap-2 ">
              <BookmarkIcon class="w-9 h-9 float-left mr-2 mt-1" />What's in our fridge
            </h3>
            <p class="mt-4">
              Let's look at what is available to us.
            </p>
            <h6 class="text-lg font-bold mt-4">CMU Movies</h6>
            <p class="mt-2">
              The base of this analysis is the <a class="text-red-900 underline hover:text-red-400"
                href="http://www.cs.cmu.edu/~ark/personas/" target="_blank">CMU
                dataset</a>, in which the following ingredients are of
              interest:
            <ul class="list-disc list-inside ml-5 my-2 underline">
              <li><a href="#countries">Countries</a></li>
              <li><a href="#genres">Genres</a></li>
              <li><a href="#release-year">Release year</a></li>
              <li><a href="#actors">Actors</a></li>
            </ul>
            We also got the IMDb
            rating from the available dataset on <a class="text-red-900 underline hover:text-red-400"
              href="https://datasets.imdbws.com/">IMDb's
              website</a> and the Metascore from a scrapping of <a href="https://metacritic.com" target="_blank"
              class="text-red-900 underline hover:text-red-400">Metacric</a>.
            </p>
            <p class="mt-2">
              Our processed dataset contains <b>7'770 movies with both IMDb and Metascore ratings</b>.
            </p>
  
            <h6 class="text-lg font-bold mt-4">Awards</h6>
            <p class="mt-1">
              In addition to that, we also scrapped the awards nominations and wins from <a href="https://www.imdb.com/"
                target="_blank" class="text-red-900 underline hover:text-red-400">IMDb</a> for each movie, in order to
              create the <a href="#awards" class="underline">Awards</a> ingredient.
            </p>
  
            <h6 class="text-lg font-bold mt-4">Tropes</h6>
            <p class="mt-1">
              And for our last ingredient, we also used <a href="https://github.com/dhruvilgala/tvtropes" target="_blank"
                class="text-red-900 underline hover:text-red-400">an external dataset</a> associating
              tropes to <b>2495 movies</b> out of our 7'770 movies, in order to create the <a href="#tropes"
                class="underline">Tropes</a> ingredient.
            </p>
  
  
            <p class="mt-8">
              Before we start cooking, let's take a look at our convives' likings to see if they are similar or not.
            </p>
  
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-2">
                <h4 class="text-xl font-bold">IMDb Users Ratings</h4>
                <p class="mt-2">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium magni quam neque voluptatibus!
                  Inventore, praesentium aliquid reiciendis necessitatibus quos iure maxime, unde deserunt hic doloribus
                  vitae. Vitae aliquid culpa dolorum?
                </p>
              </div>
              <div class="flex flex-col order-1 lg:order-1 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartUsers" class="aspect-square w-full"></div>
                </div>
              </div>
            </div>
  
  
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <h4 class="text-xl font-bold">Metascore</h4>
                <p class="mt-2">
                  Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corrupti incidunt non, illo assumenda a illum,
                  quasi similique nisi, error architecto maxime dolorem. Tempora qui nesciunt tenetur! Quasi esse distinctio
                  eveniet.
                </p>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartMetascore" class="aspect-square w-full"></div>
                </div>
              </div>
            </div>
  
          </section>
  
          <section id="cookbook" class="section text-justify">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start gap-2 ">
              <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Statistics Cookbook
            </h3>
            <p class="mt-2">
              We have a lot of tools and nice recipes to use with our ingredients, and we'll try
              to describe and justify them in the following section:
            </p>
            <div>
              <h4 class="text-xl font-bold mt-4">T-Test</h4>
              <p class="mt-2">
                Basic statistics are conducted using the <b>p-value threshold of 0.05</b> to determine if the imdb users and
                metascore
                rating distribution have a significantly different mean.
              </p>
              <h4 class="text-xl font-bold mt-4">Pearson Correlation</h4>
              <p class="mt-2">
                The Pearson correlation will be used systematically on all the features, allowing us to extract a first
                glimpse of which of them is significant on the rating difference. The Pearson correlation measures the
                linear correlation between 2 sets of data, so by measuring the Pearson Correlation Coefficient (PCC) between
                one feature and the rating difference, we will extract the linear correlation between both.
                The significance threshold has been chosen at the <b>p-value of 0.05</b> since it's the most commonly used
                value.
              </p>
              <p class="mt-2">
                In general, the plots will display up to the top and bottom 10 significant features, based on the magnitude
                of the Pearson correlation.
              </p>
              <h4 class="text-xl font-bold mt-4">Ordinary Least Squares (OLS)</h4>
              <p class="mt-2">
                The main tool used throughout the project is the Ordinary Least Square (OLS) regression. The goal of that
                regression is to extract the relative impact of each feature on our variable of interest, the rating
                difference. When relevant, a naive OLS has been conducted and its metrics (F-Statistics, adjusted R&#178;,
                condition number, …) inspected to judge the relevancy of the model itself, and the results have been
                selected based on their p-value significance, using once more the common <b>p-value threshold of 0.05</b>.
                Nevertheless, OLS regression is not perfect: one of the biggest challenges we faced
                was that it is <b>strongly sensitive to outliers</b> and <b>multicollinear features</b>.
              </p>
              <p class="mt-2">
                When the filtering
                was proved necessary, a second OLS was conducted on the filtered features before being reviewed again to
                assess the improvement.
              </p>
              <p class="my-4 bg-slate-200 rounded-r-lg border-l-8 border-slate-600 pl-6 pr-8 py-4">
                <span class="font-bold">
                  Grandma Hack:</span> To detect multicollinear features, one can look at the condition number. Following <a
                  target="_blank"
                  href="https://github.com/statsmodels/statsmodels/blob/main/statsmodels/regression/linear_model.py#L2843C1-L2844C1"
                  class="text-red-900 underline hover:text-red-400">statsmodel's
                  official implementation</a>, we can say that if the value is bigger than 1000, there is a huge
                likelihood that a multicollinear feature problem is present!
              </p>
              <h4 class="text-xl font-bold mt-4">Variance Inflation Factor (VIF)</h4>
              <p class="mt-2">
                The VIF is a metric that measures the <b>multicollinearity</b> of a feature. It is calculated by regressing
                each feature against all the other features and then extracting the R&#178; of that regression. The VIF is
                then
                calculated as 1/(1-R&#178;). The higher the VIF, the higher the multicollinearity. A VIF of 1 means that
                there
                is no multicollinearity, while a VIF of 5 or more means that there is a strong multicollinearity.
              </p>
              <p class="mt-2">
                In case of multicollinearity, we computed the VIF coefficients of the already pearson significant features
                and filtered out the ones with a VIF higher than 5.
              </p>
            </div>
          </section>
  
          <section id="noodles" class="section  text-justify">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2 pt-1" />Instantaneous Noodles and T-Taste
            </h3>
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <p class="">
                  The first impression when using raw ingredients is that indeed, the users and critics are not exactly
                  appreciating the same things. The following plot shows the distribution of the rating difference between
                  the critics and the users.
                </p>
                <p class="mt-4">
                  We can learn a few things from this graph. First, we can note that both users and critics seem to have in
                  general a similar taste, as there seems to be a positive correlation between both ratings. We can
                  nevertheless note that the critic's mean and median are around 60% of the max score and the user's ones
                  are around 70% of the max score. We can see that there are some outliers of course, but also that
                  sometimes, the critics and the users don't agree, for example, if we take a look at the top left quadrant
                  (where users find the movies better than the average and the critics find the movies worse than the
                  average) and at the bottom right quadrant (where the users find the movies worse than the average and the
                  critics find the movies better than on average).
                </p>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartUsersCritics1" class="w-full aspect-square"></div>
                </div>
              </div>
            </div>
  
  
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-2">
                <h4 class="text-xl font-bold">Rating Difference</h4>
                <p class="mt-2">
                  Let's define what we're interested in: <b>the rating difference between the critics and the users</b>.
                </p>
                <p class="mt-4">We can see
                  from the following plot that, while this distribution looks normal, it's shifted to the left (as we said
                  before the
                  user tends to slightly grade more generously than the critics, which means that when making the difference
                  we end up with a negative mean).
                </p>
                <p class="mt-4">
                  Running classic statistical tools allows us to affirm that those distributions are normal, and more
                  interestingly, the <u>rating difference is significant</u>. It's worth studying and analyzing it deeper.
                </p>
                <p class="mt-4">
                  Even if this first meal is quite quickly prepared, it raises the question we want to answer: <b>what can
                    explain
                    this discrepancy?</b>
                </p>
  
                <p class="mt-4">
                  Let's open our favorite cookbook and look for recipes that could help us explain that.
                </p>
  
              </div>
              <div class="flex flex-col order-1 lg:order-1 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartUsersCritics2" class="w-full aspect-square"></div>
                </div>
              </div>
            </div>
  
  
          </section>
        </section>
  
        <section id="cooking-time" class="section text-justify">
          <h2 class="text-4xl lg:text-5xl font-bold mt-8">Time to cook</h2>
          <h5 class="text-xl lg:text-2xl italic text-slate-600 mt-1 ml-1">Exploring the ingredients</h5>
  
          <!-- == COUNTRIES == -->
          <section id="countries" class="section">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Countries
            </h3>
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <h4 class="text-xl font-bold">Visual Appetizer</h4>
                <p class="mt-2">
                  In the grand kitchen of our data-driven analysis, let's craft a narrative as we examine the intricate
                  relationship between a film's country of origin and its critical reception. To whet our appetites for
                  understanding, we must first visually savor the prepared plots—each a dish to be dissected for its unique
                  storytelling flavors.
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
                <h4 class="text-xl font-bold">Pearson Correlation</h4>
                <p class="mt-2">
                  The Pearson coefficient provides a more nuanced but raw flavor profile of each country's cinematic output,
                  taking into account only one variable at a time. Each bar, with its confidence interval whiskers,
                  indicates the strength and direction of the relationship between a film's country of origin and its rating
                  difference. Notice the subtle hints of positive correlations for <i
                    class="text-red-900 font-semibold">France</i> and <i class="text-red-900 font-semibold">Iran</i>,
                  suggesting that films
                  from these regions carry a certain <i>je ne sais quoi</i> that resonates with critics. On the flip side,
                  the
                  <i class="text-red-900 font-semibold">United States</i> and <i
                    class="text-red-900 font-semibold">Canada</i> show negative correlations, implying a different critical
                  reception, perhaps due
                  to the commercial seasoning of their film industries. <i class="text-red-900 font-semibold">French
                    movies</i>, with a <b>correlation of 0.141</b> and a
                  <b>p-value strikingly close to zero</b>, showcase a strong positive alignment with critic ratings. <i
                    class="text-red-900 font-semibold">Iran</i> follows
                  suit but with a lesser <b>correlation of 0.065</b>, still significant enough to suggest that its films are
                  savored by critics. The plot also reveals the statistical significance (p-value) of these relationships,
                  emphasizing the reliability of our findings.
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
                <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                <p class="mt-2">
                  Let's delve deeper into the gourmet guide of global cinema by closely examining the OLS coefficients. This
                  plot refines this relationship by controlling for multiple variables. Here, we see <i
                    class="text-red-900 font-semibold">Iran</i>'s <b>coefficient
                    soaring to 7.383</b>, a testament to its films' critical acclaim when other factors are constant. This
                  is
                  contrasted by the <i class="text-red-900 font-semibold">United States</i>, which sees a <b>negative
                    coefficient of -5.8119</b>, painting a picture of a
                  cinematic giant whose films are, perhaps, too rich in mainstream appeal for the critic's more selective
                  taste.Iran's positive coefficient is robust, further validating the country's standing with critics. The
                  negative coefficients for powerhouses like the <i class="text-red-900 font-semibold">United States</i> and
                  India are stark, reinforcing the
                  narrative that commercial success is not a guaranteed recipe for critical acclaim. Comparing the with the
                  Pearson correlation, we note a shift in the order of countries and the magnitude of their influence. For
                  example, while <i class="text-red-900 font-semibold">France</i> tops the Pearson plot, <i
                    class="text-red-900 font-semibold">Iran</i> takes the lead in the OLS analysis, highlighting how
                  controlling for other variables can change the taste profile of our data dish. Despite slight differences,
                  it appears that critics tend to favor films that offer a distinct cultural voice, complex narratives, and
                  a strong artistic vision—qualities that are often highlighted in French and Iranian films. Conversely,
                  industries known for their box office prowess, such as Hollywood and Bollywood, might prioritize elements
                  that ensure commercial success. This industry caters to mass appeal rather than the gourmet tastes of
                  critics.
                </p>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartCountries3" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- Tabs -->
            <div class="flex flex-col mt-6 w-full">
              <TabsSection :tabs="countriesTabs" :defaultIndex="5" />
            </div>
          </section>
  
  
          <!-- == GENRES == -->
          <section id="genres" class="section">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Genres
            </h3>
            <h5 class="text-lg lg:text-xl italic text-slate-600 text-start">Crafting the Narrative of Preference</h5>
  
            <!-- Basic Viz -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <h4 class="text-xl font-bold">Vizual Appetizer</h4>
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
              <div class="flex flex-col order-2 lg:order-2 text-justify">
                <div>
                  <h4 class="text-xl font-bold">Pearson Correlation</h4>
                  <p class="mt-2">
                    The first technique in our cookbook is the beloved Pearson correlation. This lovely tool allows us to
                    extract significant genres. Out of 314 genres and subgenres, only <u>61 are significant</u>
                    for
                    our
                    analysis.
                  </p>
                  <p class="mt-4">
                    Looking a bit more in detail at this plot, the genres exhibited feel way more concrete than
                    before. It's not surprising to see critics liking more <i class="text-red-900 font-semibold">World
                      cinema</i> or <i class="text-red-900 font-semibold">Art film</i>
                    categories.
                    On the other
                    end of the spectrum, <i class="text-red-900 font-semibold">Action</i> films and <i
                      class="text-red-900 font-semibold">Comedy</i> have the support of a wider audience.
                    Interestingly, we do
                    see <i class="text-red-900 font-semibold">Gross-out</i> and <i
                      class="text-red-900 font-semibold">Gross-out films</i> both appear. Why do we see this kind of genre
                    twice with
                    the same
                    result? And even worse: is there something odd behind our analysis?</p>
  
                  <p class="mt-4">
                    While filtering out subgenres would
                    sound natural, it's often in those small niche genres that the critics' tastes were hiding. We took the
                    gambit to keep them at first and filter them later through significance methods if needed. While
                    instructive, we have to work a bit more on our data.
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-1 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartGenres2" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- OLS -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1 text-justify">
                <div>
                  <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                  <p class="mt-2">
                    It occured that the first OLS's showed a very high condition number hinting the presence of
                    a strong multicollinearity. This threatened the interpretation of the results and required some VIF
                    filtering. After filtering according to our cookbook, only 93 features were retained and passed again
                    through our OLS.
                    Finally, applying our
                    significance threshold (p-value&lt;0.05), the filtered OLS yields about <u>22 significant genres</u>.
                  </p>
                  <p class="mt-4">
                    Looking closer at our plot, we see that the previously spotted parasitic genres such as <i
                      class="text-red-900 font-semibold">Gross
                      out</i> have been correctly filtered out, providing a way cleaner overview of what genres impact the
                    rating
                    difference. For the finest gourmet amongst you, the results give an adjusted R&#178; of 0.136, meaning
                    that
                    the genres alone can explain up to <b>13.6%</b> of the variance of the rating difference between critics
                    and
                    users.
                  </p>
                  <p class="mt-4">
                    However, let's stay down-to-earth. The confidence interval around some of these genres triggers a small
                    warning, and for instance, the <i class="text-red-900 font-semibold">Inspirational Drama</i> or <i
                      class="text-red-900 font-semibold">Feminist Film</i> genres shouldn't be judged
                    so fast. This
                    wide confidence interval can partially be explained by the relatively low number of films in those
                    categories.
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartGenres3" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- Tabs -->
            <div class="flex flex-col mt-8 w-full gap-5">
              <TabsSection :tabs="genresTabs" :defaultIndex="1" />
            </div>
          </section>
  
          <!-- === AWARDS === -->
          <section id="awards" class="section text-justify">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Awards
            </h3>
            <!-- Basic Viz -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <h4 class="text-xl font-bold">Visual Appetizer</h4>
                <p class="mt-2">
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
                  <div ref="chartAwards1" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- Pearson -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-2">
                <div>
                  <h4 class="text-xl font-bold">Pearson Correlation</h4>
                  <p class="mt-2">
                    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Animi culpa, dignissimos consequuntur deserunt
                    maiores voluptas reiciendis pariatur cum? Temporibus ipsum odit in corporis? Nostrum voluptatem magni
                    quo nulla reprehenderit nemo?
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-1 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartAwards2" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- OLS -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1">
                <div>
                  <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                  <p class="mt-2">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sunt saepe, recusandae culpa nisi earum optio
                    laborum temporibus voluptatibus vel aliquid placeat quas non ab ullam deserunt rem incidunt asperiores
                    veritatis!
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartAwards3" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- Tabs -->
            <div class="flex flex-col mt-8 w-full gap-5">
              <TabsSection :tabs="awardsTabs" :defaultIndex="6" />
            </div>
          </section>
  
  
          <section id="release-year" class="section">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Release Year
            </h3>
            <p class="mt-2 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
              consequat
              aliquam, nunc
              ipsum
              aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
              ipsum
              aliquet nunc, vitae aliquam nisl nunc vitae nisl.</p>
          </section>
  
          <!-- == ACTORS == -->
          <section id="actors" class="section">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Actors
            </h3>
            <!-- Pearson -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-2">
                <div>
                  <h4 class="text-xl font-bold">Pearson Correlation</h4>
                  <p class="mt-2 text-justify">
                    Once again, a rotten tomato could spoil the real taste of the preparation, and we want to avoid such
                    mistakes. Cleaning our ingredient basket with the Pearson correlation gives this yummy plot of <u>426
                      significant</u> actors out of 3151 ones.
                  </p>
                  <p class="text-justify mt-4">
                    Let's look a bit more in detail at what this shows us. Analyzing the significant actors already gives
                    quite interesting results. We can notice that the best-performing actors for impressing critics are
                    mostly
                    old actors, such as <i class="text-red-900 font-semibold">Cary Grant</i> or <i
                      class="text-red-900 font-semibold">Ward Bond</i>. A small warning here: since those actors are mostly
                    from the
                    beginning of cinema history, their results might be biased. Indeed, it is possible that their less
                    renowned movies or less-performing roles were simply filtered out due to the lack of data. Indeed, a
                    film
                    too old might not even be rated retrospectively by critics and users if it was a forgettable experience.
                    This phenomenon could bias them toward higher scores. This is also to be mitigated by the fact that, in
                    a
                    way, if those actors are still known to experts, they marked cinema history and could deserve their
                    place.
                  </p>
                  <p class="text-justify mt-4">
                    On the other hand, recent movies and actors are much less likely to be given the chance to not be scored
                    badly for a bad movie. No second chances for <i class="text-red-900 font-semibold">Ryan Reynolds</i> or
                    <i class="text-red-900 font-semibold">Ashton Kutcher</i>. Indeed, alternating between
                    deep roles highlighting their talent and lighter characters might be detrimental to them in this plot.
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-1 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartActors1" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- OLS -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-1 text-justify">
                <div>
                  <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                  <p class="mt-2 ">
                    Running the OLS gives once more insightful results, with an adjusted R&#178; of 0.13 (<b>13%</b>).
                    Having
                    specific actors
                    seems then to be impactful on the results, with the <u>20 significant</u> ones shown in this plot.
                  </p>
                  <p class="mt-4">Once
                    again, the variances are quite big, probably due to the relatively low number of films each actor's been
                    in compared to the total number of films and actors. A final remark must be noted too: we can't be sure
                    that the genres and the actors are not entangled in a way. Some actors are probably performing well in
                    specific genres while being considered awful in others. Sadly, we've been unable to completely rule out
                    that kind of confounding effect, since all of the features we have are of course strongly
                    interconnected.
                  </p>
                  <p class="mt-4">
                    Comparing the result of the Pearson shows that the results seem comparable, with some slight difference
                    in
                    the order. The type of the actors, however, seem quite consistent between the two.
                  </p>
                </div>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartActors2" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <!-- Tabs -->
            <div class="flex flex-col mt-8 w-full gap-5">
              <TabsSection :tabs="actorsTabs" :defaultIndex="3" />
            </div>
          </section>
  
          <!-- == TROPES == -->
          <section id="tropes" class="section">
            <h3 class="text-3xl lg:text-4xl font-bold mt-8 items-center text-start mb-4">
              <BookmarkIcon class="w-9 h-9 float-left mr-2" />Tropes
            </h3>
  
            <p>
              The last ingredient for our glorious meal are the tropes. As a friendly reminder, tropes are “a significant
              or recurrent theme; a motif”. Maybe this boring repetitive structure in this site was an artistic choice from
              the beginning? Let's get back to the kitchen. Because tropes are categories that are human made and manually
              assigned to each movie on the internet, the classification can be even messier than movie genres. But since
              it's born from human need for categorization, we do think it can be a very valuable source of information.
              Notice that, while the dataset merging in the previous steps didn't leave out a lot of movies, the tropes
              merging drastically reduced the number of datapoints, down to approximately 2495, as mentioned during our
              fridge inspection. Still plenty of room to work with! We know you're already drooling, but hold on through
              this last step!
            </p>
  
            <!-- Pearson -->
            <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
              <div class="flex flex-col order-2 lg:order-2">
                <h4 class="text-xl font-bold">Pearson Correlation</h4>
                <p class="mt-2 text-justify">
                  As expected, the Pearson correlation filtered out our movies down to around <u>300 significant tropes</u>,
                  which
                  is indeed enough to continue our analysis. Diving into the plot, we can see really funny and odd tropes
                  standing out. What is absolutely great is that the <i class="text-red-900 font-semibold">Oscar Bait</i>
                  type of film, with <b>correlation of 0.1</b>, is
                  actually taking the highest place of the plot, meaning that indeed, this trope is a significant indicator
                  for critical reception. On the other end, <i class="text-red-900 font-semibold">Ms Fanservice</i>, with
                  <b>correlation of 0.11</b> too, indicates that
                  …fans like it. So far so good. This is no real surprise, since these qualifiers could have been attributed
                  a posteriori. In general, we can suspect that these tropes are tightly related to all other features, like
                  <i class="text-red-900 font-semibold">Deliberately Monochrome</i> is way more likely to qualify art films,
                  and are likely to be considered part of
                  Auteur license too. On the other hand, expected tropes binded with genre, like <i
                    class="text-red-900 font-semibold">Slasher</i> reappears,
                  reinforcing the insights provided by the Genre analysis. In general, the confidence intervals are wide,
                  but quite constant over the sample. However, the most precise tropes standing out might be a bit harder to
                  interpret. Furthermore, we do see that the <i class="text-red-900 font-semibold">Magical something</i>
                  trope appears twice, and referring to the
                  methods we used, we could expect high multicollinearity.
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
                <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
                <p class="mt-2 text-justify">
                  By running our first OLS, we get as expected a high condition number implying a high multicollinearity. By
                  applying VIF filtering we cut out almost 20 tropes, leaving us now with 315 features. The OLS regression
                  can now be performed with the hopes of better results. With an impressive <b>adjusted R&#178; of 0.2</b>
                  and <u>36
                    significant tropes</u>, the OLS shows very encouraging numbers. However, visualizing what's the outcome
                  in our
                  now classic plot can be a little bit disturbing. Instead of cleaning out obscure tropes, the outcome is
                  even harder to interpret. Based on the metrics evaluating the regression quality, the results are good,
                  but here we're probably limited by our own projections. These results could've been expected, since most
                  of them are heavily tailored and strongly related to the movie's target audience. However, we do observe
                  wider confidence intervals, getting us an insight that maybe, the variance of these rating differences are
                  high. Let's still highlight the fact that <i class="text-red-900 font-semibold">Roof hopping</i> performs
                  well to impress critics, while strangely,
                  films like Mary Poppins and The Matrix are both part of this category. If you're curious to know what a
                  trope means, play around our <a href="#playground"
                    class="py-[.28em] px-2 bg-slate-800 text-white rounded-lg hover:bg-slate-600">playground</a> at the end,
                  and don't hesitate to learn using the source of our
                  tropes data, <a href="https://tvtropes.org" target="_blank"
                    class="text-red-900 underline hover:text-red-400">tvtropes.org</a>.
                </p>
              </div>
              <div class="flex flex-col order-1 lg:order-2 w-full">
                <div class="flex flex-col h-full w-full">
                  <div ref="chartTropes2" class="h-full min-h-[600px] w-full"></div>
                </div>
              </div>
            </div>
  
            <div class="flex flex-col mt-8 w-full gap-5">
              <TabsSection :tabs="tropesTabs" :defaultIndex="4" />
            </div>
          </section>
        </section>
  
        <section id="conclusion" class="section">
          <h2 class="text-4xl lg:text-5xl font-bold mt-8 mb-6">Conclusion</h2>
          <p class="mt-2 text-justify">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget
            consequat
            aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl. Donec euismod, nisl eget consequat aliquam, nunc
            ipsum
            aliquet nunc, vitae aliquam nisl nunc vitae nisl.
          </p>
  
          <!-- Pearson -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-2">
              <h4 class="text-xl font-bold">Pearson Correlation</h4>
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
                <div ref="chartGlobal1" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>
  
          <!-- OLS -->
          <div class="grid lg:grid-cols-2 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1">
              <h4 class="text-xl font-bold">Ordinary Least Squares (OLS)</h4>
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
                <div ref="chartGlobal2" class="h-full min-h-[600px] w-full"></div>
              </div>
            </div>
          </div>
  
          <div class="grid lg:grid-cols-3 mt-8 w-full gap-5">
            <div class="flex flex-col order-2 lg:order-1 col-span-2">
              <p class="mt-3">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus id, quod veritatis eos laboriosam omnis
                quas. Impedit aut, odit possimus iusto error mollitia voluptatem, esse numquam eveniet reprehenderit, veniam
                commodi.
              </p>
            </div>
            <div class="flex flex-col col-span-3 order-1 lg:col-span-1 lg:order-2 w-full items-center justify-center">
              <div class="flex flex-col h-full w-full items-center justify-center">
                <img src="/ego.png" alt="ego"
                  class="lg:w-full mt-4 drop-shadow-xl max-h-[400px] lg:max-h-none hover:scale-y-105 hover:-scale-x-105 hover:drop-shadow-none transition duration-300 -scale-x-100" />
              </div>
            </div>
          </div>
  
  
        </section>
  
        <section id="playground" class="section">
          <h2 class="text-4xl lg:text-5xl font-bold mt-8">Playground</h2>
          <div>
            <Playground />
          </div>
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
  
  
  
  <script setup>
  import { onMounted, ref, defineAsyncComponent } from 'vue';
  import { BookmarkIcon } from "@heroicons/vue/24/solid"
  const BASE_URL = import.meta.env.VITE_BASE_URL;
  import * as plotFunctions  from './plots.js'
  
  const Playground = defineAsyncComponent(() => import('./Playground.vue'));
  const TabsSection = defineAsyncComponent(() => import('./TabsSection.vue'));
  
  const chartUsers = ref(null);
  const chartMetascore = ref(null);
  const chartUsersCritics1 = ref(null);
  const chartUsersCritics2 = ref(null);
  const chartCountries1 = ref(null);
  const chartCountries2 = ref(null);
  const chartCountries3 = ref(null);
  const chartGenres1 = ref(null);
  const chartGenres2 = ref(null);
  const chartGenres3 = ref(null);
  const chartAwards1 = ref(null);
  const chartAwards2 = ref(null);
  const chartAwards3 = ref(null);
  const chartActors1 = ref(null);
  const chartActors2 = ref(null);
  const chartTropes1 = ref(null);
  const chartTropes2 = ref(null);
  const chartGlobal1 = ref(null)
  const chartGlobal2 = ref(null)
  
  const countriesTabs = ref(null)
  const genresTabs = ref(null)
  const awardsTabs = ref(null)
  const tropesTabs = ref(null)
  const actorsTabs = ref(null)
  
  const fetchData = async (path) => {
    const originUrl = window.location.origin;
    if (BASE_URL && BASE_URL !== '/') return await fetch(`${originUrl}/${BASE_URL}/${path}`).then(response => response.json());
    return await fetch(`${originUrl}/${path}`).then(response => response.json());
  };
  
  
  onMounted(async () => {
  
    const movies = await fetchData('/data/playground-movies.json');
  
    // == TABS WIDGETS == //
    fetchData('/data/countriesTabs.json').then(data => {
      countriesTabs.value = data;
    });
    fetchData('/data/genresTabs.json').then(data => {
      genresTabs.value = data;
    });
    fetchData('/data/awardsTabs.json').then(data => {
      awardsTabs.value = data;
    });
    fetchData('/data/tropesTabs.json').then(data => {
      tropesTabs.value = data;
    });
    fetchData('/data/actorsTabs.json').then(data => {
      actorsTabs.value = data;
    });
    
    // == CHARTS == //
    // Users Bar Chart
    if (chartUsers) {
      plotFunctions.callbackUser(movies, chartUsers)
    }
  
    // Metascore Bar Chart 
    if (chartMetascore) {
      plotFunctions.callbackMetascore(movies, chartMetascore)
    }
  
    // Users vs Critics Scatter
    if (chartUsersCritics1) {
      plotFunctions.callbackUsersCritics1(movies, chartUsersCritics1)
    }
  
    // User vs Critics 2
    if (chartUsersCritics2) {
      plotFunctions.callbackUsersCritics2(movies, chartUsersCritics2)
    }
  
  
    // Countries 1
    if (chartCountries1) {
      plotFunctions.callbackCountries1(chartCountries1, "/data/countries-1.json")
    }
  
    // Countries 2
    if (chartCountries2) {
      plotFunctions.callbackCountries2(chartCountries2, "/data/countries-2.json")
    }
  
    // Countries 3
    if (chartCountries3) {
      plotFunctions.callbackCountries3(chartCountries3, "/data/countries-3.json")
    }
  
  
    // Genres 1
    if (chartGenres1) {
      plotFunctions.callbackGenres1(chartGenres1, "/data/genres-1.json")
    }
  
    // Genres 2
    if (chartGenres2) {
      plotFunctions.callbackGenres2(chartGenres2, "/data/genres-2.json")
    }
  
    // Genres 3
    if (chartGenres3) {
      plotFunctions.callbackGenres3(chartGenres3, "/data/genres-3.json")
    }
  
    // Awards 1
    if (chartAwards1) {
      plotFunctions.callbackAwards1(chartAwards1, "/data/awards-1.json")
    }
  
    // Awards 2
    if (chartAwards2) {
      plotFunctions.callbackAwards2(chartAwards2, "/data/awards-2.json")
    }
  
    // Awards 3
    if (chartAwards3) {
      plotFunctions.callbackAwards3(chartAwards3, "/data/awards-3.json")
    }
  
    // Actors 1
    if (chartActors1) {
      plotFunctions.callbackActors1(chartActors1, "/data/actors-1.json")
    }
  
    // Actors 2
    if (chartActors2) {
      plotFunctions.callbackActors2(chartActors2, "/data/actors-2.json")
    }
  
    // Tropes 1
    if (chartTropes1) {
      plotFunctions.callbackTropes1(chartTropes1, "/data/tropes-1.json")
    }
  
    // Tropes 2
    if (chartTropes2) {
      plotFunctions.callbackTropes2(chartTropes2, "/data/tropes-2.json")
    }
  
  
    // Global 1
    if (chartGlobal1) {
      plotFunctions.callbackGlobal1(chartGlobal1, "/data/global-1.json")
    }
  
    // Global 2
    if (chartGlobal2) {
      plotFunctions.callbackGlobal2(chartGlobal2, "/data/global-2.json")
    }
  
  });
  
  </script>